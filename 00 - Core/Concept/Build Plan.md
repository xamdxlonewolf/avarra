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

## Task 1 — the playable surface (this build)

Tracked in the task list (IDs 1a–1d). Sequencing (dependencies enforced in the tracker):

```
1a  Imperial geography & map        ← FOUNDATION, unblocked, start here
      ├── 1b  Conquered peoples       (needs 1a)
      │        └── 1c  The rebellion  (needs 1a + 1b)
      └── 1d  The commission of inquiry (needs 1a)   ← the PC-facing engine
```

- **1a — Geography & map.** Imperial core / frontier / recently-pacified provinces; how it's administered; where the circuit rides; geography that makes "roads work, famines rare, trade protected" plausible. → `04 - Settlements` (+ maybe `01 - World`). Skills: `settlement-design`, `systemic-worldbuilding`, `memetic-depth`, `cliche-transcendence`.
- **1b — Conquered peoples.** 2–4 distinct cultures with real texture; ≥1 recently-pacified (grievance), ≥1 long-integrated (content). The human ground the rebellion grows from. Skills: `memetic-depth`, `belief-systems`, `cliche-transcendence`, `character-naming`.
- **1c — The rebellion.** Who, what they know/suspect, why *now*, methods, internal factions. **Must stay sympathetic.** Skills: `moral-parallax` (primary), `governance-systems`, `character-arc`.
- **1d — The commission of inquiry.** The PCs' institution: remit, authority & limits, ranks, how it travels and staffs itself (the "job not identity" frame). The week-to-week engine — prioritize table usability. Skills: `governance-systems`, `positional-revelation`, `underdog-unit`.

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

## Later (not this build)

Task 2 — the secret's **selection mechanism** (the `moral-parallax` centerpiece; where defensible-vs-monstrous is won). Then: revelation architecture, magic & Daggerheart fit, session/arc structure.

## Links
- [[The Premise]] · [[Themes]] · [[The Cost]] · [[00 - Core]]
