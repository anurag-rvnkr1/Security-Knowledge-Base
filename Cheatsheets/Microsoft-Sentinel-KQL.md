# Microsoft Sentinel KQL Quick Reference

KQL examples use common Sentinel tables; available columns vary by connector.

```kusto
// Recent sign-in events; verify table and column names in your workspace
SigninLogs
| where TimeGenerated > ago(24h)
| project TimeGenerated, UserPrincipalName, IPAddress, ResultType
| sort by TimeGenerated desc
```

```kusto
// Aggregate event count by host
SecurityEvent
| where TimeGenerated > ago(24h)
| summarize EventCount = count() by Computer
| sort by EventCount desc
```

Use time bounds, inspect the schema, and validate query cost and alert semantics. See [Kusto Query Language](https://learn.microsoft.com/azure/data-explorer/kusto/query/) and [SIEM](../SIEM/).
