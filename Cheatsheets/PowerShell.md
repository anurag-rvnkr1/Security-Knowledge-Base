# PowerShell Quick Reference

| Task | Example |
|---|---|
| Get help | `Get-Help Get-Process -Examples` |
| Find commands | `Get-Command *Event*` |
| Filter objects | `Get-Service | Where-Object Status -eq 'Running'` |
| Select fields | `Get-Process | Select-Object Name, Id, CPU` |
| Sort | `Get-Process | Sort-Object CPU -Descending | Select-Object -First 10` |
| Read a file | `Get-Content .\events.txt -Tail 50` |
| Hash a file | `Get-FileHash .\artifact.bin -Algorithm SHA256` |
| Event log | `Get-WinEvent -FilterHashtable @{LogName='System'; StartTime=(Get-Date).AddHours(-1)}` |

PowerShell pipelines pass objects, not merely text. Inspect command output and permissions before piping to commands that change state. See [Windows](../Windows/).
