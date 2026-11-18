# 🧰 Skills & Tooling

*Weighted toward the domains where I have documented solves.*

| Domain | Techniques I've applied | Tools |
|---|---|---|
| **OSINT** | Image & metadata analysis, barcode/standards lookups (e.g. GS1), public-record and search-operator research, methodical guess-economy under limited attempts | Search engines, reverse image search, metadata/EXIF inspection |
| **Password Cracking** | Algorithm identification, dictionary + rule/mask/combinator/hybrid attacks, l33t-speak mutation spaces, encrypted-vault (KeePass) key recovery, Unicode/UTF-8 byte-level cracking, keyspace/feasibility analysis | `hashcat`, `John the Ripper`, `princeprocessor`, `pykeepass` |
| **Cryptography** | Encoding analysis, XOR, multi-step decoding recipes, hash/collision concepts | `CyberChef`, Python |
| **Log Analysis** | Log parsing & timeline reconstruction, event correlation, anomaly hunting | CLI text processing, `Zeek`, `grep`/`awk`/`jq` |
| **Network Traffic** | PCAP analysis, protocol inspection, extracting artifacts from captures | `Wireshark` / `tshark` |
| **Also engaged** (less documented) | Forensics, Web App Exploitation, Scanning & Enumeration | `YARA`, `Burp Suite`, `nmap` *(trim any you haven't used in earnest)* |

---

## How I approach a challenge

1. **Read the prompt fully** — the answer (or a strong hint) is often embedded in the text or title.
2. **Identify the problem class** — what *kind* of weakness or encoding is this?
3. **Pick the right tool for the shape** — e.g. word+word → combinator; word+digits → hybrid.
4. **Debug setup before method** — when an attack "fails" instantly, suspect a parsing/loading
   issue (a stray prefix, a misplaced rule file, the wrong mode) before blaming the wordlist.
5. **Mind feasibility** — estimate keyspace vs. hash speed so I don't launch an attack that can't finish.
