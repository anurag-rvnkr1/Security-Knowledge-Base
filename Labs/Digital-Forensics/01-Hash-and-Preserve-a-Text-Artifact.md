# Lab: Hash and Preserve a Text Artifact

> Category: Digital Forensics  
> Difficulty: Beginner  
> Estimated Time: 15 minutes  
> Environment: Local shell

## Objective

Create a harmless synthetic artifact, record its SHA-256 digest, and verify that a copy matches the original.

## Procedure

```bash
mkdir -p forensic-lab
printf 'Synthetic training artifact\n' > forensic-lab/evidence.txt
sha256sum forensic-lab/evidence.txt
cp forensic-lab/evidence.txt forensic-lab/evidence-copy.txt
sha256sum forensic-lab/evidence-copy.txt
cmp forensic-lab/evidence.txt forensic-lab/evidence-copy.txt
```

On Windows PowerShell, use `Get-FileHash .\forensic-lab\evidence.txt -Algorithm SHA256` and `Compare-Object (Get-Content ...) (Get-Content ...)` for this text-only exercise.

## Expected Results

Both files initially produce the same digest and `cmp` exits successfully without output. A matching digest supports that the file contents match; it does not prove source authenticity or chain of custody.

## Safety and Cleanup

Only synthetic text is created. When finished, remove the specific `forensic-lab` directory with your file manager or an explicitly targeted command after verifying its path.

## Further Practice

Change one byte in the copy and note the digest difference. See [Digital Forensics](../../Digital-Forensics/).
