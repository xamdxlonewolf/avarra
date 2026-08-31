#!/usr/bin/env python3
"""Deterministic naming aid for The Turning.

This is a production tool, not canon. It uses a documented 32-bit LCG so a
seed, mode, and register always reproduce the same candidate stream.
"""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass


MODULUS = 2**32
MULTIPLIER = 1_664_525
INCREMENT = 1_013_904_223
ALGORITHM_VERSION = 1

RESERVED = {
    "aeloren",
    "brenledd",
    "brenod",
    "brenorn",
    "brenvaeth",
    "brenthael",
    "eoloren",
    "eolstrand",
    "eolthael",
    "eolvaeth",
    "heskoren",
    "leddhael",
    "leddoren",
    "leddvael",
    "lestrand",
    "brudu",
    "delvor",
    "firstbowl",
    "lonasir",
    "millhold",
    "milsun",
    "talen",
    "thefirstbowl",
    "themillhold",
    "thurrei",
    "vilraet",
    "lirorn",
    "maiaethlir",
    "maiethlir",
    "maiethorn",
    "maiethren",
    "maiethvael",
    "netstrand",
    "nethoren",
    "orenbren",
    "orenhael",
    "orentel",
    "ornath",
    "ornled",
    "ornsael",
    "ornthael",
    "saelhael",
    "saelorn",
    "saelthael",
    "saelvaeth",
    "stelhael",
    "strandoren",
    "thaeloren",
    "thaelvaeth",
    "threnhael",
    "threnmaieth",
    "trenledd",
    "vaelbren",
    "vaelhesk",
    "vaeloren",
    "vaelun",
    "vaethledd",
    "vaethorn",
}

CLOSED_ROOTS = {
    "ael",
    "bren",
    "eol",
    "hael",
    "maieth",
    "oren",
    "sael",
    "thren",
    "vael",
    "vaeth",
}

ROOTS = {
    "orn": "land, ground, holding",
    "lir": "thaw, water running again",
    "neth": "night, the long dark",
    "ledd": "commercial reckoning",
    "hesk": "far or outer edge",
    "strand": "shore or landing-coast",
    "stel": "stillness or holding",
    "crae": "craft or elemental working",
}


@dataclass(frozen=True)
class Register:
    onsets: tuple[str, ...]
    vowels: tuple[str, ...]
    codas: tuple[str, ...]
    syllables: tuple[int, ...]


REGISTERS = {
    "conservative": Register(
        ("m", "n", "l", "r", "v", "s", "t", "th", "br"),
        ("a", "e", "i", "o", "u", "ae", "ai", "ei", "eo"),
        ("", "", "n", "l", "r", "th"),
        (2, 2, 3),
    ),
    "worn": Register(
        ("m", "n", "l", "r", "v", "s", "t", "d", "h", "br"),
        ("a", "e", "i", "o", "u", "ae", "ei"),
        ("", "", "n", "l", "r", "t"),
        (2, 2, 3),
    ),
    "eroded": Register(
        ("m", "n", "l", "r", "v", "s", "t", "d", "b"),
        ("a", "e", "i", "o", "u"),
        ("", "", "", "n", "l", "r", "d"),
        (2, 2, 2, 3),
    ),
    "kusawe": Register(
        ("k", "s", "sh", "n", "r", "m", "t", "w", "y", "f", "h"),
        ("a", "i", "u", "e", "o", "ai"),
        ("", "", "n", "m", "r"),
        (2, 2, 3),
    ),
    "sakoa": Register(
        ("l", "r", "n", "m", "s", "v", "f", "d", "b", "k", "w"),
        ("o", "u", "a", "ea", "oa", "i", "e"),
        ("", "l", "r", "n", "m", "s", "d", "k"),
        (2, 2, 3),
    ),
    "gonan": Register(
        ("k", "t", "g", "n", "r", "h", "s", "b", "d", "kr", "gr", "hr"),
        ("a", "o", "u", "e"),
        ("", "k", "n", "r", "t"),
        (1, 2, 2, 2, 3),
    ),
    "kumbaan": Register(
        ("m", "n", "mb", "nd", "nk", "nj", "s", "l", "r", "w", "y", "b", "k"),
        ("a", "aa", "i", "o", "oo", "u", "e"),
        ("", "", "n", "m", "l", "r"),
        (2, 2, 3),
    ),
}


class LCG:
    def __init__(self, seed: int) -> None:
        self.state = seed & 0xFFFFFFFF

    def next(self) -> int:
        self.state = (MULTIPLIER * self.state + INCREMENT) % MODULUS
        return self.state

    def choose(self, values: tuple[str, ...] | tuple[int, ...]):
        # Use the high half of a multiply, rather than the LCG's weak low bits.
        # Consecutive modulo-8 draws otherwise visit only a small set of root
        # pairs and can exhaust compound generation despite many valid pairs.
        return values[(self.next() * len(values)) >> 32]


def normalize(value: str) -> str:
    return re.sub(r"[^a-z]", "", value.lower())


def distance(left: str, right: str) -> int:
    previous = list(range(len(right) + 1))
    for i, left_char in enumerate(left, 1):
        current = [i]
        for j, right_char in enumerate(right, 1):
            current.append(
                min(
                    current[-1] + 1,
                    previous[j] + 1,
                    previous[j - 1] + (left_char != right_char),
                )
            )
        previous = current
    return previous[-1]


def collision_reasons(candidate: str) -> list[str]:
    word = normalize(candidate)
    reasons: list[str] = []
    if word in RESERVED:
        reasons.append("exactly matches a reserved or retired name")
    for reserved in sorted(RESERVED):
        if word != reserved and distance(word, reserved) <= 2:
            reasons.append(f"within edit distance 2 of {reserved}")
            break
    for root in sorted(CLOSED_ROOTS):
        if word.startswith(root) or word.endswith(root):
            reasons.append(f"uses closed compound family {root}")
            break
    return reasons


def person_candidates(seed: int, register_name: str, count: int) -> list[str]:
    register = REGISTERS[register_name]
    rng = LCG(seed)
    results: list[str] = []
    seen: set[str] = set()
    attempts = 0
    while len(results) < count and attempts < count * 200:
        attempts += 1
        syllable_count = rng.choose(register.syllables)
        pieces = [
            f"{rng.choose(register.onsets)}{rng.choose(register.vowels)}"
            f"{rng.choose(register.codas)}"
            for _ in range(syllable_count)
        ]
        candidate = "".join(pieces).capitalize()
        key = normalize(candidate)
        if key in seen or collision_reasons(candidate):
            continue
        seen.add(key)
        results.append(candidate)
    if len(results) < count:
        raise RuntimeError("candidate space exhausted under current collision rules")
    return results


def drift_word(word: str, drift: str) -> str:
    if drift == "conservative":
        return word
    if drift == "worn":
        return re.sub(r"(?<=[aeiou])th", "t", word)
    if drift == "eroded":
        eroded = word.replace("th", "t")
        for old, new in (("ae", "e"), ("ai", "a"), ("ei", "i"), ("eo", "o")):
            eroded = eroded.replace(old, new)
        return eroded
    raise ValueError(drift)


def compound_candidates(seed: int, drift: str, count: int) -> list[str]:
    rng = LCG(seed)
    roots = tuple(ROOTS)
    results: list[str] = []
    seen: set[str] = set()
    attempts = 0
    while len(results) < count and attempts < count * 200:
        attempts += 1
        first = rng.choose(roots)
        second = rng.choose(roots)
        if first == second:
            continue
        candidate = drift_word(first + second, drift).capitalize()
        key = normalize(candidate)
        if key in seen or collision_reasons(candidate):
            continue
        seen.add(key)
        results.append(candidate)
    if len(results) < count:
        raise RuntimeError("candidate space exhausted under current collision rules")
    return results


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s algorithm {ALGORITHM_VERSION}",
    )
    parser.add_argument("--seed", required=True, type=int)
    parser.add_argument("--count", type=int, default=12)
    parser.add_argument("--register", choices=tuple(REGISTERS))
    parser.add_argument("--compound-drift", choices=("conservative", "worn", "eroded"))
    parser.add_argument("--check", metavar="NAME")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    selected = sum(
        option is not None
        for option in (args.register, args.compound_drift, args.check)
    )
    if selected != 1:
        raise SystemExit("choose exactly one of --register, --compound-drift, or --check")

    if args.check:
        reasons = collision_reasons(args.check)
        if reasons:
            print(f"REJECT {args.check}: {'; '.join(reasons)}")
            return 1
        print(f"PASS {args.check}")
        return 0

    if args.register:
        candidates = person_candidates(args.seed, args.register, args.count)
    else:
        candidates = compound_candidates(args.seed, args.compound_drift, args.count)
    print("\n".join(candidates))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
