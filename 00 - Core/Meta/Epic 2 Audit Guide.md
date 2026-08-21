---
title: Epic 2 Audit Guide
type: reference
visibility: gm
note_status: draft
status: active
tags: [meta, audit, epic-2, review, handoff]
aliases: [Epic 2 Review, Society Audit]
created: 2026-08-21
updated: 2026-08-21
---

# Epic 2 Audit Guide

> **Purpose.** A **fresh-context read-through** companion. The user wants to walk through everything built in Epic 2 so far, read each note together, and audit it against intent — *does it sound like what they want?* This note is the map: what to read, in what order, and what to pressure-test. Start here, then open each artifact in the listed order.

> **Where the work lives.** Branch `worktree-epic-2-society`, **draft PR #7** (pushed, not merged — awaiting this audit). Not on `master` yet except the keystone-edge salvage.

## How to run the audit (suggested)

Read in **dependency order** (each note leans on the one above it). For each: read it aloud/together, then check it against the *intent checkpoints* listed. Flag anything that feels off → route through `story-sense` if it's unclear *why* it feels off. Adjust in place; re-commit. Nothing here is locked past the frame — the notes are `fleshed`, not `canon`.

**Tone north star for the whole audit:** **~5% scary** — mostly warm, mundane, integrated; a real dangerous obstacle underneath. If anything reads as *baseline* grim/dystopian/invasive, that's a flag (the user already caught one such case — see 2.1).

---

## Reading order & intent checkpoints

### 1. Frame — `The Premise.md` (new section: "World scale & register")
The two dials locked 2026-08-20, before any content.
- [ ] **Scale:** ~15 large polities across 3 large + 1 small continent. Build *universal rules + 2–3 archetypes* now; defer the rest. — *Right amount of world? Right split (rules now, places later)?*
- [ ] **Register:** late-medieval burgher surface (no printing press, no gunpowder); the *only* advancement beyond comes from **Condition-labor**. — *Does "advanced by Conditions, not generic magic-tech" still feel right? Is the "everything is paid for" rule the texture you want?*

### 2. Keystone edge — `11 - Secrets/GM Truth/Is the Leaf-Mother Real.md` (GM-ONLY)
The salvaged refinement: she's real & benevolent **but bounded, and giving costs her**; the **R2 social guard** (her kindness is cosmological, not social — don't let it launder injustice).
- [ ] *Does the "bounded/costly" edge improve the schism (two-sided) without reopening "is she kind" (locked yes)?*
- [ ] *Is the R2 guard the right instinct — society can be unjust atop true gifts?* (This guard drives the injustice in both 2.1 and 2.2.)

### 3. Story 2.1 — `03 - Cultures/Social Structures/Law and Citizenship.md`
**The big reframe.** Citizenship is **witnessed, not recorded** (user call: a universal register was too invasive). Key beats to check:
- [ ] **Witnessed citizenship** — you belong because your town *saw you Turn*; no register. — *Warm enough? Un-invasive enough?*
- [ ] **Proof by vouching people** (Long-Lived memory / Bound binding word / Far-Voiced unfakeable feeling), not papers; the vulnerable are the *unvouched*. — *Does this feel like a clever Condition-labor advance or a stretch?*
- [ ] **The Struck** = those who changed *unwitnessed* (later, alone) → must be vouched anew. — *Is "a little suspect" now earned rather than prejudiced?*
- [ ] **The Inviolate Will** — no Condition compels a will; the legal floor under ~5%-scary. — *Good as constitutional bedrock?*
- [ ] **Guild safety-licence** — only the ~3 hazardous Conditions; held by the person; ~90% carry nothing. — *Narrow enough to not feel like surveillance?*
- [ ] **The three pillars** (Long-Lived/Bound/Far-Voiced *are* the legal apparatus). — *Love it or too neat?*
- [ ] **Rights of the Kept** — default legal person; still-Struck-later; pitied where reverence runs hot.
- [ ] **Three polity stances:** Warm / **Watchful** (the one register-keeping kingdom — the dictator idea) / Frontier. — *Do these three read as good-faith + distinct? Is the Watchful the right "creepy exception"?*
- [ ] **Names are provisional** (deferred). — *Confirm you're happy leaving names for later.*

### 4. Story 2.2 — `03 - Cultures/Social Structures/Economy and the Tithe.md`
Built on 2.1. The load-bearing ideas the user flagged for review:
- [ ] **Thesis: the Tithe is the engine** — upkeep for 75% = a whole provisioning sector ("why society organizes around the Conditioned"). — *Does this framing land?*
- [ ] **Self-paying vs provided-for Tithes** — work-is-payment (Answered/Two-Bodied/Stilled/Returned) vs pure-cost (Taken-In/Long-Lived/Far-Voiced/Unbound/Bound). **This is the structural key — check it hardest.** — *Does the split hold? Are the assignments right?*
- [ ] **Tithe-poverty** — "too poor to stay whole" → slides toward the scary edge; the welfare question. — *Right kind of stakes?*
- [ ] **Whoever furnishes a provided-for Tithe holds power** — coercion with a friendly face (the R2 lever). — *Is this the injustice you want mechanized?*
- [ ] **Labor by Condition** — Tithe and vocation are the same shape; **the Kept = free generalist labor** (freedom under the slight). — *Like the inversion?*
- [ ] **Deathless banking** — the trusted note ≈ gold standard; century instruments; concentration risk; **outlive-all-heirs → endow** (fund the libraries that feed their own novelty-Tithe). — *Does the endow-not-inherit loop delight or overreach? Register kept medieval (letters of credit, NOT stock markets) — correct?*
- [ ] **Center/periphery** (reach-edge shapes trade) + **shadow economy** (illicit Tithe-supply, off-book contracts, sold vouching).

---

## Known open threads (already tracked — not audit failures)
- **Naming pass** — all Epic 2 institution names are provisional; in-world names + regional/language variants come after the polity archetypes + language sketches exist (Epic 2 tail → Epic 4). *(User directive.)*
- **Story 2.3 — Daily life** (marriage/family across stacked Kind+Condition, medicine, city design) — **not yet built.** Next up after this audit.
- **2–3 polity archetypes** — named/built at the end of Epic 2; will make the naming pass possible.
- The keystone-edge salvage commit is on local `master` (unpushed) *and* on this branch.

## Questions the user specifically wanted to sit with
1. Do the **self-paying vs provided-for** split and **Tithe-poverty** feel right before Daily Life builds on them?
2. Is the **witnessed-not-recorded** citizenship foundation solid, or are there holes?
3. Overall: does Epic 2 so far **sound like what they want** — right tone, right depth, right register?

## Links
- [[The Premise]] · [[Law and Citizenship]] · [[Economy and the Tithe]] · [[Is the Leaf-Mother Real]] · [[Roadmap]] (Epic 2)
