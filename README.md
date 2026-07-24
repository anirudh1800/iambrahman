# Brahman Mindmap — Cloudflare Workers

Static site. The markdown source lives in `brahman.md`; `build.py` inlines it into
`templates/index.html` to produce `public/index.html`, which markmap renders in
the browser. No server-side code — the build step just concatenates two static
files before deploy.

```
brahman-map/
├── wrangler.jsonc
├── build.py
├── brahman.md
├── templates/
│   └── index.html
└── public/
    └── index.html      (generated — do not edit directly)
```

## Deploy

```bash
npm install -D wrangler          # optional; npx will fetch it otherwise
python3 build.py                 # inline brahman.md into public/index.html
npx wrangler login
npx wrangler deploy
```

Live at `https://brahman-map.<your-subdomain>.workers.dev`.

## Preview locally

```bash
python3 build.py
npx wrangler dev
```

## Custom domain

Cloudflare dashboard → Workers & Pages → `brahman-map` → Settings → Domains &
Routes → Add custom domain. DNS and the certificate are handled for you if the
zone is already on Cloudflare.

## Editing the map

Edit `brahman.md`, run `python3 build.py` to regenerate `public/index.html`
(or just let `deploy.sh` do it), then redeploy. Don't edit `public/index.html`
directly — it's overwritten on every build.

## Notes

- markmap is loaded from jsDelivr, pinned to the `0.18` line. Pin an exact
  version (`markmap-autoloader@0.18.12`) if you want the render frozen.
- To drop the CDN dependency entirely, vendor the script:
  `npm i markmap-autoloader`, copy `dist/index.js` into `public/`, and point the
  `<script src>` at the local copy.
- To pre-render instead of rendering client-side:
  `npx markmap-cli map.md -o public/index.html --offline`. That inlines
  everything and removes the network fetch, at the cost of the custom page chrome.
