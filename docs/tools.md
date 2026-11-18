# 🛠️ Tools

Two small, self-authored Python tools I built for CTF password-cracking challenges.
Both tackle the same problem — **l33t-speak + mixed-case mutations of known base
words** — from two angles: a self-contained Python cracker for exact/exhaustive runs,
and a hashcat rule generator for GPU-scale runs.

!!! success "My own code"
    These are original tools I wrote. No competition-provided content (hashes, flags,
    answers, or challenge files) is included. Source lives in
    [`tools/`](https://github.com/jwpamer/jwpamer.github.io/tree/main/tools) in this repo.

| Tool | What it does |
|---|---|
| `leet_crack.py` | Generates every leet + mixed-case spelling of each base word via a substitution map (`itertools.product` over per-character option lists), hashes each candidate, and prints matches against a target hash file. Handles multi-character subs (`F→ph`, `W→vv`, `V→\/`, `X→><`). |
| `gen_hashcat_leet_rules.py` | Emits a hashcat `.dict` + `.rule` pair per base word (positional-overwrite `oNX` rules) so the *same* search space runs on the GPU. Single-char subs only — use `leet_crack.py` for words needing multi-char subs. |

## Usage

```bash
# Self-contained Python cracker (confirm the algorithm by hash length first)
python3 -I leet_crack.py --hashes hashes.txt --algo md5 --words Falcon Harbor Lantern

# GPU route: generate dict+rule pairs, then run hashcat
python3 -I gen_hashcat_leet_rules.py --out ./rules Falcon Harbor Lantern
hashcat -m 0 -a 0 hashes.txt rules/falcon.dict -r rules/falcon.rule --force
hashcat -m 0 hashes.txt --show        # hash:plaintext from the potfile
```

!!! warning "Safe handling of challenge files"
    **Run with `-I`** and keep these scripts **out of** any directory holding downloaded
    challenge files. Python auto-imports modules from the script's own directory and the
    CWD, so a planted `json.py` next to untrusted files could run on import. `-I` disables that.

---

## Password-cracking method cheat-sheet

1. **Identify the algorithm first.** Hash length in hex chars → `32 = MD5`, `40 = SHA1`,
   `64 = SHA256`. For structured hashes (`$keepass$…`, `$2y$…`) let `john`/`hashcat`
   identify the mode. The wrong algorithm means nothing ever matches.
2. **Cracking = generate candidates → hash → compare.** Make sure the real password is
   *inside* the candidate set: right algorithm, right base words, complete mutation rulebook.
3. **Match the attack to the password's shape.**
    - word **+ word** → combinator (`-a 1 list list`)
    - word **+ digits/pattern** → hybrid (`-a 6 list ?d?d?d`)
    - word **+ leet/case mutations** → a rule file, or an exhaustive generator like these tools
4. **When a run "fails" instantly, suspect setup before method** — the hash not loading
   (a `user:` prefix, trailing shadow fields), a rule file in the wordlist slot, or the wrong mode.
5. **Pick the tool by cost** — hashcat for scale / slow algorithms; a tailored Python
   script for a small, exact, exhaustive search against a custom spec.
