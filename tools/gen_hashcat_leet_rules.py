#!/usr/bin/env python3
"""
gen_hashcat_leet_rules.py  -  emit hashcat dict + rule files for a l33t attack.

For each base word it writes:
    <word>.dict   the lowercase base word (a length placeholder; rules overwrite it)
    <word>.rule   one rule line per leet+case combination, using oNX (overwrite
                  char at position N with X)

Then crack with:
    hashcat -m 0 -a 0 hashes.txt <word>.dict -r <word>.rule --force
    hashcat -m 0 hashes.txt --show        # results (hash:plaintext) from the potfile

-m sets the algorithm: 0=MD5, 100=SHA1, 1400=SHA256, 13400=KeePass.

NOTE: oNX overwrites exactly ONE character, so combinations that use a multi-char
substitution (ph, vv, \\/, ><) are skipped here -- do those with leet_crack.py,
or extend this to emit insert rules.

Usage:
    python3 -I gen_hashcat_leet_rules.py --subs map.json --out ./rules Word1 Word2
"""
import argparse, itertools, json, os, sys

DEFAULT_SUBS = {
    "A": ["a", "4", "@"], "B": ["b", "8"], "C": ["c", "("], "D": ["d"],
    "E": ["e", "3"], "F": ["f", "ph"], "G": ["g", "9"], "H": ["h", "#"],
    "I": ["i", "1", "!"], "J": ["j"], "K": ["k"], "L": ["l", "1"],
    "M": ["m"], "N": ["n"], "O": ["o", "0"], "P": ["p", "9"], "Q": ["q"],
    "R": ["r"], "S": ["s", "5", "$"], "T": ["t", "7", "+"], "U": ["u", "v"],
    "V": ["v", "\\/"], "W": ["w", "vv"], "X": ["x", "><"], "Y": ["y"],
    "Z": ["z", "2"],
}
POS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # hashcat position labels (0-35)


def options(ch, subs):
    out = []
    for o in subs.get(ch.upper(), [ch]):
        if o.isalpha():
            out += [o.lower(), o.upper()]   # both cases, every letter
        else:
            out.append(o)
    return list(dict.fromkeys(out))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("words", nargs="+")
    ap.add_argument("--subs", help="JSON substitution map (default: built-in)")
    ap.add_argument("--out", default=".", help="output directory (default: cwd)")
    args = ap.parse_args()

    subs = json.load(open(args.subs)) if args.subs else DEFAULT_SUBS
    os.makedirs(args.out, exist_ok=True)

    for word in args.words:
        if len(word) > len(POS):
            print(f"! {word}: too long for oNX positions, skipping", file=sys.stderr)
            continue
        base = word.lower()
        rules = []
        for combo in itertools.product(*[options(c, subs) for c in word]):
            if any(len(c) != 1 for c in combo):      # oNX = single char only
                continue
            rules.append(" ".join(f"o{POS[i]}{c}" for i, c in enumerate(combo)))
        rules = list(dict.fromkeys(rules))
        dpath = os.path.join(args.out, f"{base}.dict")
        rpath = os.path.join(args.out, f"{base}.rule")
        open(dpath, "w").write(base + "\n")
        open(rpath, "w").write("\n".join(rules) + "\n")
        print(f"{word}: {len(rules)} rules -> {rpath} (+ {dpath})")


if __name__ == "__main__":
    main()
