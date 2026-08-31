---
title: Naming Tools
type: asset
visibility: gm
note_status: fleshed
tags: [asset, naming, language, generator]
aliases: [Naming Tools, Name Generator, Naming Generator]
created: 2026-08-31
updated: 2026-08-31
---

# Naming Tools

Production tooling for [[The Old Tongue]] and [[Naming People in the Turning]]. This folder is not a second source of canon: the language note owns phonology, roots, drifts, and the collision register.

## Reproducible algorithm

`generate_names.py` uses **algorithm version 1**:

1. Begin with the decimal seed reduced to an unsigned 32-bit integer.
2. Advance an LCG with  
   `state = (1664525 × state + 1013904223) mod 2^32`.
3. Select each inventory item with `(state × len(inventory)) >> 32`. Using
   the high half of the product avoids the weak low-bit cycle of an LCG when
   an inventory has a power-of-two length.
4. Reject duplicates, exact reserved names, names within Levenshtein distance 2 of a reserved name, and compounds in a closed root family.
5. Continue advancing the same stream until the requested count is filled.

The seed, mode, register or drift, count, algorithm version, and candidate position together reproduce a draw. A seed alone does not. Run `python3 "14 - Assets/Names/generate_names.py" --version` to print the algorithm version.

Existing canon names are **reserved inputs**, not output fixtures. The tool does not pretend to reconstruct old lists whose original generator was never stored. It makes future entropy reproducible and prevents the crowded namespace from worsening.

## Usage

```bash
# Person-name candidates
python3 "14 - Assets/Names/generate_names.py" \
  --seed 20260831 --register conservative --count 20

# Hearth registers: kusawe, sakoa, gonan, kumbaan
python3 "14 - Assets/Names/generate_names.py" \
  --seed 20260831 --register kusawe --count 20

# Old-Tongue compounds from the open root reserve
python3 "14 - Assets/Names/generate_names.py" \
  --seed 20260831 --compound-drift worn --count 12

# Collision gate for a proposed name (exit 0 passes; exit 1 rejects)
python3 "14 - Assets/Names/generate_names.py" \
  --seed 0 --check "Aeloren"
```

Do not select the first candidate automatically. Generate a field, choose for meaning and table clarity, record the full command and selected position in production notes, then add an approved name to the script's reserved set.

## Links

- [[The Old Tongue]] — canonical sound system, roots, drift, and collision register
- [[Naming in the Turning]] — spoken and written naming rule
- [[Naming People in the Turning]] — person and hearth registers
