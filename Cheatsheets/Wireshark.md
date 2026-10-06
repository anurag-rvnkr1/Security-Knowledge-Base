# Wireshark Quick Reference

Display filters limit visible packets; they do not alter the capture.

| Goal | Display filter |
|---|---|
| Host address | `ip.addr == 192.0.2.10` |
| TCP port | `tcp.port == 443` |
| DNS traffic | `dns` |
| HTTP requests | `http.request` |
| TLS handshake | `tls.handshake` |
| Failed TCP setup | `tcp.flags.syn == 1 && tcp.flags.ack == 0` |

Capture filters use a different syntax from display filters. Captures can contain credentials or personal data; collect only with authorization and protect the files. See [Networking](../Networking/) and [Network Security](../Network-Security/).
