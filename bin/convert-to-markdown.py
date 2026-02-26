#!/usr/bin/env python3
"""
Convert HTML wiki pages to Markdown for Jekyll.
"""

import html as html_module
import re
import subprocess
import sys
from pathlib import Path


# Map DokuWiki note types to GFM alert types
NOTE_TYPE_MAP = {
    'noteimportant': 'IMPORTANT',
    'notewarning': 'WARNING',
    'notetip': 'TIP',
    'noteclassic': 'NOTE',
}

# Map DokuWiki smileys to Unicode emoji
SMILEY_MAP = {
    'exclaim.svg': '\u26a0\ufe0f',      # Warning sign
    'question.svg': '\u2753',            # Question mark
    'fixme.svg': '\U0001f6a7',           # Construction sign
    'cool.svg': '\U0001f60e',            # Sunglasses
    'wink.svg': '\U0001f609',            # Wink
    'sad.svg': '\U0001f61e',             # Sad
    'fun.svg': '\U0001f60a',             # Smile
    'thumbsup.svg': '\U0001f44d',        # Thumbs up
    'thumbsdown.svg': '\U0001f44e',      # Thumbs down
}


def extract_content_and_title(html_path):
    """Extract main content and title from HTML file."""
    content = html_path.read_text(encoding="utf-8")

    # Extract title and decode HTML entities
    title_m = re.search(r'<title>([^<]+) - CSS Working Group Wiki', content)
    title = title_m.group(1).strip() if title_m else html_path.parent.name
    title = html_module.unescape(title)

    # Extract main content
    main_m = re.search(r'<main>\s*(.*?)\s*</main>', content, re.DOTALL)
    if not main_m:
        return title, ""

    main_content = main_m.group(1)

    # Remove TOC
    main_content = re.sub(r'<!-- TOC START -->.*?<!-- TOC END -->', '', main_content, flags=re.DOTALL)
    main_content = re.sub(r'<div id="dw__toc"[^>]*>.*?</div>\s*</div>', '', main_content, flags=re.DOTALL)

    return title, main_content.strip()


def convert_plugin_notes(html):
    """Convert plugin_note divs to alert-marked divs that pandoc will preserve."""
    def replace_note(m):
        classes = m.group(1)
        content = m.group(2)
        
        alert_type = 'NOTE'
        for note_class, gfm_type in NOTE_TYPE_MAP.items():
            if note_class in classes:
                alert_type = gfm_type
                break
        
        return f'<div class="gfm-alert-{alert_type.lower()}">{content}</div>'
    
    html = re.sub(
        r'<div class="(plugin_note[^"]*)">(.*?)</div>',
        replace_note,
        html,
        flags=re.DOTALL
    )
    
    return html


def extract_definition_lists(html):
    """Extract definition lists and replace with placeholders."""
    definition_lists = []
    
    def extract_dl(m):
        dl_content = m.group(1)
        kramdown_lines = []
        
        pattern = r'<dt[^>]*>(.*?)</dt>\s*((?:<dd[^>]*>.*?</dd>\s*)+)'
        
        for dt_match in re.finditer(pattern, dl_content, re.DOTALL):
            term = dt_match.group(1)
            dds_html = dt_match.group(2)
            
            # Clean up term
            term = re.sub(r'<span[^>]*class="term"[^>]*>\s*', '', term)
            term = re.sub(r'\s*</span>', '', term)
            term = re.sub(r'<[^>]+>', '', term)
            term = html_module.unescape(term.strip())
            
            if term:
                if kramdown_lines:
                    kramdown_lines.append('')
                kramdown_lines.append(term)
            
            for dd_match in re.finditer(r'<dd[^>]*>(.*?)</dd>', dds_html, re.DOTALL):
                definition = dd_match.group(1).strip()
                definition = re.sub(r'<code>([^<]*)</code>', r'`\1`', definition)
                definition = re.sub(r'<[^>]+>', '', definition)
                definition = html_module.unescape(definition.strip())
                if definition:
                    kramdown_lines.append(f': {definition}')
        
        if kramdown_lines:
            idx = len(definition_lists)
            definition_lists.append('\n'.join(kramdown_lines))
            return f'DLPLACEHOLDER{idx}DLPLACEHOLDER'
        return ''
    
    html = re.sub(
        r'<dl[^>]*>\s*(.*?)\s*</dl>',
        extract_dl,
        html,
        flags=re.DOTALL
    )
    
    return html, definition_lists


def restore_definition_lists(md, definition_lists):
    """Replace placeholders with kramdown definition lists."""
    for idx, dl_content in enumerate(definition_lists):
        placeholder = f'DLPLACEHOLDER{idx}DLPLACEHOLDER'
        md = md.replace(placeholder, f'\n\n{dl_content}\n')
    return md


def extract_dataplugin_entries(html):
    """Extract dataplugin_entry metadata and replace with placeholders."""
    dataplugin_entries = []
    
    def convert_entry(m):
        content = m.group(1)
        fields = []
        
        # Extract dt/dd pairs from the nested dl
        pattern = r'<dt[^>]*>([^<]*)<span class="sep">[^<]*</span></dt>\s*<dd[^>]*>(.*?)</dd>'
        
        for field_match in re.finditer(pattern, content, re.DOTALL):
            field_name = field_match.group(1).strip()
            field_value = field_match.group(2).strip()
            
            if not field_name:
                continue
            
            # Remove DokuWiki filter links but keep the text
            field_value = re.sub(r'<a[^>]*dataflt[^>]*>([^<]*)</a>', r'\1', field_value)
            
            # Convert regular links to markdown
            def convert_link(lm):
                href = lm.group(1)
                text = lm.group(2)
                if 'dataflt' in href:
                    return text
                return f'[{text}]({href})'
            field_value = re.sub(r"<a[^>]*href=['\"]([^'\"]+)['\"][^>]*>([^<]*)</a>", convert_link, field_value)
            
            # Remove remaining HTML and decode entities
            field_value = re.sub(r'<[^>]+>', '', field_value)
            field_value = html_module.unescape(field_value.strip())
            
            if field_value:
                fields.append(f'**{field_name}:** {field_value}')
        
        if fields:
            idx = len(dataplugin_entries)
            dataplugin_entries.append(' | '.join(fields))
            return f'METADATAPLACEHOLDER{idx}METADATAPLACEHOLDER'
        return ''
    
    html = re.sub(
        r'<div class="[^"]*dataplugin_entry[^"]*">\s*(.*?)\s*</div>',
        convert_entry,
        html,
        flags=re.DOTALL
    )
    
    return html, dataplugin_entries


def restore_dataplugin_entries(md, entries):
    """Replace placeholders with formatted metadata."""
    for idx, metadata in enumerate(entries):
        placeholder = f'METADATAPLACEHOLDER{idx}METADATAPLACEHOLDER'
        md = md.replace(placeholder, f'{metadata}\n\n')
    return md


def convert_smileys(html):
    """Convert DokuWiki smiley images to Unicode emoji."""
    def replace_smiley(m):
        src = m.group(1)
        filename = src.split('/')[-1]
        return SMILEY_MAP.get(filename, '')
    
    html = re.sub(
        r'<img[^>]*src="(/lib/images/smileys/[^"]+)"[^>]*class="icon smiley"[^>]*/?>',
        replace_smiley,
        html
    )
    html = re.sub(
        r'<img[^>]*class="icon smiley"[^>]*src="(/lib/images/smileys/[^"]+)"[^>]*/?>',
        replace_smiley,
        html
    )
    
    return html


def convert_no_divs(html):
    """Convert <div class="no"> (bad example markers) to CAUTION alerts."""
    html = re.sub(
        r'<div class="no">\s*',
        '<div class="gfm-alert-caution">',
        html
    )
    return html


def clean_media(html):
    """Clean up media elements for conversion."""
    # Unwrap <a class="media"> wrappers around images, keeping the <img>
    html = re.sub(
        r'<a[^>]*class="media"[^>]*>\s*(<img[^>]*/?>)\s*</a>',
        r'\1',
        html
    )

    # Remove DokuWiki logo
    html = re.sub(
        r'<img[^>]*src="[^"]*/_media/wiki/dokuwiki[^"]*"[^>]*/?>',
        '',
        html
    )

    # Remove any remaining unrewritten /_media/ or fetch.php references
    html = re.sub(
        r'<a[^>]*href="[^"]*lib/exe/fetch\.php[^"]*"[^>]*>\s*<(?:img|embed)[^>]*>\s*</a>',
        '',
        html
    )
    html = re.sub(
        r'<(?:img|embed)[^>]*src="[^"]*lib/exe/fetch\.php[^"]*"[^>]*/?>',
        '',
        html
    )
    html = re.sub(
        r'<img[^>]*src="[^"]*/_media/[^"]*"[^>]*/?>',
        '',
        html
    )

    # Strip DokuWiki attributes from <img> so pandoc converts to ![alt](src)
    def strip_img_attrs(m):
        tag = m.group(0)
        tag = re.sub(r'\s+class="media(?:left|right|center)?"', '', tag)
        tag = re.sub(r'\s+loading="lazy"', '', tag)
        tag = re.sub(r'\s+width="\d+"', '', tag)
        tag = re.sub(r'\s+height="\d+"', '', tag)
        return tag

    html = re.sub(r'<img[^>]*/?>',  strip_img_attrs, html)

    # Remove title that duplicates alt on images (avoids redundant ![alt](src "alt"))
    def strip_dup_title(m):
        tag = m.group(0)
        alt_m = re.search(r'alt="([^"]*)"', tag)
        title_m = re.search(r'title="([^"]*)"', tag)
        if alt_m and title_m and alt_m.group(1) == title_m.group(1):
            tag = re.sub(r'\s+title="[^"]*"', '', tag)
        return tag

    html = re.sub(r'<img[^>]*/?>',  strip_dup_title, html)

    return html


def cleanup_html(html):
    """Clean up HTML before pandoc conversion."""
    # Convert plugin_note divs to alert-marked divs
    html = convert_plugin_notes(html)
    
    # Convert smileys to Unicode emoji
    html = convert_smileys(html)
    
    # Convert "no" divs (bad examples) to CAUTION alerts
    html = convert_no_divs(html)
    
    # Remove/fix broken media references
    html = clean_media(html)
    
    # Remove rel="noopener", rel="nofollow" and similar attributes
    html = re.sub(r'\s+rel="[^"]*"', '', html)

    # Remove class attributes on links
    html = re.sub(r'<a\s+class="[^"]*"\s+href="([^"]*)">', r'<a href="\1">', html)
    html = re.sub(r'<a\s+href="([^"]*)"\s+class="[^"]*">', r'<a href="\1">', html)

    # Remove id attributes on links
    html = re.sub(r'(<a[^>]*)\s+id="[^"]*"', r'\1', html)

    # Remove title attributes that just duplicate the href URL
    def remove_redundant_title(m):
        href = m.group(1)
        title = m.group(2)
        if title.rstrip('/') == href.rstrip('/'):
            return f'href="{href}"'
        return m.group(0)

    html = re.sub(r'href="([^"]+)"\s+title="([^"]+)"', remove_redundant_title, html)

    # Strip various span wrappers
    html = re.sub(r'<span class="abbr" title="[^"]*">([^<]*)</span>', r'\1', html)
    html = re.sub(r'<span[^>]*class="term"[^>]*>([^<]*)</span>', r'\1', html)
    html = re.sub(r'<span class="sep">[^<]*</span>', '', html)
    
    # Remove table styling classes
    html = re.sub(r'\s+class="(?:col|row)\d+[^"]*"', '', html)
    html = re.sub(r'\s+class="(?:inline|sectionedit\d+|leftalign|rightalign|centeralign)"', '', html)

    return html


def html_to_markdown(html_content):
    """Convert HTML to Markdown using pandoc."""
    if not html_content:
        return ""

    # Extract dataplugin_entry FIRST (contains nested <dl>)
    html_content, dataplugin_entries = extract_dataplugin_entries(html_content)
    
    # Extract definition lists before pandoc
    html_content, definition_lists = extract_definition_lists(html_content)

    # Clean up HTML before conversion
    html_content = cleanup_html(html_content)

    result = subprocess.run(
        ["pandoc", "-f", "html", "-t", "gfm", "--wrap=none"],
        input=html_content,
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        print(f"  pandoc error: {result.stderr}", file=sys.stderr)
        return ""

    md = result.stdout
    
    # Restore definition lists as kramdown syntax
    md = restore_definition_lists(md, definition_lists)
    
    # Restore dataplugin metadata
    md = restore_dataplugin_entries(md, dataplugin_entries)

    # Escape Liquid tags
    md = md.replace("{%", "{% raw %}{%{% endraw %}")
    md = md.replace("{{", "{% raw %}{{{% endraw %}")

    return md


def convert_gfm_alerts(md):
    """Convert alert-marked divs to GFM alert blockquote syntax."""
    def format_alert(m):
        alert_type = m.group(1).upper()
        content = m.group(2).strip()
        
        lines = content.split('\n')
        result_lines = [f'> [!{alert_type}]']
        for line in lines:
            stripped = line.strip()
            if stripped:
                result_lines.append(f'> {stripped}')
            else:
                result_lines.append('>')
        
        return '\n'.join(result_lines)
    
    md = re.sub(
        r'<div class="gfm-alert-(note|tip|important|warning|caution)">\s*(.*?)\s*</div>',
        format_alert,
        md,
        flags=re.DOTALL | re.IGNORECASE
    )
    
    return md


def cleanup_markdown(md):
    """Clean up markdown after pandoc conversion."""
    # Convert GFM alert divs to blockquote syntax
    md = convert_gfm_alerts(md)
    
    # Remove leftover div wrappers
    md = re.sub(r'<div class="plugin_note[^"]*">\s*\n?', '', md)
    md = re.sub(r'<div class="table[^"]*">\s*\n?', '', md)
    md = re.sub(r'<div class="topic-metadata">\s*', '', md)
    md = re.sub(r'\n</div>\s*(?=\n|$)', '\n', md)
    md = re.sub(r'</div>\s*$', '', md)

    # Convert remaining links
    def convert_link(m):
        full_match = m.group(0)
        href = m.group(1)
        text = m.group(2)
        if re.search(r'<(?!/?(?:em|strong|code|b|i)\b)[^>]+>', text):
            return full_match
        if 'dataflt' in href:
            return text
        text_clean = re.sub(r'<[^>]+>', '', text)
        if not text_clean.strip():
            return full_match
        return f'[{text_clean}]({href})'

    md = re.sub(r'<a\s+href="([^"]+)"(?:\s+[^>]*)?>([^<]*)</a>', convert_link, md)

    # Strip remaining spans
    md = re.sub(r'<span class="abbr" title="[^"]*">([^<]*)</span>', r'\1', md)
    md = re.sub(r'<span[^>]*class="term"[^>]*>([^<]*)</span>', r'\1', md)
    
    # Clean up multiple blank lines
    md = re.sub(r'\n{3,}', '\n\n', md)

    return md.strip()


def convert_file(html_path, output_dir):
    """Convert a single HTML file to Markdown."""
    title, html_content = extract_content_and_title(html_path)
    markdown = html_to_markdown(html_content)
    markdown = cleanup_markdown(markdown)

    rel_path = html_path.parent.relative_to(output_dir)
    page_path = str(rel_path) if str(rel_path) != "." else ""

    if page_path:
        md_path = output_dir / rel_path / "index.md"
    else:
        md_path = output_dir / "index.md"

    title_escaped = title.replace('"', '\\"')
    front_matter = f'---\ntitle: "{title_escaped}"\n---\n\n'

    md_path.write_text(front_matter + markdown, encoding="utf-8")
    html_path.unlink()

    return md_path


def main():
    script_dir = Path(__file__).parent
    output_dir = script_dir.parent

    html_files = list(output_dir.glob("**/index.html"))
    html_files = [f for f in html_files if "_layouts" not in str(f) and "_site" not in str(f)]

    print(f"Converting {len(html_files)} HTML files to Markdown...")

    for i, html_path in enumerate(sorted(html_files)):
        rel = html_path.relative_to(output_dir)
        print(f"[{i+1}/{len(html_files)}] {rel}")
        convert_file(html_path, output_dir)

    print("\nDone!")


if __name__ == "__main__":
    main()
