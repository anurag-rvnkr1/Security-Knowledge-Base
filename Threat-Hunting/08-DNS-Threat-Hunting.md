# DNS Threat Hunting

## Overview

Domain Name System (DNS) is one of the most important protocols for threat hunting.

Almost every enterprise endpoint, server, application, cloud workload, and security platform depends on DNS to resolve names into network destinations.

From a security perspective, DNS can provide visibility into:

- Malware infrastructure
- Command and control
- Domain generation algorithms
- DNS tunneling
- Data exfiltration
- Phishing infrastructure
- Newly observed domains
- Newly registered domains
- Compromised domains
- Internal reconnaissance
- Suspicious cloud infrastructure
- Malware staging
- Endpoint compromise

DNS is particularly valuable because attackers frequently need name resolution even when other network traffic is encrypted.

A mature DNS threat-hunting capability therefore combines:

```text
DNS Logs
   +
Endpoint Telemetry
   +
Network Flow
   +
Proxy Logs
   +
Threat Intelligence
   +
Identity
   +
Asset Context
   +
Time-Series Analysis
```

The objective is not simply to identify "bad domains."

The objective is to determine:

> **Which host queried which domain, why it queried it, how frequently it queried it, what happened afterward, and whether the behavior is consistent with the host's normal activity?**

---

# Why DNS Matters for Threat Hunting

DNS sits between applications and network infrastructure.

A simplified flow looks like:

```text
Application
     │
     ▼
Operating System
     │
     ▼
DNS Resolver
     │
     ▼
Authoritative DNS
     │
     ▼
IP Address
     │
     ▼
Network Connection
```

An attacker may therefore generate a sequence such as:

```text
Malicious Process
      │
      ▼
DNS Query
      │
      ▼
Malicious Domain
      │
      ▼
Resolved IP
      │
      ▼
HTTPS Connection
      │
      ▼
Command & Control
```

Even when the final HTTPS payload cannot be inspected, DNS can provide the first observable indication.

---

# DNS Threat-Hunting Architecture

```text
                         CLIENT
                            │
                            ▼
                    Local DNS Resolver
                            │
              ┌─────────────┴─────────────┐
              │                           │
              ▼                           ▼
          DNS Cache                  DNS Forwarder
                                          │
                                          ▼
                                  External Resolver
                                          │
                                          ▼
                                Authoritative Server
                                          │
                                          ▼
                                     IP Address
                                          │
                                          ▼
                                     Destination
```

Security telemetry can be collected at multiple points:

```text
                DNS Activity
                     │
       ┌─────────────┼─────────────┐
       ▼             ▼             ▼
 Endpoint         Resolver       Network
   Logs             Logs          Sensors
       │             │             │
       └─────────────┼─────────────┘
                     ▼
                    SIEM
                     │
                     ▼
                Threat Hunter
```

---

# DNS Components

A threat hunter should understand the basic DNS architecture.

## Stub Resolver

The endpoint's local component that initiates DNS resolution.

```text
Application
     │
     ▼
Stub Resolver
```

---

## Recursive Resolver

The recursive resolver performs DNS resolution on behalf of the client.

```text
Client
  │
  ▼
Recursive Resolver
  │
  ├── Root
  ├── TLD
  └── Authoritative
```

---

## Authoritative DNS Server

The authoritative server provides the authoritative answer for a DNS zone.

---

## DNS Cache

Resolvers and endpoints may cache DNS responses.

This can affect visibility and hunting.

A domain may not generate a DNS query every time an application connects because the result may already exist in cache.

---

# Important DNS Record Types

| Record | Purpose |
|---|---|
| A | IPv4 address |
| AAAA | IPv6 address |
| CNAME | Alias |
| MX | Mail server |
| NS | Name server |
| TXT | Text information |
| SOA | Zone authority information |
| PTR | Reverse DNS |
| SRV | Service discovery |
| CAA | Certificate authority authorization |

Attackers can abuse or interact with different record types depending on their objective.

---

# DNS Query Lifecycle

Consider:

```text
User Opens Browser
        │
        ▼
example.com
        │
        ▼
DNS Query
        │
        ▼
Resolver
        │
        ▼
DNS Response
        │
        ▼
IP Address
        │
        ▼
TCP/TLS
        │
        ▼
Application
```

For hunting, the critical correlation is:

```text
DNS Query
    ↓
Resolved IP
    ↓
Network Connection
    ↓
Endpoint Process
```

---

# DNS Telemetry

Useful DNS fields include:

```text
Timestamp
Client IP
Client Hostname
User
Resolver
Query
Query Type
Response Code
Response
TTL
Answer
```

Additional metadata may include:

```text
Process
Device
Network Zone
GeoIP
ASN
Threat Intelligence
Domain Age
Category
```

---

# DNS Logging

Common DNS sources include:

- Windows DNS Server
- Windows DNS Client telemetry
- Linux resolver logs
- BIND
- Unbound
- Infoblox
- Cisco DNS infrastructure
- Cloud DNS services
- Security DNS resolvers
- Firewall DNS telemetry
- Zeek
- Network sensors
- EDR platforms
- DNS security platforms

A mature organization should centralize DNS telemetry where possible.

---

# DNS Hunting Data Model

A useful normalized DNS event:

```text
Timestamp
    │
    ├── Source Host
    ├── Source IP
    ├── User
    ├── Query
    ├── Query Type
    ├── Response Code
    ├── Answer
    ├── Resolver
    └── Network Segment
```

This makes cross-source hunting easier.

---

# DNS Threat-Hunting Workflow

```text
DNS Event
    │
    ▼
Normalize
    │
    ▼
Enrich
    │
    ├── Domain Age
    ├── Reputation
    ├── ASN
    ├── WHOIS
    └── Threat Intelligence
    │
    ▼
Baseline
    │
    ▼
Detect Anomaly
    │
    ▼
Correlate Endpoint
    │
    ▼
Correlate Network
    │
    ▼
Investigate
```

---

# Hunt Category 1 — Rare Domains

One of the simplest DNS hunts is identifying domains rarely queried within the organization.

Example:

```text
Domain                 Hosts
--------------------------------
google.com             4,200
microsoft.com          3,700
github.com             1,900
rare-example.xyz           1
```

The rare domain deserves investigation.

However:

> **Rare does not mean malicious.**

A new business application may legitimately be used by only one department.

---

# Domain Prevalence

Calculate:

```text
Unique Hosts
Unique Users
Query Count
First Seen
Last Seen
```

Example:

```text
Domain:
example.net

Hosts:
1

Users:
1

Queries:
4

First Seen:
Today

Last Seen:
Today
```

This becomes more interesting if the endpoint also shows:

```text
PowerShell
+
New File
+
External Connection
```

---

# First-Seen Domains

Newly observed domains can be valuable hunting leads.

Example:

```text
Domain
   │
   ▼
First Seen = Today
   │
   ▼
Host Count = 1
   │
   ▼
Suspicious Process
```

Potentially suspicious.

But legitimate software releases and new SaaS platforms also create first-seen domains.

---

# Newly Registered Domains

Threat actors sometimes use recently registered domains for:

- Phishing
- Malware
- C2
- Credential harvesting
- Staging

A hunting model can combine:

```text
New Domain
+
Rare Domain
+
Suspicious Endpoint
```

instead of relying on registration age alone.

---

# Domain Age Limitations

Domain age is not proof of maliciousness.

Legitimate domains may be:

- Newly registered
- Newly acquired
- Newly activated
- Used during product launches
- Used for temporary infrastructure

Therefore:

```text
Domain Age
      +
Threat Intelligence
      +
Endpoint Context
      +
Network Behavior
```

is a stronger model.

---

# Hunt Category 2 — NXDOMAIN

NXDOMAIN means the requested domain does not exist according to the DNS response.

High NXDOMAIN activity can indicate:

- Typographical errors
- Broken applications
- Malware
- DGA
- Scanning
- Misconfiguration

Example:

```text
Host A

abc123.example.com → NXDOMAIN
qwe912.example.com → NXDOMAIN
zxc781.example.com → NXDOMAIN
mnb512.example.com → NXDOMAIN
```

This should be investigated when the pattern is unusual.

---

# NXDOMAIN Ratio

A useful metric:

```text
NXDOMAIN Ratio =
NXDOMAIN Queries / Total DNS Queries
```

Example:

```text
Total Queries = 10,000
NXDOMAIN = 4,500

Ratio = 45%
```

An unusually high ratio may indicate anomalous behavior.

But legitimate applications can also produce high failure rates.

---

# DGA Hunting

Domain Generation Algorithms can generate large numbers of domains programmatically.

Conceptually:

```text
Malware
   │
   ▼
Algorithm
   │
   ├── abcd1234.com
   ├── xq91m2.com
   ├── p7k29z.com
   └── ...
```

Only some generated domains may actually be registered.

---

# DGA Indicators

Potential signals include:

- High NXDOMAIN ratio
- Many unique domains
- Random-looking labels
- High entropy
- Short domain lifetime
- Unusual TLDs
- Repeated algorithmic structure
- High query volume

---

# DGA Detection Model

```text
Host
 │
 ├── Unique Domains ↑
 ├── NXDOMAIN ↑
 ├── Entropy ↑
 ├── Query Frequency ↑
 └── Regular Pattern
          │
          ▼
      Investigate
```

---

# Domain Entropy

Entropy can be used as one signal for measuring randomness.

Conceptually:

```text
Low Entropy
www.company.com

Higher Entropy
x7Qm92pLk3.example.com
```

However:

- CDNs
- Tracking systems
- Authentication systems
- Cloud platforms

can legitimately produce high-entropy subdomains.

Therefore entropy should never be used as a standalone maliciousness decision.

---

# Shannon Entropy

For a string:

```text
H(X) = -Σ p(x) log₂ p(x)
```

Where:

- `x` is a character
- `p(x)` is the probability of that character

Higher entropy can indicate greater character diversity.

A basic Python example:

```python
from collections import Counter
from math import log2

def entropy(value):
    counts = Counter(value)
    length = len(value)

    return -sum(
        (count / length) * log2(count / length)
        for count in counts.values()
    )
```

This is useful for exploratory hunting, not definitive malware classification.

---

# Hunt Category 3 — Long DNS Labels

DNS tunneling and automated infrastructure can produce unusually long labels.

Example:

```text
normal.example.com
```

versus:

```text
aGVsbG93b3JsZGZpbGVkYXRhMTIzNDU2.example.com
```

Potential indicators:

```text
Long Label
+
High Entropy
+
High Frequency
+
Rare Parent Domain
```

---

# DNS Tunneling

DNS tunneling abuses DNS as a communication channel.

Conceptual model:

```text
Compromised Host
       │
       ▼
Data Encoding
       │
       ▼
DNS Query
       │
       ▼
Attacker-Controlled Domain
       │
       ▼
Attacker Infrastructure
```

Responses may also carry encoded data.

---

# DNS Tunneling Indicators

Potential signals include:

- Long query labels
- High entropy
- High DNS volume
- Many unique subdomains
- Repeated TXT queries
- Unusual query types
- Persistent communication
- Rare parent domain
- Consistent query intervals

---

# DNS Tunneling vs Legitimate Services

Legitimate services can also produce:

```text
High Volume
Long Hostnames
Random Tokens
TXT Records
```

Examples include:

- Cloud authentication
- Content delivery networks
- Advertising
- Tracking
- Security products

Therefore, combine multiple signals.

---

# Hunt Category 4 — TXT Record Abuse

TXT records have legitimate uses:

- SPF
- DKIM
- Domain verification
- Application configuration

They can also be used by tunneling systems.

Hunt for:

```text
Unusual TXT Volume
+
Rare Destination
+
Long Responses
+
Suspicious Endpoint
```

---

# Hunt Category 5 — DNS Over HTTPS

DNS over HTTPS (DoH) encrypts DNS queries within HTTPS.

Traditional DNS monitoring may therefore lose visibility.

Conceptually:

```text
Endpoint
   │
   ▼
HTTPS
   │
   ▼
DoH Resolver
   │
   ▼
DNS
```

This creates a visibility challenge.

---

# DoH Hunting

Potential signals include:

- Known DoH resolver destinations
- Endpoint browser configuration
- Direct HTTPS connections to public resolvers
- Unexpected encrypted DNS behavior
- Policy violations

Organizations may choose to:

- Route approved DNS centrally
- Monitor known resolver destinations
- Control browser DNS settings
- Use endpoint security telemetry
- Monitor TLS metadata

Policies should reflect organizational requirements.

---

# DNS Over TLS

DNS over TLS similarly encrypts DNS traffic.

Conceptually:

```text
Endpoint
    │
    ▼
TLS
    │
    ▼
DNS Resolver
```

Monitoring therefore requires network and endpoint context.

---

# Encrypted DNS Visibility Model

```text
Traditional DNS
    │
    └── Query Visible

Encrypted DNS
    │
    ├── Destination Visible
    ├── Timing Visible
    ├── Volume Visible
    └── Endpoint Context Available
```

Encryption reduces payload visibility but does not necessarily eliminate behavioral visibility.

---

# Hunt Category 6 — DNS Beaconing

Periodic DNS requests may indicate automated communication.

Example:

```text
10:00:00 → c2.example.com
10:01:00 → c2.example.com
10:02:00 → c2.example.com
10:03:00 → c2.example.com
```

Potential indicators:

```text
Regular Interval
+
Rare Domain
+
Single Endpoint
+
Suspicious Process
```

---

# Beacon Jitter

Real-world beaconing may include variation:

```text
60 sec
63 sec
58 sec
61 sec
65 sec
```

This makes simple fixed-interval rules less effective.

Analyze distributions rather than exact equality.

---

# DNS Burst Analysis

Some malware may generate short bursts.

Example:

```text
10:00:01  Query
10:00:02  Query
10:00:02  Query
10:00:03  Query
10:00:04  Query
```

Followed by inactivity.

This can indicate:

- Startup activity
- Discovery
- DGA
- C2 negotiation
- Malware staging

---

# Hunt Category 7 — DNS to Network Correlation

A DNS query should often precede network communication.

Example:

```text
DNS Query
     │
     ▼
example.com
     │
     ▼
203.0.113.50
     │
     ▼
TCP/443
     │
     ▼
Endpoint Process
```

Investigate when:

```text
DNS Domain
+
Resolved IP
+
Network Connection
+
Suspicious Process
```

align temporally.

---

# DNS and Endpoint Correlation

Suppose:

```text
10:30:01
powershell.exe starts

10:30:02
DNS query to rare-domain.example

10:30:03
HTTPS connection to resolved IP

10:30:10
File created in Temp
```

This is significantly more suspicious than the DNS query alone.

---

# Hunt Category 8 — Internal DNS Reconnaissance

Attackers may query internal DNS records to discover:

- Servers
- Domain controllers
- Applications
- Services
- Internal names

Potential signals:

```text
One Endpoint
      │
      ├──► Many Internal Names
      ├──► Many Service Records
      └──► Unusual Query Types
```

Correlate with:

- User
- Endpoint role
- Administrative activity
- Network scanning

---

# Active Directory DNS Hunting

In Windows environments, DNS can provide information about:

- Domain controllers
- LDAP services
- Kerberos services
- Global Catalog
- Internal applications

Unusual DNS activity from a workstation can therefore support discovery hunting.

---

# Reverse DNS Hunting

PTR lookups can provide hostnames for IP addresses.

Potentially useful for:

```text
IP
 ↓
PTR
 ↓
Hostname
 ↓
Asset Identification
```

Reverse DNS can also support investigation of unusual destinations.

---

# DNS and Phishing

Phishing infrastructure may involve:

```text
New Domain
    │
    ▼
DNS
    │
    ▼
Web Server
    │
    ▼
Credential Collection
```

Potential indicators include:

- Newly registered domain
- Lookalike naming
- Suspicious hosting
- Rare internal access
- Multiple users querying the domain
- Email-related activity

DNS should be correlated with email telemetry.

---

# Lookalike Domains

Attackers may register domains resembling legitimate organizations.

Example concept:

```text
company.com
compaany.com
company-login.example
company-secure.example
```

Defensive hunting can identify:

- Character substitutions
- Added characters
- Homoglyphs
- Similar subdomains

DNS monitoring can provide an early warning.

---

# Typosquatting

Common patterns:

```text
company.com
compnay.com
compny.com
companyy.com
```

A domain may be legitimate or malicious.

The security value comes from correlation with:

```text
Email
Browser
Endpoint
DNS
Identity
```

---

# DNS Sinkhole

A sinkhole redirects known malicious domains to controlled infrastructure.

Conceptually:

```text
Compromised Host
      │
      ▼
Malicious Domain
      │
      ▼
DNS Sinkhole
      │
      ▼
Security Team
```

Sinkhole telemetry can reveal:

- Infected hosts
- Query frequency
- Affected users
- Malware families
- C2 attempts

---

# Sinkhole Hunting

A useful workflow:

```text
Sinkhole Hit
     │
     ▼
Identify Host
     │
     ▼
Identify User
     │
     ▼
Identify Process
     │
     ▼
Investigate Timeline
     │
     ▼
Scope Enterprise
```

A sinkhole hit should be treated as an investigation lead.

---

# DNS Threat Intelligence

DNS indicators can be enriched with:

```text
Domain Reputation
IP Reputation
Passive DNS
WHOIS
Domain Age
Registrar
ASN
Hosting Provider
Certificate
Threat Actor Associations
Malware Associations
ATT&CK
```

---

# Passive DNS

Passive DNS records historical DNS observations.

Conceptually:

```text
Domain
 │
 ├── IP A
 ├── IP B
 ├── IP C
 └── IP D
```

This can help determine infrastructure relationships.

---

# Infrastructure Pivoting

Suppose a suspicious domain resolves to an IP.

Investigate:

```text
Domain
  │
  ▼
IP
  │
  ├── Other Domains
  ├── ASN
  ├── Certificates
  └── Historical Resolutions
```

This can identify related infrastructure.

---

# DNS Infrastructure Graph

```text
               Domain A
                  │
                  ▼
               IP 1
              /    \
             /      \
        Domain B   Domain C
             \      /
              \    /
               IP 2
```

Graph-based hunting can reveal clusters that are difficult to identify through individual indicators.

---

# Domain Generation and Machine Learning

Organizations may use statistical or machine-learning approaches to identify algorithmically generated domains.

Features can include:

```text
Length
Entropy
Character Distribution
TLD
NXDOMAIN Ratio
Query Frequency
Domain Age
Host Prevalence
```

Machine learning should complement analyst investigation rather than replace it.

---

# DNS Baselines

A good DNS baseline should consider:

```text
Host
User
Department
Location
Application
Time
Domain
Query Frequency
```

For example:

```text
Developer Laptop
Expected:
github.com
pypi.org
npmjs.com
microsoft.com
```

A sudden query to:

```text
random-domain.example
```

may deserve investigation.

But a new development dependency could also explain it.

---

# Role-Based DNS Baselines

Different users have different normal behavior.

Example:

```text
Developer
 ├── GitHub
 ├── Package Repositories
 └── Cloud Platforms

Finance User
 ├── ERP
 ├── Banking
 └── Office SaaS

Server
 ├── Update Services
 ├── Internal APIs
 └── Monitoring
```

Role-aware baselines reduce false positives.

---

# DNS Query Volume

High volume can indicate:

- Malware
- DGA
- DNS tunneling
- Misconfiguration
- Application behavior
- Browser activity

Therefore:

```text
High Volume
    +
Rare Destination
    +
High Entropy
```

is more valuable than volume alone.

---

# Time-Based DNS Hunting

Compare DNS activity by:

```text
Hour
Day
Week
Month
```

An endpoint that normally communicates during business hours but begins generating unusual DNS activity overnight may deserve investigation.

---

# After-Hours DNS Activity

Example:

```text
Normal:
09:00–18:00

Observed:
02:14
02:15
02:16
02:17
```

Potentially suspicious.

But servers, backup systems, and automated applications frequently operate overnight.

Asset role is essential.

---

# User-to-Domain Analysis

Build relationships:

```text
User
 │
 ├── Domain A
 ├── Domain B
 ├── Domain C
 └── Domain D
```

Look for:

```text
User
   │
   ▼
Rare Domain
   │
   ▼
Rare Process
```

---

# Host-to-Domain Analysis

Similarly:

```text
Host
 │
 ├── Common Domain
 ├── Common Domain
 ├── Rare Domain
 └── Rare Domain
```

Rare host-domain relationships can become hunt candidates.

---

# Domain-to-Host Analysis

Reverse the relationship:

```text
Domain
 │
 ├── Host A
 ├── Host B
 ├── Host C
 └── Host D
```

A domain suddenly appearing across many endpoints may indicate:

- Malware campaign
- Phishing campaign
- Software deployment
- New SaaS service

Context determines meaning.

---

# DNS Hunting With Splunk

Example:

```spl
index=dns
| stats
    count as queries
    dc(src_ip) as hosts
    min(_time) as first_seen
    max(_time) as last_seen
    by query
| sort hosts
```

This can help identify rare domains.

---

# NXDOMAIN Hunt

```spl
index=dns
response_code=NXDOMAIN
| stats
    count as nxdomain_count
    dc(query) as unique_domains
    by src_ip
| sort - nxdomain_count
```

Investigate high-volume sources.

---

# Long Domain Hunt

Conceptually:

```spl
index=dns
| eval query_length=len(query)
| where query_length > 60
| stats count by src_ip, query
| sort - count
```

Thresholds should be tuned for the environment.

---

# Rare Domain Hunt

```spl
index=dns
| stats dc(src_ip) as host_count by query
| where host_count <= 2
```

Then enrich the results.

---

# DNS Hunt With KQL

Conceptually:

```kusto
DnsEvents
| summarize
    QueryCount = count(),
    HostCount = dcount(DeviceName)
    by Name
| order by HostCount asc
```

The exact table and fields depend on the telemetry platform.

---

# DNS Entropy Analysis With Python

Example:

```python
import math
from collections import Counter

def shannon_entropy(value):
    counts = Counter(value)
    total = len(value)

    return -sum(
        (count / total) * math.log2(count / total)
        for count in counts.values()
    )

domain = "x7a92kq1p9"
print(shannon_entropy(domain))
```

For enterprise hunting, calculate entropy at the label level rather than blindly applying it to the entire FQDN.

---

# Practical Lab 1 — Rare Domain Hunt

## Objective

Identify domains queried by very few hosts.

### Procedure

1. Collect DNS telemetry.
2. Group by domain.
3. Calculate host prevalence.
4. Identify low-prevalence domains.
5. Enrich the domain.
6. Correlate with endpoint activity.

### Investigation Questions

```text
Who queried it?
Which endpoint?
When?
How often?
What process was active?
What IP did it resolve to?
Did the endpoint connect to it?
```

---

# Practical Lab 2 — NXDOMAIN Hunt

## Objective

Identify hosts generating unusually high NXDOMAIN activity.

### Procedure

```text
DNS Logs
   │
   ▼
Filter NXDOMAIN
   │
   ▼
Group by Host
   │
   ▼
Count
   │
   ▼
Calculate Ratio
   │
   ▼
Investigate Outliers
```

Then determine whether the host is:

- User endpoint
- Server
- DNS infrastructure
- Security scanner
- Application server

---

# Practical Lab 3 — DNS Beaconing

## Objective

Find periodic DNS queries.

### Procedure

1. Group events by host and domain.
2. Sort by timestamp.
3. Calculate intervals.
4. Measure interval consistency.
5. Check destination reputation.
6. Correlate endpoint process.

Example:

```text
Host
 │
 ▼
Domain
 │
 ├── 60 sec
 ├── 62 sec
 ├── 59 sec
 ├── 61 sec
 └── 60 sec
```

---

# Practical Lab 4 — DNS Tunneling

## Objective

Identify potential DNS tunneling.

Look for combinations of:

```text
High Query Volume
+
Long Labels
+
High Entropy
+
Many Unique Subdomains
+
Rare Domain
```

Then inspect:

```text
TXT Queries
NXDOMAIN
Query Timing
Endpoint Process
Network Connections
```

---

# Practical Lab 5 — DGA Hunting

## Objective

Identify possible domain-generation behavior.

Search for:

```text
High NXDOMAIN
+
High Unique Domain Count
+
High Entropy
+
Short-Lived Domains
```

Then determine whether the behavior belongs to:

- Security software
- Browser
- Application
- Malware
- Unknown process

---

# Practical Lab 6 — DNS-to-Process Correlation

## Objective

Determine which process generated suspicious DNS behavior.

Workflow:

```text
DNS Query
    │
    ▼
Host
    │
    ▼
EDR
    │
    ▼
Process
    │
    ▼
Parent Process
    │
    ▼
Command Line
```

This can transform a weak DNS signal into a high-value investigation lead.

---

# Practical Lab 7 — Sinkhole Investigation

Given:

```text
Known malicious domain
```

search:

```text
DNS logs
```

Identify:

```text
Affected Hosts
Users
Query Count
First Seen
Last Seen
Associated Process
```

Then determine whether multiple endpoints are affected.

---

# Practical Lab 8 — Domain Infrastructure Pivot

Start with:

```text
Suspicious Domain
```

Pivot through:

```text
Domain
 ↓
IP
 ↓
ASN
 ↓
Other Domains
 ↓
Certificates
 ↓
Historical DNS
```

Document the infrastructure relationships.

---

# DNS Incident Timeline

Example:

```text
08:41:22
User logs in

08:42:15
Suspicious process starts

08:42:16
DNS query to rare domain

08:42:17
Domain resolves to external IP

08:42:18
HTTPS connection established

08:42:21
File downloaded

08:42:25
New persistence mechanism created
```

This is a strong example of why DNS should be correlated with endpoint telemetry.

---

# DNS Detection Engineering

A mature DNS detection pipeline:

```text
DNS Telemetry
      │
      ▼
Normalization
      │
      ▼
Enrichment
      │
      ▼
Baseline
      │
      ▼
Behavioral Analysis
      │
      ▼
Detection
      │
      ▼
Correlation
      │
      ▼
SOC Investigation
```

---

# Example Detection — Suspicious DNS Volume

Conceptually:

```text
IF

Host DNS volume
    >
Historical baseline

AND

NXDOMAIN ratio
    >
Expected threshold

AND

Unique domains
    >
Expected threshold

THEN

Generate hunting signal
```

Do not automatically classify the host as compromised.

---

# Example Detection — DNS Tunneling

Conceptually:

```text
IF

Long DNS labels
+
High entropy
+
High query frequency
+
Many unique subdomains
+
Rare parent domain

THEN

Generate DNS tunneling investigation signal
```

---

# Example Detection — Beaconing

```text
IF

Same Host
+
Same Destination Domain
+
Repeated Queries
+
Stable Intervals
+
Rare Destination

THEN

Generate C2 hunting signal
```

Enhance it with:

```text
+
Suspicious Endpoint Process
```

---

# DNS False Positives

Common sources include:

- CDNs
- Cloud applications
- Antivirus
- EDR
- Browser extensions
- Advertising
- Telemetry
- Software updates
- Service discovery
- Load balancing
- Authentication platforms

Before creating a permanent exception:

```text
Understand
   ↓
Validate
   ↓
Document
   ↓
Scope
   ↓
Tune
```

---

# DNS Detection Tuning

Poor detection:

```text
Long Domain = Alert
```

Better:

```text
Long Domain
+
High Entropy
+
Rare Parent Domain
+
High Frequency
+
Single Host
```

Even better:

```text
DNS Anomaly
+
Suspicious Process
+
Network Connection
+
Threat Intelligence
```

---

# DNS Data Quality

A mature DNS monitoring system should answer:

```text
Which host?
Which user?
Which domain?
Which query type?
When?
How often?
What answer?
Which resolver?
What happened afterward?
```

If these fields are unavailable, document the telemetry gap.

---

# DNS Telemetry Gaps

Example:

```text
DNS Query Logs       ✓
Source IP             ✓
Hostname              ✓
User                  ✗
Process                ✗
Query Type             ✓
Response               ✓
Endpoint Correlation   ✗
```

The SOC should understand the limitations before relying on the data for high-confidence detection.

---

# Secure DNS Architecture

A mature enterprise may use:

```text
Endpoint
   │
   ▼
Enterprise DNS Policy
   │
   ▼
Internal Resolver
   │
   ├── Logging
   ├── Filtering
   ├── Threat Intelligence
   └── Sinkhole
   │
   ▼
Approved External Resolution
```

This creates centralized visibility.

---

# DNS Security Controls

Common defensive controls include:

- Centralized DNS resolution
- DNS filtering
- Malicious-domain blocking
- Sinkholing
- DNS logging
- Threat intelligence integration
- Split-horizon DNS
- DNSSEC where appropriate
- Resolver access control
- Monitoring unauthorized DNS resolvers
- DoH/DoT governance
- Endpoint DNS telemetry

---

# Unauthorized DNS Resolver Hunting

A useful enterprise hunt:

```text
Endpoint
   │
   ├──► Corporate Resolver ✓
   │
   └──► External Resolver ✗
```

Direct use of external resolvers may be legitimate in some environments but should be understood and governed.

---

# DNS and Zero Trust

DNS should not automatically imply trust.

A resolved internal hostname should still require:

```text
Identity
+
Authorization
+
Network Policy
+
Application Policy
```

DNS provides naming and resolution, not authorization.

---

# DNS and Cloud

Cloud environments introduce additional DNS considerations:

- Private DNS zones
- Service discovery
- Cloud-native resolvers
- Container DNS
- Kubernetes DNS
- Metadata-related hostnames
- SaaS endpoints

DNS hunting should therefore extend into cloud environments.

---

# Kubernetes DNS Hunting

Kubernetes commonly uses cluster DNS.

A simplified model:

```text
Pod
 │
 ▼
Cluster DNS
 │
 ├── Service
 ├── Internal Name
 └── External Domain
```

Potential anomalies include:

- Pods querying unusual external domains
- Excessive DNS queries
- Compromised containers contacting C2
- Unexpected external resolvers

---

# Container DNS Hunting

Correlate:

```text
Pod
+
Namespace
+
Service Account
+
Container
+
DNS Query
+
Network Connection
```

This provides significantly better context than source IP alone.

---

# DNS and Malware Analysis

During malware analysis, DNS can reveal:

```text
C2 Domains
Fallback Infrastructure
Update Servers
Download Servers
Tracking Infrastructure
```

A malware sample may attempt:

```text
Domain A
 ↓
Domain B
 ↓
Domain C
 ↓
IP Fallback
```

This creates an infrastructure graph.

---

# DNS and Incident Response

During incident response, DNS can answer:

```text
When did the compromised host first contact infrastructure?
Which other hosts contacted it?
Which users were involved?
Was the domain queried before compromise?
What IPs did it resolve to?
```

This helps establish the incident scope.

---

# Enterprise DNS Hunting Checklist

## Collection

- [ ] DNS query logs enabled
- [ ] Source IP captured
- [ ] Hostname available
- [ ] Query type captured
- [ ] Response code captured
- [ ] Answers captured
- [ ] Timestamp synchronized

## Detection

- [ ] Rare domains
- [ ] First-seen domains
- [ ] NXDOMAIN
- [ ] DGA
- [ ] High entropy
- [ ] Long labels
- [ ] DNS tunneling
- [ ] Beaconing
- [ ] TXT anomalies
- [ ] Unauthorized resolvers

## Correlation

- [ ] Endpoint
- [ ] User
- [ ] Process
- [ ] Network
- [ ] Proxy
- [ ] Threat intelligence
- [ ] Identity

## Response

- [ ] Identify affected hosts
- [ ] Identify users
- [ ] Scope domain activity
- [ ] Block malicious infrastructure
- [ ] Investigate endpoint
- [ ] Remove persistence
- [ ] Reset credentials where necessary
- [ ] Document findings

---

# Common DNS Hunting Mistakes

## 1. Treating Rare Domains as Malicious

Rare domains are investigation candidates, not automatic threats.

---

## 2. Using Entropy Alone

High entropy can be completely legitimate.

---

## 3. Ignoring DNS Caching

Not every connection results in a DNS query.

---

## 4. Ignoring Encrypted DNS

DoH and DoT can reduce traditional DNS visibility.

---

## 5. Ignoring Internal DNS

Internal DNS can reveal reconnaissance and lateral movement.

---

## 6. Ignoring Role-Based Behavior

A server's DNS profile differs from a workstation's.

---

## 7. Failing to Correlate DNS With Endpoint Data

DNS becomes substantially more valuable when tied to the responsible process.

---

# Professional DNS Investigation Template

```text
Incident ID:

Date/Time:

Host:
IP:
User:

DNS Query:
Query Type:
Response Code:
Answer:

Resolver:

Domain Age:

Domain Reputation:

IP Reputation:

ASN:

First Seen:
Last Seen:

Query Count:

NXDOMAIN Count:

Unique Subdomains:

Entropy:

Associated Process:

Parent Process:

Command Line:

Network Connections:

Related Hosts:

Related Users:

Threat Intelligence:

MITRE ATT&CK:

Timeline:

Assessment:

Containment:

Remediation:

Detection Improvement:

Lessons Learned:
```

---

# MITRE ATT&CK Mapping

Relevant techniques include:

| Technique | Description |
|---|---|
| T1071.004 | DNS |
| T1046 | Network Service Scanning |
| T1071.001 | Web Protocols |
| T1105 | Ingress Tool Transfer |
| T1095 | Non-Application Layer Protocol |
| T1572 | Protocol Tunneling |
| T1041 | Exfiltration Over C2 Channel |
| T1568 | Dynamic Resolution |
| T1568.001 | Fast Flux DNS |
| T1568.002 | Domain Generation Algorithms |
| T1568.003 | DNS/Domain Trust Discovery |

ATT&CK technique and sub-technique mappings should be validated against the current ATT&CK knowledge base before being used in production detection documentation.

---

# Interview Questions

## 1. Why is DNS useful for threat hunting?

Because DNS provides visibility into domain resolution, infrastructure relationships, C2 activity, DGA behavior, tunneling, phishing infrastructure, and unusual network behavior.

---

## 2. What is DNS tunneling?

DNS tunneling is the use of DNS queries or responses to transport information through a DNS-based communication channel.

---

## 3. What is a DGA?

A Domain Generation Algorithm generates domains algorithmically, often allowing malware to locate command-and-control infrastructure dynamically.

---

## 4. What is NXDOMAIN?

NXDOMAIN indicates that the requested DNS name does not exist.

High NXDOMAIN activity can be a hunting signal when combined with other suspicious behavior.

---

## 5. How would you hunt for DNS tunneling?

I would combine:

```text
Long Labels
+
High Entropy
+
High Query Volume
+
Many Unique Subdomains
+
Rare Domain
+
Regular Communication
```

and then correlate the behavior with endpoint and network telemetry.

---

## 6. Is high DNS entropy malicious?

No.

Cloud services, CDNs, authentication systems, and legitimate applications can produce high-entropy hostnames.

---

## 7. How would you identify DNS beaconing?

I would group DNS events by host and destination, calculate query intervals, analyze periodicity and jitter, then correlate the destination and originating process.

---

## 8. What is DNS over HTTPS?

DoH transports DNS queries through HTTPS, providing encryption between the client and resolver.

---

## 9. How does encrypted DNS affect hunting?

It can reduce visibility into DNS query content at traditional DNS monitoring points, requiring additional endpoint, TLS, network, and resolver telemetry.

---

## 10. What is a DNS sinkhole?

A DNS sinkhole redirects known malicious domains toward controlled infrastructure so organizations can block or monitor compromised systems attempting to communicate with them.

---

## 11. How would you investigate a suspicious DNS domain?

I would examine:

```text
Domain
Age
Reputation
Historical DNS
IP
ASN
Certificate
Hosts
Users
Processes
Query Frequency
Network Connections
```

---

## 12. What is passive DNS?

Passive DNS is historical DNS observation data that can show relationships between domains and IP addresses over time.

---

## 13. Why is first-seen analysis useful?

A domain that appears for the first time on a single endpoint can provide a useful investigation lead, especially when combined with suspicious endpoint behavior.

---

## 14. Can DNS identify malware?

DNS alone generally cannot prove malware infection. It provides behavioral evidence that should be correlated with endpoint, network, identity, and threat-intelligence data.

---

## 15. How would you detect unauthorized DNS resolvers?

Identify endpoints communicating directly with DNS infrastructure outside the organization's approved resolver architecture and correlate those connections with process and user context.

---

# Key Takeaways

1. **DNS is a foundational threat-hunting data source.**
2. **Rare domains are useful investigation leads.**
3. **First-seen domains deserve contextual analysis.**
4. **NXDOMAIN patterns can reveal DGA and other anomalies.**
5. **High entropy alone is not proof of malicious activity.**
6. **DNS tunneling can be identified through multiple behavioral signals.**
7. **Beaconing can reveal automated C2 communication.**
8. **Encrypted DNS changes visibility but does not eliminate all hunting opportunities.**
9. **Internal DNS can reveal reconnaissance and service discovery.**
10. **DNS should be correlated with endpoint processes and network connections.**
11. **Passive DNS enables infrastructure pivoting.**
12. **Sinkhole telemetry can identify potentially compromised endpoints.**
13. **Role-based DNS baselines reduce false positives.**
14. **Cloud and Kubernetes DNS must be included in modern hunting programs.**
15. **Successful DNS hunts should become repeatable detections.**

The core mindset is:

> **Don't ask only "Is this domain malicious?" Ask "Why did this host query this domain, how often, what process initiated the activity, what did the domain resolve to, and what happened immediately afterward?"**

---

# References

- MITRE ATT&CK — Enterprise  
  https://attack.mitre.org/

- MITRE ATT&CK — DNS  
  https://attack.mitre.org/techniques/T1071/004/

- RFC 1034 — Domain Names  
  https://www.rfc-editor.org/rfc/rfc1034

- RFC 1035 — Domain Names  
  https://www.rfc-editor.org/rfc/rfc1035

- RFC 8484 — DNS Queries over HTTPS  
  https://www.rfc-editor.org/rfc/rfc8484

- RFC 7858 — DNS over TLS  
  https://www.rfc-editor.org/rfc/rfc7858

- Zeek Documentation  
  https://docs.zeek.org/

- ISC BIND Documentation  
  https://bind9.readthedocs.io/

- Unbound Documentation  
  https://nlnetlabs.nl/projects/unbound/about/

- CISA Cybersecurity Resources  
  https://www.cisa.gov/topics/cybersecurity

- NIST Cybersecurity Framework  
  https://www.nist.gov/cyberframework
