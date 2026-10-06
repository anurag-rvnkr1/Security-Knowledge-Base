# YARA Quick Reference

YARA rules match content patterns; they do not establish that a file is malicious by themselves.

```yara
rule Example_Training_String
{
    meta:
        description = "Illustrative training rule; not a malware signature"
    strings:
        $marker = "TRAINING_SAMPLE_MARKER" ascii
    condition:
        $marker
}
```

Validate syntax with the installed YARA version and test against benign and relevant sample sets. Avoid broad rules that generate excessive false positives. See [YARA documentation](https://yara.readthedocs.io/) and [Malware Analysis](../Malware-Analysis/).
