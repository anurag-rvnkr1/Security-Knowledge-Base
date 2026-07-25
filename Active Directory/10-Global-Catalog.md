# 10-Global-Catalog.md

# Part 1 — Introduction to the Global Catalog, Architecture, Partial Attribute Set, Forest Searches, and Enterprise Fundamentals

---

# Learning Objectives

After completing this part, you will be able to:

- Understand what the Global Catalog (GC) is.
- Learn why the Global Catalog exists.
- Understand Partial Attribute Sets (PAS).
- Learn how the Global Catalog supports forest-wide searches.
- Understand Global Catalog architecture.
- Learn enterprise deployment strategies.
- Prepare for advanced Global Catalog concepts.

---

# Introduction

An Active Directory forest can contain:

- Multiple Domains
- Thousands of Organizational Units
- Millions of Objects
- Hundreds of Domain Controllers

Finding information across such a large environment would be inefficient if every query had to contact every Domain Controller individually.

Microsoft solves this problem using the **Global Catalog (GC).**

---

# What is the Global Catalog?

The **Global Catalog (GC)** is a specialized Domain Controller that stores:

- A complete writable copy of all objects in its own domain.
- A **partial, read-only copy** of objects from every other domain in the forest.

This allows users and applications to quickly locate directory objects without contacting every Domain Controller.

---

# Visual Overview

```text
Forest

│

├── Domain A

├── Domain B

├── Domain C

└── Domain D

↓

Global Catalog

↓

Partial Information

↓

Entire Forest Search
```

---

# Why Does the Global Catalog Exist?

Imagine a company with:

- India Domain
- Europe Domain
- USA Domain
- Japan Domain

An administrator wants to locate:

```text
Alice Johnson
```

Without a Global Catalog:

```text
Search Domain A

↓

Not Found

↓

Search Domain B

↓

Not Found

↓

Search Domain C

↓

Found
```

Every domain would need to be queried individually.

---

# With a Global Catalog

```text
Administrator

↓

Global Catalog

↓

Forest Search

↓

Alice Johnson Found
```

Only one query is required.

---

# Real-World Analogy

Imagine a university.

Each department has:

- Student records
- Faculty records
- Research records

Without a central directory:

You must visit every department individually.

With a university directory:

One search locates the correct department immediately.

The Global Catalog functions like this centralized directory.

---

# Full Copy vs Partial Copy

Normal Domain Controller:

```text
Own Domain

↓

100% Information
```

Global Catalog:

```text
Own Domain

↓

100% Information

+

Other Domains

↓

Partial Information
```

---

# Why Not Store Everything?

Suppose a forest contains:

- 20 domains
- 5 million users
- Millions of groups
- Millions of computers

If every Global Catalog stored every attribute of every object:

- Storage requirements would increase dramatically.
- Replication traffic would become excessive.
- Synchronization would take longer.

Instead, Microsoft stores only frequently searched attributes from other domains.

---

# Partial Attribute Set (PAS)

The **Partial Attribute Set (PAS)** is the collection of attributes replicated to every Global Catalog for objects outside its own domain.

Examples include:

- Display Name
- User Logon Name
- Email Address
- Object GUID
- SID
- Distinguished Name
- Object Class

Not every attribute is included.

---

# PAS Example

User object:

```text
John Smith

↓

Display Name

↓

Email

↓

Department

↓

Phone

↓

Manager

↓

Employee ID

↓

Office
```

The Global Catalog stores only selected attributes needed for efficient searching and logon operations.

---

# Benefits of the Partial Attribute Set

Benefits include:

- Faster replication
- Reduced storage
- Lower bandwidth usage
- Faster searches
- Better scalability

---

# Global Catalog Architecture

```text
Forest

│

├── Domain A

├── Domain B

├── Domain C

└── Domain D

↓

Global Catalog Server

↓

Partial Attribute Set

↓

Search Results
```

---

# Global Catalog Servers

Not every Domain Controller must be a Global Catalog.

Example:

```text
Domain Controllers

│

├── DC01 (GC)

├── DC02

├── DC03 (GC)

└── DC04
```

Only Domain Controllers configured as Global Catalog servers maintain the Partial Attribute Set.

---

# Identifying a Global Catalog

A Domain Controller can perform two roles:

```text
Domain Controller

↓

Authentication

↓

Directory Services
```

Global Catalog Server:

```text
Domain Controller

↓

Authentication

↓

Directory Services

↓

Forest Search

↓

Universal Group Support
```

A GC is a Domain Controller with additional responsibilities.

---

# Information Stored in a Global Catalog

For its own domain:

```text
Full Object

↓

All Attributes
```

For other domains:

```text
Object

↓

Selected Attributes

↓

Partial Copy
```

---

# Enterprise Example

Company:

```text
company.com

│

├── india.company.com

├── europe.company.com

├── usa.company.com

└── japan.company.com
```

Employee:

```text
Sarah Patel
```

Works in:

```text
india.company.com
```

An administrator in Europe searches for Sarah.

Instead of querying India directly:

```text
Europe GC

↓

Search PAS

↓

Find Sarah

↓

Return Result
```

---

# Read-Only Nature of Remote Domain Data

The partial copies stored for other domains are **read-only**.

Administrators cannot modify another domain's objects through the Global Catalog.

Changes must be made on writable Domain Controllers in the object's own domain.

---

# Global Catalog Replication

Whenever important attributes change:

```text
Domain Controller

↓

Replication

↓

Global Catalog

↓

Updated PAS
```

Only attributes included in the Partial Attribute Set are replicated forest-wide.

---

# Advantages of the Global Catalog

The Global Catalog provides:

- Forest-wide searches
- Faster object discovery
- Efficient directory lookups
- Universal group support
- Reduced query traffic
- Improved user experience
- Better scalability

---

# Common Use Cases

Applications commonly use the Global Catalog for:

- User searches
- Exchange address lookups
- Enterprise applications
- Identity management
- Authentication support
- Administrative tools

---

# Cybersecurity Perspective

Security teams use Global Catalog servers to:

- Search directory objects
- Investigate user accounts
- Locate privileged groups
- Audit object information
- Support incident response

Since GCs contain information about every domain, they should be protected as critical infrastructure.

---

# Common Mistakes

Avoid:

- Assuming every Domain Controller is automatically a Global Catalog.
- Assuming the GC stores every attribute from every domain.
- Modifying objects through a read-only Global Catalog copy.
- Ignoring Global Catalog placement in large forests.
- Confusing Global Catalog replication with normal domain replication.

---

# Hands-on Lab

## Objective

Identify Global Catalog servers in a lab environment.

### Tasks

1. Open **Active Directory Sites and Services**.
2. Expand:
   - Sites
   - Servers
   - NTDS Settings
3. Identify which Domain Controllers are configured as Global Catalog servers.
4. Record:
   - Server names
   - Site location
   - Domains served
5. Compare GC servers with non-GC Domain Controllers.

---

# Interview Questions

1. What is the Global Catalog?
2. Why was the Global Catalog introduced?
3. What information does a Global Catalog store?
4. What is the Partial Attribute Set?
5. Why doesn't the Global Catalog store every attribute from every domain?
6. Is every Domain Controller automatically a Global Catalog?
7. Can you modify another domain's objects through the Global Catalog?
8. What are the benefits of the Partial Attribute Set?
9. Which enterprise services commonly use the Global Catalog?
10. Why is the Global Catalog important in multi-domain forests?

---

# Key Takeaways

- The Global Catalog is a specialized Domain Controller that enables forest-wide searches.
- It stores a full writable copy of its own domain and a partial read-only copy of objects from every other domain.
- The Partial Attribute Set (PAS) contains only commonly required attributes, reducing replication traffic and storage requirements.
- Global Catalog servers improve scalability, object discovery, and enterprise directory searches.
- Proper Global Catalog deployment is essential for efficient Active Directory operations in multi-domain forests.

---

# 10-Global-Catalog.md

# Part 2 — Global Catalog in Authentication, Universal Groups, UPN Resolution, Replication, and Enterprise Operations

---

# Learning Objectives

After completing this part, you will be able to:

- Understand the role of the Global Catalog during user logon.
- Learn how Universal Groups depend on the Global Catalog.
- Understand User Principal Name (UPN) resolution.
- Learn Global Catalog replication.
- Understand Global Catalog ports and communication.
- Learn enterprise deployment considerations.

---

# Global Catalog and User Authentication

One of the most important responsibilities of the Global Catalog is assisting during **user authentication**, especially in multi-domain forests.

A normal authentication process involves:

```text
User

↓

Domain Controller

↓

Kerberos Authentication

↓

Access Granted
```

However, additional steps are required when Universal Groups or forest-wide identities are involved.

---

# Authentication in a Multi-Domain Forest

Consider the following forest:

```text
Forest

│

├── india.company.com

├── europe.company.com

└── usa.company.com
```

A user belongs to:

```text
india.company.com
```

But logs on from:

```text
europe.company.com
```

The authenticating Domain Controller may need Global Catalog information to build the user's complete authorization token.

---

# Authentication Workflow

```text
User

↓

Nearest Domain Controller

↓

Password Verification

↓

Global Catalog

↓

Universal Group Membership

↓

Kerberos Ticket

↓

User Logged In
```

---

# Why is the Global Catalog Needed?

The authenticating Domain Controller knows its own domain very well.

However, it may not know:

- Universal Group memberships
- Objects in other domains
- Forest-wide identity information

The Global Catalog supplies this information quickly.

---

# Universal Groups

Active Directory supports several group scopes:

- Domain Local
- Global
- Universal

The Global Catalog is especially important for **Universal Groups**.

---

# Universal Group Overview

Example:

```text
Forest

│

├── India Domain

├── Europe Domain

└── USA Domain

↓

Universal Group

↓

CyberSecurity-Team
```

Members may come from multiple domains.

---

# Example

Employees:

```text
India

↓

Rahul
```

```text
Europe

↓

Emma
```

```text
USA

↓

David
```

All belong to:

```text
Universal Group

↓

Security-Operations
```

The Global Catalog maintains the information required to resolve this membership efficiently.

---

# Why Universal Groups Need the GC

Without a Global Catalog:

```text
Authentication

↓

Query Domain A

↓

Query Domain B

↓

Query Domain C

↓

Build Access Token
```

With a Global Catalog:

```text
Authentication

↓

Global Catalog

↓

Universal Group Membership

↓

Access Token Ready
```

---

# Universal Group Membership Caching

Some branch offices may not have a local Global Catalog.

To improve logon performance, Windows supports **Universal Group Membership Caching (UGMC).**

Workflow:

```text
First Logon

↓

Contact Global Catalog

↓

Cache Membership

↓

Future Logons

↓

Use Cached Information
```

This reduces WAN traffic while allowing users to authenticate even if a Global Catalog is temporarily unreachable.

---

# User Principal Name (UPN)

Users often log on using a **User Principal Name (UPN).**

Example:

```text
john.smith@company.com
```

Instead of:

```text
COMPANY\johnsmith
```

---

# UPN Resolution

When a user enters:

```text
alice@company.com
```

The Domain Controller may consult the Global Catalog to determine where the account exists within the forest.

Workflow:

```text
User

↓

Enter UPN

↓

Global Catalog

↓

Locate Account

↓

Authenticate
```

---

# Forest-Wide Searches

Suppose an administrator searches for:

```text
Sophia Williams
```

The search request:

```text
Administrator

↓

Global Catalog

↓

Forest Search

↓

Matching Objects
```

The administrator does not need to know the user's domain beforehand.

---

# Exchange Server Example

Microsoft Exchange heavily relies on the Global Catalog.

Example:

```text
User

↓

Search Address Book

↓

Global Catalog

↓

Return User Details
```

This allows fast organization-wide address lookups.

---

# Identity Management Example

Identity management systems often query the Global Catalog to:

- Locate users
- Verify identities
- Search groups
- Retrieve email addresses
- Discover organizational information

Because the GC spans the forest, one query can replace many domain-specific queries.

---

# Global Catalog Replication

The Global Catalog receives updates through Active Directory replication.

Example:

```text
User Updated

↓

Domain Controller

↓

Replication

↓

Global Catalog

↓

PAS Updated
```

Only attributes included in the Partial Attribute Set are replicated to Global Catalog servers in other domains.

---

# Replication Scope

For its own domain:

```text
All Attributes

↓

Replicated Normally
```

For other domains:

```text
Partial Attribute Set

↓

Replicated Forest-Wide
```

This design reduces replication traffic.

---

# Global Catalog Ports

Common LDAP ports:

| Service | Port |
|----------|-----:|
| LDAP | 389 |
| LDAP over SSL (LDAPS) | 636 |
| Global Catalog (LDAP) | 3268 |
| Global Catalog over SSL | 3269 |

Applications that require forest-wide searches commonly use ports **3268** or **3269**.

---

# LDAP vs Global Catalog

Normal LDAP query:

```text
Client

↓

LDAP (389)

↓

Single Domain
```

Global Catalog query:

```text
Client

↓

GC (3268)

↓

Entire Forest
```

---

# Enterprise Deployment

Large organizations often deploy multiple Global Catalog servers.

Example:

```text
Head Office

↓

GC01
```

```text
Regional Office

↓

GC02
```

```text
Branch Office

↓

GC03
```

Benefits include:

- Faster searches
- Reduced WAN traffic
- Better availability
- Improved authentication performance

---

# Branch Office Example

Without a nearby GC:

```text
User

↓

WAN

↓

Remote GC

↓

Authentication Delay
```

With a local GC:

```text
User

↓

Local GC

↓

Immediate Response
```

---

# High Availability

Enterprises generally deploy more than one Global Catalog.

Example:

```text
GC01

↓

Primary
```

If unavailable:

```text
GC02

↓

Handles Requests
```

This improves resilience during maintenance or outages.

---

# Global Catalog Placement Guidelines

Recommended practices:

- Place at least one GC in each major Active Directory site.
- Ensure reliable replication between sites.
- Consider WAN bandwidth.
- Evaluate authentication volume.
- Monitor replication latency.

---

# Cybersecurity Perspective

Because the Global Catalog contains searchable information from every domain:

Security teams should:

- Restrict administrative access.
- Secure LDAP with LDAPS where appropriate.
- Monitor LDAP query activity.
- Audit directory searches.
- Protect Global Catalog servers with the same rigor as other critical Domain Controllers.

---

# Common Mistakes

Avoid:

- Assuming a Global Catalog stores every attribute.
- Deploying only one GC in a large forest.
- Ignoring WAN latency when placing GCs.
- Blocking required GC ports with firewalls.
- Confusing LDAP queries with Global Catalog queries.

---

# Hands-on Lab

## Objective

Verify Global Catalog connectivity.

### Tasks

1. Identify a Global Catalog server.
2. Verify that it listens on:
   - TCP 3268
   - TCP 3269 (if LDAPS is configured)
3. Search for users located in another domain using Active Directory Users and Computers or an LDAP query tool.
4. Observe that the search succeeds without manually specifying the target domain.

---

# Interview Questions

1. Why is the Global Catalog important during authentication?
2. What are Universal Groups?
3. Why do Universal Groups depend on the Global Catalog?
4. What is Universal Group Membership Caching?
5. What is a User Principal Name (UPN)?
6. Which ports are used by the Global Catalog?
7. What is the difference between LDAP port 389 and GC port 3268?
8. Why does Microsoft use a Partial Attribute Set?
9. Why do Exchange and identity management systems rely on the Global Catalog?
10. How should Global Catalog servers be distributed in a large enterprise?

---

# Key Takeaways

- The Global Catalog plays a vital role in authentication by providing Universal Group membership information.
- UPN logons and forest-wide searches rely on the Global Catalog for efficient object location.
- Universal Group Membership Caching helps branch offices authenticate users even without a local GC.
- Global Catalog servers use ports **3268** (LDAP) and **3269** (LDAPS).
- Proper placement and redundancy of Global Catalog servers improve authentication performance, scalability, and availability.

---

**Next:** Part 3