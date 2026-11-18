#!/usr/bin/env python3
"""
leet_crack.py  -  l33t-speak substitution cracker for password challenges.

Takes base word(s) + a target hash file, generates every leetspeak + mixed-case
spelling of each word using a substitution map, hashes each candidate, and prints
any that match a target hash.

KEY LESSON:
  The passwords capitalise letters ANYWHERE in the word, not just the first.
  So every alphabetic position must try BOTH cases, on top of the symbol swaps.
  Only toggling the first letter (or none) produced zero hits.

Run it with -I and keep it OUT of the folder holding downloaded challenge files.

Confirm the algorithm by hash length first: 32=md5, 40=sha1, 64=sha256.
"""
import argparse, itertools, hashlib, json, sys

# Default map. Override with --subs.
DEFAULT_SUBS = {
    "A": ["a", "4", "@"], "B": ["b", "8"], "C": ["c", "("], "D": ["d"],
    "E": ["e", "3"], "F": ["f", "ph"], "G": ["g", "9"], "H": ["h", "#"],
    "I": ["i", "1", "!"], "J": ["j"], "K": ["k"], "L": ["l", "1"],
    "M": ["m"], "N": ["n"], "O": ["o", "0"], "P": ["p", "9"], "Q": ["q"],
    "R": ["r"], "S": ["s", "5", "$"], "T": ["t", "7", "+"], "U": ["u", "v"],
    "V": ["v", "\\/"], "W": ["w", "vv"], "X": ["x", "><"], "Y": ["y"],
    "Z": ["z", "2"],
}


def build_options(ch, subs, case_mode):
    """Option list for one character: substitutions + case variants."""
    raw = subs.get(ch.upper(), [ch])
    out = []
    for o in raw:
        if o.isalpha():
            if case_mode == "all":            # both cases, every letter  <-- the winner
                out += [o.lower(), o.upper()]
            elif case_mode == "smart":        # match the base letter's case only
                out.append(o.upper() if ch.isupper() else o.lower())
            else:                             # "none": lowercase as given
                out.append(o.lower())
        else:
            out.append(o)                     # digits / symbols unchanged
    return list(dict.fromkeys(out))           # de-dupe, keep order


def variants(word, subs, case_mode):
    per_char = [build_options(c, subs, case_mode) for c in word]
    for combo in itertools.product(*per_char):
        yield "".join(combo)


def main():
    ap = argparse.ArgumentParser(description="l33t-speak hash cracker")
    ap.add_argument("--hashes", required=True, help="file of target hashes, one per line")
    ap.add_argument("--words", nargs="*", default=[], help="base words to mangle")
    ap.add_argument("--wordlist", help="file of base words, one per line")
    ap.add_argument("--subs", help="JSON substitution map (default: built-in)")
    ap.add_argument("--algo", default="md5", help="md5 (default), sha1, sha256, ...")
    ap.add_argument("--case", default="all", choices=["all", "smart", "none"],
                    help="case handling; 'all' (both cases every letter) is the proven default")
    args = ap.parse_args()

    subs = json.load(open(args.subs)) if args.subs else DEFAULT_SUBS
    targets = {l.strip() for l in open(args.hashes) if l.strip()}
    bases = list(args.words)
    if args.wordlist:
        bases += [l.strip() for l in open(args.wordlist) if l.strip()]
    if not bases:
        sys.exit("No base words given (use --words and/or --wordlist).")

    def h(s):
        return hashlib.new(args.algo, s.encode()).hexdigest()

    found = 0
    for base in bases:
        for cand in variants(base, subs, args.case):
            if h(cand) in targets:
                print(f"{base} -> {cand}")
                found += 1
    print(f"# done: {found} match(es) across {len(bases)} base word(s), {len(targets)} target(s)",
          file=sys.stderr)


if __name__ == "__main__":
    main()
