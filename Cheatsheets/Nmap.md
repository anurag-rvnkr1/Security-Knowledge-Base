# Nmap Quick Reference

Use Nmap only on targets explicitly in scope. The examples below target loopback only.

| Purpose | Command | Notes |
|---|---|---|
| Identify local host | `nmap 127.0.0.1` | Default scan behavior depends on privileges and platform |
| Selected local ports | `nmap -p 22,80,443 127.0.0.1` | Checks only listed ports |
| Service version probe | `nmap -sV -p 22,80 127.0.0.1` | Generates additional traffic |
| Save normal output | `nmap -oN scan.txt 127.0.0.1` | Protect output if it contains sensitive details |

`-Pn` skips host discovery; it does not make scanning authorized. See [Network Security](../Network-Security/) and the [Nmap reference guide](https://nmap.org/book/man.html).
