# Linux Quick Reference

Quick reference only; see the detailed [Linux cheatsheet](../Linux/26-Linux-Cheat-Sheet.md).

| Task | Command | Notes |
|---|---|---|
| Identity | `id` | Current UID, GIDs, and groups |
| Host/kernel | `hostnamectl` · `uname -a` | Host and kernel context |
| Processes | `ps aux` · `top` | Process inventory |
| Listening sockets | `ss -lntup` | May require elevated privileges for process names |
| Disk space | `df -h` · `du -sh PATH` | `du` reads the selected path |
| Services | `systemctl status NAME` | Service status |
| Journal | `journalctl -u NAME --since today` | Adjust time range as needed |
| File hash | `sha256sum FILE` | Useful for evidence integrity |
| Search text | `grep -Rni -- 'pattern' DIR` | Avoid searching sensitive locations unnecessarily |

`sudo` runs commands with elevated privileges; review a command and its target before using it. See [Linux security](../Linux/).
