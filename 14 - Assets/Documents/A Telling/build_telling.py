#!/usr/bin/env python3
"""Compile A Telling of the Turning into HTML and PDF."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path
from shutil import which

try:
    import markdown
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "markdown", "-q"])
    import markdown

HERE = Path(__file__).resolve().parent
SRC = HERE / "telling.md"
OUT_HTML = HERE / "The-Turning-A-Telling.html"
OUT_PDF = HERE / "The-Turning-A-Telling.pdf"

CSS = r"""
:root {
  --paper: #f6f1e6;
  --ink: #2a241c;
  --muted: #5c5348;
  --leaf: #2f4f3e;
  --rule: #c9bba6;
}
* { box-sizing: border-box; }
body {
  margin: 0;
  background: var(--paper);
  color: var(--ink);
  font-family: "Liberation Serif", "DejaVu Serif", Palatino, Georgia, serif;
  font-size: 18px;
  line-height: 1.55;
}
main {
  max-width: 42rem;
  margin: 0 auto;
  padding: 2.4rem 1.6rem 5rem;
}
.title-page {
  min-height: 88vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  text-align: center;
  border-bottom: 1px solid var(--rule);
  margin-bottom: 2.4rem;
  padding: 3rem 1rem 3.5rem;
}
.title-page .kicker {
  font-variant: small-caps;
  letter-spacing: 0.28em;
  color: var(--leaf);
  font-size: 0.85rem;
  margin-bottom: 1.2rem;
}
.title-page h1 {
  font-size: 3.1rem;
  font-weight: 400;
  color: var(--leaf);
  margin: 0 0 0.6rem;
  border: 0;
  padding: 0;
  page-break-before: auto;
}
.title-page .subtitle {
  font-style: italic;
  font-size: 1.2rem;
  color: var(--muted);
  margin: 0;
}
h1 {
  font-size: 1.85rem;
  font-weight: 400;
  color: var(--leaf);
  margin: 2.4rem 0 0.8rem;
  padding-top: 1rem;
  border-top: 1px solid var(--rule);
  page-break-before: always;
}
h2 {
  font-size: 1.28rem;
  font-weight: 400;
  color: var(--leaf);
  margin: 1.8rem 0 0.5rem;
  page-break-after: avoid;
}
p { margin: 0.65rem 0; }
strong { font-weight: 700; }
em { font-style: italic; }
@media print {
  body { background: white; font-size: 12.5pt; line-height: 1.68; }
  main { max-width: none; margin: 0; padding: 0; }
  a { color: inherit; text-decoration: none; }
  .title-page { min-height: 90vh; }
}
@page { size: Letter; margin: 0.85in 0.9in; }
"""


def build_html() -> Path:
    text = SRC.read_text(encoding="utf-8")
    body = markdown.markdown(text, extensions=["extra", "sane_lists"])
    # The first heading is the title page.
    body = body.replace("<h1>", '<div class="title-page"><p class="kicker">The Turning</p><h1>', 1)
    body = body.replace("</h1>", '</h1><p class="subtitle">For the person who will run it</p></div>', 1)
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>A Telling of the Turning</title>
<style>{CSS}</style>
</head>
<body>
<main>
{body}
</main>
</body>
</html>
"""
    OUT_HTML.write_text(html, encoding="utf-8")
    return OUT_HTML


def build_pdf(html_path: Path) -> None:
    chrome = None
    for name in ("google-chrome", "google-chrome-stable", "chromium", "chromium-browser"):
        chrome = which(name)
        if chrome:
            break
    if not chrome:
        print("Chrome not found; HTML only.", file=sys.stderr)
        return
    profile = Path("/tmp/chrome-telling-print")
    profile.mkdir(parents=True, exist_ok=True)
    try:
        subprocess.check_call(
            [
                chrome,
                "--headless=new",
                "--disable-gpu",
                "--no-pdf-header-footer",
                "--no-sandbox",
                "--disable-dev-shm-usage",
                f"--user-data-dir={profile}",
                f"--print-to-pdf={OUT_PDF}",
                "--virtual-time-budget=90000",
                html_path.as_uri(),
            ],
            timeout=240,
        )
    except subprocess.TimeoutExpired:
        if not OUT_PDF.exists() or OUT_PDF.stat().st_size < 1000:
            raise
        print("Chrome timed out after writing the PDF; continuing.", file=sys.stderr)
    gs = which("gs")
    if not gs:
        print("Ghostscript not found; PDF left uncompressed.", file=sys.stderr)
        return
    tmp = OUT_PDF.with_suffix(".gs.pdf")
    subprocess.check_call(
        [
            gs,
            "-q",
            "-dNOPAUSE",
            "-dBATCH",
            "-dSAFER",
            "-sDEVICE=pdfwrite",
            "-dCompatibilityLevel=1.7",
            "-dPDFSETTINGS=/printer",
            f"-sOutputFile={tmp}",
            str(OUT_PDF),
        ]
    )
    tmp.replace(OUT_PDF)


def main() -> None:
    html = build_html()
    print(f"Wrote {html} ({html.stat().st_size:,} bytes)")
    build_pdf(html)
    if OUT_PDF.exists():
        print(f"Wrote {OUT_PDF} ({OUT_PDF.stat().st_size:,} bytes)")


if __name__ == "__main__":
    main()
