#!/usr/bin/env python3
"""Compile The Turning world-book markdown into a single HTML (and PDF)."""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

try:
    import markdown
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "markdown", "-q"])
    import markdown

HERE = Path(__file__).resolve().parent
CHAPTERS_DIR = HERE / "chapters"
STRUCTURE = HERE / "STRUCTURE.md"
OUT_HTML = HERE / "The-Turning-World-Book.html"
OUT_PDF = HERE / "The-Turning-World-Book.pdf"
GM_FILE = "24-gm-canon.md"

CSS = r"""
:root {
  --paper: #f6f1e6;
  --ink: #2a241c;
  --muted: #5c5348;
  --leaf: #2f4f3e;
  --leaf-2: #4a6b57;
  --rule: #c9bba6;
  --box: #eef3ee;
  --gm: #3a332c;
  --gm-paper: #efe6d6;
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
  line-height: 1.55;
}
a { color: var(--link); text-decoration: none; border-bottom: 1px dotted var(--leaf-2); }
a:hover { border-bottom-style: solid; }
nav#toc {
  position: fixed;
  top: 0; left: 0; bottom: 0;
  width: 17.5rem;
  overflow: auto;
  padding: 1.4rem 1.1rem 2rem;
  background: #efe8d8;
  border-right: 1px solid var(--rule);
  font-size: 0.82rem;
  line-height: 1.35;
}
nav#toc .toc-title {
  font-variant: small-caps;
  letter-spacing: 0.14em;
  color: var(--leaf);
  font-size: 0.78rem;
  margin: 0 0 0.8rem;
}
nav#toc ol { list-style: none; margin: 0; padding: 0; }
nav#toc > ol > li { margin: 0.55rem 0 0.15rem; }
nav#toc a { border: 0; color: var(--ink); }
nav#toc a:hover { color: var(--leaf); }
nav#toc .h1 > a { font-weight: 700; color: var(--leaf); }
nav#toc .h2 { margin-left: 0.7rem; font-size: 0.92em; color: var(--muted); }
nav#toc .h3 { display: none; }
main {
  margin-left: 17.5rem;
  max-width: 46rem;
  padding: 2.2rem 2.4rem 6rem;
}
.title-page {
  min-height: 88vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  text-align: center;
  border-bottom: 1px solid var(--rule);
  margin-bottom: 3rem;
  padding: 4rem 1rem 4.5rem;
}
.title-page .kicker {
  font-variant: small-caps;
  letter-spacing: 0.42em;
  color: var(--leaf);
  font-size: 0.85rem;
  margin-bottom: 1.4rem;
}
.title-page h1 {
  font-size: 4.2rem;
  font-weight: 400;
  letter-spacing: 0.08em;
  margin: 0 0 0.4rem;
  color: var(--leaf);
  page-break-before: auto;
  border: 0;
  padding: 0;
}
.title-page .subtitle {
  font-style: italic;
  font-size: 1.35rem;
  color: var(--muted);
  margin: 0 0 2.2rem;
}
.title-page .meta {
  color: var(--muted);
  font-size: 0.95rem;
  line-height: 1.6;
}
h1 {
  font-size: 2.15rem;
  font-weight: 400;
  color: var(--leaf);
  letter-spacing: 0.02em;
  margin: 3.2rem 0 1.1rem;
  padding-top: 1.4rem;
  border-top: 1px solid var(--rule);
  page-break-before: always;
}
h1:first-of-type { page-break-before: auto; border-top: 0; padding-top: 0; }
h2 {
  font-size: 1.45rem;
  font-weight: 400;
  color: var(--leaf);
  margin: 2.3rem 0 0.7rem;
  page-break-after: avoid;
}
h3 {
  font-size: 1.12rem;
  font-weight: 700;
  color: var(--leaf-2);
  margin: 1.6rem 0 0.45rem;
  page-break-after: avoid;
}
h4 {
  font-size: 1.02rem;
  font-style: italic;
  font-weight: 400;
  color: var(--ink);
  margin: 1.2rem 0 0.35rem;
}
p { margin: 0.7rem 0; }
em { font-style: italic; }
strong { font-weight: 700; }
blockquote {
  margin: 1.1rem 1.4rem;
  padding: 0.15rem 0 0.15rem 1rem;
  border-left: 3px solid var(--leaf-2);
  color: var(--muted);
  font-style: italic;
}
blockquote p { margin: 0.35rem 0; }
ul, ol { margin: 0.5rem 0 0.9rem 1.3rem; padding: 0; }
li { margin: 0.22rem 0; }
hr {
  border: 0;
  border-top: 1px solid var(--rule);
  margin: 2rem 0;
}
table {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.88rem;
  margin: 1rem 0 1.4rem;
  page-break-inside: avoid;
}
th, td {
  border: 1px solid var(--rule);
  padding: 0.38rem 0.5rem;
  text-align: left;
  vertical-align: top;
}
th {
  background: #e7efe8;
  color: var(--leaf);
  font-weight: 700;
}
tr:nth-child(even) td { background: #fbf8f1; }
.rules-block {
  background: var(--box);
  border: 1px solid #c5d4c8;
  border-left: 4px solid var(--leaf);
  padding: 0.7rem 1rem 0.85rem;
  margin: 1rem 0 1.4rem;
  page-break-inside: avoid;
}
.rules-block > .rules-heading {
  margin-top: 0;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  font-size: 0.78rem;
  color: var(--leaf);
}
.gm-banner {
  background: var(--gm);
  color: #f6f1e6;
  padding: 1.4rem 1.3rem;
  margin: 2rem 0 1.6rem;
}
.gm-banner h1 {
  color: #f6f1e6;
  border: 0;
  margin: 0 0 0.4rem;
  padding: 0;
  page-break-before: always;
}
.gm-banner p { margin: 0; font-size: 0.95rem; color: #e4dccb; }
#gm-appendix {
  background: var(--gm-paper);
  margin: 0 -2.4rem;
  padding: 0.2rem 2.4rem 4rem;
}
.note-col { display: none; }
.book-open {
  margin: 3.4rem 0 0.4rem;
  padding: 1.3rem 0 0.4rem;
  border-top: 2px solid var(--leaf);
  color: var(--leaf);
  page-break-before: always;
}
.book-open .book-num {
  display: block;
  font-variant: small-caps;
  letter-spacing: 0.28em;
  font-size: 0.82rem;
  margin-bottom: 0.25rem;
}
.book-open .book-title {
  font-size: 1.35rem;
  letter-spacing: 0.04em;
}
blockquote.tbd {
  background: #efe4cc;
  border-left: 4px dashed #8a7349;
  font-style: normal;
  color: var(--ink);
  padding: 0.7rem 1rem;
  margin: 1rem 0 1.3rem;
}
blockquote.tbd strong:first-child {
  color: #6a5428;
  letter-spacing: 0.04em;
}
nav#toc .reserved a::after {
  content: " (to write)";
  color: #8a7349;
  font-style: italic;
  font-weight: 400;
}
@media screen and (max-width: 980px) {
  nav#toc { display: none; }
  main { margin-left: 0; padding: 1.4rem 1.1rem 4rem; }
}
@media print {
  nav#toc { display: none; }
  body { background: white; font-size: 11pt; }
  main {
    margin: 0;
    max-width: none;
    padding: 0;
  }
  #gm-appendix { margin: 0; padding: 0; background: white; }
  .title-page { min-height: 90vh; }
  a { border: 0; color: inherit; }
  h1 { page-break-before: always; }
  .title-page + * h1, main > h1:first-of-type { page-break-before: auto; }
  .gm-banner h1 { page-break-before: always; }
}
@page {
  size: Letter;
  margin: 0.85in 1.35in 0.85in 0.85in;
}
"""

HTML_HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>The Turning: A World Book</title>
<style>
{css}
</style>
</head>
<body>
<nav id="toc">
  <p class="toc-title">Contents</p>
  {toc}
</nav>
<main>
<section class="title-page">
  <div class="kicker">A world book</div>
  <h1>The Turning</h1>
  <p class="subtitle">Kind, Condition, and the reach of the Tree</p>
  <p class="meta">
    Living world book · Cut-year 387<br>
    Spine locked · reserved chapters marked <em>to write</em>
  </p>
</section>
"""

HTML_FOOT = """
</main>
</body>
</html>
"""


def slugify(text: str) -> str:
    text = re.sub(r"<[^>]+>", "", text)
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text).strip("-")
    return text or "section"


def parse_structure() -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    in_table = False
    for line in STRUCTURE.read_text(encoding="utf-8").splitlines():
        if line.startswith("| File | Book |"):
            in_table = True
            continue
        if not in_table:
            continue
        if not line.startswith("|"):
            break
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < 4 or cells[0].startswith("---") or set(cells[0]) <= {"-"}:
            continue
        rows.append(
            {
                "file": cells[0],
                "book": cells[1],
                "chapter": cells[2],
                "status": cells[3],
            }
        )
    return rows


def book_divider(book: str) -> str:
    if book in ("Front", ""):
        return ""
    if "·" in book:
        num, title = [p.strip() for p in book.split("·", 1)]
    else:
        num, title = book, ""
    return (
        f'<div class="book-open"><span class="book-num">Book {num}</span>'
        f'<span class="book-title">{title}</span></div>\n\n'
    )


def load_chapters() -> tuple[str, str, list[dict[str, str]]]:
    rows = parse_structure()
    main_parts: list[str] = []
    gm_md = ""
    last_book = None
    for row in rows:
        path = CHAPTERS_DIR / row["file"]
        text = path.read_text(encoding="utf-8").strip() + "\n\n"
        if row["file"] == GM_FILE:
            gm_md = text
            continue
        if row["book"] != last_book:
            divider = book_divider(row["book"])
            if divider:
                main_parts.append(divider)
            last_book = row["book"]
        main_parts.append(text)
    return "\n\n".join(main_parts), gm_md, rows


def convert(md: str) -> str:
    return markdown.markdown(
        md,
        extensions=["tables", "sane_lists", "smarty", "nl2br"],
        output_format="html5",
    )


def add_heading_ids(html: str) -> tuple[str, str]:
    toc_items: list[str] = []
    used: dict[str, int] = {}

    def repl(m: re.Match) -> str:
        level = m.group(1)
        attrs = m.group(2) or ""
        inner = m.group(3)
        base = slugify(inner)
        n = used.get(base, 0)
        used[base] = n + 1
        hid = base if n == 0 else f"{base}-{n+1}"
        attrs = re.sub(r'\s*id="[^"]*"', "", attrs)
        if level in ("1", "2"):
            toc_items.append(
                f'<li class="h{level}"><a href="#{hid}">{inner}</a></li>'
            )
        return f'<h{level}{attrs} id="{hid}">{inner}</h{level}>'

    html = re.sub(r"<h([1-4])([^>]*)>(.*?)</h\1>", repl, html, flags=re.DOTALL)
    toc = "<ol>\n" + "\n".join(toc_items) + "\n</ol>"
    return html, toc


def wrap_rules(html: str) -> str:
    """Wrap a Rules heading plus following block until the next h2/h3/hr/h1."""

    def repl(m: re.Match) -> str:
        attrs, title, rest = m.group(1), m.group(2), m.group(3)
        return (
            f'<div class="rules-block"><h3{attrs} class="rules-heading">'
            f"{title}</h3>{rest}</div>"
        )

    return re.sub(
        r"<h3([^>]*)>(\s*Rules\s*)</h3>(.*?)(?=<h[1-3]|<hr|<div class=\"rules-block\"|$)",
        repl,
        html,
        flags=re.DOTALL | re.IGNORECASE,
    )


def wrap_tbd(html: str) -> str:
    def repl(m: re.Match) -> str:
        inner = m.group(1)
        head = re.sub(r"<[^>]+>", "", inner)[:80]
        if "Not yet written" in head or "Reserved." in head:
            return f'<blockquote class="tbd">{inner}</blockquote>'
        return m.group(0)

    return re.sub(r"<blockquote>(.*?)</blockquote>", repl, html, flags=re.S)


def wrap_gm(html: str) -> str:
    html = re.sub(
        r"<h1([^>]*)>GM Canon</h1>\s*<p>(.*?)</p>",
        r'<div class="gm-banner"><h1\1>GM Canon</h1><p>\2</p></div>',
        html,
        count=1,
        flags=re.DOTALL,
    )
    return '<section id="gm-appendix">\n' + html + "\n</section>"


def mark_reserved_toc(toc: str, rows: list[dict[str, str]]) -> str:
    for row in rows:
        if row["status"] != "reserved":
            continue
        slug = slugify(row["chapter"])
        toc = toc.replace(
            f'<li class="h1"><a href="#{slug}">',
            f'<li class="h1 reserved"><a href="#{slug}">',
            1,
        )
    return toc


def build_html() -> Path:
    main_md, gm_md, rows = load_chapters()
    body = convert(main_md)
    body = wrap_tbd(body)
    gm_html = convert(gm_md) if gm_md.strip() else ""
    if gm_html:
        gm_html = wrap_tbd(gm_html)
        gm_html = book_divider("X · For the GM") + gm_html
        gm_html = wrap_gm(gm_html)
        body = body + "\n" + gm_html
    body = wrap_rules(body)
    body, toc = add_heading_ids(body)
    toc = mark_reserved_toc(toc, rows)
    html = HTML_HEAD.format(css=CSS, toc=toc) + body + HTML_FOOT
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
        from shutil import which

        chrome = which(candidate)
        if chrome:
            break
    if not chrome:
        print("Chrome not found; skipping PDF.", file=sys.stderr)
        return None
    profile = Path("/tmp/chrome-worldbook-print")
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
        "--virtual-time-budget=15000",
        html_path.as_uri(),
    ]
    try:
        subprocess.check_call(cmd, timeout=120)
    except subprocess.TimeoutExpired:
        if not OUT_PDF.exists():
            raise
        print("Chrome timed out after writing PDF; continuing.", file=sys.stderr)
    return OUT_PDF


def main() -> None:
    html_path = build_html()
    print(f"Wrote {html_path} ({html_path.stat().st_size:,} bytes)")
    pdf_path = build_pdf(html_path)
    if pdf_path and pdf_path.exists():
        print(f"Wrote {pdf_path} ({pdf_path.stat().st_size:,} bytes)")


if __name__ == "__main__":
    main()
