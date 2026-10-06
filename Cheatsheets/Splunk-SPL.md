# Splunk SPL Quick Reference

Examples assume a search-time field named `sourcetype`; adapt indexes and fields to your environment.

| Purpose | SPL |
|---|---|
| Search source | `index=main sourcetype=syslog earliest=-24h` |
| Select fields | `... \| table _time host user action` |
| Count by field | `... \| stats count by user` |
| Time buckets | `... \| timechart span=1h count by action` |
| Deduplicate values | `... \| dedup host` |

Use bounded time ranges and confirm field extraction. Do not run expensive broad searches on production without considering platform impact. See [Splunk Search Reference](https://docs.splunk.com/Documentation/Splunk/latest/SearchReference) and [SIEM](../SIEM/).
