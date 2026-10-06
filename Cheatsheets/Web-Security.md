# Web Security Quick Reference

| Review area | Questions |
|---|---|
| Authentication | Are credentials protected and login flows rate-limited? |
| Authorization | Is access enforced server-side for each object and action? |
| Input handling | Are untrusted inputs validated and encoded for their output context? |
| Sessions | Are cookies appropriately scoped, `Secure`, `HttpOnly`, and `SameSite`? |
| Transport | Is HTTPS enforced with suitable TLS configuration? |
| Errors and logs | Do responses avoid leaking secrets while retaining useful audit events? |

Use an authorized test environment and the [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/). More: [Web Security](../Web-Security/).
