(() => {
  'use strict';

  let searchIndex = null;
  let searchData = null;
  const resultsContainer = document.getElementById('search-results');
  const searchInput = document.getElementById('search-input');
  const searchForm = document.getElementById('search-form');

  // Get base URL from the search form action
  const baseUrl = searchForm.action.replace(/\/search\/$/, '');

  // Load search data and build index
  async function loadSearchIndex() {
    if (searchIndex) return;

    const response = await fetch(`${baseUrl}/search.json`);
    searchData = await response.json();

    searchIndex = lunr(function() {
      this.ref('url');
      this.field('title', { boost: 10 });
      this.field('content');

      searchData.forEach(doc => this.add(doc));
    });
  }

  // Escape HTML to prevent XSS
  function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
  }

  // Extract excerpt around first match and highlight terms
  function getExcerpt(content, terms) {
    const lowerContent = content.toLowerCase();
    let position = -1;

    for (const term of terms) {
      const pos = lowerContent.indexOf(term.toLowerCase());
      if (pos !== -1 && (position === -1 || pos < position)) {
        position = pos;
      }
    }

    if (position === -1) position = 0;

    const start = Math.max(0, position - 60);
    const end = Math.min(content.length, position + 200);
    let excerpt = content.substring(start, end);

    if (start > 0) excerpt = '…' + excerpt;
    if (end < content.length) excerpt += '…';

    // Highlight matching terms
    let highlighted = escapeHtml(excerpt);
    for (const term of terms) {
      const regex = new RegExp(`(${term.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')})`, 'gi');
      highlighted = highlighted.replace(regex, '<mark>$1</mark>');
    }

    return highlighted;
  }

  // Display search results
  function displayResults(results, query) {
    if (!results.length) {
      resultsContainer.innerHTML = `<p class="search-no-results">No results found for "${escapeHtml(query)}"</p>`;
      return;
    }

    const terms = query.toLowerCase().split(/\s+/).filter(t => t.length > 1);
    const count = results.length;
    const plural = count === 1 ? '' : 's';

    let html = `<p class="search-summary">Found ${count} result${plural} for "${escapeHtml(query)}"</p>`;
    html += '<ul class="search-results-list">';

    for (const result of results) {
      const doc = searchData.find(d => d.url === result.ref);
      if (!doc) continue;

      const excerpt = getExcerpt(doc.content, terms);
      const path = doc.url.replace(/^\/csswg-wiki/, '').replace(/\/$/, '') || '/';

      html += `
        <li class="search-result">
          <a href="${escapeHtml(doc.url)}" class="search-result-title">${escapeHtml(doc.title)}</a>
          <span class="search-result-path">${escapeHtml(path)}</span>
          <p class="search-result-excerpt">${excerpt}</p>
        </li>`;
    }

    html += '</ul>';
    resultsContainer.innerHTML = html;
  }

  // Perform search
  async function doSearch(query) {
    if (!query || query.length < 2) {
      resultsContainer.innerHTML = '<p class="search-hint">Enter at least 2 characters to search.</p>';
      return;
    }

    resultsContainer.innerHTML = '<p class="search-loading">Searching…</p>';

    try {
      await loadSearchIndex();

      let results;
      try {
        results = searchIndex.search(query);
      } catch {
        // Handle Lunr parse errors by doing a simpler search
        results = searchIndex.search(query.replace(/[^\w\s]/g, ''));
      }

      displayResults(results, query);
    } catch (err) {
      resultsContainer.innerHTML = '<p class="search-error">Error loading search index.</p>';
      console.error(err);
    }
  }

  // Handle form submission
  searchForm.addEventListener('submit', e => {
    e.preventDefault();
    const query = searchInput.value.trim();
    history.replaceState(null, '', `?q=${encodeURIComponent(query)}`);
    doSearch(query);
  });

  // Check for query parameter on page load
  const params = new URLSearchParams(window.location.search);
  const initialQuery = params.get('q');
  if (initialQuery) {
    searchInput.value = initialQuery;
    doSearch(initialQuery);
  }
})();
