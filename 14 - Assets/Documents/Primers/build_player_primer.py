#!/usr/bin/env python3
"""Compile the Player Primer vault note into HTML and PDF.

Reuses the world book's type, colours, table rules, and the Chrome print
step (plus Ghostscript) from build_world_book.py. The note's front-matter,
Links, and any GM Notes stay in the vault and stay out of the reading copy.
"""

from __future__ import annotations

import re
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
SOURCE = HERE / "Player Primer.md"
OUT_HTML = HERE / "The-Turning-Player-Primer.html"
OUT_PDF = HERE / "The-Turning-Player-Primer.pdf"

# Palette, type, and table rules match the world book. No sidebar: this is a short book.
CSS = r"""
:root {
  --paper: #f6f1e6;
  --ink: #2a241c;
  --muted: #5c5348;
  --leaf: #2f4f3e;
  --leaf-2: #4a6b57;
  --rule: #c9bba6;
  --link: #2f4f3e;
}
* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
body {
  margin: 0;
  background: var(--paper);
  color: var(--ink);
  font-family: "Liberation Serif", "DejaVu Serif", Palatino, Georgia, serif;
  font-size: 18px;
  line-height: 1.45;
}
a { color: var(--link); text-decoration: none; border-bottom: 1px dotted var(--leaf-2); }
main {
  max-width: 42rem;
  margin: 0 auto;
  padding: 2.2rem 1.6rem 4rem;
}
h1 {
  font-size: 2.6rem;
  font-weight: 400;
  color: var(--leaf);
  letter-spacing: 0.06em;
  margin: 0 0 0.35rem;
  padding: 0;
  border: 0;
  page-break-before: auto;
}
h2 {
  font-size: 1.28rem;
  font-weight: 400;
  color: var(--leaf);
  margin: 1.35rem 0 0.4rem;
  padding-top: 0.55rem;
  border-top: 1px solid var(--rule);
  page-break-after: avoid;
}
h3 {
  font-size: 1.05rem;
  font-weight: 700;
  color: var(--leaf-2);
  margin: 1rem 0 0.3rem;
  page-break-after: avoid;
}
p { margin: 0.45rem 0; orphans: 3; widows: 3; }
strong { font-weight: 700; }
ul, ol { margin: 0.35rem 0 0.7rem 1.2rem; padding: 0; }
li { margin: 0.18rem 0; }
table {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.92rem;
  margin: 0.6rem 0 0.9rem;
  page-break-inside: avoid;
}
th, td {
  border: 1px solid var(--rule);
  padding: 0.28rem 0.45rem;
  text-align: left;
  vertical-align: top;
}
td:first-child, th:first-child { white-space: nowrap; }
th {
  background: #e7efe8;
  color: var(--leaf);
  font-weight: 700;
}
tr:nth-child(even) td { background: #fbf8f1; }
@media print {
  body { background: white; font-size: 10.5pt; line-height: 1.38; }
  main { max-width: none; margin: 0; padding: 0; }
  a { border: 0; color: inherit; }
  h1 { font-size: 22pt; }
  h2 { font-size: 13pt; margin-top: 0.85rem; }
  p { margin: 0.28rem 0; }
}
@page {
  size: Letter;
  margin: 0.65in 0.72in 0.62in 0.72in;
}
"""

HTML_HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>The Turning: A Primer for Players</title>
<style>
{css}
</style>
</head>
<body>
<main>
"""

HTML_FOOT = """
</main>
</body>
</html>
"""


def reading_markdown(text: str) -> str:
    """Vault note to player reading copy. Strip production matter."""
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            text = text[end + 4 :]
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    text = re.split(r"\n## Links\b", text, maxsplit=1)[0]
    text = re.split(r"\n## GM Notes\b", text, maxsplit=1)[0]
    return text.strip() + "\n"


def convert(md: str) -> str:
    return markdown.markdown(
        md,
        extensions=["tables", "sane_lists", "smarty"],
        output_format="html5",
    )


def build_html() -> Path:
    md = reading_markdown(SOURCE.read_text(encoding="utf-8"))
    body = convert(md)
    html = HTML_HEAD.format(css=CSS) + body + HTML_FOOT
    OUT_HTML.write_text(html, encoding="utf-8")
    return OUT_HTML


def build_pdf(html_path: Path) -> Path | None:
    chrome = None
    for candidate in (
        "google-chrome",
        "google-chrome-stable",
        "chromium",
        "chromium-browser",
    ):
        chrome = which(candidate)
        if chrome:
            break
    if not chrome:
        print("Chrome not found; skipping PDF.", file=sys.stderr)
        return None
    profile = Path("/tmp/chrome-player-primer-print")
    profile.mkdir(parents=True, exist_ok=True)
    cmd = [
        chrome,
        "--headless=new",
        "--disable-gpu",
        "--no-pdf-header-footer",
        "--no-sandbox",
        "--disable-dev-shm-usage",
        f"--user-data-dir={profile}",
        f"--print-to-pdf={OUT_PDF}",
        "--virtual-time-budget=60000",
        html_path.as_uri(),
    ]
    try:
        # Chrome writes the PDF, then often hangs on a missing system bus.
        # The file is already on disk; do not wait out a long hang.
        subprocess.check_call(cmd, timeout=45)
    except subprocess.TimeoutExpired:
        if not OUT_PDF.exists():
            raise
        print("Chrome timed out after writing PDF; continuing.", file=sys.stderr)
    compress_pdf(OUT_PDF)
    return OUT_PDF


def compress_pdf(pdf: Path) -> None:
    """Same Ghostscript pass as the world book, so the file stays small enough to keep."""
    gs = which("gs")
    if not gs:
        print("Ghostscript not found; PDF left uncompressed.", file=sys.stderr)
        return
    tmp = pdf.with_suffix(".gs.pdf")
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
            str(pdf),
        ]
    )
    tmp.replace(pdf)


def main() -> None:
    html_path = build_html()
    print(f"Wrote {html_path} ({html_path.stat().st_size:,} bytes)")
    pdf_path = build_pdf(html_path)
    if pdf_path and pdf_path.exists():
        print(f"Wrote {pdf_path} ({pdf_path.stat().st_size:,} bytes)")
        info = which("pdfinfo")
        if info:
            subprocess.check_call([info, str(pdf_path)])


if __name__ == "__main__":
    main()
