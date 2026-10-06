# Active Directory Quick Reference

Use read-only queries in an authorized domain and follow least-privilege access.

| Task | PowerShell |
|---|---|
| Current identity | `whoami /all` |
| Domain information | `Get-ADDomain` |
| Find a user | `Get-ADUser -Identity USER -Properties Enabled,LastLogonDate` |
| Find locked users | `Search-ADAccount -LockedOut` |
| List domain controllers | `Get-ADDomainController -Filter *` |

ActiveDirectory PowerShell module availability and permissions vary. Avoid dumping sensitive directory attributes. See [Active Directory](../Active-Directory/).
