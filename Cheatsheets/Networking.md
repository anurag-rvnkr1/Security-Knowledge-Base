# Networking Quick Reference

| Purpose | Linux | Windows |
|---|---|---|
| Interfaces and addresses | `ip addr` | `ipconfig /all` |
| Routes | `ip route` | `route print` |
| DNS lookup | `dig example.org` | `nslookup example.org` |
| TCP listeners | `ss -lnt` | `Get-NetTCPConnection -State Listen` |
| Reachability | `ping HOST` | `Test-Connection HOST` |
| HTTP headers | `curl -I https://example.org` | Same in modern Windows |

ICMP filtering may make ping inconclusive. Use these commands only for systems in scope. More: [Networking](../Networking/) and [Network Security](../Network-Security/).
