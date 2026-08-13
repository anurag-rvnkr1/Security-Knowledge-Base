# Chapter 05 – Search, Queries & Event Analysis

> SIEM search is the foundation of security investigation. Analysts use queries to move from millions of raw events to a small set of relevant evidence, identify patterns, build timelines, validate detections, and investigate suspicious behavior.

---

# 1. Introduction

A SIEM can collect billions of events, but collected data has little value if analysts cannot efficiently search and analyze it.

The basic workflow is:

```text
Security Question
       ↓
Search Query
       ↓
Relevant Events
       ↓
Filtering
       ↓
Aggregation
       ↓
Correlation
       ↓
Analysis
       ↓
Conclusion
```

For example:

```text
Question:
"Did this user log in from an unusual IP?"

        ↓

Search:
user.name = alice
AND
event.category = authentication

        ↓

Events

        ↓

Compare:
Source IP
Location
Device
Time
Previous Activity

        ↓

Conclusion
```

---

# 2. What is SIEM Search?

SIEM search is the process of querying stored security telemetry to find events matching specific conditions.

Example:

```text
Find all failed logins for user alice
during the last 24 hours.
```

Conceptually:

```text
SELECT events
WHERE
    user = alice
    AND
    outcome = failure
    AND
    event_type = authentication
```

Different SIEM platforms use different query languages.

---

# 3. Why Search Matters

Search supports:

```text
Alert Investigation
Threat Hunting
Incident Response
Detection Development
Detection Validation
Root Cause Analysis
Forensics
Compliance
Reporting
```

---

# 4. Search vs Detection

These concepts are closely related but different.

## Search

An analyst manually asks:

```text
"Show me failed logins from this IP."
```

## Detection

The SIEM automatically asks:

```text
"Alert me whenever an IP generates
more than 20 failed logins in 5 minutes."
```

Therefore:

```text
SEARCH
Human-driven

DETECTION
Machine-driven
```

---

# 5. Search vs Correlation

### Search

Find events matching conditions.

```text
source.ip = X
```

### Correlation

Connect multiple events.

```text
Failed Login
     +
Successful Login
     +
Privilege Escalation
```

Search can be used as the building block for correlation.

---

# 6. The Security Question

Good investigations begin with a question.

Examples:

```text
Did the account authenticate successfully?

Where did the login originate?

Which hosts did the account access?

What processes executed afterward?

Did the account access sensitive data?

Did another account perform similar activity?
```

Avoid starting with:

```text
"Let me search everything."
```

Instead:

```text
Question
 ↓
Hypothesis
 ↓
Query
 ↓
Evidence
```

---

# 7. Query Fundamentals

Most SIEM queries use concepts such as:

```text
Field
Operator
Value
Condition
Time Range
Aggregation
Sorting
Grouping
```

Example:

```text
event.outcome = failure
```

Breakdown:

```text
Field:
event.outcome

Operator:
=

Value:
failure
```

---

# 8. Common Query Operators

Common operators include:

```text
=
!=
>
<
>=
<=
IN
NOT IN
AND
OR
NOT
CONTAINS
MATCHES
EXISTS
```

Exact syntax depends on the SIEM.

---

# 9. Equality

Example:

```text
event.outcome = failure
```

Meaning:

```text
Return events where outcome is failure.
```

---

# 10. Inequality

Example:

```text
event.outcome != success
```

Meaning:

```text
Return events whose outcome is not success.
```

Be careful with missing/null fields because behavior differs between query languages.

---

# 11. Greater Than

Example:

```text
network.bytes > 100000000
```

Could identify events involving unusually large data volumes.

---

# 12. Less Than

Example:

```text
destination.port < 1024
```

Could identify connections to commonly privileged/system ports.

The query alone does not prove malicious activity.

---

# 13. AND

```text
event.category = authentication
AND
event.outcome = failure
```

Both conditions must match.

---

# 14. OR

```text
event.action = login
OR
event.action = authentication
```

Useful when different sources represent similar activity differently.

---

# 15. NOT

Example:

```text
event.outcome = failure
AND
NOT
source.ip = 10.10.10.10
```

Excludes a known source.

Use exclusions carefully because attackers can abuse assumptions behind allowlists.

---

# 16. Parentheses

Complex queries should use explicit grouping.

Example:

```text
event.category = authentication
AND
(
    event.outcome = failure
    OR
    event.action = password_change
)
```

This improves readability and avoids logical ambiguity.

---

# 17. Time Range

Time is one of the most important dimensions in SIEM search.

Example:

```text
Last 15 minutes
Last 1 hour
Last 24 hours
Last 7 days
Custom range
```

A query without an appropriate time range can produce:

```text
Too Much Data
Slow Search
Irrelevant Results
```

---

# 18. Start Narrow

A good investigation strategy is:

```text
Narrow Time Range
+
Specific Entity
+
Specific Event Type
```

Example:

```text
User:
alice

Time:
09:00–10:00

Event:
Authentication
```

Then expand if necessary.

---

# 19. Query Example

Question:

> "Did Alice have failed logins today?"

Conceptual query:

```text
user.name = "alice"
AND
event.category = "authentication"
AND
event.outcome = "failure"
```

Time:

```text
Today
```

---

# 20. Query Example — Source IP

Question:

> "What activity came from this IP?"

```text
source.ip = "10.10.10.20"
```

Then expand:

```text
source.ip = "10.10.10.20"
AND
@timestamp >= ...
```

---

# 21. Query Example — Destination

```text
destination.ip = "10.10.20.10"
```

This can help determine:

```text
Who contacted the server?
When?
How frequently?
Which ports?
Which protocols?
```

---

# 22. Query Example — User

```text
user.name = "alice"
```

This can become an investigation pivot.

Search related:

```text
Authentication
Process
Network
Cloud
File
Application
```

---

# 23. Query Example — Host

```text
host.name = "WEB01"
```

Then inspect:

```text
Authentication
Process Creation
Network Connections
File Activity
Security Alerts
```

---

# 24. Query Example — Process

```text
process.name = "powershell.exe"
```

Then investigate:

```text
Who launched it?
What was the command line?
Parent process?
Network connections?
User?
Host?
Time?
```

---

# 25. Query Example — Command Line

Search for suspicious command-line indicators.

Examples:

```text
powershell
EncodedCommand
certutil
bitsadmin
rundll32
regsvr32
wmic
```

A keyword match is an indicator, not proof of malicious activity.

---

# 26. Query Example — Failed Authentication

```text
event.category = authentication
AND
event.outcome = failure
```

Then aggregate by:

```text
source.ip
user.name
host.name
```

This can reveal:

```text
Brute Force
Password Spraying
Misconfiguration
User Error
```

---

# 27. Aggregation

Aggregation summarizes large numbers of events.

Instead of:

```text
Event 1
Event 2
Event 3
...
Event 10,000
```

we can ask:

```text
How many failures occurred per source IP?
```

Result:

```text
10.0.0.1 → 5
10.0.0.2 → 83
10.0.0.3 → 2
```

---

# 28. Count

Conceptually:

```text
COUNT(events)
GROUP BY source.ip
```

This is useful for:

```text
Brute Force
Scanning
High-Volume Requests
Repeated Failures
```

---

# 29. Group By

Example:

```text
GROUP BY user.name
```

Could produce:

```text
alice → 4
bob   → 2
charlie → 57
```

This identifies unusual concentrations.

---

# 30. Top-N Analysis

Example:

```text
Top 10 source IPs
by failed login count
```

Output:

```text
IP            Count
10.0.0.20     500
10.0.0.21     350
10.0.0.22     240
```

This is useful for prioritization.

---

# 31. Unique Count

Sometimes total event count is less useful than unique entities.

Example:

```text
Source IP:
10.0.0.20

Failed Login Count:
100
```

vs:

```text
Unique Users:
50
```

The second signal may be more indicative of password spraying.

Conceptually:

```text
COUNT(DISTINCT user)
```

---

# 32. Cardinality

Cardinality refers to the number of unique values.

Example:

```text
100 login attempts
```

with:

```text
1 unique user
```

may suggest brute force.

Whereas:

```text
100 login attempts
50 unique users
```

may suggest password spraying.

---

# 33. Statistical Analysis

SIEM queries can be used to identify:

```text
Average
Maximum
Minimum
Count
Percentiles
Unique Values
Rates
Distribution
```

Example:

```text
Average bytes transferred per user
```

---

# 34. Baseline

A baseline describes normal behavior.

Example:

```text
Alice normally:
09:00–18:00
India
Corporate Device
```

Observed:

```text
03:00
Unknown Device
Foreign IP
```

The difference is an anomaly candidate.

---

# 35. Baseline Queries

Example:

```text
Count logins by user
over previous 30 days
```

Then compare:

```text
Current Activity
vs
Historical Pattern
```

---

# 36. Rare Event Analysis

Search for events that occur infrequently.

Example:

```text
Rare process
Rare destination domain
Rare country
Rare user-agent
Rare administrative action
```

Rare does not automatically mean malicious.

---

# 37. Frequency Analysis

Search for unusually frequent events.

Example:

```text
10,000 DNS queries
from one host
in 1 minute
```

Potential:

```text
Malware
DNS Tunneling
Misconfiguration
Automated Application
```

Further investigation is required.

---

# 38. Time-Series Analysis

Security events can be analyzed over time.

Example:

```text
09:00 → 10
09:05 → 12
09:10 → 15
09:15 → 900
```

A sudden spike may indicate:

```text
Attack
Outage
Misconfiguration
Logging Change
```

---

# 39. Event Rate

Example:

```text
500 login failures
in 5 minutes
```

Rate:

```text
100 failures/minute
```

Rate-based detections are useful for:

```text
Brute Force
Scanning
Flooding
Abuse
```

---

# 40. Threshold Queries

Example:

```text
IF
failed_logins > 20
```

This is a threshold.

A better detection might specify:

```text
failed_logins > 20
within 5 minutes
from same source.ip
```

Context improves signal quality.

---

# 41. Query Optimization

Poor:

```text
Search all events
for all time
with complex wildcard conditions
```

Better:

```text
Restrict Time
 ↓
Restrict Index/Data Source
 ↓
Filter High-Value Fields
 ↓
Aggregate
```

---

# 42. Time Filtering

Always use the narrowest reasonable time range.

Instead of:

```text
Last 365 days
```

start with:

```text
Last 15 minutes
```

then:

```text
1 hour
```

then:

```text
24 hours
```

if required.

---

# 43. Field Filtering

Instead of searching all event fields:

```text
"powershell"
```

prefer a specific field where possible:

```text
process.name = "powershell.exe"
```

or:

```text
process.command_line CONTAINS "EncodedCommand"
```

This improves precision.

---

# 44. Search Scope

Possible search scopes:

```text
All Data
Specific Index
Specific Data Source
Specific Host
Specific User
Specific Event Category
```

Narrowing scope improves efficiency.

---

# 45. Search Performance

Large SIEM environments can contain:

```text
Billions
or
Trillions
of events
```

Poor queries can consume significant resources.

Analysts should understand:

```text
Time Range
Indexes
Fields
Aggregations
Cardinality
Wildcards
Joins
Subqueries
```

---

# 46. Wildcards

Example:

```text
*.example.com
```

Wildcards can be useful but expensive.

Broad wildcard:

```text
*login*
```

may scan many values.

More specific queries are generally preferable.

---

# 47. Full-Text Search

Example:

```text
"failed password"
```

Useful when field-level parsing is unavailable.

However:

```text
Full-Text Search
```

may be less precise than:

```text
Structured Field Search
```

---

# 48. Structured Search

Prefer:

```text
event.outcome = failure
```

over:

```text
message contains "failed"
```

when the normalized field exists.

Structured fields are generally:

```text
More Precise
More Efficient
More Consistent
```

---

# 49. Query Languages

Different SIEMs use different query languages.

Examples include:

```text
KQL
SPL
Lucene-style Query Syntax
AQL
SQL-like Queries
Platform-Specific Languages
```

The concepts remain similar:

```text
Filter
Search
Aggregate
Group
Sort
Correlate
```

---

# 50. KQL

Kusto Query Language is widely associated with Microsoft security analytics.

Conceptual example:

```text
SigninLogs
| where ResultType != 0
| summarize count() by UserPrincipalName
```

This identifies authentication failures grouped by user.

---

# 51. SPL

Splunk Search Processing Language can express searches such as:

```text
index=auth action=failure
| stats count by src_ip
```

Conceptually:

```text
Search
 ↓
Filter
 ↓
Aggregate
```

---

# 52. SQL-Style SIEM Queries

Some security platforms support SQL-like analytics.

Conceptually:

```sql
SELECT source_ip, COUNT(*)
FROM authentication_events
WHERE outcome = 'failure'
GROUP BY source_ip;
```

This returns:

```text
Source IP
+
Failure Count
```

---

# 53. Query Portability

A query written for one SIEM may not work directly in another.

For example:

```text
Splunk SPL
```

is not the same as:

```text
KQL
```

However, the security logic can be translated.

Example:

```text
"Count failed logins per source IP over 5 minutes"
```

is platform-independent.

---

# 54. Search Logic vs Query Syntax

Separate:

```text
SECURITY LOGIC
```

from:

```text
QUERY LANGUAGE
```

Security logic:

```text
More than 20 failures
from same IP
within 5 minutes
```

Implementation:

```text
SPL
KQL
SQL
AQL
Lucene
```

This makes detection engineering more portable.

---

# 55. Event Analysis

Searching finds events.

Analysis determines what those events mean.

Example:

```text
Search:
source.ip = X
```

returns:

```text
500 events
```

Analysis asks:

```text
What users?
What hosts?
What actions?
What time?
What destination?
What sequence?
Is it normal?
Is it malicious?
```

---

# 56. Event Context

Never analyze an event in isolation when more context is available.

Example:

```text
PowerShell execution
```

Ask:

```text
Who?
Where?
When?
Parent process?
Command line?
Network?
File?
User privilege?
Related alerts?
```

---

# 57. Pivoting

Pivoting means using one discovered artifact to search for related activity.

Example:

```text
Suspicious IP
     ↓
Search IP
     ↓
Find User
     ↓
Search User
     ↓
Find Host
     ↓
Search Host
     ↓
Find Process
     ↓
Search Process
```

---

# 58. Investigation Pivot Types

Common pivots:

```text
IP
User
Hostname
Domain
URL
File Hash
Process
Email
Cloud Resource
Alert ID
Session ID
```

---

# 59. IP Pivot

Start:

```text
Suspicious IP
```

Search:

```text
source.ip = X
OR
destination.ip = X
```

Then identify:

```text
Users
Hosts
Ports
Domains
Actions
```

---

# 60. User Pivot

Start:

```text
user.name = alice
```

Search:

```text
Authentication
Endpoint
Cloud
Application
Privilege
```

Then construct:

```text
User Activity Timeline
```

---

# 61. Host Pivot

Start:

```text
host.name = WEB01
```

Search:

```text
Processes
Network
Authentication
Files
Security Alerts
```

---

# 62. Hash Pivot

If a suspicious file hash is discovered:

```text
file.hash.sha256 = X
```

Search:

```text
Which hosts saw it?
Which users executed it?
When?
What process launched it?
Did it connect externally?
```

---

# 63. Domain Pivot

If a suspicious domain appears:

```text
dns.question.name = suspicious.example
```

Search:

```text
DNS
Proxy
Firewall
Endpoint
Email
```

This may reveal the scope of activity.

---

# 64. Timeline Analysis

Timeline analysis organizes events chronologically.

Example:

```text
08:55
Phishing Email

09:01
User Click

09:02
Credential Submission

09:07
Successful Login

09:08
MFA Event

09:12
Privilege Change

09:20
Data Access
```

The timeline provides an attack narrative.

---

# 65. Timeline Sources

A timeline can combine:

```text
Email
Identity
Endpoint
Network
Cloud
Application
EDR
Firewall
DNS
```

This is one of the strongest advantages of centralized security analytics.

---

# 66. Before-and-After Analysis

For an important event:

```text
Suspicious Login
```

Search:

```text
15 minutes before
+
15 minutes after
```

This can reveal:

```text
Initial Access
Authentication
Execution
Privilege Escalation
Persistence
Data Access
```

---

# 67. Blast Radius

Investigation should determine scope.

Questions:

```text
How many users affected?

How many hosts?

How many IPs?

How many accounts?

How many applications?

How much data?

Which critical assets?
```

---

# 68. Scope Query

Example:

```text
Find all hosts associated with
user alice during incident window.
```

Then:

```text
GROUP BY host.name
```

Result:

```text
WEB01
DB01
APP01
LAPTOP01
```

---

# 69. Evidence Quality

Not all events have equal reliability.

Consider:

```text
Source Reliability
Timestamp Accuracy
Parsing Accuracy
Completeness
Correlation
Independent Confirmation
```

Example:

```text
Single application log
```

vs:

```text
Application
+
Firewall
+
EDR
+
Identity
```

Multiple independent sources can provide stronger evidence.

---

# 70. Event Corroboration

Suppose:

```text
EDR:
PowerShell executed
```

and:

```text
Network:
Connection to suspicious domain
```

and:

```text
DNS:
Domain resolved
```

Together:

```text
Higher Confidence
```

---

# 71. Query Results

A good query should answer a question.

Bad:

```text
Search:
all events
```

Better:

```text
Question:
Did the compromised user access a database?

Query:
user = X
AND
destination.category = database
```

---

# 72. Search Result Columns

Useful investigation columns include:

```text
Timestamp
User
Source IP
Destination IP
Host
Action
Outcome
Process
Command Line
URL
Event ID
Severity
```

The best columns depend on the investigation.

---

# 73. Saved Searches

Frequently used queries can be saved.

Examples:

```text
Failed Logins
Privileged Activity
New Admin Accounts
Suspicious PowerShell
Rare DNS Domains
Critical Asset Activity
```

Benefits:

```text
Consistency
Speed
Knowledge Sharing
Repeatability
```

---

# 74. Search Templates

SOC teams can create templates.

Example:

```text
USER INVESTIGATION

1. Authentication
2. Hosts
3. Processes
4. Network
5. Cloud
6. Privilege
7. Alerts
```

This helps analysts investigate consistently.

---

# 75. Query Documentation

A useful query should document:

```text
Purpose
Data Source
Required Fields
Time Range
Logic
Expected Result
Known Limitations
```

---

# 76. Detection Development Using Search

Detection engineering often begins with exploratory search.

```text
Threat Hypothesis
      ↓
Manual Search
      ↓
Find Pattern
      ↓
Validate Pattern
      ↓
Create Detection
      ↓
Test
      ↓
Deploy
```

---

# 77. Example: Brute Force

Hypothesis:

> An attacker may repeatedly attempt authentication.

Search:

```text
event.category = authentication
AND
event.outcome = failure
```

Aggregate:

```text
COUNT BY source.ip
```

Then:

```text
Identify High-Volume Sources
```

Then test:

```text
20+
within 5 minutes
```

---

# 78. Example: Password Spraying

Hypothesis:

> An attacker may use one password against many accounts.

Search:

```text
authentication failures
```

Group by:

```text
source.ip
```

Calculate:

```text
unique(user.name)
```

Potential indicator:

```text
1 source IP
+
many unique users
+
short time window
```

---

# 79. Example: Suspicious PowerShell

Search:

```text
process.name = powershell.exe
```

Then inspect:

```text
process.command_line
parent process
user.name
host.name
network connections
file creation
```

A more suspicious chain may be:

```text
Office Application
 ↓
PowerShell
 ↓
Encoded Command
 ↓
Network Connection
```

---

# 80. Example: Data Exfiltration

Search:

```text
Large outbound transfers
```

Group by:

```text
user
host
destination
```

Compare against:

```text
Historical baseline
```

Then investigate:

```text
What data?
Who initiated?
Where sent?
Was it authorized?
```

---

# 81. Query Mistakes

Common mistakes:

```text
No time range
Overly broad search
Wrong field
Wrong data source
Case sensitivity assumptions
Incorrect Boolean logic
Ignoring null values
Ignoring time zones
Ignoring duplicates
Ignoring delayed events
```

---

# 82. Boolean Logic Mistake

Incorrect:

```text
A OR B AND C
```

Depending on language/operator precedence, this may not mean what the analyst intended.

Safer:

```text
(A OR B)
AND C
```

Use parentheses.

---

# 83. Time Range Mistake

Analyst searches:

```text
10:00–10:05
```

but events arrive at:

```text
10:06
```

The event is missed.

Consider:

```text
Event Time
Ingestion Delay
Clock Drift
```

---

# 84. Field Mapping Mistake

Analyst searches:

```text
source.ip
```

but the source only contains:

```text
src_ip
```

If normalization failed:

```text
No results
```

This may be mistaken for:

```text
No activity
```

when the real problem is:

```text
Data Pipeline Issue
```

---

# 85. Empty Search Results

"No results" does not necessarily mean:

```text
No activity
```

Possible reasons:

```text
No activity
Wrong field
Wrong time range
Wrong index
Parser failure
Log source failure
Data retention
Query syntax error
Delayed ingestion
```

Always validate the data pipeline.

---

# 86. Query Validation

Before trusting a query:

```text
1. Verify data source exists.
2. Verify events exist.
3. Verify field names.
4. Verify timestamp.
5. Test known event.
6. Test narrow query.
7. Expand scope.
```

---

# 87. Search Performance Best Practices

```text
1. Use narrow time windows.

2. Filter on indexed/structured fields.

3. Avoid unnecessary wildcard searches.

4. Avoid scanning all data unnecessarily.

5. Limit returned fields where supported.

6. Aggregate instead of retrieving millions of raw events.

7. Use specific indexes/data sources.

8. Test expensive queries.

9. Avoid unnecessary repeated searches.

10. Reuse saved queries when appropriate.
```

---

# 88. Search and Privacy

Queries can expose sensitive information.

Examples:

```text
User Activity
Email
Authentication
Command Lines
URLs
Business Data
```

Analysts should access only data necessary for their authorized duties.

---

# 89. Search Audit Logs

SIEM platforms should ideally record administrative and security-relevant actions such as:

```text
Who searched?
When?
What was accessed?
Who modified a rule?
Who changed permissions?
```

This supports:

```text
Accountability
Security
Compliance
Investigation
```

---

# 90. Query-Based Threat Hunting

A hunt often starts with:

```text
Hypothesis
```

Example:

> "An attacker may be using PowerShell to execute commands on endpoints."

Then:

```text
Search PowerShell
 ↓
Identify unusual users
 ↓
Identify unusual hosts
 ↓
Inspect command lines
 ↓
Inspect parent processes
 ↓
Inspect network
 ↓
Look for related indicators
```

---

# 91. Threat Hunting Loop

```text
HYPOTHESIS
    ↓
SEARCH
    ↓
FILTER
    ↓
PIVOT
    ↓
CORRELATE
    ↓
VALIDATE
    ↓
FINDING
    ↓
NEW HYPOTHESIS
```

Threat hunting is iterative.

---

# 92. Query-Based Detection Validation

After creating a detection:

```text
Detection Rule
      ↓
Generate Test Activity
      ↓
Search Raw Events
      ↓
Verify Expected Fields
      ↓
Verify Rule Trigger
      ↓
Verify Alert Context
```

---

# 93. Detection Debugging

If a detection does not trigger:

```text
1. Did the event arrive?

2. Was it parsed?

3. Are fields normalized?

4. Is the timestamp correct?

5. Is the query correct?

6. Is the time window correct?

7. Is the detection enabled?

8. Is the threshold correct?

9. Is the rule suppressed?

10. Did correlation state expire?
```

---

# 94. Query and Detection Relationship

```text
QUERY
   ↓
Explore Data
   ↓
Find Pattern
   ↓
Validate Pattern
   ↓
DETECTION RULE
   ↓
Continuous Monitoring
```

This is one of the most important workflows in SIEM engineering.

---

# 95. Practical Lab

Create a small SIEM lab with:

```text
Windows
Linux
Network Telemetry
Authentication Logs
```

Practice:

```text
1. Find failed logins.

2. Group by source IP.

3. Find top source IPs.

4. Count unique users.

5. Search successful login after failures.

6. Pivot from IP to user.

7. Pivot from user to host.

8. Build a timeline.

9. Identify suspicious behavior.

10. Turn the finding into a detection.
```

---

# 96. Practical Query Exercise

Given:

```text
09:00 Alice failed login from 10.0.0.5
09:01 Alice failed login from 10.0.0.5
09:02 Bob failed login from 10.0.0.5
09:03 Charlie failed login from 10.0.0.5
09:04 Alice successful login from 10.0.0.5
```

Ask:

```text
How many failures?

How many unique users?

Was there a successful login?

What is the source IP?

What pattern is present?
```

Possible conclusion:

```text
Multiple authentication failures
against multiple users
followed by a success
from one source IP.
```

This warrants investigation but is not by itself proof of an attack.

---

# 97. Practical Timeline Exercise

Given:

```text
10:00 Failed Login
10:01 Failed Login
10:02 Successful Login
10:03 MFA Failure
10:04 Successful MFA
10:06 New Admin Group Membership
10:10 Large Data Download
```

Construct:

```text
Authentication
      ↓
Account Access
      ↓
Privilege Change
      ↓
Data Access
```

Then identify:

```text
Potential Attack Stages
```

---

# 98. Investigation Questions

For any suspicious event ask:

```text
WHO?
WHAT?
WHEN?
WHERE?
HOW?
WHAT BEFORE?
WHAT AFTER?
WHAT ELSE?
HOW MANY?
HOW FAR?
```

---

# 99. Query Checklist

Before executing:

```text
☐ What question am I answering?
☐ Correct data source?
☐ Correct field?
☐ Correct time range?
☐ Correct timezone?
☐ Correct Boolean logic?
☐ Are fields normalized?
☐ Could events be delayed?
☐ Could duplicates exist?
☐ Is the query expensive?
```

---

# 100. Interview Questions

### What is SIEM search?

> The process of querying security telemetry to identify events and patterns relevant to investigation, hunting, detection, or analysis.

### Why is time range important?

> It reduces irrelevant data, improves query performance, and ensures the investigation covers the relevant activity window.

### What is aggregation?

> Summarizing events using operations such as count, unique count, average, or grouping.

### What is cardinality?

> The number of unique values in a field.

### Why is cardinality useful?

> It can distinguish patterns such as brute force against one account from password spraying across many accounts.

### What is pivoting?

> Using a discovered artifact such as an IP, user, host, domain, or hash to search for related activity.

### What is timeline analysis?

> Ordering events chronologically to reconstruct activity and understand an incident.

### Why are structured fields preferred?

> They provide more precise and efficient searching than broad free-text searches.

### What is a false "no results" situation?

> When a query returns nothing because of a data or query problem rather than because the activity did not occur.

### How do you optimize SIEM queries?

> Use narrow time ranges, specific structured fields, appropriate indexes, efficient aggregations, and avoid unnecessary broad wildcard searches.

### What is a detection hypothesis?

> A testable assumption about suspicious behavior that can be investigated through telemetry and potentially converted into a detection rule.

### What is threat hunting?

> Proactively searching telemetry for evidence of malicious or anomalous behavior based on a hypothesis.

### How do search and detection engineering relate?

> Analysts often use exploratory searches to identify and validate patterns before converting them into automated detection rules.

### What should you do if a query returns no events?

> Verify the time range, data source, field names, parser/normalization, ingestion health, retention, and query syntax before concluding there was no activity.

---

# 101. Quick Revision

```text
SEARCH
→ Find relevant events

QUERY
→ Express investigation logic

FILTER
→ Reduce data

AGGREGATE
→ Summarize data

GROUP BY
→ Organize events by entity

CARDINALITY
→ Count unique values

BASELINE
→ Understand normal behavior

PIVOT
→ Move from one artifact to related activity

TIMELINE
→ Reconstruct chronological activity

CORRELATION
→ Connect events

HUNT
→ Proactively search for threats

DETECTION
→ Automate validated search logic
```

---

# 102. Golden Rules

```text
1. Start with a security question.

2. Use the narrowest useful time range.

3. Prefer structured fields over broad text search.

4. Validate field names before trusting results.

5. Always consider timezone differences.

6. Consider ingestion delays.

7. "No results" does not always mean "no activity."

8. Use aggregation to reduce large datasets.

9. Use unique counts to identify behavioral patterns.

10. Pivot from discovered artifacts.

11. Build timelines during investigations.

12. Corroborate important findings across multiple sources.

13. Treat rare activity as an indicator, not automatic proof of compromise.

14. Treat high-volume activity as an investigation signal, not automatic proof of attack.

15. Use parentheses for complex Boolean logic.

16. Optimize expensive queries.

17. Document important investigation queries.

18. Convert validated search patterns into detections.

19. Query performance matters in large SIEM environments.

20. The goal of SIEM search is not to find more data—it is to find the right evidence.
```

---

# 103. Final Mental Model

Remember SIEM search using:

```text
QUESTION
   ↓
HYPOTHESIS
   ↓
TIME RANGE
   ↓
DATA SOURCE
   ↓
FIELD
   ↓
FILTER
   ↓
AGGREGATE
   ↓
PIVOT
   ↓
CORRELATE
   ↓
TIMELINE
   ↓
EVIDENCE
   ↓
CONCLUSION
```

And for detection engineering:

```text
SEARCH
   ↓
FIND PATTERN
   ↓
VALIDATE
   ↓
GENERALIZE
   ↓
DETECTION RULE
   ↓
TEST
   ↓
DEPLOY
   ↓
MONITOR
   ↓
TUNE
```

---

# 104. Chapter Summary

SIEM search is the bridge between **stored telemetry** and **security intelligence**.

The complete analytical process is:

```text
               SECURITY QUESTION
                       │
                       ▼
                  SEARCH DATA
                       │
                       ▼
                    FILTER
                       │
                       ▼
                  AGGREGATE
                       │
                       ▼
                    PIVOT
                       │
                       ▼
                 CORRELATE
                       │
                       ▼
                   TIMELINE
                       │
                       ▼
                CORROBORATE
                       │
                       ▼
                   ANALYZE
                       │
                       ▼
                  CONCLUSION
```

The most important principle is:

> **Searching finds events; analysis gives those events meaning.**

An effective SOC analyst does not simply search for suspicious strings. They ask focused questions, understand the data model, build queries, compare activity against context and baselines, pivot across entities, reconstruct timelines, and evaluate evidence.

This leads directly into the next chapter:

```text
Chapter 06 – Detection Engineering & Detection Rules
```

The next step is to take the searches and behavioral patterns discovered here and turn them into **repeatable, tested, production-ready security detections**.