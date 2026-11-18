# 🛠️ Password-Cracking Method

A technique-first reference for the password-cracking challenges I've worked, focused on
how to choose and drive the right attack. No competition-provided content (hashes, flags,
answers, or challenge files) is included.

## Method cheat-sheet

1. **Identify the algorithm first.** Hash length in hex chars → `32 = MD5`, `40 = SHA1`,
   `64 = SHA256`. For structured hashes (`$keepass$…`, `$2y$…`) let `john`/`hashcat`
   identify the mode. The wrong algorithm means nothing ever matches.
2. **Cracking = generate candidates → hash → compare.** Make sure the real password is
   *inside* the candidate set: right algorithm, right base words, complete mutation rulebook.
3. **Match the attack to the password's shape.**
    - word **+ word** → combinator (`-a 1 list list`)
    - word **+ digits/pattern** → hybrid (`-a 6 list ?d?d?d`)
    - word **+ leet/case mutations** → a rule file or an exhaustive candidate generator
4. **When a run "fails" instantly, suspect setup before method** — the hash not loading
   (a `user:` prefix, trailing shadow fields), a rule file in the wordlist slot, or the wrong mode.
5. **Pick the tool by cost** — hashcat for scale / slow algorithms; a tailored script for a
   small, exact, exhaustive search against a custom spec.

!!! warning "Safe handling of challenge files"
    When running any cracking script, invoke Python with **`-I`** and keep the script
    **out of** any directory holding downloaded challenge files. Python auto-imports
    modules from the script's own directory and the CWD, so a planted `json.py` next to
    untrusted files could run on import. `-I` disables that.
