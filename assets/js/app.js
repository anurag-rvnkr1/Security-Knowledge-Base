(() => {
  'use strict';

  const REPO = 'anurag-rvnkr1/Security-Knowledge-Base';
  const BRANCH = 'main';
  const HOME_TITLE = 'Security Knowledge Base | Cybersecurity Documentation Portal';
  const HOME_DESCRIPTION = document.querySelector('meta[name="description"]')?.content || '';
  const $ = (selector, scope = document) => scope.querySelector(selector);
  const $$ = (selector, scope = document) => [...scope.querySelectorAll(selector)];
  const escapeHTML = value => String(value).replace(/[&<>"']/g, char => ({
    '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;'
  })[char]);
  const stopWords = new Set([
    'a', 'about', 'after', 'all', 'also', 'an', 'and', 'any', 'are', 'as', 'at',
    'be', 'because', 'been', 'before', 'between', 'both', 'but', 'by', 'can',
    'could', 'did', 'do', 'does', 'each', 'for', 'from', 'had', 'has', 'have',
    'how', 'if', 'in', 'into', 'is', 'it', 'its', 'may', 'more', 'most', 'must',
    'not', 'of', 'on', 'one', 'or', 'our', 'over', 'should', 'such', 'than',
    'that', 'the', 'their', 'them', 'then', 'there', 'these', 'they', 'this',
    'those', 'through', 'to', 'under', 'up', 'use', 'used', 'using', 'was',
    'we', 'were', 'what', 'when', 'where', 'which', 'while', 'who', 'will',
    'with', 'you', 'your'
  ]);
  const state = {
    catalogue: null,
    docs: [],
    category: '',
    searchIndex: null,
    searchPromise: null,
    searchSequence: 0,
    routeSequence: 0,
    abortController: null,
    currentPath: '',
    opener: null,
    wasReaderOpen: false
  };

  function docURL(path, fragment = '') {
    const url = new URL('index.html', document.baseURI);
    url.searchParams.set('doc', path);
    if (fragment) url.hash = fragment;
    return `${url.pathname}${url.search}${url.hash}`;
  }

  function githubURL(path) {
    return `https://github.com/${REPO}/blob/${BRANCH}/` +
      path.split('/').map(encodeURIComponent).join('/');
  }

  function githubTreeURL(path) {
    return `https://github.com/${REPO}/tree/${BRANCH}/` +
      path.split('/').filter(Boolean).map(encodeURIComponent).join('/');
  }

  function localPath(path) {
    return path.split('/').map(encodeURIComponent).join('/');
  }

  function categoryFor(path) {
    return state.docs.find(doc => doc.path === path)?.category ||
      state.catalogue.categories.find(category =>
        path === category.path || path.startsWith(`${category.path}/`)
      );
  }

  function iconFor(name) {
    const icons = {
      'API-Security': 'API', 'Active-Directory': 'AD', 'CTF-Writeups': 'CTF',
      Cheatsheets: 'REF', 'Cloud-Security': 'CLOUD', Containers: 'BOX',
      Cryptography: 'KEY', 'Detection-Engineering': 'DET', DevSecOps: 'CI',
      'Digital-Forensics': 'DFIR', 'Email-Security': 'MAIL',
      'Endpoint-Security': 'END', 'Identity-and-Access-Management': 'IAM',
      'Incident-Response': 'IR', Kubernetes: 'K8S', Labs: 'LAB', Linux: 'NIX',
      'MITRE-ATTACK': 'ATT&CK', 'Malware-Analysis': 'MAL',
      'Network-Security': 'NET', Networking: 'NET', OSINT: 'OSINT',
      OWASP: 'APPSEC', Resources: 'DOC', 'Reverse-Engineering': 'REV',
      SIEM: 'SIEM', SOC: 'SOC', 'Security-Architecture': 'ARCH',
      'Security-Automation': 'AUTO', 'Threat-Hunting': 'HUNT',
      'Threat-Intelligence': 'TI', 'Vulnerability-Management': 'VM',
      'Web-Security': 'WEB', Windows: 'WIN'
    };
    return icons[name] || 'DOC';
  }

  async function loadCatalogue() {
    const response = await fetch('site/content.json', { cache: 'no-cache' });
    if (!response.ok) throw new Error(`Catalogue request failed (${response.status})`);
    const catalogue = await response.json();
    if (catalogue.version !== 2 || !Array.isArray(catalogue.categories)) {
      throw new Error('Catalogue schema is missing or outdated.');
    }
    state.catalogue = catalogue;
    state.docs = catalogue.categories.flatMap(category =>
      category.documents.map(doc => ({ ...doc, category }))
    );
  }

  function render() {
    const categories = state.catalogue.categories;
    const find = path => categories.find(category => category.path === path);
    const labs = find('Labs');
    const ctf = find('CTF-Writeups');
    const cheatsheets = find('Cheatsheets');
    const stats = [
      [categories.length, 'Knowledge Domains'],
      [state.docs.length, 'Markdown Documents'],
      [labs?.documents.length || 0, 'Labs'],
      [ctf?.documents.length || 0, 'CTF Documents'],
      [cheatsheets?.documents.length || 0, 'Cheatsheets']
    ];
    $('#stats').innerHTML = stats.map(([value, label]) =>
      `<div class="stat"><strong>${value}</strong><small>${escapeHTML(label)}</small></div>`
    ).join('');
    $('#termstats').innerHTML = stats.slice(0, 4).map(([value, label]) =>
      `<div class="termstat"><strong>${value}</strong><small>${escapeHTML(label)}</small></div>`
    ).join('');

    const selectable = categories.filter(category => category.documents.length);
    $('#filter').innerHTML = '<option value="">All domains</option>' +
      selectable.map(category =>
        `<option value="${escapeHTML(category.path)}">${escapeHTML(category.name)}</option>`
      ).join('');
    renderDomains();

    const list = category => category?.documents.slice(0, 7).map(doc =>
      `<div class="item"><a href="${docURL(doc.path)}">${escapeHTML(doc.title)}</a>` +
      `<small>${escapeHTML(doc.path.split('/').slice(0, -1).join(' / '))}</small></div>`
    ).join('') || '<p class="empty">No indexed documents.</p>';
    $('#labsPanel').innerHTML = list(labs);
    $('#ctfPanel').innerHTML = list(ctf);
    $('#cheatPanel').innerHTML = (cheatsheets?.documents || []).slice(0, 12).map(doc =>
      `<a href="${docURL(doc.path)}"><b>${escapeHTML(doc.title)}</b>` +
      '<span>Open source document →</span></a>'
    ).join('');

    $('#paths').innerHTML = (state.catalogue.learningPaths || []).map(path =>
      `<article class="path"><h3>${escapeHTML(path.name)}</h3><ol>` +
      path.documents.map(documentPath => {
        const doc = state.docs.find(item => item.path === documentPath);
        return doc ? `<li><a class="step" href="${docURL(doc.path)}">${escapeHTML(doc.title)}</a></li>` : '';
      }).join('') +
      '</ol></article>'
    ).join('');
  }

  function renderDomains() {
    const query = ($('#domainSearch').value || '').trim().toLocaleLowerCase();
    const categories = state.catalogue.categories.filter(category =>
      category.documents.length &&
      (!state.category || category.path === state.category) &&
      (!query || `${category.name} ${category.description} ` +
        category.documents.map(doc => doc.title).join(' ').toLocaleLowerCase().includes(query))
    );
    $('#domainsGrid').innerHTML = categories.length ? categories.map(category => {
      const first = category.documents.find(doc => doc.kind === 'index') ||
        category.documents.find(doc => doc.kind !== 'index') || category.documents[0];
      return `<article class="card"><div class="icon" aria-hidden="true">${escapeHTML(iconFor(category.path))}</div>` +
        `<h3>${escapeHTML(category.name)}</h3><p>${escapeHTML(category.description)}</p>` +
        `<div class="cardfoot"><span>${category.documents.length} documents</span>` +
        `<a href="${docURL(first.path)}">Start reading →</a></div></article>`;
    }).join('') : '<p class="empty">No domains match the current filter.</p>';
  }

  function searchTokens(query) {
    const matches = query.normalize('NFKC').toLocaleLowerCase().match(
      /\.?[\p{L}\p{N}]+(?:[+#]+|(?:[.&/-][\p{L}\p{N}]+)*)/gu
    ) || [];
    return [...new Set(matches.filter(token => !stopWords.has(token) && token.length > 1))];
  }

  async function loadSearchIndex() {
    if (state.searchIndex) return state.searchIndex;
    if (!state.searchPromise) {
      state.searchPromise = (async () => {
        const response = await fetch('site/search-index.json', { cache: 'force-cache' });
        if (!response.ok) throw new Error(`Search index request failed (${response.status})`);
        const index = await response.json();
        const catalogueDocs = state.docs;
        if (index.version !== 1 || index.catalogueVersion !== state.catalogue.version ||
            !Array.isArray(index.documents) ||
            index.documents.length !== catalogueDocs.length ||
            index.documents.some((doc, i) =>
              doc.path !== catalogueDocs[i].path || doc.title !== catalogueDocs[i].title
            ) || !index.terms || typeof index.terms !== 'object') {
          throw new Error('Search index does not match the catalogue. Please reload the handbook.');
        }
        state.searchIndex = index;
        return index;
      })().catch(error => {
        state.searchPromise = null;
        throw error;
      });
    }
    return state.searchPromise;
  }

  function escapeRegExp(value) {
    return value.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  }

  function highlight(text, tokens) {
    let result = escapeHTML(text);
    for (const token of tokens) {
      const escaped = escapeHTML(token);
      result = result.replace(new RegExp(`(${escapeRegExp(escaped)})`, 'giu'), '<mark>$1</mark>');
    }
    return result;
  }

  function renderSearchResults(query, tokens, index) {
    const resultElement = $('#searchResults');
    if (!query.trim()) {
      resultElement.hidden = true;
      resultElement.innerHTML = '';
      return;
    }
    resultElement.hidden = false;
    if (!tokens.length) {
      resultElement.innerHTML = '<p>Enter a topic, acronym, tool, or technique to search the handbook.</p>';
      return;
    }

    const scores = new Map();
    for (const token of tokens) {
      for (const [docId, titleCount, headingCount, bodyCount] of index.terms[token] || []) {
        const entry = scores.get(docId) || { score: 0, coverage: 0 };
        entry.coverage += 1;
        entry.score += titleCount * 12 + headingCount * 6 + Math.min(bodyCount, 4);
        scores.set(docId, entry);
      }
    }
    const normalizedQuery = query.normalize('NFKC').trim().toLocaleLowerCase();
    const results = [...scores.entries()]
      .filter(([docId]) => {
        const doc = index.documents[docId];
        return doc && (!state.category || doc.collection === state.category);
      })
      .map(([docId, result]) => {
        const doc = index.documents[docId];
        const title = doc.title.toLocaleLowerCase();
        const phraseBoost = title === normalizedQuery ? 32 :
          title.startsWith(normalizedQuery) ? 20 :
            title.includes(normalizedQuery) ? 12 : 0;
        return { ...doc, ...result, score: result.score + phraseBoost };
      })
      .sort((a, b) =>
        b.coverage - a.coverage || b.score - a.score || a.title.localeCompare(b.title)
      );

    if (!results.length) {
      resultElement.innerHTML = '<p class="search-count">No results for ' +
        `<strong>${escapeHTML(query)}</strong>. Try fewer words, a common acronym, or a related term.</p>`;
      return;
    }
    const shown = results.slice(0, 12);
    resultElement.innerHTML = `<p class="search-count" role="status">${results.length} result${results.length === 1 ? '' : 's'}; ` +
      `showing ${shown.length} for <strong>${escapeHTML(query)}</strong></p>` +
      `<ol>${shown.map(result => {
        const matchingHeading = result.headings.find(heading =>
          tokens.some(token => heading.toLocaleLowerCase().includes(token))
        );
        const context = matchingHeading || result.snippet || result.collection;
        const category = state.catalogue.categories.find(item => item.path === result.collection);
        return `<li><a href="${docURL(result.path)}">${highlight(result.title, tokens)}</a>` +
          `<small>${escapeHTML(category?.name || result.collection)}</small>` +
          `<p>${highlight(context, tokens)}</p></li>`;
      }).join('')}</ol>`;
  }

  async function search(query) {
    const sequence = ++state.searchSequence;
    if (!query.trim()) {
      renderSearchResults('', [], { terms: {} });
      return;
    }
    $('#searchResults').hidden = false;
    $('#searchResults').innerHTML = '<p role="status">Searching the handbook…</p>';
    try {
      const index = await loadSearchIndex();
      if (sequence !== state.searchSequence) return;
      renderSearchResults(query, searchTokens(query), index);
    } catch (error) {
      if (sequence !== state.searchSequence) return;
      console.error(error);
      $('#searchResults').hidden = false;
      $('#searchResults').innerHTML = '<p role="status">Search is temporarily unavailable. ' +
        '<button type="button" id="retrySearch">Retry</button></p>';
    }
  }

  function route() {
    const path = new URLSearchParams(location.search).get('doc');
    if (path) openDocument(path, decodeFragment(location.hash.slice(1)));
    else closeReader(false);
  }

  function decodeFragment(fragment) {
    try {
      return decodeURIComponent(fragment);
    } catch {
      return fragment;
    }
  }

  function readerError(message, doc) {
    const recovery = doc
      ? `<a href="${githubURL(doc.path)}" target="_blank" rel="noopener noreferrer">Open the source on GitHub</a>`
      : '<a href="./">Return to the handbook</a>';
    const retry = doc ? '<p><button type="button" id="retryDocument">Retry loading document</button></p>' : '';
    $('#article').innerHTML = `<div class="empty"><h2>Document unavailable</h2>` +
      `<p>${escapeHTML(message)}</p><p>${recovery}</p>${retry}` +
      '<a href="./">Return to the handbook</a></div>';
    $('#toc').innerHTML = '<p class="muted">Contents unavailable.</p>';
    $('#docnav').innerHTML = '';
  }

  function openDocument(path, fragment = '', force = false) {
    const doc = state.docs.find(item => item.path === path);
    if (!doc) {
      showReader();
      state.currentPath = '';
      $('#meta').textContent = 'Unknown document';
      $('#crumb').textContent = 'Handbook';
      $('#source').hidden = true;
      document.title = `Document unavailable | Security Knowledge Base`;
      readerError('This document is not present in the current catalogue. Return to the handbook or choose another collection.', null);
      $('#close').focus();
      return;
    }
    if (!force && state.currentPath === path && !$('#viewer').hidden) {
      if (fragment) {
        const target = document.getElementById(fragment);
        target?.scrollIntoView({ block: 'start' });
        target?.focus({ preventScroll: true });
      } else {
        $('#viewer').scrollTo({ top: 0 });
      }
      return;
    }
    if (state.abortController) state.abortController.abort();
    const requestId = ++state.routeSequence;
    state.abortController = new AbortController();
    state.currentPath = path;
    showReader();
    const category = doc.category;
    $('#meta').innerHTML = `<div class="metaTitle">${escapeHTML(doc.title)}</div>` +
      `<div class="metaCat">${escapeHTML(category.name)}</div>`;
    $('#crumb').textContent = `${category.name} / ${doc.title}`;
    $('#source').href = githubURL(doc.path);
    $('#source').hidden = false;
    $('#article').innerHTML = '<p class="loading" role="status">Loading document…</p>';
    $('#toc').innerHTML = '<p class="muted">Loading contents…</p>';
    document.title = `${doc.title} — ${category.name} | Security Knowledge Base`;
    const description = $('meta[name="description"]');
    if (description) description.content =
      `Read ${doc.title} in the ${category.name} cybersecurity handbook. The repository Markdown is the authoritative source.`;

    fetch(localPath(doc.path), { signal: state.abortController.signal })
      .then(response => {
        if (!response.ok) throw new Error(`The source returned HTTP ${response.status}.`);
        return response.text();
      })
      .then(markdown => {
        if (requestId !== state.routeSequence || state.currentPath !== path) return;
        if (!window.marked || !window.DOMPurify) {
          throw new Error('The Markdown renderer or sanitizer did not load. Check the connection and retry.');
        }
        const rendered = window.marked.parse(markdown, { gfm: true });
        $('#article').innerHTML = window.DOMPurify.sanitize(rendered, {
          USE_PROFILES: { html: true }
        });
        rewriteContentLinks(doc.path);
        buildTableOfContents();
        addCopyButtons();
        buildDocumentNavigation(doc);
        $('#article').scrollTop = 0;
        $('#viewer').scrollTop = 0;
        const target = fragment ? document.getElementById(fragment) : null;
        if (target) {
          target.tabIndex = -1;
          target.scrollIntoView({ block: 'start' });
          target.focus({ preventScroll: true });
        } else {
          const firstHeading = $('#article h1') || $('#article h2');
          if (firstHeading) {
            firstHeading.tabIndex = -1;
            firstHeading.focus({ preventScroll: true });
          }
        }
      })
      .catch(error => {
        if (error.name === 'AbortError' || requestId !== state.routeSequence) return;
        console.error(error);
        readerError(error.message || 'The source could not be loaded.', doc);
      });
  }

  function showReader() {
    if ($('#viewer').hidden) {
      state.opener = document.activeElement instanceof HTMLElement ? document.activeElement : null;
      $('#viewer').hidden = false;
      document.body.style.overflow = 'hidden';
      for (const element of $$('header, #main, footer')) element.inert = true;
    }
    state.wasReaderOpen = true;
  }

  function closeReader(updateHistory = true) {
    if ($('#viewer').hidden) return;
    if (updateHistory && new URLSearchParams(location.search).has('doc') && history.state?.doc) {
      history.back();
      return;
    }
    if (updateHistory && new URLSearchParams(location.search).has('doc')) {
      history.replaceState({}, '', `${location.pathname}${location.hash}`);
    }
    if (state.abortController) state.abortController.abort();
    state.routeSequence += 1;
    state.currentPath = '';
    $('#viewer').hidden = true;
    $('#viewer').classList.remove('toc-open');
    $('#tocbtn').setAttribute('aria-expanded', 'false');
    document.body.style.overflow = '';
    for (const element of $$('header, #main, footer')) element.inert = false;
    document.title = HOME_TITLE;
    const description = $('meta[name="description"]');
    if (description) description.content = HOME_DESCRIPTION;
    const target = state.opener?.isConnected ? state.opener : $('#search');
    target?.focus({ preventScroll: true });
    state.opener = null;
  }

  function slugHeading(text) {
    return text.normalize('NFKC').toLocaleLowerCase()
      .replace(/<[^>]*>/g, '')
      .replace(/[^\p{L}\p{N}_\-\s]/gu, '')
      .trim().replace(/\s+/g, '-');
  }

  function buildTableOfContents() {
    const headings = $$('h2, h3', $('#article'));
    const used = new Set();
    $('#toc').innerHTML = headings.length ? headings.map(heading => {
      let id = heading.id || slugHeading(heading.textContent);
      const base = id;
      let suffix = 1;
      while (!id || used.has(id)) id = `${base}-${suffix++}`;
      used.add(id);
      heading.id = id;
      return `<a class="l${heading.tagName.slice(1)}" href="#${encodeURIComponent(id)}">` +
        `${escapeHTML(heading.textContent)}</a>`;
    }).join('') : '<p class="muted">No section headings.</p>';
  }

  function rewriteContentLinks(sourcePath) {
    const sourceBase = new URL(localPath(sourcePath), document.baseURI);
    const siteBase = new URL('.', document.baseURI);
    for (const image of $$('img', $('#article'))) {
      const src = image.getAttribute('src');
      if (!src) continue;
      try {
        const target = new URL(src, sourceBase);
        if (target.origin === siteBase.origin) {
          image.src = target.href;
        } else if (!['http:', 'https:'].includes(target.protocol)) {
          image.removeAttribute('src');
        }
      } catch {
        image.removeAttribute('src');
      }
      image.loading = 'lazy';
      image.decoding = 'async';
    }
    for (const anchor of $$('a[href]', $('#article'))) {
      const href = anchor.getAttribute('href');
      if (!href) continue;
      try {
        const target = new URL(href, sourceBase);
        if (target.origin !== siteBase.origin) {
          if (!['http:', 'https:', 'mailto:', 'tel:'].includes(target.protocol)) {
            anchor.removeAttribute('href');
            continue;
          }
          anchor.target = '_blank';
          anchor.rel = 'noopener noreferrer';
          continue;
        }
        if (!target.pathname.startsWith(siteBase.pathname)) continue;
        const relativePath = decodeURIComponent(target.pathname.slice(siteBase.pathname.length));
        const markdownTarget = relativePath && /\.markdown?$/i.test(relativePath);
        const directory = target.pathname.endsWith('/');
        const collection = state.catalogue.categories.find(item =>
          item.path === relativePath.replace(/\/$/, '')
        );
        if (markdownTarget || directory || collection) {
          let destination = relativePath;
          if (directory || collection) {
            const start = collection?.documents.find(item => item.kind === 'index') ||
              collection?.documents.find(item => item.kind !== 'index');
            if (start) destination = start.path;
            else {
              anchor.href = `${githubTreeURL(relativePath)}${target.hash}`;
              anchor.target = '_blank';
              anchor.rel = 'noopener noreferrer';
              continue;
            }
          }
          if (state.docs.some(doc => doc.path === destination)) {
            anchor.href = docURL(destination, target.hash ? decodeFragment(target.hash.slice(1)) : '');
          } else {
            anchor.href = `${githubURL(destination)}${target.hash}`;
            anchor.target = '_blank';
            anchor.rel = 'noopener noreferrer';
          }
        } else {
          anchor.href = target.href;
        }
      } catch {
        anchor.removeAttribute('href');
      }
    }
  }

  function addCopyButtons() {
    for (const pre of $$('pre', $('#article'))) {
      if ($('.copy', pre)) continue;
      const button = document.createElement('button');
      button.className = 'copy';
      button.type = 'button';
      button.textContent = 'Copy';
      button.setAttribute('aria-label', 'Copy code block');
      button.addEventListener('click', async () => {
        const content = $('code', pre)?.innerText || pre.innerText;
        try {
          if (!navigator.clipboard?.writeText) throw new Error('Clipboard access is unavailable in this browser.');
          await navigator.clipboard.writeText(content);
          button.textContent = 'Copied';
          toast('Code copied to clipboard.');
          window.setTimeout(() => { button.textContent = 'Copy'; }, 1200);
        } catch (error) {
          toast(error.message || 'Could not copy this code block.');
        }
      });
      pre.append(button);
    }
  }

  function buildDocumentNavigation(doc) {
    const index = state.docs.findIndex(item => item.path === doc.path);
    const previous = state.docs[index - 1];
    const next = state.docs[index + 1];
    $('#docnav').innerHTML =
      (previous ? `<a href="${docURL(previous.path)}"><small>← PREVIOUS</small>${escapeHTML(previous.title)}</a>` : '<span></span>') +
      (next ? `<a href="${docURL(next.path)}"><small>NEXT →</small>${escapeHTML(next.title)}</a>` : '<span></span>');
  }

  function navigateToDocument(path, fragment = '') {
    if (!state.docs.some(doc => doc.path === path)) return;
    if (new URLSearchParams(location.search).get('doc') === path) {
      if (fragment) {
        const decoded = decodeFragment(fragment);
        history.pushState({ doc: path }, '', docURL(path, decoded));
        const target = document.getElementById(decoded);
        target?.scrollIntoView({ block: 'start' });
        target?.focus({ preventScroll: true });
      }
      return;
    }
    const decoded = decodeFragment(fragment);
    history.pushState({ doc: path }, '', docURL(path, decoded));
    openDocument(path, decoded);
  }

  function activateDocumentLinks(event) {
    const anchor = event.target.closest('a[href]');
    if (!anchor || anchor.target === '_blank' || event.defaultPrevented ||
        event.button !== 0 || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
    const target = new URL(anchor.href, location.href);
    if (target.origin !== location.origin || target.pathname !== new URL('index.html', document.baseURI).pathname) return;
    const path = target.searchParams.get('doc');
    if (!path) return;
    event.preventDefault();
    navigateToDocument(path, target.hash.slice(1));
    $('#nav').classList.remove('open');
    $('#menu').setAttribute('aria-expanded', 'false');
  }

  function trapFocus(event) {
    if (event.key !== 'Tab' || $('#viewer').hidden) return;
    const focusable = $$('a[href], button:not([disabled]), [tabindex="0"]', $('#viewer'))
      .filter(element => !element.hidden && element.getClientRects().length);
    if (!focusable.length) return;
    const first = focusable[0];
    const last = focusable[focusable.length - 1];
    if (event.shiftKey && document.activeElement === first) {
      event.preventDefault();
      last.focus();
    } else if (!event.shiftKey && document.activeElement === last) {
      event.preventDefault();
      first.focus();
    }
  }

  function toast(message) {
    const element = $('#toast');
    element.textContent = message;
    element.classList.add('show');
    window.setTimeout(() => element.classList.remove('show'), 2200);
  }

  function bindEvents() {
    $('#search').addEventListener('input', event => search(event.target.value));
    $('#search').addEventListener('keydown', event => {
      if (event.key === 'Enter') {
        const firstResult = $('#searchResults a');
        if (firstResult) firstResult.focus();
        else $('#searchResults').scrollIntoView({ behavior: 'smooth', block: 'nearest' });
      }
    });
    $('#domainSearch').addEventListener('input', renderDomains);
    $('#filter').addEventListener('change', event => {
      state.category = event.target.value;
      renderDomains();
      search($('#search').value);
    });
    $('#close').addEventListener('click', () => closeReader());
    $('#tocbtn').addEventListener('click', () => {
      const expanded = $('#tocbtn').getAttribute('aria-expanded') === 'true';
      $('#tocbtn').setAttribute('aria-expanded', String(!expanded));
      $('#viewer').classList.toggle('toc-open', !expanded);
    });
    $('#menu').addEventListener('click', () => {
      const open = $('#nav').classList.toggle('open');
      $('#menu').setAttribute('aria-expanded', String(open));
    });
    $('#searchResults').addEventListener('click', event => {
      if (event.target.closest('#retrySearch')) search($('#search').value);
    });
    $('#viewer').addEventListener('click', event => {
      if (event.target.closest('#retryDocument') && state.currentPath) {
        openDocument(state.currentPath, decodeFragment(location.hash.slice(1)), true);
        $('#article').focus({ preventScroll: true });
      }
    });
    document.addEventListener('click', activateDocumentLinks);
    document.addEventListener('keydown', event => {
      if (event.key === 'Escape' && !$('#viewer').hidden) {
        if ($('#viewer').classList.contains('toc-open') && matchMedia('(max-width: 950px)').matches) {
          $('#viewer').classList.remove('toc-open');
          $('#tocbtn').setAttribute('aria-expanded', 'false');
        } else closeReader();
      } else if (event.key === 'Tab') {
        trapFocus(event);
      } else if (event.key === '/' &&
          !['INPUT', 'TEXTAREA', 'SELECT'].includes(document.activeElement.tagName) &&
          $('#viewer').hidden) {
        event.preventDefault();
        $('#search').focus();
      }
    });
    window.addEventListener('popstate', route);
  }

  (async () => {
    try {
      await loadCatalogue();
      render();
      bindEvents();
      route();
    } catch (error) {
      console.error(error);
      $('#main').innerHTML = '<section class="section shell"><div class="empty">' +
        '<h2>Handbook catalogue unavailable</h2>' +
        '<p>The generated content catalogue could not be loaded. Refresh later or open the repository source.</p>' +
        `<a class="btn" href="https://github.com/${REPO}">Open repository</a></div></section>`;
    }
  })();
})();
