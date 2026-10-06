# Kerberos Quick Reference

| Task | Windows command | Notes |
|---|---|---|
| View tickets | `klist` | Shows current logon session tickets |
| Purge local tickets | `klist purge` | **State-changing:** removes cached tickets and can disrupt access |
| Check time | `w32tm /query /status` | Time skew can affect Kerberos authentication |
| Review logon events | Event Viewer → Security | Requires appropriate audit policy and access |

Ticket commands are sensitive and session-specific. Do not export or publish ticket material. See [Active Directory: Kerberos and NTLM](../Active-Directory/12-Kerberos-and-NTLM.md).
