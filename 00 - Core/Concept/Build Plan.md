---
title: Build Plan
type: reference
visibility: gm
note_status: draft
tags: [meta, build-plan, roadmap]
aliases: [Roadmap, Handoff Brief]
created: 2026-08-12
updated: 2026-08-12
---

# Build Plan

> **Handoff entry point.** If you are a fresh agent picking up this world, start here. This is the *how* and *what-order*; the *what* lives in the notes below.
>
> **STATUS (2026-08-12):** Setting locked ("The Empire That Wasn't Evil"). **Task 1 — the entire playable surface — is COMPLETE** (geography, peoples, the players' court, the rebellion; see inventory below). Committed to git (`576f855` on `master`). **Next up = Task 2 (the secret's selection mechanism)** or a **naming pass** — user's choice, not yet started. Nothing is mid-flight; you are picking up between phases.

## Read first (the source of truth, in order)

1. **[[The Premise]]** (`00 - Core/Concept`) — the setting, the players' vantage, and the **design contract**. Non-negotiable.
2. **[[Themes]]** (`00 - Core/Themes`) — the moral-parallax spine; what every piece must serve.
3. **[[The Cost]]** (`11 - Secrets/GM Truth`) — the core secret. GM-only. Direction is fixed; mechanism is open.
4. `00 - Core/Meta/Conventions.md` — vault schema, folder tree, front-matter, `type` vocab. Obey it.
5. `CLAUDE.md` — operational quick-reference + the craft-skills routing.

## How to work here

- **The design contract is law.** Both the Empire's defenders and the rebels must stay *right.* Test everything: *could a thoughtful, decent person, knowing the full truth, still keep it running?* If a choice makes the Empire simply evil, it's wrong.
- **Surface before secret.** Build the world players *touch* (map, peoples, rebellion, the commission) before descending into mechanism. This is a hard lesson from the prior scrapped setting — see memory `avarra-reset`.
- **Stay lean.** `note_status: draft`, grow with play. Don't write encyclopedia entries no session will use (shared-world philosophy; ignore its file scaffolding — this vault is the bible).
- **Diagnose, then reach for the named skill.** `story-sense` routes. Task-specific skills are named per subtask below.
- **Surface major forks for the user; don't lock them unilaterally.** Produce concrete options (as we did with the session-1 sketch), let the user's taste decide. This world is built to *their* feel.
- **Set `visibility` on every note from birth.** Player-facing world notes are `player` with any secret in a walled `## GM Notes`; anything touching [[The Cost]] is `gm`.

## Task 1 — the playable surface (COMPLETE ✅)

Built and committed. The world players *touch* now exists end to end. Inventory (all `note_status: draft` unless noted; read these to get current):

- **1a — Geography & map** ✅
  - `01 - World/Geography/Climate & Terrain.md` — physical geography; why the Empire can feed & move itself.
  - `04 - Settlements/Continents/The Shape of the Empire.md` — the administrative spine: **three rings** (Core / Provinces / Marches, by distance from the network) and **three separated powers** (Governors hold · Circuits judge · the Rolls count). The design hub for the Empire's competence.
  - `04 - Settlements/Regions/` — **The Aurenne** (content core/capital), **The Halden** (long-integrated, happy), **Kessad** (recently-pacified, aggrieved), **The Outmark** (eerie frontier).
- **1b — Peoples** ✅ (`03 - Cultures/Peoples/`) — one per ring, one per stance toward the Empire:
  - **The Vaurin** (heartland majority who mistake themselves for neutrality), **The Haldar** (genuinely content), **The Kessadi** (real grievance; the rebellion's soil), **The Tallun** (dutiful frontier; their watch-religion is a late-game Cost seed).
- **1d — The Assize** ✅ (`05 - Factions/Governments/The Assize.md`, `note_status: fleshed`) — the players' circuit court and the week-to-week engine: can/cannot authority, the open-petition door, five party-mappable seats, riding season, per-province arc recipe. Session-zero ready.
- **1c — The rebellion (the Sworn)** ✅ (`05 - Factions/Movements/The Sworn.md` + figures in `08 - People/`: Nemara Ishekar, Davan Kesharan, Marsu of the Low Wharfs) — an uneasy three-wing alliance; the players' *own fair verdicts* recruit for it.

> The three iceberg seeds planted across 1a–1c, all deniable, none confirming anything: the **"reconciled" ledger / "reconciling the rolls"** euphemism; the **Outmark's** unbroken silence (the "dam" half of [[The Cost]]); the **Zero Stone / impossible milestone counts** (land older than the Empire).

## Decided already (don't re-litigate)

- **Players = a mixed commission of inquiry / circuit court.** Job, not imposed identity.
- **The hegemon is just "the Empire."** (Rename only if a rival power / outside POV needs contrast.)
- **The secret is a fusion** (sacrifice + holding-back-a-threat; the threat's current reality is unknowable from inside). See [[The Cost]].
- **Euphemism = "reconciliation"** (candidate) is kept **out of the players' job title** (decided 2026-08-12). The court has a plain provisional name — **"the Assize"** — and "reconciliation" is reserved for frontier ledgers / old deeds, staying a rare seed. Task 2 confirms or replaces the word itself.
- **Names are provisional working labels** (Aurenne, Halden, Kessad, Outmark, Vaur, the Assize, Vaurin/Haldar/Kessadi/Tallun, …). A dedicated naming pass comes after peoples/languages exist; don't stop to lock names now.

### Task 1a/1b/1d fork decisions (2026-08-12) — do not re-litigate
- **1d — Presiding Justice = NPC** (party's anchor / moral mirror; if ever a PC, the verdict is the *commission's*).
- **1d — Assize muscle:** the Serjeant's small personal detail only; anything larger is **requisitioned from the Governor** (deliberate friction when the court must investigate that Governor).
- **1d — The posting is BOTH** prestigious (you wield the Empire's fairness) **and** a hardship (always moving, never home) — this is what staffs it with careerists *and* misfits. → an `underdog-unit` identity.
- **1b — Imperial core = single dominant-but-invisible people (the Vaurin).** Their culture is the "neutral" default; a believer-PC can't see their own particularity. **BUT dominance is not totality:** minority/older cultures persist in hard-to-reach pockets (high valleys, marsh-islands, remote coasts) where the network's smoothing pressure is weakest. Cultural uniformity thins with distance from the spine, mirroring the ring model. Pockets are an undesigned reservoir for later.
- **1b — Kessadi grievance stays mundane-political** (stolen sovereignty, the lost water-judges, the siege dead) — it must NOT be *about* [[The Cost]]. The secret is reached via the *frontier's silence* ([[The Outmark]]/Tallun), not the delta's anger. Protects the iceberg.
- **1b — Tallun are a distinct fourth people** (their watch-religion is load-bearing for the late game), not merely veterans + marchfolk.
- **1c — The rebellion (the Sworn) = uneasy alliance of three wings** (Restorationist water-judge houses / the Dispossessed commoners / hardliners) with visible seams; self-parallax, no clean side even internally.
- **1c — The Cost seed stays a single fringe crank** the movement dismisses (thinks it's a hidden mundane levy — wrong in a rhyming way). The Sworn as a body never suspect the secret.
- **1c — Leadership = coalition with a figurehead (Nemara) but no true head;** compartmented cells; she can't command the violence her legitimacy shelters.
- **1c — Violence at campaign start = mostly civil + sabotage, insurgent wing straining at the leash** (grows toward violence as the window closes). This is the campaign-temperature dial; may be re-tuned when early sessions are designed.

## Next up (not yet started — user picks the order)

The user's two candidate next moves, either is a clean start:

1. **Task 2 — the secret's selection mechanism.** THE centerpiece. Now that the world exists, design *who* pays the cost in [[The Cost]] and *how they are chosen* — the single decision that determines whether the Empire stays defensible (the design contract lives or dies here). Keep victims few, benefit vast, threat genuinely uncertain, selection not-obviously-unjust. Primary skill: `moral-parallax`. This is where the fringe "ledger doesn't balance" crank (see The Sworn) and the frontier silence eventually point.
2. **Naming pass.** Lock all provisional names now that the cultures/peoples behind them exist. Use `conlang` / `language-evolution` for phonological consistency and `character-naming`'s entropy approach so names don't cluster. Everything currently named is a working label (see the "Names are provisional" note above).

**Then, later:** revelation architecture (the clue/reveal timeline by session milestone — `key-moments` + `oblique-worldbuilding` + `memetic-depth`); magic & Daggerheart fit in an orderly world; session/arc structure (the case-of-the-arc engine).

> **How this build was run (repeat it):** each subtask went to a fresh-context background subagent, briefed to read this Build Plan + the premise notes cold, stay lean, use the named skills, and **surface high-impact forks rather than lock them.** The user made the taste calls; decisions were logged above. This pattern worked well — reuse it for Task 2 (though the secret is sensitive enough you may want to design it in the main thread with the user rather than fan out).

## Links
- [[The Premise]] · [[Themes]] · [[The Cost]] · [[00 - Core]]
