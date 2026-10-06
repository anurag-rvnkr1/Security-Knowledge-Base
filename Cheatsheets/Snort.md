# Snort Quick Reference

Example rule for a synthetic lab marker; compatibility depends on Snort version and enabled preprocessors.

```text
alert tcp $HOME_NET any -> $EXTERNAL_NET 80 (msg:"Training HTTP marker observed"; flow:to_server,established; content:"TRAINING-MARKER"; http_uri; sid:1000001; rev:1;)
```

Test with the appropriate Snort configuration and controlled test traffic. A rule may not alert if protocol decoding or rule options differ by release. See [Snort documentation](https://docs.snort.org/) and [Network Security](../Network-Security/).
