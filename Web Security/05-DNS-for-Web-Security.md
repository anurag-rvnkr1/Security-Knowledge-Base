# DNS-For-Web-Security.md

# Part 1 — Introduction to DNS, Name Resolution, DNS Hierarchy, Records, and DNS Security Fundamentals

> **"The Internet communicates using IP addresses, but humans communicate using names. DNS is the critical infrastructure that securely translates those names into addresses, making the modern Web possible."**

---

# Learning Objectives

After completing this part, you will understand:

- What DNS is
- Why DNS exists
- Domain names
- IP addresses
- DNS hierarchy
- DNS resolution process
- DNS records
- Recursive and Authoritative DNS servers
- DNS caching
- Enterprise DNS architecture
- DNS security fundamentals

---

# Introduction

Imagine opening a browser and typing:

```
https://www.google.com
```

Your computer does **NOT** initially know Google's IP address.

Instead, it asks DNS:

```
"What is the IP address for www.google.com?"
```

DNS replies with the correct IP address.

Only then can your browser establish an HTTPS connection.

---

# Why DNS Exists

Computers communicate using IP addresses.

Example:

```
142.250.182.196
```

Humans prefer readable names.

Example:

```
www.google.com
```

DNS bridges this gap.

```
Human

↓

Domain Name

↓

DNS

↓

IP Address

↓

Server
```

---

# What is DNS?

**DNS (Domain Name System)** is the Internet's distributed naming system that translates domain names into IP addresses.

Think of DNS as:

```
Internet Phone Book
```

Instead of:

```
Person → Phone Number
```

DNS performs:

```
Website

↓

IP Address
```

---

# Why DNS is Important

Without DNS:

```
Users must remember:

142.250.182.196

104.18.33.45

151.101.1.69

...
```

Instead:

```
google.com

github.com

openai.com
```

DNS makes the Internet usable.

---

# Domain Names

A domain name uniquely identifies an Internet resource.

Examples:

```
google.com

microsoft.com

amazon.com

example.org
```

---

# Structure of a Domain Name

Example:

```
www.example.com
```

Breakdown:

```
www

↓

Subdomain

example

↓

Second-Level Domain

com

↓

Top-Level Domain (TLD)
```

---

# Fully Qualified Domain Name (FQDN)

Example:

```
mail.company.example.com
```

Hierarchy:

```
mail

↓

company

↓

example

↓

com

↓

Root
```

An FQDN specifies the complete location of a host in the DNS hierarchy.

---

# DNS Hierarchy

DNS follows a hierarchical structure.

```
                 Root (.)

                    │

      ┌─────────────┼─────────────┐

     .com          .org          .net

       │

   example

       │

      www
```

This design enables global scalability.

---

# Root Domain

At the top of DNS is the **Root Zone**.

Represented as:

```
.
```

Every DNS lookup ultimately begins from the root.

---

# Top-Level Domains (TLDs)

Examples:

```
.com

.org

.net

.edu

.gov

.io

.dev

.ai
```

Country Code TLDs:

```
.in

.uk

.jp

.au

.de
```

---

# Second-Level Domain

Example:

```
example.com
```

Here:

```
example
```

is the registered domain.

---

# Subdomains

Organizations create subdomains to organize services.

Examples:

```
www.example.com

mail.example.com

vpn.example.com

api.example.com

blog.example.com
```

Each may point to different infrastructure.

---

# DNS Resolution Overview

When a browser requests:

```
www.example.com
```

DNS performs:

```
Browser

↓

DNS Resolver

↓

Root Server

↓

TLD Server

↓

Authoritative Server

↓

IP Address

↓

Browser Connects
```

---

# Recursive DNS Resolver

A recursive resolver performs DNS lookups on behalf of the client.

```
Browser

↓

Recursive Resolver

↓

Internet DNS Infrastructure
```

Responsibilities:

- Perform lookups
- Cache responses
- Return answers to clients

Examples:

- ISP DNS
- Corporate DNS
- Public DNS providers

---

# Authoritative DNS Server

An authoritative server stores official DNS information for a domain.

```
example.com

↓

Authoritative DNS

↓

Official DNS Records
```

It provides the definitive answer for that domain.

---

# Recursive vs Authoritative

| Recursive Resolver | Authoritative Server |
|---------------------|----------------------|
| Queries other servers | Stores official records |
| Caches responses | Maintains zone data |
| Serves clients | Serves DNS information |
| Performs recursion | Answers authoritatively |

---

# DNS Query Flow

```
Browser

↓

Recursive Resolver

↓

Root Server

↓

.com Server

↓

Authoritative Server

↓

IP Address Returned

↓

Browser
```

---

# DNS Resolution Example

User enters:

```
https://portal.company.com
```

Process:

```
1. Browser checks local cache

↓

2. OS cache

↓

3. Recursive resolver

↓

4. Root server

↓

5. .com TLD

↓

6. company.com authoritative server

↓

7. Returns IP

↓

8. Browser connects using HTTPS
```

---

# DNS Records

DNS stores different record types.

Common records include:

- A
- AAAA
- CNAME
- MX
- NS
- TXT
- SOA
- PTR

Each serves a different purpose.

---

# A Record

Maps:

```
Domain

↓

IPv4 Address
```

Example:

```
example.com

↓

192.0.2.10
```

---

# AAAA Record

Maps:

```
Domain

↓

IPv6 Address
```

Example:

```
example.com

↓

2001:db8::10
```

---

# CNAME Record

Creates an alias.

Example:

```
www.example.com

↓

example.com
```

Useful when multiple hostnames should resolve to the same service.

---

# MX Record

Specifies mail servers.

Example:

```
example.com

↓

mail.example.com
```

Mail servers use MX records to deliver email.

---

# NS Record

Defines authoritative name servers.

```
example.com

↓

ns1.example.com

↓

ns2.example.com
```

These servers answer DNS queries for the domain.

---

# TXT Record

Stores arbitrary text.

Common uses:

- SPF
- DKIM
- Domain verification
- Security policies

Example:

```
v=spf1 include:_spf.example.com -all
```

---

# SOA Record

Start of Authority (SOA) record contains administrative information about the DNS zone.

Typical information:

- Primary name server
- Zone serial number
- Refresh interval
- Retry interval
- Expiration time

---

# PTR Record

Used for reverse DNS.

Instead of:

```
Domain

↓

IP
```

PTR performs:

```
IP

↓

Domain
```

Useful for:

- Email validation
- Logging
- Network troubleshooting

---

# DNS Cache

To improve performance, DNS responses are cached.

```
First Lookup

↓

DNS Query

↓

Cache

↓

Future Requests

↓

Immediate Response
```

Caching reduces lookup time and DNS traffic.

---

# Time To Live (TTL)

Each DNS record includes a TTL value.

```
DNS Record

↓

TTL

↓

Cache Duration
```

After TTL expires:

```
Fresh Lookup Required
```

---

# Enterprise DNS Architecture

```
User

↓

Browser

↓

Corporate DNS Resolver

↓

Firewall

↓

Internet

↓

Root

↓

TLD

↓

Authoritative DNS

↓

Application Server
```

Enterprise DNS often includes redundancy, monitoring, and filtering.

---

# DNS and Web Security

Every web connection begins with DNS.

```
User

↓

DNS

↓

Correct Server?

↓

HTTPS

↓

Application
```

If DNS is compromised, users may be directed to malicious infrastructure.

Therefore DNS is a critical component of Web Security.

---

# Real Enterprise Example

Employee opens:

```
https://vpn.company.com
```

Resolution process:

```
Laptop

↓

Corporate DNS Resolver

↓

Authoritative DNS

↓

VPN Gateway IP

↓

TLS Connection

↓

Secure Login
```

Without accurate DNS resolution, secure communication cannot begin.

---

# Hands-on Lab (Conceptual)

Using a command prompt or terminal:

1. Run:

```
nslookup google.com
```

2. Observe:

- DNS server used
- Returned IP address
- Record type

3. Repeat with:

```
nslookup github.com

nslookup openai.com
```

Compare the responses.

---

# Interview Questions

1. What is DNS?
2. Why is DNS necessary?
3. What is an FQDN?
4. What is the difference between a recursive resolver and an authoritative server?
5. What is the purpose of an A record?
6. What is a CNAME record?
7. What is an MX record?
8. What is DNS caching?
9. What is TTL?
10. Why is DNS important for Web Security?

---

# Best Practices

- Use redundant authoritative DNS servers.
- Monitor DNS infrastructure continuously.
- Configure appropriate TTL values.
- Protect DNS management interfaces.
- Validate DNS changes before deployment.
- Keep DNS software updated.

---

# Common Mistakes

- Assuming DNS provides encryption by default.
- Misconfiguring DNS records.
- Using excessively long or extremely short TTL values without justification.
- Forgetting reverse DNS where required.
- Ignoring DNS monitoring and logging.

---

# Key Takeaways

- DNS translates domain names into IP addresses.
- DNS follows a hierarchical architecture beginning at the root.
- Recursive resolvers perform lookups, while authoritative servers provide official answers.
- DNS records define how services are located on the Internet.
- Every secure web connection starts with a successful DNS lookup, making DNS a foundational component of Web Security.


```
# DNS-For-Web-Security.md

# Part 2 — DNS Resolution Process, Recursive Queries, Iterative Queries, DNS Records in Depth, Zone Files, Delegation, and Enterprise DNS Infrastructure

> **"Every website visit starts with a DNS lookup. Understanding exactly how a DNS query travels across the Internet is essential for web security professionals, penetration testers, SOC analysts, and network engineers."**

---

# Learning Objectives

After completing this part, you will understand:

- Complete DNS resolution process
- Recursive queries
- Iterative queries
- DNS delegation
- DNS zones
- Zone files
- Forward and Reverse Lookup
- Glue records
- DNS propagation
- Enterprise DNS infrastructure
- DNS troubleshooting

---

# Recap

In Part 1, we learned:

```
User

↓

Browser

↓

Recursive Resolver

↓

Root Server

↓

TLD Server

↓

Authoritative Server

↓

IP Address
```

Now let's examine what happens internally.

---

# Complete DNS Resolution Process

Suppose a user visits:

```
https://portal.company.com
```

DNS resolution follows multiple stages.

```
Browser

↓

Browser Cache

↓

Operating System Cache

↓

Recursive Resolver

↓

Root Server

↓

TLD Server

↓

Authoritative Server

↓

IP Address

↓

Browser Connects
```

---

# Step 1 — Browser Cache

Browsers maintain their own DNS cache.

```
Browser

↓

Cached?

↓

Yes

↓

Return IP
```

Benefits:

- Faster browsing
- Fewer DNS requests
- Reduced latency

---

# Step 2 — Operating System Cache

If the browser cache misses:

```
Browser

↓

Operating System DNS Cache
```

Windows, Linux, and macOS maintain local DNS caches.

---

# Step 3 — Recursive Resolver

If the OS has no cached entry:

```
Client

↓

Recursive DNS Resolver
```

The recursive resolver now performs the complete lookup.

---

# Recursive Query

A recursive query means:

```
Client

↓

Resolver

↓

"Find the Final Answer"
```

The resolver performs all necessary work and returns either:

- Final IP address
- Error

The client does **not** contact Root or TLD servers directly.

---

# Recursive Query Diagram

```
Client

↓

Recursive Resolver

↓

Root

↓

TLD

↓

Authoritative

↓

Answer

↓

Client
```

---

# Iterative Query

Recursive resolvers communicate with Internet DNS servers using iterative queries.

Instead of receiving the final answer immediately:

```
Resolver

↓

Root Server

↓

Referral

↓

TLD Server

↓

Referral

↓

Authoritative Server

↓

Final Answer
```

Each server points the resolver closer to the destination.

---

# Recursive vs Iterative Queries

| Recursive Query | Iterative Query |
|-----------------|-----------------|
| Client expects final answer | Server returns best available information |
| Performed by recursive resolver | Performed between DNS servers |
| Simpler for clients | Reduces workload on root servers |

---

# Root DNS Server

The recursive resolver first contacts a Root Server.

Question:

```
Where is company.com?
```

Response:

```
Ask the .com TLD server.
```

The Root Server does **not** know the final IP.

---

# Top-Level Domain (TLD) Server

Next:

```
Resolver

↓

.com Server
```

Question:

```
Where is company.com?
```

Response:

```
Ask the authoritative server.
```

Again, only a referral is returned.

---

# Authoritative Server

Finally:

```
Resolver

↓

Authoritative DNS
```

Question:

```
portal.company.com?
```

Response:

```
203.0.113.45
```

This is the official answer.

---

# Entire Resolution Flow

```
User

↓

Browser

↓

Recursive Resolver

↓

Root Server

↓

.com Server

↓

company.com Authoritative Server

↓

203.0.113.45

↓

Browser Opens HTTPS Connection
```

---

# DNS Zones

DNS information is organized into **Zones**.

Example:

```
company.com
```

Everything under this domain belongs to its DNS zone unless delegated elsewhere.

---

# Zone Hierarchy

```
company.com

│

├── www

├── api

├── vpn

├── mail

└── blog
```

Each host typically has corresponding DNS records.

---

# Zone File

A zone file contains DNS records for a domain.

Example:

```
example.com

↓

A Record

↓

MX Record

↓

TXT Record

↓

NS Record
```

The authoritative server loads these records to answer queries.

---

# Typical Zone File Contents

```
SOA

↓

NS

↓

A

↓

AAAA

↓

MX

↓

TXT

↓

CNAME
```

---

# Start of Authority (SOA)

Every DNS zone begins with an SOA record.

Contains:

- Zone owner
- Primary DNS server
- Serial number
- Refresh interval
- Retry interval
- Expiration
- Default TTL

The serial number changes whenever the zone is updated.

---

# Delegation

Large organizations often divide DNS responsibilities.

Example:

```
company.com

↓

research.company.com

↓

Different DNS Server
```

This is called **delegation**.

---

# Delegation Diagram

```
company.com

│

├── hr.company.com

├── vpn.company.com

└── research.company.com

        │

        └── Separate Authoritative DNS
```

Delegation improves scalability and administrative separation.

---

# Glue Records

Sometimes the nameserver for a domain is inside the same domain.

Example:

```
example.com

↓

ns1.example.com
```

To avoid circular dependency, parent zones provide **Glue Records**.

```
Parent Zone

↓

Glue Record

↓

Resolver Can Reach DNS Server
```

---

# Forward Lookup

The most common DNS query.

```
Domain

↓

IP Address
```

Example:

```
vpn.company.com

↓

203.0.113.15
```

---

# Reverse Lookup

Reverse lookup performs:

```
IP Address

↓

Domain Name
```

Uses:

- Email validation
- Network diagnostics
- Logging
- Security investigations

---

# Reverse DNS Zone

Instead of:

```
company.com
```

Reverse DNS uses special domains.

Example:

```
in-addr.arpa
```

for IPv4.

```
IP

↓

PTR Record

↓

Hostname
```

---

# DNS Propagation

When DNS records change:

```
Administrator Updates Record

↓

Authoritative DNS

↓

Resolvers Refresh Cache

↓

Internet Receives New Information
```

This process is commonly called **DNS propagation**.

---

# Why DNS Changes Take Time

DNS caching delays updates.

```
Old Record Cached

↓

TTL Not Expired

↓

Old Answer Returned
```

Only after TTL expiration do resolvers fetch updated records.

---

# TTL Example

```
TTL = 3600 Seconds
```

Meaning:

```
Cache

↓

1 Hour

↓

Refresh
```

Lower TTL:

- Faster updates
- Increased DNS traffic

Higher TTL:

- Better performance
- Slower propagation

---

# DNS Load Balancing

Multiple A or AAAA records can distribute traffic.

```
api.company.com

↓

203.0.113.10

203.0.113.11

203.0.113.12
```

Resolvers may receive different addresses depending on configuration.

---

# GeoDNS

Large organizations may return different IP addresses based on client location.

```
India

↓

Mumbai Server

────────────

Europe

↓

Frankfurt Server

────────────

USA

↓

Virginia Server
```

Benefits:

- Lower latency
- Improved availability
- Better user experience

---

# Enterprise DNS Infrastructure

```
Users

↓

Local DNS Cache

↓

Corporate Recursive Resolver

↓

Firewall

↓

Internet

↓

Root Servers

↓

TLD Servers

↓

Authoritative DNS Cluster

↓

Load Balancer

↓

Web Servers
```

Large enterprises often deploy redundant recursive resolvers and geographically distributed authoritative DNS servers.

---

# High Availability DNS

Mission-critical services require redundancy.

```
Primary DNS

↓

Secondary DNS

↓

Multiple Geographic Locations

↓

24×7 Availability
```

No single DNS server should become a single point of failure.

---

# DNS Failure Scenario

```
Authoritative DNS Offline

↓

Resolution Fails

↓

Users Cannot Reach Website
```

Even if web servers remain operational, users cannot access them without successful name resolution.

---

# Enterprise Example

A multinational company hosts:

```
portal.company.com

api.company.com

mail.company.com

vpn.company.com
```

DNS infrastructure:

```
Global Users

↓

Nearest Recursive Resolver

↓

Authoritative DNS Cluster

↓

Load Balancer

↓

Regional Data Center

↓

Application Servers
```

The infrastructure supports millions of DNS queries every day.

---

# Hands-on Lab (Conceptual)

Use the following commands:

```
nslookup github.com
```

```
nslookup -type=MX gmail.com
```

```
nslookup -type=TXT google.com
```

Observe:

- Returned records
- Authoritative server (if shown)
- TTL (tool dependent)
- Different record types

---

# Interview Questions

1. What is the difference between recursive and iterative queries?
2. Why do Root DNS servers return referrals?
3. What is a DNS zone?
4. What is contained in a zone file?
5. What is the purpose of an SOA record?
6. What is DNS delegation?
7. What are Glue Records?
8. What is DNS propagation?
9. How does TTL affect DNS performance?
10. Why is redundant DNS infrastructure important?

---

# Best Practices

- Deploy redundant authoritative DNS servers.
- Use appropriate TTL values based on operational requirements.
- Monitor zone changes and serial numbers.
- Separate administrative responsibilities using delegation where appropriate.
- Regularly validate DNS configurations.
- Document all DNS infrastructure.

---

# Common Mistakes

- Setting excessively long TTL values before planned migrations.
- Forgetting to increment the SOA serial number after manual zone updates.
- Misconfiguring NS or Glue Records.
- Assuming DNS changes propagate instantly.
- Operating with only one authoritative DNS server.

---

# Key Takeaways

- DNS resolution involves browser caches, operating system caches, recursive resolvers, Root servers, TLD servers, and authoritative servers.
- Recursive resolvers perform full lookups on behalf of clients using iterative queries.
- DNS zones organize records for domains, and zone files store authoritative data.
- TTL controls how long DNS information is cached, directly affecting performance and propagation.
- Enterprise DNS infrastructure relies on redundancy, delegation, and monitoring to ensure high availability.


```
# DNS-For-Web-Security.md

# Part 3 — DNS Security, DNS Attacks, DNSSEC, Secure DNS Protocols, Enterprise Defense, and Threat Detection

> **"DNS is one of the most targeted services on the Internet. Attackers often compromise DNS first because controlling name resolution allows them to redirect, monitor, or disrupt almost every other Internet service."**

---

# Learning Objectives

After completing this part, you will understand:

- DNS security fundamentals
- DNS threat landscape
- DNS spoofing
- DNS cache poisoning
- DNS hijacking
- DNS tunneling
- DNS amplification attacks
- DNSSEC
- DNS over HTTPS (DoH)
- DNS over TLS (DoT)
- Enterprise DNS monitoring
- Defensive best practices

---

# Why DNS Security Matters

Every web connection begins with DNS.

```
User

↓

DNS Lookup

↓

Correct IP?

↓

HTTPS Connection

↓

Application
```

If DNS is compromised:

```
User

↓

Fake DNS Response

↓

Attacker Server

↓

Credential Theft
```

Therefore, DNS is a primary target in cyber attacks.

---

# DNS Threat Landscape

Common DNS-based attacks include:

- DNS Spoofing
- DNS Cache Poisoning
- DNS Hijacking
- DNS Tunneling
- DNS Amplification
- DNS Reflection
- Domain Shadowing
- Fast Flux DNS
- Malicious DNS Servers

---

# DNS Spoofing

DNS Spoofing occurs when an attacker sends a forged DNS response.

Normal flow:

```
Client

↓

DNS Resolver

↓

Correct IP
```

Attack flow:

```
Client

↓

Fake DNS Response

↓

Malicious IP
```

The user unknowingly connects to the attacker's infrastructure.

---

# DNS Spoofing Example

User visits:

```
bank.example.com
```

Expected:

```
203.0.113.10
```

Attacker returns:

```
198.51.100.55
```

The browser connects to the wrong server.

---

# Impact of DNS Spoofing

Possible consequences:

- Credential theft
- Phishing
- Malware delivery
- Session hijacking
- Financial fraud

---

# DNS Cache Poisoning

Resolvers cache DNS responses.

Attackers attempt to insert malicious data into the cache.

```
Attacker

↓

Fake DNS Response

↓

Resolver Cache

↓

Future Users Receive Fake IP
```

One poisoned cache can affect many users.

---

# Cache Poisoning Flow

```
Resolver

↓

Poisoned Cache

↓

Client 1

↓

Malicious IP

──────────────

Client 2

↓

Malicious IP

──────────────

Client 3

↓

Malicious IP
```

---

# DNS Hijacking

Instead of poisoning a cache, attackers may compromise DNS settings.

Possible targets:

- Home router
- Enterprise DNS server
- Registrar account
- DNS hosting provider

```
Legitimate DNS

↓

Compromised Configuration

↓

Malicious Records

↓

Users Redirected
```

---

# Router DNS Hijacking

Attackers may modify home router DNS settings.

```
User

↓

Router

↓

Malicious DNS Server

↓

Fake Website
```

Users often remain unaware of the compromise.

---

# Registrar Hijacking

Attackers compromise a domain registrar account.

```
Registrar Account

↓

DNS Records Modified

↓

Entire Domain Redirected
```

Potential impact:

- Website takeover
- Email interception
- Brand damage

---

# DNS Tunneling

DNS was designed for name resolution.

Attackers abuse DNS queries to transfer arbitrary data.

```
Victim

↓

DNS Query

↓

Encoded Data

↓

Attacker DNS Server
```

---

# Why DNS Tunneling Works

Many organizations allow outbound DNS.

```
Firewall

↓

Allows DNS

↓

Hidden Data Transfer
```

Attackers exploit this trusted traffic.

---

# DNS Tunneling Example

```
secret-data.company.com

↓

ZXhhbXBsZS1kYXRh.attacker.com

↓

Attacker Extracts Data
```

Encoded information is hidden inside DNS labels.

---

# Indicators of DNS Tunneling

SOC analysts should investigate:

- Extremely long domain names
- High DNS query volume
- Random-looking subdomains
- Frequent TXT queries
- Queries to unusual domains

---

# DNS Amplification Attack

DNS primarily uses UDP.

Small requests can trigger much larger responses.

```
Small Query

↓

Large Response
```

Attackers exploit this amplification.

---

# Reflection Attack

The attacker spoofs the victim's IP.

```
Attacker

↓

Spoofed DNS Query

↓

Open Resolver

↓

Large Response

↓

Victim
```

The victim receives traffic it never requested.

---

# DNS Amplification Diagram

```
Attacker

↓

Spoofed Packet

↓

Open Resolver

↓

Large DNS Response

↓

Victim Server
```

This is commonly used in Distributed Denial-of-Service (DDoS) attacks.

---

# Open DNS Resolver

A resolver that answers requests from anyone on the Internet.

```
Internet

↓

Open Resolver

↓

DNS Response
```

Publicly exposed recursive resolvers can be abused if not properly configured.

---

# Fast Flux DNS

Attackers rapidly change DNS records.

```
malware.example

↓

IP A

↓

IP B

↓

IP C

↓

IP D
```

Benefits for attackers:

- Increased resilience
- Harder takedown
- Infrastructure rotation

---

# Domain Shadowing

An attacker compromises a legitimate DNS account.

Instead of modifying the main domain:

```
example.com

↓

abc.example.com

↓

xyz.example.com

↓

hidden.example.com
```

Many malicious subdomains are created without the owner's knowledge.

---

# DNSSEC

**DNS Security Extensions (DNSSEC)** add authenticity and integrity to DNS data.

DNSSEC **does not encrypt** DNS traffic.

Instead, it verifies that DNS records have not been altered.

---

# DNSSEC Goals

Provides:

- Data authenticity
- Data integrity
- Authenticated denial of existence

Does **NOT** provide:

- Confidentiality
- Encryption
- Privacy

---

# DNSSEC Chain of Trust

```
Root Zone

↓

TLD

↓

Domain

↓

DNS Record
```

Each level signs the next.

---

# DNSSEC Validation

```
DNS Response

↓

Digital Signature

↓

Resolver Verification

↓

Trusted Answer
```

If validation fails:

```
DNS Response Rejected
```

---

# DNSSEC Components

| Component | Purpose |
|-----------|----------|
| DNSKEY | Stores public keys |
| RRSIG | Digital signature for records |
| DS | Links parent and child zones |
| NSEC / NSEC3 | Authenticated denial of existence |

---

# DNS over HTTPS (DoH)

Traditional DNS:

```
DNS

↓

UDP/TCP Port 53
```

DoH:

```
DNS

↓

HTTPS

↓

Port 443
```

Benefits:

- Encryption
- Privacy
- Protection against passive monitoring

---

# DoH Architecture

```
Browser

↓

HTTPS

↓

DoH Resolver

↓

DNS Response
```

The DNS request is encapsulated within HTTPS.

---

# DNS over TLS (DoT)

Another secure DNS protocol.

```
Client

↓

TLS

↓

DNS Resolver
```

Unlike DoH:

- Dedicated DNS protocol
- Typically uses TCP Port 853

---

# DoH vs DoT

| DNS over HTTPS | DNS over TLS |
|---------------|--------------|
| Uses HTTPS | Uses TLS directly |
| Port 443 | Port 853 |
| Blends with web traffic | Dedicated secure DNS |
| Browser-friendly | Network infrastructure-friendly |

Both protect DNS queries in transit but differ in deployment models.

---

# Enterprise DNS Security Architecture

```
Users

↓

Endpoint Protection

↓

Secure Recursive Resolver

↓

DNS Filtering

↓

Firewall

↓

Threat Intelligence

↓

Authoritative DNS

↓

Applications
```

Multiple security layers reduce DNS-related risk.

---

# DNS Filtering

Enterprise DNS services can block known malicious domains.

```
Client

↓

DNS Query

↓

Threat Intelligence Check

↓

Allowed

OR

Blocked
```

Filtering helps stop phishing and malware communications before connections are established.

---

# Threat Intelligence Integration

```
DNS Query

↓

Threat Feed

↓

Known Malicious?

↓

Block

↓

Log Event
```

Security teams continuously update threat intelligence sources.

---

# DNS Logging

Organizations should record:

- Client IP
- Query timestamp
- Requested domain
- Response code
- Query type
- Resolver used

Logs support:

- Incident response
- Threat hunting
- Compliance
- Forensics

---

# SOC Detection Examples

Analysts monitor for:

```
Thousands of NXDOMAIN Responses

↓

Possible Malware

──────────────

Long Random Subdomains

↓

Possible DNS Tunneling

──────────────

Queries to Newly Registered Domains

↓

Potential Phishing

──────────────

Unusual Geographic DNS Traffic

↓

Potential Compromise
```

---

# Enterprise Example

A financial institution deploys:

```
Employees

↓

Secure DNS Resolver

↓

DNSSEC Validation

↓

Threat Intelligence

↓

DNS Logging

↓

Firewall

↓

Internet
```

Benefits:

- Malware blocking
- Phishing prevention
- Faster investigations
- DNS integrity verification

---

# Hands-on Lab (Conceptual)

Using terminal:

```
nslookup google.com
```

```
nslookup -type=TXT google.com
```

```
nslookup -type=NS google.com
```

Observe:

- Different record types
- Authoritative responses
- Query behavior

If available in your environment, inspect DNS traffic using a packet analyzer to identify:

- Query type
- Response type
- TTL
- Transaction ID

---

# Interview Questions

1. What is DNS Spoofing?
2. How does DNS Cache Poisoning work?
3. What is DNS Hijacking?
4. Explain DNS Tunneling.
5. Why are open DNS resolvers dangerous?
6. What is a DNS Amplification attack?
7. What security properties does DNSSEC provide?
8. What is the difference between DNSSEC and DoH?
9. Compare DNS over HTTPS and DNS over TLS.
10. How can SOC analysts detect DNS-based attacks?

---

# Best Practices

- Enable DNSSEC for supported domains.
- Use trusted recursive resolvers.
- Restrict recursive DNS services to authorized clients.
- Monitor DNS logs continuously.
- Block known malicious domains using threat intelligence.
- Secure registrar accounts with Multi-Factor Authentication (MFA).
- Regularly audit DNS records.
- Protect authoritative DNS servers from unauthorized changes.

---

# Common Mistakes

- Assuming DNSSEC encrypts DNS traffic.
- Exposing open recursive resolvers to the Internet.
- Ignoring DNS logs.
- Using default router DNS credentials.
- Failing to secure registrar accounts.
- Not monitoring for unusual DNS query patterns.

---

# Key Takeaways

- DNS is a high-value target because every web connection depends on successful name resolution.
- DNS Spoofing, Cache Poisoning, Hijacking, Tunneling, and Amplification are among the most common DNS attacks.
- DNSSEC provides authenticity and integrity but not encryption.
- DoH and DoT encrypt DNS queries in transit, improving privacy.
- Enterprise DNS security combines DNSSEC, secure resolvers, DNS filtering, threat intelligence, monitoring, and logging.

```text id="jid720"
**Next:** Part 4
```