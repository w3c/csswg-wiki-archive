# CSS Working Group Wiki Archive

This is a read-only static archive of the [CSS Working Group Wiki](https://wiki.csswg.org/), originally hosted on DokuWiki at wiki.csswg.org.

**Live site:** https://w3c.github.io/csswg-wiki-archive/

## Contents

The archive contains 294 pages covering:

- **Specification Issues and Planning** (`/spec/`) — Wiki pages for tracking spec-related thoughts
- **Ideas and Resolutions** (`/ideas/`) — Ideas not yet in a spec
- **Testing** (`/test/`) — CSS testing documentation
- **Meeting Planning** (`/planning/`) — Face-to-face meeting plans and schedules
- **CSSWG Tools** (`/tools/`) — Documentation about working group tools

## Regenerating the Archive

The archive was generated using a Python scraper that crawls the DokuWiki site and produces static HTML files.

### Requirements

- Python 3.8+
- Network access to wiki.csswg.org

### Usage

```bash
# Scrape the wiki and output to a directory
python3 bin/scrape.py /path/to/output

# Or output to current directory
python3 bin/scrape.py .

# Preview locally
python3 -m http.server -d /path/to/output
```

The scraper:
1. Discovers all pages by crawling the DokuWiki index
2. Fetches each page and extracts the main content
3. Generates clean HTML with modern styling and dark mode support
4. Creates proper relative links for hosting at any URL path

### Rate Limiting

The scraper includes a 0.3-second delay between requests, to be nice to the server. A full scrape of ~294 pages takes approximately 2 minutes.

## Deployment

The site is automatically deployed to GitHub Pages via the workflow in `.github/workflows/deploy.yml` whenever changes are pushed to the `main` branch.

## License

The wiki content is governed by the [W3C Document License](https://www.w3.org/Consortium/Legal/2015/doc-license).
