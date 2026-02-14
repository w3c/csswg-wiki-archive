#!/usr/bin/env python3
"""
Crawl wiki.csswg.org and update README.md with last-modified dates.

Outputs a markdown table grouped by year and path, excluding pages that were
bulk-imported on 2014/12/09.
"""

import re
import sys
import time
import urllib.request
from collections import defaultdict
from datetime import datetime
from pathlib import Path

BASE_URL = "https://wiki.csswg.org"
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
DELAY = 0.3


def fetch(url):
    """Fetch a URL with proper headers."""
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return resp.read().decode("utf-8", errors="replace")
    except Exception as e:
        print(f"  Error fetching {url}: {e}", file=sys.stderr)
        return None


def get_all_pages():
    """Discover all wiki pages by crawling the index."""
    pages = set()
    namespaces = set()

    print("Fetching main index...", file=sys.stderr)
    html = fetch(f"{BASE_URL}/?do=index")
    if not html:
        return []

    for m in re.finditer(r'\?idx=([a-z0-9_-]+)', html):
        namespaces.add(m.group(1))

    for m in re.finditer(r'href="/([a-z0-9_-]+)"', html):
        page = m.group(1)
        if page not in ('lib', '_export', '_detail', '_media') and not page.startswith('feed'):
            pages.add(page)

    for ns in sorted(namespaces):
        print(f"Expanding: {ns}", file=sys.stderr)
        time.sleep(DELAY)
        html = fetch(f"{BASE_URL}/?do=index&idx={ns}")
        if html:
            for m in re.finditer(r'href="/([^"?#]+)"', html):
                p = m.group(1)
                if not p.startswith(('lib/', '_', 'feed')) and '?' not in p:
                    pages.add(p)
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


def extract_lastmod(html):
    """Extract last-modified timestamp from page HTML."""
    m = re.search(r'Last modified:\s*(\d{4}/\d{2}/\d{2}\s+\d{2}:\d{2})\s+by\s+<bdi>([^<]+)</bdi>', html)
    if m:
        return m.group(1), m.group(2)
    m = re.search(r'Last modified:\s*(\d{4}/\d{2}/\d{2}\s+\d{2}:\d{2})\s+by\s+(\S+)', html)
    if m:
        return m.group(1), m.group(2)
    return None, None


def generate_table(entries):
    """Generate the markdown table from entries."""
    lines = []
    lines.append("## Last Modified Dates")
    lines.append("")
    lines.append(f"Generated: {datetime.now().strftime('%Y-%m-%d')}")
    lines.append("")
    lines.append("This listing excludes 166 pages that were bulk-imported on 2014/12/09.")
    lines.append("")
    lines.append("| Year | Count | Path | Pages |")
    lines.append("|------|-------|------|-------|")

    # Group by year, then by path prefix
    by_year = defaultdict(lambda: defaultdict(list))
    for year, date, page in entries:
        if '/' in page:
            prefix = page.split('/')[0]
        else:
            prefix = '(root)'
        by_year[year][prefix].append(page)

    years = sorted(by_year.keys(), reverse=True)
    for year in years:
        prefixes = by_year[year]
        total = sum(len(pages) for pages in prefixes.values())
        sorted_prefixes = sorted(prefixes.keys(), key=lambda x: (x == '(root)', x))

        first_row = True
        for prefix in sorted_prefixes:
            pages = prefixes[prefix]
            path_label = "(root)" if prefix == '(root)' else f"{prefix}/"
            links = ", ".join(
                f"[{p.split('/')[-1] if '/' in p else p}](https://wiki.csswg.org/{p})"
                for p in pages
            )

            if first_row:
                lines.append(f"| {year} | {total} | {path_label} | {links} |")
                first_row = False
            else:
                lines.append(f"| | | {path_label} | {links} |")

    lines.append("")
    lines.append("To regenerate this listing:")
    lines.append("")
    lines.append("```bash")
    lines.append("python3 bin/list-timestamps.py")
    lines.append("```")

    return "\n".join(lines)


def update_readme(table_content):
    """Update README.md with the new table content."""
    script_dir = Path(__file__).parent
    readme_path = script_dir.parent / "README.md"

    if not readme_path.exists():
        print(f"Error: {readme_path} not found", file=sys.stderr)
        sys.exit(1)

    content = readme_path.read_text(encoding="utf-8")

    # Replace the "Last Modified Dates" section
    pattern = r'## Last Modified Dates\n.*?(?=\n## [A-Z]|\Z)'
    new_content = re.sub(pattern, table_content + "\n", content, flags=re.DOTALL)

    if new_content == content:
        print("Warning: No changes made to README.md", file=sys.stderr)
    else:
        readme_path.write_text(new_content, encoding="utf-8")
        print(f"Updated {readme_path}", file=sys.stderr)


def main():
    pages = get_all_pages()
    if 'main' not in pages:
        pages = ['main'] + list(pages)

    print(f"\nFound {len(pages)} pages. Fetching timestamps...\n", file=sys.stderr)

    entries = []
    for i, page in enumerate(pages):
        print(f"[{i+1}/{len(pages)}] {page}", file=sys.stderr)
        time.sleep(DELAY)

        html = fetch(f"{BASE_URL}/{page}")
        if html:
            date, author = extract_lastmod(html)
            if date and not date.startswith("2014/12/09"):
                entries.append((date.split('/')[0], date, page))

    # Sort by date descending
    entries.sort(key=lambda x: x[1], reverse=True)

    table_content = generate_table(entries)
    update_readme(table_content)


if __name__ == "__main__":
    main()
