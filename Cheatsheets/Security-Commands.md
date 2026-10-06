# Security Commands Quick Reference

Examples are read-oriented and should be scoped to authorized hosts and data.

| Need | Command | Caveat |
|---|---|---|
| SHA-256 file hash | `sha256sum FILE` / `Get-FileHash FILE` | A hash is an identifier, not a verdict |
| DNS lookup | `dig example.org` / `Resolve-DnsName example.org` | Public lookups may disclose queried names |
| TLS certificate summary | `openssl s_client -connect example.org:443 -servername example.org` | Connect only to authorized services |
| HTTP response headers | `curl -I https://example.org` | Server behavior can vary |
| Current sockets | `ss -plant` / `Get-NetTCPConnection` | Privilege affects process details |

Avoid copying commands blindly. Check the target, permissions, side effects, and output sensitivity first.
