# 🛠️ Password-Cracking Tools

Two small, self-authored Python tools I built for CTF password-cracking challenges,
plus a short method cheat-sheet. Both tackle the same problem — **l33t-speak +
mixed-case mutations of known base words** — from two angles: a self-contained Python
cracker for exact/exhaustive runs, and a hashcat rule generator for GPU-scale runs.

> These are my own code. No competition-provided content (hashes, flags, answers,
> or challenge files) is included here.

---

## Tools

| Tool | What it does |
|---|---|
| [`leet_crack.py`](./leet_crack.py) | Generates every leet + mixed-case spelling of each base word via a substitution map (`itertools.product` over per-character option lists), hashes each candidate, and prints matches against a target hash file. Handles multi-character subs (`F→ph`, `W→vv`, `V→\/`, `X→><`). |
| [`gen_hashcat_leet_rules.py`](./gen_hashcat_leet_rules.py) | Emits a hashcat `.dict` + `.rule` pair per base word (positional-overwrite `oNX` rules) so the *same* search space runs on the GPU. Single-char subs only — use `leet_crack.py` for words needing multi-char subs. |

### Usage

```bash
# Self-contained Python cracker (confirm the algorithm by hash length first)
python3 -I leet_crack.py --hashes hashes.txt --algo md5 --words Falcon Harbor Lantern

# GPU route: generate dict+rule pairs, then run hashcat
python3 -I gen_hashcat_leet_rules.py --out ./rules Falcon Harbor Lantern
hashcat -m 0 -a 0 hashes.txt rules/falcon.dict -r rules/falcon.rule --force
hashcat -m 0 hashes.txt --show        # hash:plaintext from the potfile
```

> ⚠️ **Run with `-I`** and keep these scripts **out of** any directory holding
> downloaded challenge files. Python auto-imports modules from the script's own
> directory and the CWD, so a planted `json.py` (etc.) next to untrusted files
> could run on import. `-I` disables that.

---

## Password-cracking method cheat-sheet

**1. Identify the algorithm first.** Hash length in hex chars → `32 = MD5`,
`40 = SHA1`, `64 = SHA256`. For structured hashes (`$keepass$…`, `$2y$…`) let
`john`/`hashcat` identify the mode. Hashing guesses with the wrong algorithm means
nothing ever matches.

**2. Cracking = generate candidates → hash → compare.** The whole game is making
sure the real password is *inside* the candidate set: right algorithm, right base
words, and a mutation rulebook complete enough to cover what was actually done.

**3. Match the attack to the password's shape.**
- word **+ word** → combinator (`-a 1 list list`)
- word **+ digits/pattern** → hybrid (`-a 6 list ?d?d?d`)
- word **+ leet/case mutations** → a rule file, or an exhaustive generator like these tools

**4. When a run "fails" instantly, suspect setup before method.** Common causes:
the hash isn't loading (a `user:` prefix or trailing shadow fields), a rule file
sitting in the wordlist slot, or the wrong mode. *Does the hash load? → is the
shape right? → is the mutation covered?*

**5. Pick the tool by cost.** hashcat for scale / slow algorithms; a tailored
Python script for a small, exact, exhaustive search against a custom spec.

---

## License

MIT — see the repository's `LICENSE`. Use freely; attribution appreciated.
