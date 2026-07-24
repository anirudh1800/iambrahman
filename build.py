#!/usr/bin/env python3
import pathlib

root = pathlib.Path(__file__).parent


def build(md_name, template_name, placeholder, output_name):
    template = (root / "templates" / template_name).read_text()
    content = (root / md_name).read_text()

    if placeholder not in template:
        raise SystemExit(f"templates/{template_name} is missing the {placeholder} placeholder")

    output = template.replace(placeholder, content)
    (root / "public" / output_name).write_text(output)
    print(f"Built public/{output_name} from templates/{template_name} + {md_name}")


build("brahman.md", "index.html", "{{MARKMAP_CONTENT}}", "index.html")
build("shaivism.md", "shaivism.html", "{{MARKDOWN_CONTENT}}", "shaivism.html")
