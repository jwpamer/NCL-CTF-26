# CTF Portfolio

A technique-first portfolio of my Capture The Flag experience (National Cyber League &
more), built as a [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) site. All write-ups are
sanitized per each competition's rules of conduct — see `docs/disclosure.md`.

## Live site

> After you deploy: **https://jwpamer.github.io/**

## Develop locally

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

mkdocs serve        # live preview at http://127.0.0.1:8000
mkdocs build        # render static site into ./site
```

## Deploy to GitHub Pages

This repo includes a workflow (`.github/workflows/deploy.yml`) that builds and publishes
the site on every push to `main`. One-time setup: in your repo's **Settings → Pages**,
set **Source = GitHub Actions**. (Or run `mkdocs gh-deploy` locally.)

## Layout

```
ctf-portfolio/
├── mkdocs.yml            # site config (Material theme, nav)
├── docs/                 # site content (Markdown)
│   ├── index.md
│   ├── experience.md
│   ├── skills.md
│   ├── writeups/
│   ├── tools.md
│   └── disclosure.md
├── tools/                # my original password-cracking tools
└── requirements.txt
```

## License

Original code and write-ups © Jordan Pamer, MIT License (see `LICENSE`). No competition-
provided challenge content is included.
