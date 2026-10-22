"""Epic V mechanical scan. Run: python3 "14 - Assets/Documents/Audits/Vault Audit 2026-10-22/mechanical_scan.py" > /tmp/scan.txt

Checks front-matter, broken wikilinks, retired phrases in player bodies (GM Notes stripped), and percentages outside The Premise. Many hits are allowed; read them, do not blindly delete."""
import os, re, collections, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
SKIP = ("14 - Assets/Documents/Setting Book", "14 - Assets/Documents/Audits/Vault Audit 2026-10-22", "00 - Core/Meta/Templates", ".agents", ".claude", ".git", ".obsidian", "node_modules")
TYPES = set("""moc reference lore cosmology theme region settlement city town village site people language custom tradition faction era event timeline npc pc character deity faith myth ritual creature adversary condition item magic secret mystery clue revelation campaign arc chapter session thread system rule encounter table asset map handout""".split())
STATUS = {"stub", "draft", "fleshed", "canon"}
PHRASES = [r"\binscrutable\b", r"\bleave it\b", r"\b20%", r"\bClock [12]\b", r"\bLeftover\b", r"\bPlayable square", r"\bSession wants", r"\bsame trick\b", r"\bone lintel\b",
           r"\bmouths?\b", r"\bC\.Y\.", r"\bdrinks? (that|the) winter", r"\bcupboard\b", r"wears the face", r"\bclean hands\b", r"courtesy travels", r"manners walked out",
           r"\bSpeaked\b", r"\bStory [A-Z0-9]+\.\d", r"\bEpic [A-Z0-9]\b", r"🔒", r"🟡", r"do not clone", r"\bthe sitting\b", r"\bseeing\b", r"\bhearth-glance", r"\bdoor(s)?\b"]
files = []
for dp, dn, fn in os.walk(ROOT):
    rel = os.path.relpath(dp, ROOT)
    if any(rel.startswith(s) for s in SKIP):
        continue
    for f in fn:
        if f.endswith(".md") and rel != "." :
            files.append(os.path.join(rel, f))
names = {}
for f in files:
    names[os.path.splitext(os.path.basename(f))[0].lower()] = f
for f in os.listdir(os.path.dirname(os.path.abspath(__file__))):
    if f.endswith(".md"):
        names[f[:-3].lower()] = f
fm_re = re.compile(r"^---\n(.*?)\n---\n", re.S)
out = collections.defaultdict(list)
aliases = set()
bodies = {}
for f in files:
    t = open(os.path.join(ROOT, f), encoding="utf-8").read()
    m = fm_re.match(t)
    fm = m.group(1) if m else ""
    body = t[m.end():] if m else t
    bodies[f] = (fm, body)
    am = re.search(r"^aliases:\s*\[(.*)\]", fm, re.M)
    if am:
        for a in am.group(1).split(","):
            a = a.strip().strip('"\'')
            if a: aliases.add(a.lower())
for f, (fm, body) in bodies.items():
    if not fm:
        out["no-front-matter"].append(f); continue
    def key(k):
        m = re.search(rf"^{k}:\s*(.*)$", fm, re.M)
        return m.group(1).strip() if m else None
    for k in ("title", "type", "visibility", "note_status"):
        if key(k) is None: out[f"missing-{k}"].append(f)
    if key("type") and key("type") not in TYPES: out["bad-type"].append(f"{f} ({key('type')})")
    if key("note_status") and key("note_status") not in STATUS: out["bad-note_status"].append(f"{f} ({key('note_status')})")
    if key("visibility") and key("visibility") not in ("gm", "player"): out["bad-visibility"].append(f"{f} ({key('visibility')})")
    for link in re.findall(r"\[\[([^\]|#]+)", body):
        l = link.strip().rstrip("\\").strip().lower()
        if l and l not in names and l not in aliases and not l.endswith((".png", ".jpg", ".pdf", ".html")):
            out["broken-link"].append(f"{f} -> [[{link.strip()}]]")
    vis = key("visibility")
    # player body = body with GM Notes sections removed
    pb = body
    if vis == "player":
        lines = pb.split("\n"); keep = []; skip_level = None
        for ln in lines:
            h = re.match(r"^(#+)\s+(.*)", ln)
            if h:
                lvl = len(h.group(1))
                if skip_level is not None and lvl <= skip_level: skip_level = None
                if skip_level is None and h.group(2).strip().startswith("GM Notes"):
                    skip_level = lvl; continue
            if skip_level is None: keep.append(ln)
        pb = "\n".join(keep)
        pb = re.sub(r"<!--.*?-->", "", pb, flags=re.S)
        for i, ln in enumerate(pb.split("\n")):
            if f.startswith("00 - Core/Meta/Roadmap") : break
            for p in PHRASES:
                if re.search(p, ln, re.I if p.startswith(r"\binscrut") else 0):
                    out["phrase:" + p].append(f"{f}: {ln.strip()[:160]}")
        if not f.endswith("The Premise.md"):
            for ln in pb.split("\n"):
                if re.search(r"~?\d+(\.\d+)?\s?%", ln):
                    out["percent-in-player-body"].append(f"{f}: {ln.strip()[:160]}")
os.makedirs("/tmp/vault-audit", exist_ok=True)
with open("/tmp/vault-audit/mechanical.md", "w") as o:
    o.write(f"# Mechanical scan\n\n{len(files)} notes scanned (world book chapters excluded).\n\n")
    for k in sorted(out):
        o.write(f"## {k} ({len(out[k])})\n\n")
        for v in out[k]: o.write(f"- {v}\n")
        o.write("\n")
for k in sorted(out): print(len(out[k]), k)
