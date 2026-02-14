// Wrap known abbreviations in <abbr> tags with tooltips
(function() {
  const abbreviations = {
    'CSS': 'Cascading Style Sheets',
    'HTML': 'HyperText Markup Language',
    'W3C': 'World Wide Web Consortium',
    'IRC': 'Internet Relay Chat',
    'URL': 'Uniform Resource Locator',
    'GUI': 'Graphical User Interface'
  };

  // Build regex pattern matching whole words only
  const pattern = new RegExp(
    '\\b(' + Object.keys(abbreviations).join('|') + ')\\b',
    'g'
  );

  function processTextNode(node) {
    const text = node.textContent;
    if (!pattern.test(text)) return;

    // Reset regex lastIndex
    pattern.lastIndex = 0;

    const fragment = document.createDocumentFragment();
    let lastIndex = 0;
    let match;

    while ((match = pattern.exec(text)) !== null) {
      // Add text before match
      if (match.index > lastIndex) {
        fragment.appendChild(
          document.createTextNode(text.slice(lastIndex, match.index))
        );
      }

      // Create <abbr> element
      const abbr = document.createElement('abbr');
      abbr.textContent = match[1];
      abbr.title = abbreviations[match[1]];
      fragment.appendChild(abbr);

      lastIndex = pattern.lastIndex;
    }

    // Add remaining text
    if (lastIndex < text.length) {
      fragment.appendChild(document.createTextNode(text.slice(lastIndex)));
    }

    node.parentNode.replaceChild(fragment, node);
  }

  function walkTextNodes(root) {
    const walker = document.createTreeWalker(
      root,
      NodeFilter.SHOW_TEXT,
      {
        acceptNode: function(node) {
          // Skip script, style, code, pre, abbr elements
          const parent = node.parentNode;
          const tag = parent.tagName;
          if (tag === 'SCRIPT' || tag === 'STYLE' || tag === 'CODE' ||
              tag === 'PRE' || tag === 'ABBR' || tag === 'A') {
            return NodeFilter.FILTER_REJECT;
          }
          return NodeFilter.FILTER_ACCEPT;
        }
      }
    );

    const nodes = [];
    while (walker.nextNode()) {
      nodes.push(walker.currentNode);
    }

    // Process in reverse to avoid index issues
    nodes.forEach(processTextNode);
  }

  // Run when DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function() {
      walkTextNodes(document.querySelector('main'));
    });
  } else {
    walkTextNodes(document.querySelector('main'));
  }
})();
