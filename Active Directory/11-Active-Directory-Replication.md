# 11-Active-Directory-Replication.md

# Part 1 — Introduction to Active Directory Replication, Architecture, Components, and Enterprise Fundamentals

---

# Learning Objectives

After completing this part, you will be able to:

- Understand what Active Directory replication is.
- Learn why replication is required.
- Understand multi-master replication.
- Learn replication terminology.
- Understand replication architecture.
- Differentiate replication from synchronization.
- Prepare for advanced replication concepts.

---

# Introduction

Active Directory is designed to be:

- Highly Available
- Fault Tolerant
- Scalable
- Distributed

Unlike traditional directory services that rely on a single server, Active Directory allows multiple Domain Controllers (DCs) to maintain copies of the directory database.

To ensure every Domain Controller has consistent information, Microsoft uses **Active Directory Replication**.

---

# What is Active Directory Replication?

**Active Directory Replication** is the process of copying directory changes between Domain Controllers to ensure that all writable Domain Controllers eventually contain consistent directory information.

Example:

```text
Administrator

↓

Creates User

↓

DC01

↓

Replication

↓

DC02

↓

DC03

↓

DC04
```

Eventually, every writable Domain Controller knows about the new user.

---

# Why is Replication Necessary?

Imagine an organization with offices in:

- Bangalore
- Mumbai
- Delhi
- Hyderabad

Each office has its own Domain Controller.

A user account is created in Bangalore.

Without replication:

```text
Bangalore DC

↓

User Exists
```

```text
Mumbai DC

↓

User Not Found
```

Users would experience inconsistent authentication and directory information.

Replication solves this problem.

---

# Replication Goal

The objective is:

```text
One Change

↓

Replicated

↓

Entire Directory

↓

Consistent Environment
```

Replication provides **eventual consistency** across Domain Controllers.

---

# Multi-Master Replication

Every writable Domain Controller can normally:

- Create users
- Delete users
- Reset passwords
- Create groups
- Modify attributes
- Join computers

Example:

```text
Admin A

↓

DC01

↓

Create User
```

Simultaneously:

```text
Admin B

↓

DC02

↓

Reset Password
```

Both changes are replicated.

This architecture is known as **multi-master replication**.

---

# Replication vs Synchronization

Although often used interchangeably, they are different concepts.

| Replication | Synchronization |
|-------------|-----------------|
| Copies directory changes | General data consistency process |
| Specific to Active Directory | Used in many technologies |
| Event-driven | Can be scheduled or manual |
| Maintains AD database | May involve files, databases, cloud services, etc. |

Active Directory replication is a specialized synchronization mechanism.

---

# What Gets Replicated?

Examples include:

- User accounts
- Computer accounts
- Groups
- Organizational Units
- Group Policies
- Password changes
- Security descriptors
- DNS-integrated zones
- Trust information
- Schema changes

Not every change is replicated in the same manner or with the same urgency.

---

# Replication Scope

Depending on the object:

```text
Domain Data

↓

Within Domain
```

```text
Forest Data

↓

Across Forest
```

For example:

- Schema changes replicate forest-wide.
- User account changes replicate within the domain.

---

# Replication Components

Core components include:

- Domain Controllers
- Active Directory Database (NTDS.DIT)
- Update Sequence Numbers (USNs)
- Invocation IDs
- High-Watermark Vectors
- Up-to-Dateness Vectors
- Replication Topology
- Knowledge Consistency Checker (KCC)

These work together to provide efficient and reliable replication.

---

# Replication Architecture

```text
Administrator

↓

Domain Controller

↓

Directory Database

↓

Replication Engine

↓

Partner Domain Controllers

↓

Consistent Directory
```

---

# Example

Suppose:

```text
User

↓

Changes Password

↓

DC01
```

Replication distributes the change:

```text
DC01

↓

DC02

↓

DC03

↓

DC04
```

Soon, users can authenticate using the new password from any Domain Controller after replication completes.

---

# Why Not Copy Everything Every Time?

Imagine:

- 200,000 users
- Millions of objects
- Hundreds of Domain Controllers

Copying the entire database after every change would:

- Consume excessive bandwidth
- Increase replication time
- Reduce scalability

Instead, Active Directory replicates **only the changes**.

---

# Change-Based Replication

Workflow:

```text
Attribute Modified

↓

Replication Engine

↓

Changed Attributes

↓

Replication Partner
```

Only modified attributes are transferred whenever possible.

---

# Benefits of Change-Based Replication

Advantages include:

- Reduced bandwidth
- Faster replication
- Better scalability
- Lower CPU utilization
- Efficient WAN usage

---

# Replication Partners

Each Domain Controller communicates with selected partner Domain Controllers.

Example:

```text
DC01

↔

DC02

↔

DC03

↔

DC04
```

Not every Domain Controller directly replicates with every other Domain Controller.

The replication topology determines these relationships.

---

# Replication Terminology

| Term | Description |
|------|-------------|
| Source DC | Sends updates |
| Destination DC | Receives updates |
| Replication Partner | Domain Controller participating in replication |
| Change Notification | Signals new updates |
| Convergence | State where all DCs have received changes |
| Multi-Master | Multiple writable DCs can accept updates |

---

# Replication Convergence

Convergence means:

```text
DC01

↓

Updated
```

↓

```text
DC02

↓

Updated
```

↓

```text
DC03

↓

Updated
```

↓

```text
DC04

↓

Updated
```

Every Domain Controller eventually reaches the same directory state.

---

# Replication is Not Instant

Many administrators expect immediate updates.

Reality:

```text
Change Made

↓

Replication Scheduled

↓

Replication Occurs

↓

Other DC Updated
```

Replication timing depends on:

- Site topology
- Change notification
- Replication schedules
- Network latency
- WAN links

---

# Enterprise Example

Company:

- 150,000 users
- 70 Domain Controllers
- 12 Active Directory sites

Administrator in Bangalore:

```text
Creates User

↓

Local DC
```

The user information is replicated across all appropriate Domain Controllers according to the configured replication topology and schedules.

---

# Replication and High Availability

Suppose:

```text
DC01

↓

Offline
```

Users can still authenticate through:

```text
DC02

↓

Same Directory Data
```

Replication provides redundancy by ensuring multiple Domain Controllers hold current directory information.

---

# Cybersecurity Perspective

Replication is security-critical because it distributes:

- User accounts
- Privileged group memberships
- Password changes
- Trust relationships
- Security policies

Security teams should:

- Monitor replication failures.
- Audit unexpected replication activity.
- Protect privileged Domain Controllers.
- Review directory service logs.
- Secure replication traffic.

Compromised replication can spread unauthorized directory changes throughout the environment.

---

# Common Mistakes

Avoid:

- Assuming replication is instantaneous.
- Thinking every DC communicates directly with every other DC.
- Ignoring replication health.
- Confusing replication with backup.
- Believing every directory change replicates forest-wide.

---

# Hands-on Lab

## Objective

Observe Active Directory replication.

### Tasks

1. Create a test user on one Domain Controller.
2. Wait for replication or force replication in a lab.
3. Verify the user appears on another Domain Controller.
4. Record:
   - Time of creation
   - Time replication completed
   - Replication partners involved

---

# Interview Questions

1. What is Active Directory replication?
2. Why is replication necessary?
3. What is multi-master replication?
4. What is replication convergence?
5. Why doesn't Active Directory replicate the entire database after every change?
6. What is a replication partner?
7. Is replication instantaneous?
8. Which types of data are replicated?
9. What is the difference between replication and synchronization?
10. How does replication improve availability?

---

# Key Takeaways

- Active Directory replication keeps writable Domain Controllers synchronized by distributing directory changes.
- Replication is change-based, transferring only updated information rather than the entire database.
- Multi-master replication allows multiple Domain Controllers to accept routine updates simultaneously.
- Replication convergence ensures that all Domain Controllers eventually contain consistent directory information.
- Healthy replication is essential for authentication, authorization, and overall Active Directory reliability.

---

# 11-Active-Directory-Replication.md

# Part 2 — Replication Components, Update Sequence Numbers (USN), Invocation ID, KCC, Connection Objects, and Replication Topology

---

# Learning Objectives

After completing this part, you will be able to:

- Understand how Active Directory tracks changes.
- Learn Update Sequence Numbers (USNs).
- Understand Invocation IDs.
- Learn High-Watermark Vectors.
- Understand Up-to-Dateness (UTD) Vectors.
- Learn the role of the Knowledge Consistency Checker (KCC).
- Understand replication topology and connection objects.

---

# How Active Directory Tracks Changes

Replication is **change-based**.

Instead of comparing the entire database every time, Active Directory tracks every modification using metadata.

Example:

```text
User Modified

↓

Metadata Updated

↓

Replication Triggered

↓

Only Changes Replicated
```

This makes replication fast and scalable.

---

# Replication Metadata

Each directory object contains metadata describing:

- Attribute modified
- Time of modification
- Originating Domain Controller
- Version number
- Update Sequence Number (USN)

Example:

```text
User Object

↓

Display Name

↓

Version 5

↓

USN 18254
```

This information helps Domain Controllers determine what has changed.

---

# Update Sequence Number (USN)

A **USN** is a locally incrementing number maintained by every writable Domain Controller.

Every change increases the local USN.

Example:

```text
DC01

USN

1000

↓

Create User

↓

1001

↓

Reset Password

↓

1002

↓

Modify Group

↓

1003
```

---

# Important Characteristics of USNs

USNs are:

- Local to each Domain Controller
- Always increasing
- Never reused on the same database instance
- Used to identify changes

USNs are **not** synchronized between Domain Controllers.

---

# Example

```text
DC01

Current USN

5000
```

```text
DC02

Current USN

9200
```

Both values are correct because USNs are maintained independently.

---

# Why Local USNs?

Imagine:

```text
DC01

↓

Creates User
```

```text
DC02

↓

Creates Computer
```

Each Domain Controller assigns its own USN.

Replication later exchanges the changes without requiring globally synchronized counters.

---

# Invocation ID

Each Domain Controller database has a unique **Invocation ID**.

Purpose:

- Identifies a specific database instance.
- Prevents replication confusion after restores.
- Helps replication partners recognize database changes.

---

# Invocation ID Example

```text
DC01

↓

Invocation ID

A1B2-C3D4
```

```text
DC02

↓

Invocation ID

E5F6-G7H8
```

Every Domain Controller has its own unique identifier.

---

# Why Invocation IDs Matter

Suppose:

```text
DC01

↓

System State Restore
```

The restored database may represent an earlier point in time.

To avoid replaying outdated replication information incorrectly:

```text
Restore

↓

New Invocation ID

↓

Partners Detect Change

↓

Replication Continues Safely
```

---

# Replication Metadata Summary

Every replicated update contains information such as:

```text
Attribute

↓

Version

↓

USN

↓

Originating DC

↓

Timestamp

↓

Invocation ID
```

This allows Domain Controllers to determine which updates should be applied.

---

# High-Watermark Vector

A **High-Watermark Vector** records the highest USN successfully received from a replication partner.

Example:

```text
DC01

↓

Sent

USN 1050
```

```text
DC02

↓

High-Watermark

1050
```

Next replication starts **after** USN 1050, avoiding duplicate transfers.

---

# High-Watermark Workflow

```text
DC01

↓

USN 1050 Sent

↓

DC02

↓

Records 1050

↓

Future Replication

↓

Starts with 1051
```

This reduces unnecessary replication.

---

# Up-to-Dateness (UTD) Vector

The **Up-to-Dateness Vector** helps prevent redundant replication when updates have already been received through another replication path.

Example:

```text
DC01

↓

Update

↓

DC02

↓

DC03
```

If DC03 already received the update from DC02, it does not request the same update again directly from DC01.

---

# Why UTD Vectors Matter

Without UTD vectors:

```text
DC01

↓

Same Update

↓

DC02

↓

DC03

↓

Repeated Again
```

This wastes bandwidth.

With UTD vectors:

```text
Update Already Known

↓

Skip Duplicate Replication
```

---

# Knowledge Consistency Checker (KCC)

The **Knowledge Consistency Checker (KCC)** is an Active Directory component that automatically builds and maintains the replication topology.

Administrators normally do **not** create replication paths manually.

---

# Responsibilities of the KCC

The KCC:

- Builds replication topology.
- Creates connection objects.
- Removes obsolete connections.
- Adapts to topology changes.
- Optimizes replication paths.

---

# KCC Workflow

```text
Domain Controllers

↓

KCC

↓

Analyze Topology

↓

Create Connections

↓

Replication Begins
```

---

# Connection Objects

A **Connection Object** defines how one Domain Controller replicates from another.

Example:

```text
DC01

↓

Connection Object

↓

DC02
```

This represents an inbound replication relationship.

---

# Example Topology

```text
DC01

↔

DC02

↔

DC03

↔

DC04
```

The KCC automatically creates and maintains these connections.

---

# Automatic Topology Management

When a new Domain Controller joins:

```text
New DC

↓

KCC Detects

↓

Creates Connections

↓

Replication Starts
```

Administrators typically do not need to configure replication manually.

---

# Replication Ring Concept

Within a site, the KCC commonly builds a logical topology that provides redundancy while avoiding unnecessary connections.

Illustrative example:

```text
DC01

↔

DC02

↔

DC03

↔

DC04

↺
```

This ensures there are multiple paths for replication if one connection becomes unavailable.

---

# Why Not Full Mesh?

Suppose there are:

20 Domain Controllers.

Full mesh:

```text
Every DC

↓

Connected

↓

Every Other DC
```

This would create an excessive number of replication connections.

Instead, the KCC creates an optimized topology that balances redundancy with efficiency.

---

# Topology Benefits

Automatic topology provides:

- Reduced bandwidth consumption
- Scalability
- Fault tolerance
- Automatic adaptation
- Simplified administration

---

# Enterprise Example

Organization:

- 40 Domain Controllers
- 6 Sites

When a new Domain Controller is deployed:

```text
Install DC

↓

KCC Runs

↓

Creates Replication Partners

↓

Replication Begins
```

No manual topology creation is required under normal circumstances.

---

# Cybersecurity Perspective

Replication metadata is essential for directory integrity.

Security teams should:

- Monitor unexpected replication partners.
- Audit unauthorized Domain Controllers.
- Investigate abnormal replication behavior.
- Protect Domain Controllers from unauthorized restores.
- Review replication-related event logs.

Compromised replication metadata can lead to inconsistent or unauthorized directory changes.

---

# Common Mistakes

Avoid:

- Assuming USNs are globally unique.
- Confusing USNs with SIDs.
- Manually creating unnecessary connection objects.
- Ignoring replication metadata.
- Disabling or interfering with KCC-generated topology without a valid design reason.

---

# Hands-on Lab

## Objective

Explore replication topology.

### Tasks

1. Open **Active Directory Sites and Services**.
2. Navigate to:
   - Sites
   - Servers
   - NTDS Settings
3. Examine:
   - Connection Objects
   - Replication Partners
4. Run:

```powershell
repadmin /showrepl
```

5. Identify:
   - Replication source
   - Replication destination
   - Successful replication times

---

# Interview Questions

1. What is a USN?
2. Are USNs unique across the entire forest?
3. What is an Invocation ID?
4. Why is the Invocation ID important after restoring a Domain Controller?
5. What does a High-Watermark Vector track?
6. What is the purpose of the Up-to-Dateness Vector?
7. What is the Knowledge Consistency Checker (KCC)?
8. What are Connection Objects?
9. Why doesn't Active Directory use a full-mesh replication topology?
10. How does the KCC simplify replication management?

---

# Key Takeaways

- Active Directory uses replication metadata such as USNs, version numbers, timestamps, and Invocation IDs to track changes.
- USNs are local to each Domain Controller and are not globally synchronized.
- High-Watermark and Up-to-Dateness vectors prevent unnecessary or duplicate replication.
- The Knowledge Consistency Checker (KCC) automatically builds and maintains an efficient replication topology.
- Connection Objects define replication relationships between Domain Controllers, allowing scalable and resilient directory replication.

---

# 11-Active-Directory-Replication.md

# Part 3 — Intra-Site Replication, Inter-Site Replication, Site Links, Bridgehead Servers, Conflict Resolution, and Replication Scheduling

---

# Learning Objectives

After completing this part, you will be able to:

- Understand Intra-Site Replication.
- Learn Inter-Site Replication.
- Understand Active Directory Sites.
- Learn Site Links and Site Link Bridges.
- Understand Bridgehead Servers.
- Learn replication scheduling.
- Understand replication conflict resolution.

---

# Understanding Active Directory Sites

An **Active Directory Site** represents one or more well-connected IP subnets.

Sites are created to optimize:

- Replication
- Authentication
- Network bandwidth
- Service location

Example:

```text
Company Network

│

├── Bangalore Office

├── Mumbai Office

├── Delhi Office

└── Hyderabad Office
```

Each office can be configured as an individual Active Directory Site.

---

# Why Sites Exist

Without sites:

```text
Client

↓

Random Domain Controller

↓

High WAN Usage
```

With sites:

```text
Client

↓

Nearest Site

↓

Nearest Domain Controller

↓

Fast Authentication
```

Sites improve efficiency by keeping authentication and replication as local as possible.

---

# Intra-Site Replication

**Intra-Site Replication** occurs **within the same Active Directory Site**.

Example:

```text
Bangalore Site

│

├── DC01

├── DC02

└── DC03
```

Replication occurs between these Domain Controllers inside the same site.

---

# Characteristics of Intra-Site Replication

Intra-site replication assumes:

- High-speed LAN
- Reliable network
- Low latency
- Minimal bandwidth concerns

Therefore replication is optimized for speed.

---

# Intra-Site Replication Flow

```text
Administrator

↓

Modify User

↓

DC01

↓

Change Notification

↓

DC02

↓

DC03
```

Changes are propagated quickly throughout the site.

---

# Change Notification

Inside a site:

```text
Change Made

↓

Notify Partner

↓

Replication Starts
```

Instead of waiting for long schedules, Domain Controllers notify their partners when updates occur.

---

# Typical Intra-Site Timing

Illustrative process:

```text
Object Changed

↓

Partner Notified

↓

Replication Begins

↓

Other DC Updated
```

Windows uses configurable notification intervals and offsets to efficiently distribute changes while avoiding excessive traffic.

---

# Benefits of Intra-Site Replication

Advantages:

- Fast updates
- Low authentication delay
- Efficient synchronization
- Better user experience
- High availability

---

# Inter-Site Replication

**Inter-Site Replication** occurs **between different Active Directory Sites**.

Example:

```text
Bangalore Site

↓

WAN

↓

Mumbai Site
```

---

# Why Inter-Site Replication is Different

WAN links may have:

- Higher latency
- Lower bandwidth
- Greater cost
- Variable reliability

Therefore replication is optimized to conserve bandwidth.

---

# Inter-Site Replication Flow

```text
DC01

↓

Bangalore Site

↓

WAN

↓

Mumbai Site

↓

DC05
```

Replication is controlled by schedules and topology rather than immediate notifications.

---

# Comparing Intra-Site and Inter-Site Replication

| Feature | Intra-Site | Inter-Site |
|----------|------------|------------|
| Network | LAN | WAN |
| Speed | Faster | Typically slower |
| Optimization | Low latency | Bandwidth conservation |
| Notification | Change notifications | Schedule-based (by default) |
| Compression | Generally not used | Compression enabled by default |

---

# Replication Compression

For WAN efficiency:

```text
Directory Changes

↓

Compress

↓

Transmit

↓

Decompress

↓

Apply Changes
```

Compression significantly reduces network utilization during inter-site replication.

---

# Active Directory Site Links

A **Site Link** defines the logical connection between two or more Active Directory Sites.

Example:

```text
Bangalore

↓

Site Link

↓

Mumbai
```

---

# Why Site Links Matter

Without Site Links:

```text
Sites

↓

No Replication Path
```

With Site Links:

```text
Site A

↓

Site Link

↓

Site B

↓

Replication
```

Site Links define the routes used for inter-site replication.

---

# Site Link Components

Each Site Link includes:

- Member sites
- Cost
- Schedule
- Replication interval
- Transport protocol (typically IP)

---

# Site Link Cost

Each Site Link has a **cost**.

Example:

```text
Bangalore ↔ Mumbai

Cost = 50
```

```text
Bangalore ↔ Delhi

Cost = 100
```

The Knowledge Consistency Checker (KCC) generally prefers lower-cost routes.

---

# Example Topology

```text
             Delhi

               │

          Cost 100

               │

Bangalore ─────┼────── Mumbai

     Cost 50
```

Replication normally follows the least-cost available path.

---

# Site Link Schedule

Administrators can control **when** inter-site replication occurs.

Example:

```text
Business Hours

↓

Limited Replication
```

```text
Night

↓

Frequent Replication
```

Schedules help optimize WAN usage.

---

# Replication Interval

Administrators can configure how frequently Site Links replicate.

Example:

```text
Every Configured Interval

↓

Replication Begins
```

The appropriate interval depends on:

- Business requirements
- WAN capacity
- Recovery objectives
- Directory change frequency

---

# Site Link Bridges

Sometimes multiple Site Links must be treated as connected paths.

Example:

```text
Site A

↓

Site B

↓

Site C
```

If bridging is enabled:

```text
A

↓

B

↓

C
```

Active Directory can calculate indirect replication routes across multiple Site Links.

---

# Bridgehead Servers

Inter-site replication is handled by **Bridgehead Servers**.

Instead of every Domain Controller replicating across the WAN:

```text
Site A

↓

Bridgehead Server

↓

WAN

↓

Bridgehead Server

↓

Site B
```

This reduces WAN traffic and simplifies replication management.

---

# Automatic Bridgehead Selection

Normally:

```text
KCC

↓

Selects Bridgehead

↓

Replication Begins
```

Administrators can manually specify preferred bridgehead servers when necessary, though automatic selection is recommended in most environments.

---

# Bridgehead Responsibilities

Bridgehead Servers:

- Receive inter-site updates.
- Send inter-site updates.
- Reduce WAN connections.
- Optimize cross-site replication.

---

# Replication Conflict Resolution

Sometimes two administrators modify the same object before replication completes.

Example:

```text
DC01

↓

Phone Number

↓

1111111111
```

Simultaneously:

```text
DC02

↓

Phone Number

↓

2222222222
```

How does Active Directory decide which value wins?

---

# Conflict Resolution Rules

Active Directory uses replication metadata such as:

- Version number
- Timestamp
- Originating Domain Controller
- Attribute metadata

The directory applies deterministic rules to resolve conflicts and maintain consistency.

---

# Simplified Example

```text
DC01

↓

Attribute Version

5
```

```text
DC02

↓

Attribute Version

6
```

Version 6 is considered the newer change and is replicated.

If version numbers are equal, additional metadata (such as timestamps and originating information) is evaluated.

---

# Tombstones

When an object is deleted:

```text
Delete User

↓

Object Marked

↓

Tombstone

↓

Replication

↓

Permanent Cleanup
```

Deletion information is replicated before the object is permanently removed.

This prevents deleted objects from being recreated by outdated replicas.

---

# Enterprise Example

Company:

- 12 Active Directory Sites
- 60 Domain Controllers
- Dedicated WAN links

Configuration:

```text
Each Site

↓

Local Replication

↓

Bridgehead

↓

WAN

↓

Remote Bridgehead

↓

Local Replication
```

Benefits:

- Efficient WAN utilization
- Faster local authentication
- Controlled replication traffic
- High availability

---

# Cybersecurity Perspective

Replication traffic carries critical directory information.

Recommendations:

- Secure WAN links.
- Monitor unexpected replication paths.
- Review Site Link configurations.
- Audit replication failures.
- Protect Bridgehead Servers.
- Monitor unusual object modifications across sites.

Compromised replication between sites can spread unauthorized directory changes throughout the forest.

---

# Common Mistakes

Avoid:

- Configuring unrealistic Site Link costs.
- Ignoring WAN bandwidth limitations.
- Disabling replication schedules without understanding the impact.
- Creating unnecessary manual replication connections.
- Assuming inter-site replication is immediate.

---

# Hands-on Lab

## Objective

Explore Active Directory Sites and replication topology.

### Tasks

1. Open **Active Directory Sites and Services**.
2. Examine:
   - Sites
   - Subnets
   - Site Links
3. Identify:
   - Bridgehead Servers
   - Replication connections
4. Record:
   - Site Link costs
   - Replication intervals
   - Connected sites
5. Draw the inter-site replication topology for your lab.

---

# Interview Questions

1. What is an Active Directory Site?
2. What is the difference between Intra-Site and Inter-Site replication?
3. Why is inter-site replication typically compressed?
4. What is a Site Link?
5. What does Site Link cost represent?
6. What is a Bridgehead Server?
7. How are Bridgehead Servers selected?
8. What metadata is used during replication conflict resolution?
9. What is a tombstone object?
10. Why are replication schedules important in WAN environments?

---

# Key Takeaways

- Intra-site replication is optimized for fast, reliable LAN environments using change notifications.
- Inter-site replication is optimized for WAN environments using schedules, compression, and Site Links.
- The KCC uses Site Link costs to calculate efficient replication paths.
- Bridgehead Servers manage replication traffic between Active Directory Sites.
- Active Directory resolves replication conflicts using replication metadata and replicates deletions through tombstone objects before permanent removal.

---

**Next:** Part 4