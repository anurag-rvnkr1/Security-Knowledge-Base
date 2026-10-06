# API Security Quick Reference

| Control | Check |
|---|---|
| Authentication | Validate issuer, audience, expiry, signature, and intended token use |
| Authorization | Check object- and function-level access on every request |
| Input | Validate schema, type, range, and size on the server |
| Rate control | Apply quotas appropriate to identity and operation |
| Data exposure | Return only fields required by the caller |
| Operations | Log security-relevant events without recording secrets |

See the [OWASP API Security Top 10](https://owasp.org/www-project-api-security/) and [API Security](../API-Security/).
