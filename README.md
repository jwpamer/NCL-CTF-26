# Jordan W. Pamer — Cybersecurity Portfolio

**Cybersecurity student · CTF player · U.S. Marine Corps veteran**

A technique-first portfolio of my Capture The Flag experience (Cyber Skyline & more).
All write-ups are sanitized per each competition's rules of conduct.

### 🔗 **[View the live site → jwpamer.github.io](https://jwpamer.github.io/)**

---

## About me

My path into cybersecurity didn't start in a classroom. After serving in the **United
States Marine Corps**, I'm now pursuing a **B.S. in Cybersecurity at SANS.edu**, where I
hold the **GFACT, GSEC, and GCIH** certifications.

## Explore

- **[About / Background](https://jwpamer.github.io/about/)** — my story, education, certifications, and work history
- **[Experience](https://jwpamer.github.io/experience/)** — Cyber Skyline Fall 2026 (Individual + Team) with Scouting Reports
- **[Skills & Tooling](https://jwpamer.github.io/skills/)** — domains, techniques, and tools
- **[Write-ups](https://jwpamer.github.io/writeups/)** — sanitized, technique-first solves
- **[Password-Cracking Method](https://jwpamer.github.io/tools/)** — attack-selection and workflow cheat-sheet
- **[Disclosure & Privacy](https://jwpamer.github.io/disclosure/)** — how and why content is sanitized

## Contact

[GitHub](https://github.com/jwpamer) · [LinkedIn](https://www.linkedin.com/in/)

---

<details>
<summary>Building this site locally (for reference)</summary>

This portfolio is built with [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/).
A GitHub Actions workflow (`.github/workflows/deploy.yml`) builds and publishes the site on
every push to `main`.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

mkdocs serve        # live preview at http://127.0.0.1:8000
mkdocs build        # render static site into ./site
```

Content lives in `docs/` (Markdown); site configuration is in `mkdocs.yml`.

</details>

## License

Write-ups and notes © Jordan Pamer, MIT License (see [`LICENSE`](LICENSE)).
No competition-provided challenge content is included.
