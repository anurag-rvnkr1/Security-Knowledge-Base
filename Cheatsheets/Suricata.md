# Suricata Quick Reference

Suricata rule syntax and supported keywords depend on version and configuration.

```text
alert dns $HOME_NET any -> $EXTERNAL_NET 53 (msg:"Example DNS query observed"; dns.query; content:"training.invalid"; nocase; sid:1000001; rev:1;)
```

This example matches a synthetic training domain and is not a threat indicator. Validate rule parsing, variables, and traffic direction in a test sensor before deployment. See [Suricata documentation](https://docs.suricata.io/) and [Network Security](../Network-Security/).
