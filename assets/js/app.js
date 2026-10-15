(() => {
  'use strict';

  const REPOSITORY = 'anurag-rvnkr1/Security-Knowledge-Base';
  const $ = (selector, scope = document) => scope.querySelector(selector);
  const state = {
    catalog: null,
    documents: [],
    documentByPath: new Map(),
    collectionById: new Map(),
    directoryIndexes: new Map(),
    assetPaths: new Set(),
    searchIndex: null,
    currentDocument: null,
    currentCollection: null,
    searchTimer: 0,
    requestId: 0,
    returnFocus: null,
    readerPreviousFocus: null,
    readerDirect: false,
    collectionDirect: false
  };

  const rootURL = new URL('./', window.location.href);
  const rootPath = rootURL.pathname;
  const kindLabels = {
    chapter: 'Chapter',
    'collection-index': 'Collection guide',
    lab: 'Lab',
    'ctf-writeup': 'CTF writeup',
    cheatsheet: 'Cheatsheet',
    template: 'Template',
    reference: 'Reference',
    document: 'Document'
  };

  function create(tag, className, text) {
    const element = document.createElement(tag);
    if (className) element.className = className;
    if (text !== undefined) element.textContent = text;
    return element;
  }

  function encodePath(path) {
    return path.split('/').map(part => encodeURIComponent(part)).join('/');
  }

  function localFileURL(path) {
    return new URL(encodePath(path), rootURL);
  }

  function sourceURL(path) {
    const branch = state.catalog?.generatedFrom || 'main';
    const encoded = encodePath(path);
    return `https://github.com/${REPOSITORY}/blob/${encodeURIComponent(branch)}/${encoded}`;
  }

  function getCollection(path) {
    const document = state.documentByPath.get(path);
    return document ? state.collectionById.get(document.collection) : null;
  }

  function orderedReadingDocuments(collection) {
    return collection.documents.filter(document =>
      document.type !== 'collection-index' && document.type !== 'template'
    );
  }

  function documentURL(path, fragment = '', resourceQuery = '') {
    const url = new URL('index.html', rootURL);
    url.searchParams.set('doc', path);
    if (resourceQuery) url.searchParams.set('_resourceQuery', resourceQuery);
    if (fragment) url.hash = fragment;
    return url;
  }

  function showElement(element, visible) {
    if (!element) return;
    element.hidden = !visible;
  }

  function setPageTitle(title = 'Security Knowledge Base | Cybersecurity Handbook') {
    document.title = title;
  }

  function updateHistory(url, data, replace = false) {
    const method = replace ? 'replaceState' : 'pushState';
    window.history[method]({ ...window.history.state, ...data }, '', url);
  }

  function categoryDisplay(document) {
    return state.collectionById.get(document.collection)?.name || document.collection;
  }

  function appendDocumentLink(container, document, options = {}) {
    const link = create('a', options.className || 'document-link');
    link.href = documentURL(document.path).href;
    link.dataset.documentPath = document.path;
    link.append(create('span', 'document-link-title', document.title));
    if (options.showCollection !== false) {
      link.append(create('span', 'document-link-meta', categoryDisplay(document)));
    }
    if (options.showKind !== false) {
      const kind = create('span', 'document-kind', kindLabels[document.type] || 'Document');
      link.append(kind);
    }
    container.append(link);
    return link;
  }

  function renderDocumentList(element, documents, emptyText = 'No documents are available in this collection yet.') {
    element.replaceChildren();
    if (!documents.length) {
      element.append(create('p', 'empty-state', emptyText));
      return;
    }
    for (const document of documents) appendDocumentLink(element, document);
  }

  function renderStats() {
    const stats = $('#stats');
    stats.replaceChildren();
    const types = state.catalog.stats.documentTypes;
    const values = [
      [state.catalog.stats.collections, 'Collections'],
      [state.catalog.stats.markdownDocuments, 'Indexed documents'],
      [types.chapter || 0, 'Chapters'],
      [types.lab || 0, 'Labs'],
      [types['ctf-writeup'] || 0, 'CTF writeups']
    ];
    for (const [value, label] of values) {
      const item = create('div', 'stat-item');
      item.append(create('strong', '', value.toLocaleString()));
      item.append(create('span', '', label));
      stats.append(item);
    }
  }

  function renderCollectionCards() {
    const cards = $('#domainsGrid');
    const filterSelect = $('#filter');
    const search = $('#domainSearch');
    if (filterSelect.options.length === 1) {
      for (const collection of state.catalog.collections) {
        const option = create('option', '', collection.name);
        option.value = collection.id;
        filterSelect.append(option);
      }
    }
    const query = search.value.trim().toLocaleLowerCase();
    cards.replaceChildren();
    const matching = state.catalog.collections.filter(collection =>
      (!filterSelect.value || collection.id === filterSelect.value) &&
      `${collection.name} ${collection.description} ${collection.id}`.toLocaleLowerCase().includes(query)
    );
    for (const collection of matching) {
      const link = create('a', 'collection-card');
      link.href = `index.html?collection=${encodeURIComponent(collection.id)}`;
      link.dataset.collectionId = collection.id;
      const top = create('span', 'collection-card-top');
      top.append(create('span', 'collection-index-label', collection.id === 'docs' ? 'GUIDANCE' : 'COLLECTION'));
      top.append(create('span', 'collection-count', `${collection.documentCount} ${collection.documentCount === 1 ? 'document' : 'documents'}`));
      link.append(top, create('h3', '', collection.name), create('p', '', collection.description));
      const arrow = create('span', 'collection-card-link', 'Open collection →');
      link.append(arrow);
      cards.append(link);
    }
    if (!matching.length) cards.append(create('p', 'empty-state', 'No collections match this filter.'));
  }

  function renderLearningPaths() {
    const root = $('#paths');
    root.replaceChildren();
    for (const path of state.catalog.learningPaths) {
      const card = create('article', 'path-card');
      card.append(create('h3', '', path.title), create('p', '', path.description));
      const steps = create('ol', 'path-steps');
      for (const step of path.steps) {
        const item = create('li');
        const document = state.documentByPath.get(step.path);
        if (!document) continue;
        const link = create('a', '', step.label);
        link.href = documentURL(step.path).href;
        link.dataset.documentPath = step.path;
        item.append(link);
        steps.append(item);
      }
      card.append(steps);
      root.append(card);
    }
  }

  function renderDiscovery() {
    const chapterDocs = state.documents.filter(document =>
      document.type === 'chapter' && !document.collection.startsWith('CTF-Writeups/')
    ).slice(0, 5);
    const labDocs = state.documents.filter(document => document.type === 'lab').slice(0, 4);
    const ctfDocs = state.documents.filter(document => document.type === 'ctf-writeup').slice(0, 4);
    const cheatDocs = state.documents.filter(document => document.type === 'cheatsheet').slice(0, 4);
    const resourceDocs = state.documents.filter(document => document.collection === 'Resources' && document.type !== 'collection-index').slice(0, 6);
    renderDocumentList($('#chapterList'), chapterDocs);
    renderDocumentList($('#labsPanel'), labDocs);
    renderDocumentList($('#ctfPanel'), ctfDocs, 'No standalone writeups are currently indexed; explore the challenge-category guides.');
    renderDocumentList($('#cheatPanel'), cheatDocs);
    renderDocumentList($('#resourcesPanel'), resourceDocs);
  }

  function renderHome() {
    renderStats();
    renderCollectionCards();
    renderLearningPaths();
    renderDiscovery();
  }

  function renderCollection(collectionId, focusHeading = false) {
    const collection = state.collectionById.get(collectionId);
    if (!collection) {
      hideCollection();
      showRouteError(`The collection “${collectionId}” is not in the generated catalogue.`);
      return;
    }
    hideRouteError();
    state.currentCollection = collection;
    $('#collectionTitle').textContent = collection.name;
    $('#collectionDescription').textContent = collection.description;
    $('#collectionPrerequisites').textContent = collection.prerequisites?.length
      ? `Useful background: ${collection.prerequisites.join('; ')}`
      : 'Start with the overview where available, then follow the numbered chapters in order.';

    const related = $('#relatedCollections');
    related.replaceChildren();
    if (collection.related?.length) {
      related.append(create('span', 'related-label', 'Related'));
      for (const id of collection.related) {
        const item = state.collectionById.get(id);
        if (!item) continue;
        const link = create('a', 'related-link', item.name);
        link.href = `index.html?collection=${encodeURIComponent(item.id)}`;
        link.dataset.collectionId = item.id;
        related.append(link);
      }
    }
    const learningPaths = state.catalog.learningPaths.filter(path =>
      path.steps.some(step => step.collection === collection.id)
    );
    if (learningPaths.length) {
      related.append(create('span', 'related-label', 'Learning paths'));
      for (const path of learningPaths) {
        const step = path.steps.find(item => item.collection === collection.id);
        const link = create('a', 'related-link', path.title);
        link.href = documentURL(step.path).href;
        link.dataset.documentPath = step.path;
        related.append(link);
      }
    }
    $('#collectionFilter').value = '';
    renderCollectionDocuments();
    showElement($('#collectionView'), true);
    document.body.classList.add('overlay-open');
    if (focusHeading) $('#collectionTitle').focus({ preventScroll: true });
    setPageTitle(`${collection.name} | Security Knowledge Base`);
  }

  function renderCollectionDocuments() {
    const collection = state.currentCollection;
    const container = $('#collectionDocuments');
    if (!collection) return;
    const query = $('#collectionFilter').value.trim().toLocaleLowerCase();
    const documents = collection.documents.filter(document => {
      if (!query) return true;
      return `${document.title} ${document.path} ${document.type} ${document.excerpt}`.toLocaleLowerCase().includes(query);
    });
    container.replaceChildren();
    if (!documents.length) {
      container.append(create('p', 'empty-state', 'No documents match this collection filter.'));
      return;
    }
    for (const document of documents) {
      const row = create('article', 'collection-document');
      const link = create('a', 'collection-document-title', document.title);
      link.href = documentURL(document.path).href;
      link.dataset.documentPath = document.path;
      row.append(link, create('span', 'document-kind', kindLabels[document.type] || 'Document'));
      if (document.excerpt) row.append(create('p', 'collection-document-excerpt', document.excerpt));
      container.append(row);
    }
  }

  function hideCollection() {
    showElement($('#collectionView'), false);
    document.body.classList.remove('overlay-open');
    state.currentCollection = null;
    state.collectionDirect = false;
  }

  function showRouteError(message) {
    let region = $('#routeError');
    if (!region) {
      region = create('p', 'route-error');
      region.id = 'routeError';
      region.setAttribute('role', 'alert');
      $('#main').prepend(region);
    }
    region.textContent = message;
  }

  function hideRouteError() {
    $('#routeError')?.remove();
  }

  function validateDocumentPath(path) {
    if (typeof path !== 'string' || !path || path.startsWith('/') || path.includes('\0')) return null;
    if (path.split('/').some(part => part === '.' || part === '..' || part === '')) return null;
    return state.documentByPath.get(path) || null;
  }

  function resolveDestination(destination, sourcePath) {
    const raw = destination.trim();
    if (!raw) return { kind: 'invalid' };
    if (raw.includes('\\') || /%2f/i.test(raw.split(/[?#]/, 1)[0])) return { kind: 'invalid' };
    if (/^(?:javascript|vbscript|data|file|blob):/i.test(raw)) return { kind: 'invalid' };
    if (/^(?:mailto|tel):/i.test(raw)) return { kind: 'external', href: raw };

    let base;
    let target;
    try {
      base = localFileURL(sourcePath);
      target = new URL(raw, base);
    } catch {
      return { kind: 'invalid' };
    }
    if (target.origin !== rootURL.origin) {
      if (target.protocol === 'https:' || target.protocol === 'http:') {
        return { kind: 'external', href: target.href };
      }
      return { kind: 'invalid' };
    }
    if (!target.pathname.startsWith(rootPath)) return { kind: 'invalid' };

    let path;
    let fragment;
    try {
      path = target.pathname.slice(rootPath.length).split('/').map(part => decodeURIComponent(part)).join('/');
      fragment = decodeURIComponent(target.hash.slice(1));
    } catch {
      return { kind: 'invalid' };
    }
    if (!path) path = sourcePath;
    const normalized = path.replace(/\/+$/, '');
    let document = state.documentByPath.get(normalized);
    if (!document) {
      const indexPath = state.directoryIndexes.get(normalized);
      if (indexPath) document = state.documentByPath.get(indexPath);
    }
    if (document) {
      return {
        kind: 'document',
        path: document.path,
        fragment,
        query: target.search
      };
    }
    if (state.assetPaths.has(normalized)) {
      const assetURL = localFileURL(normalized);
      assetURL.search = target.search;
      assetURL.hash = target.hash;
      return { kind: 'asset', url: assetURL.href };
    }
    return { kind: 'missing', path: normalized };
  }

  function fragmentFromDestination(destination) {
    const rawHash = destination.includes('#') ? destination.slice(destination.indexOf('#') + 1) : '';
    try {
      return decodeURIComponent(rawHash);
    } catch {
      return '';
    }
  }

  function updateHeadingIds() {
    const used = new Set();
    for (const heading of $('#article').querySelectorAll('h1,h2,h3,h4,h5,h6')) {
      const existing = heading.id.trim();
      let base = existing || slugify(heading.textContent);
      if (!base) base = 'section';
      let id = base;
      let suffix = 1;
      while (used.has(id)) id = `${base}-${suffix++}`;
      used.add(id);
      heading.id = id;
      heading.tabIndex = -1;
    }
  }

  function slugify(value) {
    return value.toLocaleLowerCase()
      .replace(/_/g, '-')
      .replace(/[^\p{L}\p{N}\s-]/gu, '')
      .trim()
      .replace(/[\s-]+/g, '-') || 'section';
  }

  function renderTableOfContents() {
    const toc = $('#toc');
    toc.replaceChildren();
    const headings = [...$('#article').querySelectorAll('h2,h3')];
    for (const heading of headings) {
      const link = create('a', `toc-link toc-level-${heading.tagName.slice(1)}`, heading.textContent);
      link.href = `#${encodeURIComponent(heading.id)}`;
      link.dataset.fragment = heading.id;
      toc.append(link);
    }
    const hasHeadings = headings.length > 0;
    $('#tocButton').disabled = !hasHeadings;
    $('#tocButton').setAttribute('aria-expanded', 'false');
    toc.classList.remove('toc-open');
  }

  function sanitizeOptions() {
    return {
      ALLOW_DATA_ATTR: false,
      ALLOWED_URI_REGEXP: /^(?:(?:https?:\/\/|mailto:|tel:)|(?:\/(?!\/)|\.{1,2}\/|#)|(?!(?:[a-z][a-z0-9+.-]*):)[^\s]*)$/i,
      FORBID_ATTR: ['style', 'srcset', 'formaction', 'xlink:href'],
      FORBID_TAGS: ['audio', 'base', 'button', 'embed', 'form', 'iframe', 'input', 'link', 'meta', 'object', 'script', 'source', 'style', 'track', 'video']
    };
  }

  function rewriteRenderedContent(sourcePath) {
    const article = $('#article');
    for (const image of article.querySelectorAll('img')) {
      const source = image.getAttribute('src') || '';
      const resolved = resolveDestination(source, sourcePath);
      if (resolved.kind === 'asset') {
        image.src = resolved.url;
        image.removeAttribute('srcset');
        image.loading = 'lazy';
        image.decoding = 'async';
        continue;
      }
      const replacement = create('span', 'missing-image');
      replacement.textContent = image.alt ? `Image unavailable: ${image.alt}` : 'Image unavailable: local image was not found in the generated asset catalogue.';
      image.replaceWith(replacement);
    }

    for (const anchor of article.querySelectorAll('a')) {
      anchor.removeAttribute('target');
      anchor.removeAttribute('rel');
      const href = anchor.getAttribute('href');
      if (!href) continue;
      const resolved = resolveDestination(href, sourcePath);
      if (resolved.kind === 'external') {
        anchor.href = resolved.href;
        continue;
      }
      if (resolved.kind === 'document') {
        anchor.href = documentURL(resolved.path, resolved.fragment, resolved.query).href;
        anchor.dataset.documentPath = resolved.path;
        if (resolved.fragment) anchor.dataset.fragment = resolved.fragment;
        continue;
      }
      if (resolved.kind === 'asset') {
        anchor.href = resolved.url;
        continue;
      }
      if (resolved.kind === 'invalid') {
        anchor.removeAttribute('href');
        anchor.setAttribute('aria-disabled', 'true');
        anchor.setAttribute('title', 'This link uses an unsupported or unsafe URL.');
        continue;
      }
      anchor.removeAttribute('href');
      anchor.setAttribute('aria-disabled', 'true');
      anchor.setAttribute('title', `This local resource is not available in the generated catalogue: ${resolved.path || href}`);
    }

    for (const table of article.querySelectorAll('table')) {
      const wrapper = create('div', 'table-scroll');
      table.before(wrapper);
      wrapper.append(table);
    }
    for (const code of article.querySelectorAll('pre > code')) addCopyControl(code);
    updateHeadingIds();
    renderTableOfContents();
  }

  function addCopyControl(code) {
    const pre = code.parentElement;
    if (!pre || pre.parentElement?.classList.contains('code-block')) return;
    const wrapper = create('div', 'code-block');
    pre.before(wrapper);
    wrapper.append(pre);
    const button = create('button', 'copy-code', 'Copy code');
    button.type = 'button';
    button.setAttribute('aria-label', 'Copy this code block');
    button.addEventListener('click', async () => {
      try {
        if (!navigator.clipboard?.writeText) throw new Error('Clipboard API is unavailable.');
        await navigator.clipboard.writeText(code.textContent || '');
        button.textContent = 'Copied';
        button.dataset.state = 'success';
      } catch (error) {
        button.textContent = 'Copy unavailable';
        button.dataset.state = 'error';
        console.warn('Code copy was not available:', error);
      }
      window.setTimeout(() => {
        button.textContent = 'Copy code';
        button.removeAttribute('data-state');
      }, 2200);
    });
    wrapper.append(button);
  }

  function setReaderState(message, kind = 'loading') {
    const region = $('#readerState');
    region.textContent = message;
    region.dataset.state = kind;
    showElement(region, true);
  }

  function clearReaderState() {
    showElement($('#readerState'), false);
  }

  function setSourceLinks(document) {
    const href = sourceURL(document.path);
    for (const link of [$('#source'), $('#readerFooterSource')]) {
      link.href = href;
      link.hidden = false;
    }
  }

  function renderDocumentNavigation(document) {
    const nav = $('#docnav');
    nav.replaceChildren();
    const collection = state.collectionById.get(document.collection);
    if (!collection) return;
    const readingDocs = orderedReadingDocuments(collection);
    const currentIndex = readingDocs.findIndex(item => item.path === document.path);
    if (currentIndex < 0) return;
    const previous = readingDocs[currentIndex - 1];
    const next = readingDocs[currentIndex + 1];
    const add = (item, direction) => {
      if (!item) return;
      const link = create('a', `document-step document-step-${direction}`);
      link.href = documentURL(item.path).href;
      link.dataset.documentPath = item.path;
      link.append(create('span', 'step-direction', direction === 'previous' ? 'Previous in collection' : 'Next in collection'));
      link.append(create('span', 'step-title', item.title));
      nav.append(link);
    };
    add(previous, 'previous');
    add(next, 'next');
  }

  function scrollToFragment(fragment, updateAddress = false) {
    const target = fragment ? document.getElementById(fragment) : null;
    if (!target) {
      $('#article').scrollIntoView({ block: 'start' });
      return;
    }
    target.scrollIntoView({ block: 'start' });
    target.focus({ preventScroll: true });
    if (updateAddress && state.currentDocument) {
      const url = documentURL(state.currentDocument.path, fragment);
      updateHistory(url, { skbReader: true, skbDocument: state.currentDocument.path, skbDirect: false }, true);
    }
  }

  async function loadDocument(doc, fragment = '') {
    const requestId = ++state.requestId;
    state.currentDocument = doc;
    const collection = state.collectionById.get(doc.collection);
    $('#readerTitle').textContent = doc.title;
    $('#breadcrumb').textContent = collection ? collection.name : doc.collection;
    $('#article').replaceChildren();
    $('#toc').replaceChildren();
    $('#docnav').replaceChildren();
    $('#sidebar').classList.remove('toc-open');
    $('#tocButton').setAttribute('aria-expanded', 'false');
    setSourceLinks(doc);
    setPageTitle(`${doc.title} | Security Knowledge Base`);
    renderDocumentNavigation(doc);
    setReaderState(`Loading ${doc.title}…`);
    showElement($('#viewer'), true);
    document.body.classList.add('reader-open');
    $('#close').focus({ preventScroll: true });

    try {
      const response = await fetch(localFileURL(doc.path), { cache: 'no-cache' });
      if (!response.ok) throw new Error(`The source returned HTTP ${response.status}.`);
      const markdown = await response.text();
      if (requestId !== state.requestId) return;
      if (!window.marked?.parse || !window.DOMPurify?.sanitize) {
        throw new Error('The Markdown renderer or sanitizer did not load. Check the network connection or open the source Markdown on GitHub.');
      }
      const rendered = window.marked.parse(markdown, { gfm: true, breaks: false });
      const safeHTML = window.DOMPurify.sanitize(rendered, sanitizeOptions());
      const template = document.createElement('template');
      template.innerHTML = safeHTML;
      $('#article').replaceChildren(template.content);
      rewriteRenderedContent(doc.path);
      clearReaderState();
      $('#article').focus({ preventScroll: true });
      if (fragment) {
        window.requestAnimationFrame(() => scrollToFragment(fragment));
      } else {
        $('#article').scrollIntoView({ block: 'start' });
      }
    } catch (error) {
      if (requestId !== state.requestId) return;
      console.error(`Unable to render ${doc.path}:`, error);
      $('#article').replaceChildren();
      $('#toc').replaceChildren();
      $('#docnav').replaceChildren();
      setReaderState(`${error.message} Use “View source on GitHub” to access the Markdown directly.`, 'error');
    }
  }

  function hideReader() {
    ++state.requestId;
    state.currentDocument = null;
    showElement($('#viewer'), false);
    document.body.classList.remove('reader-open');
    $('#sidebar').classList.remove('toc-open');
    setPageTitle();
    if (state.returnFocus?.isConnected && state.returnFocus !== document.body) state.returnFocus.focus({ preventScroll: true });
    else $('#search')?.focus({ preventScroll: true });
    state.returnFocus = null;
    state.readerDirect = false;
  }

  function openDocument(path, options = {}) {
    const selected = validateDocumentPath(path);
    if (!selected) {
      setReaderState(`This document path is invalid or is not present in the generated catalogue: ${String(path)}`, 'error');
      showElement($('#viewer'), true);
      document.body.classList.add('reader-open');
      $('#article').replaceChildren();
      $('#source').hidden = true;
      $('#readerFooterSource').hidden = true;
      setPageTitle('Document unavailable | Security Knowledge Base');
      return;
    }
    if (!state.currentDocument) {
      state.returnFocus = options.trigger || document.activeElement;
      state.readerPreviousFocus = document.activeElement;
      state.readerDirect = Boolean(options.direct);
    }
    const currentURL = new URL(window.location.href);
    const currentPath = currentURL.searchParams.get('doc');
    const targetURL = documentURL(selected.path, options.fragment || '', options.query || '');
    const sameDocument = currentPath === selected.path;
    if (options.history !== false && (!sameDocument || currentURL.hash !== targetURL.hash || currentURL.search !== targetURL.search)) {
      const direct = Boolean(options.direct && !state.currentDocument);
      const depth = direct ? 0 : (Number(window.history.state?.skbReaderDepth) || 0) + 1;
      updateHistory(targetURL, {
        skbReader: true,
        skbDocument: selected.path,
        skbDirect: direct,
        skbCollection: selected.collection,
        skbReaderDepth: depth
      }, Boolean(options.replace || sameDocument));
      state.readerDirect = direct;
    }
    if (sameDocument && state.currentDocument?.path === selected.path) {
      if (options.fragment) scrollToFragment(options.fragment);
      return;
    }
    state.currentDocument = selected;
    hideCollection();
    loadDocument(selected, options.fragment || '');
  }

  function openCollection(collectionId, options = {}) {
    const collection = state.collectionById.get(collectionId);
    if (!collection) {
      showRouteError(`The collection “${collectionId}” is not in the generated catalogue.`);
      return;
    }
    if (options.history !== false) {
      const currentId = new URL(window.location.href).searchParams.get('collection');
      if (currentId !== collection.id) {
        updateHistory(`index.html?collection=${encodeURIComponent(collection.id)}`, {
          skbPortal: true,
          skbCollection: collection.id,
          skbDirectCollection: false
        }, Boolean(options.replace));
      }
    }
    state.collectionDirect = Boolean(options.direct);
    renderCollection(collection.id, Boolean(options.focus));
  }

  function closeReader() {
    if (state.readerDirect && window.history.state?.skbReader) {
      const url = new URL('index.html', rootURL);
      updateHistory(url, { skbReader: false, skbDocument: null, skbDirect: false }, true);
      hideReader();
      return;
    }
    if (window.history.state?.skbReader) {
      const depth = Number(window.history.state?.skbReaderDepth) || 1;
      window.history.go(-depth);
      return;
    }
    hideReader();
    state.readerDirect = false;
  }

  function closeCollection() {
    if (state.collectionDirect && window.history.state?.skbCollection) {
      updateHistory(new URL('index.html', rootURL), { skbCollection: null, skbDirectCollection: false }, true);
      hideCollection();
      setPageTitle();
      $('#domains-title').focus?.({ preventScroll: true });
      return;
    }
    if (window.history.state?.skbCollection) {
      window.history.back();
      return;
    }
    hideCollection();
    setPageTitle();
  }

  function routeFromLocation(options = {}) {
    const url = new URL(window.location.href);
    const documentPath = url.searchParams.get('doc');
    if (documentPath !== null) {
      const selected = validateDocumentPath(documentPath);
      if (!selected) {
        state.readerDirect = Boolean(options.initial || window.history.state?.skbDirect);
        state.currentDocument = null;
        showElement($('#viewer'), true);
        document.body.classList.add('reader-open');
        $('#article').replaceChildren();
        $('#toc').replaceChildren();
        $('#docnav').replaceChildren();
        $('#source').hidden = true;
        $('#readerFooterSource').hidden = true;
        $('#readerTitle').textContent = 'Document unavailable';
        setReaderState('This document path is invalid, missing, or is not in the generated catalogue. Choose a collection or return to the handbook.', 'error');
        setPageTitle('Document unavailable | Security Knowledge Base');
        return;
      }
      state.readerDirect = Boolean(options.initial || window.history.state?.skbDirect);
      openDocument(selected.path, {
        history: false,
        direct: state.readerDirect,
        fragment: url.hash ? fragmentFromDestination(url.hash) : ''
      });
      return;
    }
    hideReader();
    const collectionId = url.searchParams.get('collection');
    if (collectionId !== null) {
      state.collectionDirect = Boolean(options.initial || window.history.state?.skbDirectCollection);
      openCollection(collectionId, { history: false, direct: state.collectionDirect, focus: !options.initial });
      return;
    }
    hideCollection();
    setPageTitle();
    if (options.focusReturn && state.returnFocus?.isConnected) state.returnFocus.focus({ preventScroll: true });
  }

  function resolveInternalRoute(url) {
    if (url.origin !== rootURL.origin) return false;
    const indexPath = new URL('index.html', rootURL).pathname;
    if (url.pathname !== indexPath) return false;
    if (url.searchParams.has('doc')) {
      const path = url.searchParams.get('doc');
      const fragment = fragmentFromDestination(url.hash);
      openDocument(path, { trigger: document.activeElement, fragment });
      return true;
    }
    if (url.searchParams.has('collection')) {
      openCollection(url.searchParams.get('collection'), { focus: true });
      return true;
    }
    return false;
  }

  function handleContentClick(event) {
    const anchor = event.target.closest('a');
    if (!anchor || event.defaultPrevented || event.button !== 0 || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
    if (anchor.dataset.documentPath) {
      event.preventDefault();
      openDocument(anchor.dataset.documentPath, {
        trigger: anchor,
        fragment: anchor.dataset.fragment || fragmentFromDestination(anchor.href)
      });
      return;
    }
    if (anchor.dataset.collectionId) {
      event.preventDefault();
      openCollection(anchor.dataset.collectionId, { focus: true });
      return;
    }
    if (!state.currentDocument && /\.md(?:[?#]|$)/i.test(anchor.getAttribute('href') || '')) {
      const resolved = resolveDestination(anchor.getAttribute('href'), 'README.md');
      if (resolved.kind === 'document') {
        event.preventDefault();
        openDocument(resolved.path, {
          trigger: anchor,
          fragment: resolved.fragment,
          query: resolved.query
        });
        return;
      }
    }
    let url;
    try {
      url = new URL(anchor.href, window.location.href);
    } catch {
      return;
    }
    if (resolveInternalRoute(url)) event.preventDefault();
  }

  function stripMarkdownTitle(text) {
    return text.replace(/\s+/g, ' ').trim();
  }

  function highlightText(element, text, terms) {
    element.replaceChildren();
    const normalizedTerms = [...new Set(terms)].filter(term => term.length > 1);
    if (!normalizedTerms.length) {
      element.textContent = text;
      return;
    }
    const expression = new RegExp(`(${normalizedTerms.map(escapeRegExp).join('|')})`, 'giu');
    let cursor = 0;
    let match;
    while ((match = expression.exec(text)) !== null) {
      if (match.index > cursor) element.append(document.createTextNode(text.slice(cursor, match.index)));
      const marker = create('mark', 'search-highlight', match[0]);
      element.append(marker);
      cursor = match.index + match[0].length;
    }
    if (cursor < text.length) element.append(document.createTextNode(text.slice(cursor)));
  }

  function escapeRegExp(value) {
    return value.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  }

  function tokenizeQuery(value) {
    return [...new Set(value.toLocaleLowerCase().match(/[\p{L}\p{N}_]+/gu) || [])]
      .filter(term => term.length > 1);
  }

  async function ensureSearchIndex() {
    if (state.searchIndex) return state.searchIndex;
    const response = await fetch(new URL('site/search-index.json', rootURL), { cache: 'no-cache' });
    if (!response.ok) throw new Error(`Search index request failed with HTTP ${response.status}.`);
    const index = await response.json();
    if (index.version !== 1 || !Array.isArray(index.documentPaths) || !index.terms || typeof index.terms !== 'object') {
      throw new Error('The generated search index has an unexpected format.');
    }
    if (index.documentPaths.length !== state.documents.length ||
        index.documentPaths.some((path, position) => path !== state.documents[position].path)) {
      throw new Error('The search index does not match the document catalogue.');
    }
    state.searchIndex = index;
    return index;
  }

  function searchDocuments(index, terms) {
    const scores = new Map();
    const matches = new Map();
    for (const term of terms) {
      const postings = index.terms[term] || [];
      for (const [documentId, weight] of postings) {
        scores.set(documentId, (scores.get(documentId) || 0) + weight);
        if (!matches.has(documentId)) matches.set(documentId, new Set());
        matches.get(documentId).add(term);
      }
    }
    const results = [...scores.entries()]
      .map(([id, score]) => ({
        document: state.documentByPath.get(index.documentPaths[id]),
        score: score + ((matches.get(id)?.size || 0) === terms.length ? terms.length * 9 : 0),
        matchedTerms: [...(matches.get(id) || [])]
      }))
      .filter(result => result.document)
      .sort((a, b) => b.score - a.score || a.document.title.localeCompare(b.document.title));
    return { items: results.slice(0, 20), total: results.length };
  }

  function renderSearchResults(resultsElement, query, results) {
    const terms = tokenizeQuery(query);
    resultsElement.replaceChildren();
    if (!results.length) {
      resultsElement.append(create('p', 'search-empty', `No documents found for “${query}”. Try a broader term or a different phrase.`));
      return;
    }
    for (const result of results) {
      const document = result.document;
      const link = create('a', 'search-result');
      link.href = documentURL(document.path).href;
      link.dataset.documentPath = document.path;
      link.setAttribute('role', 'option');
      link.setAttribute('aria-selected', 'false');
      link.tabIndex = -1;
      const title = create('span', 'search-result-title');
      highlightText(title, stripMarkdownTitle(document.title), terms);
      const context = create('span', 'search-result-context');
      context.textContent = `${categoryDisplay(document)} · ${kindLabels[document.type] || 'Document'}`;
      const matched = create('span', 'search-result-matches');
      matched.append(document.createTextNode('Matched: '));
      highlightText(matched, result.matchedTerms.join(', '), terms);
      const excerpt = create('span', 'search-result-excerpt');
      highlightText(excerpt, document.excerpt || 'Open this source document to review its content.', terms);
      link.append(title, context, matched, excerpt);
      resultsElement.append(link);
    }
  }

  async function runSearch() {
    const input = $('#search');
    const results = $('#searchResults');
    const status = $('#searchStatus');
    const query = input.value.trim();
    showElement($('#clearSearch'), Boolean(input.value));
    if (!query) {
      results.replaceChildren();
      showElement(results, false);
      status.textContent = '';
      return;
    }
    showElement(results, true);
    results.setAttribute('aria-busy', 'true');
    results.replaceChildren(create('p', 'search-loading', 'Searching the handbook…'));
    status.textContent = 'Searching the handbook.';
    try {
      const index = await ensureSearchIndex();
      if (input.value.trim() !== query) return;
      const terms = tokenizeQuery(query);
      if (!terms.length) {
        results.replaceChildren(create('p', 'search-empty', 'Enter a word or phrase to search.'));
        status.textContent = 'Enter a word or phrase to search.';
        return;
      }
      const matches = searchDocuments(index, terms);
      renderSearchResults(results, query, matches.items);
      status.textContent = `${matches.total} ${matches.total === 1 ? 'result' : 'results'} found for ${query}; showing ${matches.items.length} at most.`;
    } catch (error) {
      console.error('Search index unavailable:', error);
      const message = create('p', 'search-error', 'Search is temporarily unavailable. The document catalogue still works.');
      const retry = create('button', 'text-button search-retry', 'Retry search');
      retry.type = 'button';
      retry.addEventListener('click', () => {
        state.searchIndex = null;
        runSearch();
      });
      results.replaceChildren(message, retry);
      status.textContent = 'Search is unavailable.';
    } finally {
      results.removeAttribute('aria-busy');
    }
  }

  function scheduleSearch() {
    window.clearTimeout(state.searchTimer);
    state.searchTimer = window.setTimeout(runSearch, 160);
  }

  function setupEvents() {
    document.addEventListener('click', handleContentClick);
    $('#searchForm').addEventListener('submit', event => {
      event.preventDefault();
      scheduleSearch();
    });
    $('#search').addEventListener('input', scheduleSearch);
    $('#clearSearch').addEventListener('click', () => {
      $('#search').value = '';
      $('#search').focus();
      runSearch();
    });
    $('#search').addEventListener('keydown', event => {
      const results = $('#searchResults');
      const options = [...results.querySelectorAll('[role="option"]')];
      if (event.key === 'ArrowDown' && options.length) {
        event.preventDefault();
        options[0].focus();
      } else if (event.key === 'Enter' && options.length) {
        event.preventDefault();
        options[0].click();
      } else if (event.key === 'Escape') {
        showElement(results, false);
        $('#searchStatus').textContent = 'Search results dismissed.';
      }
    });
    $('#searchResults').addEventListener('keydown', event => {
      const options = [...$('#searchResults').querySelectorAll('[role="option"]')];
      const current = options.indexOf(document.activeElement);
      if (event.key === 'ArrowDown' && current >= 0) {
        event.preventDefault();
        options[Math.min(current + 1, options.length - 1)].focus();
      } else if (event.key === 'ArrowUp' && current > 0) {
        event.preventDefault();
        options[current - 1].focus();
      } else if (event.key === 'ArrowUp' && current === 0) {
        event.preventDefault();
        $('#search').focus();
      } else if (event.key === 'Escape') {
        event.preventDefault();
        showElement($('#searchResults'), false);
        $('#search').focus();
        $('#searchStatus').textContent = 'Search results dismissed.';
      }
    });
    $('#domainSearch').addEventListener('input', renderCollectionCards);
    $('#filter').addEventListener('change', renderCollectionCards);
    $('#collectionFilter').addEventListener('input', renderCollectionDocuments);
    $('#menu').addEventListener('click', () => {
      const expanded = $('#menu').getAttribute('aria-expanded') === 'true';
      $('#menu').setAttribute('aria-expanded', String(!expanded));
      $('#navlinks').classList.toggle('nav-open', !expanded);
    });
    $('#navlinks').addEventListener('click', event => {
      if (event.target.closest('a')) {
        $('#menu').setAttribute('aria-expanded', 'false');
        $('#navlinks').classList.remove('nav-open');
      }
    });
    $('#close').addEventListener('click', closeReader);
    $('#readerBack').addEventListener('click', closeReader);
    $('#collectionBack').addEventListener('click', closeCollection);
    $('#tocButton').addEventListener('click', () => {
      const expanded = $('#tocButton').getAttribute('aria-expanded') === 'true';
      $('#tocButton').setAttribute('aria-expanded', String(!expanded));
      $('#sidebar').classList.toggle('toc-open', !expanded);
      if (!expanded) $('#toc').querySelector('a')?.focus();
    });
    $('#toc').addEventListener('click', event => {
      const link = event.target.closest('[data-fragment]');
      if (!link) return;
      event.preventDefault();
      scrollToFragment(link.dataset.fragment, true);
      $('#sidebar').classList.remove('toc-open');
      $('#tocButton').setAttribute('aria-expanded', 'false');
    });
    $('#article').addEventListener('click', event => {
      const anchor = event.target.closest('a[href^="#"]');
      if (!anchor) return;
      const fragment = fragmentFromDestination(anchor.getAttribute('href'));
      const heading = document.getElementById(fragment);
      if (!heading) return;
      event.preventDefault();
      scrollToFragment(fragment, true);
    });
    window.addEventListener('popstate', () => routeFromLocation({ focusReturn: true }));
    window.addEventListener('keydown', event => {
      if (event.key === '/' && !event.ctrlKey && !event.metaKey && !event.altKey &&
          !['INPUT', 'TEXTAREA', 'SELECT'].includes(document.activeElement?.tagName)) {
        event.preventDefault();
        $('#search').focus();
      }
      if (event.key === 'Escape') {
        if (!$('#viewer').hidden) closeReader();
        else if (!$('#collectionView').hidden) closeCollection();
        else if ($('#menu').getAttribute('aria-expanded') === 'true') {
          $('#menu').setAttribute('aria-expanded', 'false');
          $('#navlinks').classList.remove('nav-open');
          $('#menu').focus();
        }
      }
      if (event.key === 'Tab' && !$('#viewer').hidden) trapReaderFocus(event);
    });
  }

  function trapReaderFocus(event) {
    const focusable = [...$('#viewer').querySelectorAll(
      'a[href]:not([hidden]), button:not([disabled]):not([hidden]), [tabindex]:not([tabindex="-1"]):not([hidden])'
    )].filter(element => {
      const rect = element.getBoundingClientRect();
      return rect.width > 0 && rect.height > 0 && rect.right > 0 && rect.left < window.innerWidth;
    });
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

  async function initialize() {
    setupEvents();
    try {
      const response = await fetch(new URL('site/content.json', rootURL), { cache: 'no-cache' });
      if (!response.ok) throw new Error(`Catalogue request failed with HTTP ${response.status}.`);
      const catalog = await response.json();
      if (catalog.version !== 2 || !Array.isArray(catalog.collections)) {
        throw new Error('The generated catalogue has an unexpected format.');
      }
      state.catalog = catalog;
      state.collectionById = new Map(catalog.collections.map(collection => [collection.id, collection]));
      state.documents = catalog.collections.flatMap(collection =>
        collection.documents.map(document => ({ ...document, collection: collection.id }))
      );
      state.documentByPath = new Map(state.documents.map(document => [document.path, document]));
      state.assetPaths = new Set(catalog.assets || []);
      for (const document of state.documents) {
        const directory = document.path.slice(0, document.path.lastIndexOf('/'));
        const filename = document.path.slice(document.path.lastIndexOf('/') + 1);
        if (/^(?:readme)\.md$/i.test(filename)) state.directoryIndexes.set(directory, document.path);
      }
      renderHome();

      const initialURL = new URL(window.location.href);
      const directDocument = initialURL.searchParams.has('doc');
      const directCollection = initialURL.searchParams.has('collection');
      window.history.replaceState({
        ...window.history.state,
        skbPortal: true,
        skbReader: directDocument,
        skbDirect: directDocument,
        skbCollection: directCollection ? initialURL.searchParams.get('collection') : null,
        skbDirectCollection: directCollection
      }, '', window.location.href);
      routeFromLocation({ initial: true });
    } catch (error) {
      console.error('Handbook catalogue unavailable:', error);
      $('#stats').replaceChildren(create('p', 'error-message', 'The catalogue could not be loaded. Check that site/content.json is published with the site.'));
      showRouteError('The handbook index is temporarily unavailable. You can still open source Markdown files directly from the repository.');
    }
  }

  initialize();
})();
