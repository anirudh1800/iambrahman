#!/usr/bin/env python3
import pathlib

root = pathlib.Path(__file__).parent
template = (root / "templates" / "index.html").read_text()
content = (root / "brahman.md").read_text()

placeholder = "{{MARKMAP_CONTENT}}"
if placeholder not in template:
    raise SystemExit("templates/index.html is missing the {{MARKMAP_CONTENT}} placeholder")

output = template.replace(placeholder, content)
(root / "public" / "index.html").write_text(output)
print("Built public/index.html from templates/index.html + brahman.md")
