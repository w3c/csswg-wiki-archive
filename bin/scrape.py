#!/usr/bin/env python3
"""
Scrape wiki.csswg.org and produce a static site.

This script crawls the CSS Working Group Wiki (DokuWiki-based) and generates
a static HTML archive suitable for hosting on GitHub Pages or any static host.

Usage:
    python3 bin/scrape.py [output_dir]

If output_dir is not specified, outputs to the current directory.
"""

import re
import sys
import time
import urllib.request
from pathlib import Path

BASE_URL = "https://wiki.csswg.org"
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
DELAY = 0.3  # Seconds between requests (be nice to the server)


def fetch(url):
    """Fetch a URL with proper headers."""
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return resp.read().decode("utf-8", errors="replace")
    except Exception as e:
        print(f"  Error: {e}")
        return None


def get_all_pages():
    """Discover all wiki pages by crawling the index."""
    pages = set()
    namespaces = set()

    print("Fetching main index...")
    html = fetch(f"{BASE_URL}/?do=index")
    if not html:
        return []

    # Find namespace links like ?idx=ideas
    for m in re.finditer(r'\?idx=([a-z0-9_-]+)', html):
        namespaces.add(m.group(1))

    # Find top-level page links
    for m in re.finditer(r'href="/([a-z0-9_-]+)"', html):
        page = m.group(1)
        if page not in ('lib', '_export', '_detail', '_media') and not page.startswith('feed'):
            pages.add(page)

    # Expand each namespace to find all pages within it
    for ns in sorted(namespaces):
        print(f"Expanding: {ns}")
        time.sleep(DELAY)
        html = fetch(f"{BASE_URL}/?do=index&idx={ns}")
        if html:
            for m in re.finditer(r'href="/([^"?#]+)"', html):
                p = m.group(1)
                if not p.startswith(('lib/', '_', 'feed')) and '?' not in p:
                    pages.add(p)
            # Check for sub-namespaces
            for m in re.finditer(rf'\?idx=({ns}:[a-z0-9_:-]+)', html):
                sub_ns = m.group(1)
                time.sleep(DELAY)
                sub_html = fetch(f"{BASE_URL}/?do=index&idx={sub_ns}")
                if sub_html:
                    for m2 in re.finditer(r'href="/([^"?#]+)"', sub_html):
                        p = m2.group(1)
                        if not p.startswith(('lib/', '_', 'feed')) and '?' not in p:
                            pages.add(p)

    return sorted(pages)


PAGE_TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} - CSS Working Group Wiki (Archive)</title>
<style>
*, *::before, *::after {{ box-sizing: border-box; }}
body {{
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  max-width: 900px; margin: 0 auto; padding: 1.5em 1em; line-height: 1.6;
  color: #1f2328; background: #fff;
}}
.archive-banner {{
  background: #fff8c5; border: 1px solid #d4a72c; border-radius: 6px;
  padding: 0.75em 1em; margin-bottom: 1.5em; font-size: 0.9em;
}}
.archive-banner strong {{ color: #6e5600; }}
header {{ border-bottom: 1px solid #d1d5db; padding-bottom: 1em; margin-bottom: 1.5em; }}
header h1 {{ margin: 0; font-size: 1.25em; }}
header h1 a {{ color: #0366d6; text-decoration: none; }}
header h1 a:hover {{ text-decoration: underline; }}
nav {{ margin-top: 0.5em; font-size: 0.9em; }}
nav a {{ color: #656d76; text-decoration: none; margin-right: 1em; }}
nav a:hover {{ color: #0366d6; }}
h1, h2, h3, h4 {{ color: #1f2328; margin-top: 1.5em; }}
h1:first-child {{ margin-top: 0; }}
a {{ color: #0366d6; }}
code {{ background: #f6f8fa; padding: 0.15em 0.3em; border-radius: 3px; font-size: 0.9em; }}
pre {{ background: #f6f8fa; padding: 1em; overflow: auto; border-radius: 6px; }}
pre code {{ background: none; padding: 0; }}
table {{ border-collapse: collapse; margin: 1em 0; }}
th, td {{ border: 1px solid #d1d5db; padding: 0.4em 0.8em; }}
th {{ background: #f6f8fa; }}
img {{ max-width: 100%; }}
.breadcrumb {{ font-size: 0.85em; color: #656d76; margin-bottom: 1em; }}
.breadcrumb a {{ color: #656d76; }}
ul, ol {{ padding-left: 1.5em; }}
li {{ margin: 0.25em 0; }}
.plugin_note {{ background: #f0f4f8; border-left: 4px solid #0366d6; padding: 0.75em 1em; margin: 1em 0; border-radius: 3px; }}
abbr {{ text-decoration: underline dotted; cursor: help; }}
@media (prefers-color-scheme: dark) {{
  body {{ background: #0d1117; color: #e6edf3; }}
  .archive-banner {{ background: #3d2e00; border-color: #6e5600; }}
  .archive-banner strong {{ color: #f0c000; }}
  header {{ border-bottom-color: #30363d; }}
  header h1 a {{ color: #58a6ff; }}
  nav a {{ color: #8b949e; }}
  nav a:hover {{ color: #58a6ff; }}
  h1, h2, h3, h4 {{ color: #e6edf3; }}
  a {{ color: #58a6ff; }}
  code, pre {{ background: #161b22; }}
  th, td {{ border-color: #30363d; }}
  th {{ background: #161b22; }}
  .breadcrumb, .breadcrumb a {{ color: #8b949e; }}
  .plugin_note {{ background: #161b22; border-color: #58a6ff; }}
}}
</style>
</head>
<body>
<div class="archive-banner">
<strong>Archive Notice:</strong> This is a read-only archive of the CSS Working Group Wiki.
The original wiki was hosted at wiki.csswg.org.
</div>
<header>
<h1><a href="{home_path}">CSS Working Group Wiki</a></h1>
<nav>
<a href="{home_path}">Home</a>
<a href="{home_path}spec/">Specs</a>
<a href="{home_path}ideas/">Ideas</a>
<a href="{home_path}test/">Testing</a>
<a href="{home_path}wiki/">About</a>
</nav>
</header>
{breadcrumb}
<main>
{content}
</main>
</body>
</html>
'''


def extract_content(html, page_path):
    """Extract the main content from a DokuWiki page."""
    # Find content between wikipage start/stop comments
    m = re.search(r'<!-- wikipage start -->\s*(.*?)\s*<!-- wikipage stop -->', html, re.DOTALL)
    if not m:
        # Fallback: find the page div
        m = re.search(r'<div class="page"[^>]*>(.*?)</div>\s*(?:<div class="docInfo"|</div>\s*</div>\s*<div class="clearer")', html, re.DOTALL)

    content = m.group(1).strip() if m else "<p>Content could not be extracted.</p>"

    # Extract title from first h1 or page title
    title_m = re.search(r'<h1[^>]*>([^<]+)</h1>', content)
    if not title_m:
        title_m = re.search(r'<title>\s*([^<\[]+)', html)
    title = title_m.group(1).strip() if title_m else page_path

    # Clean up content
    # Remove edit section buttons
    content = re.sub(r'<div class="secedit[^>]*>.*?</div>', '', content, flags=re.DOTALL)
    # Remove TOC toggle buttons
    content = re.sub(r'<div class="tocheader[^>]*>.*?</div>', '', content, flags=re.DOTALL)
    # Remove section edit IDs
    content = re.sub(r' id="[^"]*sectionedit[^"]*"', '', content)
    content = re.sub(r' class="sectionedit\d+"', '', content)

    # Remove wiki-specific link classes
    content = re.sub(r' class="wikilink\d?"', '', content)
    content = re.sub(r' data-wiki-id="[^"]*"', '', content)
    # External link class cleanup
    content = re.sub(r' class="urlextern"', '', content)
    content = re.sub(r' rel="ugc nofollow"', ' rel="noopener"', content)

    # Clean up div wrappers that are just for layout
    content = re.sub(r'<div class="level\d+">\s*', '', content)
    content = re.sub(r'\s*</div>\s*(?=<h[1-6]|<ul|<ol|<p|$)', '', content)
    content = re.sub(r'<div class="li">\s*', '', content)
    content = re.sub(r'\s*</div>\s*</li>', '</li>', content)

    return title, content


def make_breadcrumb(page_path, home_path):
    """Generate breadcrumb navigation."""
    if page_path in ('main', ''):
        return ''

    parts = page_path.split('/')
    crumbs = [f'<a href="{home_path}">Home</a>']
    for i, part in enumerate(parts[:-1]):
        path = "../" * (len(parts) - i - 1)
        crumbs.append(f'<a href="{path}">{part}</a>')
    crumbs.append(parts[-1])

    return f'<div class="breadcrumb">{" / ".join(crumbs)}</div>'


def fix_internal_links(content, home_path):
    """Convert absolute wiki links to relative paths."""
    # Fix internal wiki links: /page -> {home_path}page/
    def fix_link(m):
        path = m.group(1)
        query = m.group(2) or ""
        fragment = m.group(3) or ""
        if not path.endswith("/"):
            path += "/"
        return f'href="{home_path}{path}{query}{fragment}"'
    content = re.sub(r'href="/([a-z][^"#?]*)(\?[^"#]*)?(#[^"]*)?"', fix_link, content)
    return content


def save_page(output_dir, page_path, html):
    """Process and save a page."""
    title, content = extract_content(html, page_path)

    # Calculate depth for relative paths
    if page_path == 'main':
        depth = 0
        home_path = "./"
        out_path = output_dir / 'index.html'
    else:
        depth = len(page_path.split('/'))
        home_path = "../" * depth
        out_dir = output_dir / page_path
        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / 'index.html'

    breadcrumb = make_breadcrumb(page_path, home_path)
    content = fix_internal_links(content, home_path)

    output = PAGE_TEMPLATE.format(
        title=title,
        content=content,
        breadcrumb=breadcrumb,
        home_path=home_path
    )

    out_path.write_text(output, encoding='utf-8')


def main():
    if len(sys.argv) > 1:
        output_dir = Path(sys.argv[1])
    else:
        output_dir = Path(".")

    output_dir.mkdir(parents=True, exist_ok=True)

    pages = get_all_pages()
    print(f"\nFound {len(pages)} pages. Starting download...\n")

    # Always include 'main' as the homepage
    if 'main' not in pages:
        pages = ['main'] + list(pages)

    for i, page in enumerate(pages):
        print(f"[{i+1}/{len(pages)}] {page}")
        time.sleep(DELAY)

        html = fetch(f"{BASE_URL}/{page}")
        if html:
            save_page(output_dir, page, html)

    print(f"\nDone! Static site written to {output_dir}")
    print(f"Preview with: python3 -m http.server -d {output_dir}")


if __name__ == "__main__":
    main()
