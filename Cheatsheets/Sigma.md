# Sigma Quick Reference

Sigma is a generic rule format; backend conversion and field mapping determine execution behavior.

```yaml
title: Example Windows Process Creation Review
id: 2f2f2f2f-1111-4111-8111-222222222222
status: experimental
description: Illustrative rule structure; tune and validate against local telemetry.
logsource:
  product: windows
  category: process_creation
detection:
  selection:
    Image|endswith: '\example.exe'
  condition: selection
falsepositives:
  - Authorized administration or software deployment
level: low
```

This is a syntax illustration, not a production detection. Replace the example condition with validated behavior and test mapped fields. See [Sigma documentation](https://sigmahq.io/docs/) and [Detection Engineering](../Detection-Engineering/).
