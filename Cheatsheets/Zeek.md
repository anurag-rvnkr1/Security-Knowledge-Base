# Zeek Quick Reference

| Artifact | Typical use |
|---|---|
| `conn.log` | Connection metadata and duration |
| `dns.log` | DNS query and response metadata |
| `http.log` | HTTP transaction metadata where visible |
| `ssl.log` / `tls.log` | TLS connection and certificate metadata; naming varies by version |
| `files.log` | File observations and analysis metadata |

Example offline processing: `zeek -r capture.pcap`. Run against an authorized capture and verify log schemas for your Zeek version. See [Zeek documentation](https://docs.zeek.org/) and [Digital Forensics](../Digital-Forensics/).
