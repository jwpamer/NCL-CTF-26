# 📝 Write-ups

!!! warning "Sanitized"
    These write-ups are sanitized per each competition's rules of conduct — see
    [Disclosure & Privacy](../disclosure.md). Each one explains the *approach and the
    lesson*, not the specific challenge text, input files, or answers.

| Write-up | Domain | What it demonstrates |
|---|---|---|
| Multi-step decoding with XOR | Cryptography | Building layered CyberChef recipes; reading the prompt for embedded hints |
| Recovering an encrypted vault's key | Password Cracking | Extracting a crackable hash, identifying the KDF, themed-wordlist strategy over brute force |
| Mixed-case l33t mutation spaces | Password Cracking | Why a custom exhaustive generator beats a canned rule for a bespoke substitution map |
| Debugging a "silent" cracking run | Password Cracking | Diagnosing hash-load failures (prefixes, trailing fields) before blaming the wordlist |
| Working a damaged-artifact OSINT puzzle | OSINT | Standards-database research and disciplined attempt management |
| Cracking non-ASCII (Unicode) passwords | Password Cracking | Attacking UTF-8 *bytes* not characters; scoping keyspace to a Unicode block |
| Fragment/substring combinator attacks | Password Cracking | Chaining combinators to rebuild passwords from substrings; proving decoys unreachable by keyspace |

*(Each write-up becomes its own page under `docs/writeups/`. Add it to the `nav:` in
`mkdocs.yml` as you publish it. An honest short list beats dead links.)*

---

## Write-up template

Copy this into a new `docs/writeups/<name>.md` and add it to the nav:

```markdown
# <Technique / Concept> — <Domain>

**Context:** Cyber Skyline (generalized) / self-authored demo
**Difficulty:** ★★★☆☆

## The Problem (generalized)
A non-identifying description of the *type* of challenge — the class of problem, not the instance.

## Approach
1. Observation — what signal pointed to the solution.
2. Reasoning — why that suggested this method.
3. Execution — the method, with a self-authored snippet where it helps.

## Key Takeaway
What this demonstrates about the underlying concept, and when it generalizes.

## Tools
`tool-a`, `tool-b`, ...
```
