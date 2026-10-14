// Best-effort offline cache. Not a guarantee: external CDN files (Tailwind, Google Fonts)
// are only available offline if they were fetched and cached during a previous online visit.
const CACHE = 'momentum-v2';
const CORE = ['./', './index.html', './manifest.webmanifest', './icon.svg'];
self.addEventListener('install', (e) => { e.waitUntil(caches.open(CACHE).then((c) => c.addAll(CORE)).then(() => self.skipWaiting())); });
self.addEventListener('activate', (e) => { e.waitUntil(caches.keys().then((ks) => Promise.all(ks.filter((k) => k !== CACHE).map((k) => caches.delete(k)))).then(() => clients.claim())); });
self.addEventListener('fetch', (e) => {
  const u = new URL(e.request.url);
  if (e.request.method !== 'GET' || u.hostname.endsWith('googleapis.com') && u.pathname.startsWith('/drive') || u.pathname.startsWith('/upload') || u.hostname === 'accounts.google.com') return; // never cache Drive/auth traffic
  e.respondWith(fetch(e.request).then((r) => { if (r.ok || r.type === 'opaque') { const c = r.clone(); caches.open(CACHE).then((x) => x.put(e.request, c)); } return r; }).catch(() => caches.match(e.request)));
});
