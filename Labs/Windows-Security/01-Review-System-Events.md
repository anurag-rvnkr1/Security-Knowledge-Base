# Lab: Review Recent Windows System Events

> Category: Windows Security  
> Difficulty: Beginner  
> Estimated Time: 20 minutes  
> Environment: Windows workstation or disposable VM

## Objective

Query a bounded set of recent System events and practice separating event facts from analyst interpretation.

## Procedure

In PowerShell, record the collection time and retrieve recent System log entries:

```powershell
Get-Date -Format o
Get-WinEvent -FilterHashtable @{LogName='System'; StartTime=(Get-Date).AddHours(-2)} -MaxEvents 50 |
    Select-Object TimeCreated, Id, LevelDisplayName, ProviderName, Message
```

If access is denied, do not elevate automatically; use approved access or a supplied sample dataset.

## Analysis

Group observations by time and provider. Select one warning or error and verify its meaning in Microsoft documentation for the relevant Windows version. Check for expected maintenance, reboot, or service events before inferring an incident.

## Expected Results

The command returns up to 50 events from the previous two hours. A quiet system may return fewer; event presence and message formats vary.

## Safety and Cleanup

The exercise reads local logs. Do not export or share event messages without checking for hostnames, usernames, and other sensitive details.

## Further Practice

Compare System and Application logs over the same bounded period. See [Windows](../../Windows/) and [Digital Forensics](../../Digital-Forensics/).
