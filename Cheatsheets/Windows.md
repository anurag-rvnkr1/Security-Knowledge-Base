# Windows Quick Reference

For fuller coverage see [Windows](../Windows/) and [Endpoint Security](../Endpoint-Security/).

| Task | PowerShell command | Notes |
|---|---|---|
| Identity | `whoami /all` | Includes group and privilege information |
| Host details | `Get-ComputerInfo` | Can produce extensive output |
| Processes | `Get-Process` | Current process inventory |
| Services | `Get-Service` | Service state |
| Network config | `Get-NetIPConfiguration` | Interfaces and addresses |
| Connections | `Get-NetTCPConnection` | Current TCP connections |
| Event records | `Get-WinEvent -LogName System -MaxEvents 50` | Check access and event volume |
| File hash | `Get-FileHash .\file.bin -Algorithm SHA256` | Hash does not establish file safety |

Export or share output only after checking for sensitive identifiers and data.
