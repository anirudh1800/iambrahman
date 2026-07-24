npm install -D wrangler          # optional; npx will fetch it otherwise
python3 build.py                 # inline brahman.md into public/index.html
npx wrangler login
npx wrangler deploy