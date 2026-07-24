# Active-Directory/

# 03-Domain-and-Forest.md

# Part 1 — Understanding Domains, Trees, Forests, Namespace, and Enterprise Design

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand what a Domain is.
- Explain the purpose of Domains in Active Directory.
- Understand Trees and Forests.
- Learn the difference between logical boundaries.
- Understand DNS namespaces in Active Directory.
- Design basic enterprise Active Directory structures.
- Prepare for advanced topics such as Trusts, Replication, and FSMO Roles.

---

# Introduction

Active Directory is designed to manage identities at enterprise scale.

To achieve this, it organizes resources into logical boundaries.

The most important are:

```text
Forest

↓

Tree

↓

Domain

↓

Organizational Unit (OU)

↓

Users

Groups

Computers
```

Understanding these boundaries is essential before administering large environments.

---

# What is a Domain?

A **Domain** is the primary administrative and security boundary in Active Directory.

A domain contains:

- Users
- Groups
- Computers
- Organizational Units
- Group Policies
- Domain Controllers

All objects within a domain share:

- A common directory database
- A common DNS namespace
- Common authentication infrastructure
- Shared security policies (where configured)

---

# Simple Analogy

Imagine a university.

```text
University

↓

Engineering Department

↓

Computer Science

↓

Students
```

Similarly,

```text
Forest

↓

Domain

↓

Organizational Unit

↓

Users
```

Domains organize enterprise resources into manageable administrative units.

---

# Basic Domain Structure

```text
company.com

│

├── Users

├── Groups

├── Computers

├── Servers

├── Domain Controllers

└── Organizational Units
```

---

# Characteristics of a Domain

Every domain has:

- Unique DNS name
- Domain Controllers
- Active Directory database
- Authentication services
- Group Policies
- Security identifiers
- Replication within the domain

---

# Domain Naming

Domains typically use DNS-style names.

Examples:

```text
company.com

corp.company.com

ad.company.com

contoso.local (legacy environments)

example.org
```

Modern best practice is to use names that align with an organization's registered DNS namespace rather than inventing non-routable namespaces without a clear business need.

---

# What Exists Inside a Domain?

```text
company.com

│

├── Finance OU

│     ├── Users

│     ├── Computers

│     └── Groups

│

├── HR OU

│

├── IT OU

│

└── Sales OU
```

Each Organizational Unit contains objects relevant to that department.

---

# Domain Controllers in a Domain

Every domain requires one or more Domain Controllers.

Example:

```text
company.com

│

├── DC01

├── DC02

└── DC03
```

All Domain Controllers:

- Authenticate users
- Store directory data
- Replicate changes
- Apply Group Policy
- Provide high availability

---

# Domain Boundaries

A domain defines several boundaries.

| Boundary | Purpose |
|-----------|---------|
| Administrative | Centralized administration within the domain |
| Replication | Domain partition replicates among DCs in the domain |
| Authentication | Users authenticate through the domain |
| Policy | Group Policies can be linked within the domain hierarchy |
| DNS Namespace | Unique DNS naming |

---

# Why Multiple Domains?

Not every organization requires multiple domains.

Organizations may deploy multiple domains to support:

- Business requirements
- Geographic separation
- Regulatory requirements
- Administrative autonomy
- Mergers and acquisitions
- Legacy application compatibility

Multiple domains increase administrative complexity and should be justified by clear business needs.

---

# Single Domain Example

Small organization:

```text
company.com

│

├── HR

├── Finance

├── Sales

├── IT

└── Support
```

Advantages:

- Simpler administration
- Easier Group Policy management
- Fewer Domain Controllers
- Lower operational cost

---

# Multi-Domain Example

Large enterprise:

```text
company.com

│

├── america.company.com

├── europe.company.com

├── asia.company.com

└── research.company.com
```

Benefits may include:

- Administrative separation
- Regional management
- Business-unit autonomy
- Delegated administration

---

# What is a Tree?

A **Tree** is a collection of one or more domains that share a contiguous DNS namespace.

Example:

```text
company.com

│

├── sales.company.com

├── hr.company.com

├── finance.company.com

└── it.company.com
```

All domains:

- Share a related namespace.
- Participate in the same forest.
- Have automatic transitive trust relationships (within the forest).

---

# Tree Characteristics

| Feature | Description |
|----------|-------------|
| Shared namespace | Yes |
| Common schema | Yes |
| Common configuration | Yes |
| Automatic trusts | Yes (within the forest) |
| Shared Global Catalog | Yes |

---

# Tree Example

```text
company.com

│

├── europe.company.com

│      ├── france.company.com

│      └── germany.company.com

│

└── america.company.com

       ├── usa.company.com

       └── canada.company.com
```

---

# What is a Forest?

A **Forest** is the highest logical boundary in Active Directory.

A forest contains:

- One or more trees
- One or more domains
- A shared schema
- Shared configuration data
- Shared Global Catalog infrastructure
- Trust relationships between domains

Think of the forest as the complete Active Directory environment.

---

# Forest Structure

```text
Forest

│

├── company.com

│      ├── hr.company.com

│      └── sales.company.com

│

└── fabrikam.com

       ├── europe.fabrikam.com

       └── asia.fabrikam.com
```

A forest can include multiple trees, including trees with different DNS namespaces.

---

# Forest Characteristics

| Feature | Description |
|----------|-------------|
| Highest logical boundary | Yes |
| Shared schema | Yes |
| Shared configuration partition | Yes |
| Shared Global Catalog | Yes |
| Automatic trust between domains | Yes (within the forest) |
| Security boundary | Considered the primary administrative security boundary |

---

# Domain vs Tree vs Forest

| Component | Purpose |
|-----------|---------|
| Domain | Administrative unit containing directory objects |
| Tree | Collection of related domains with a contiguous namespace |
| Forest | Highest logical structure containing one or more trees |

---

# Visual Comparison

```text
Forest

│

├── Tree 1

│      ├── Domain A

│      └── Domain B

│

└── Tree 2

       ├── Domain C

       └── Domain D
```

---

# DNS Namespace

Every Active Directory domain has a DNS namespace.

Example:

```text
company.com

↓

finance.company.com

↓

accounts.finance.company.com
```

DNS enables clients to locate services such as Domain Controllers and is fundamental to Active Directory operation.

---

# Enterprise Example

A global enterprise has:

- Headquarters in New York
- Offices in London
- Offices in Singapore

Possible structure:

```text
Forest

│

└── company.com

       ├── americas.company.com

       ├── europe.company.com

       └── asia.company.com
```

This design supports regional administration while maintaining a common forest.

---

# Cybersecurity Perspective

Domains and forests influence how privileges, authentication, and administration are organized.

Key considerations:

- The forest is the primary trust boundary.
- Compromise of highly privileged forest-level accounts can affect the entire forest.
- Administrative roles should be separated.
- Domain Controllers should be protected.
- Forest-wide changes require careful governance.

Understanding these boundaries is essential for both defenders and administrators.

---

# Hands-on Lab

## Objective

Design a simple Active Directory hierarchy.

### Scenario

Company:

- 500 employees
- Departments:
  - HR
  - Finance
  - IT
  - Sales

### Tasks

1. Create a single-domain design.
2. Create Organizational Units for each department.
3. Draw the hierarchy.
4. Explain why a single domain is sufficient for this scenario.

---

# Key Takeaways

- A domain is the primary administrative unit in Active Directory.
- A tree is a collection of domains sharing a contiguous DNS namespace.
- A forest is the highest logical boundary and contains one or more trees.
- DNS namespaces are fundamental to Active Directory.
- Multiple domains should be created only when justified by business or technical requirements.
- Forest design affects administration, scalability, and security.

---

# Interview Questions

1. What is an Active Directory domain?
2. What objects are stored within a domain?
3. What is the difference between a tree and a forest?
4. What is the highest logical boundary in Active Directory?
5. Why do organizations create multiple domains?
6. Why is DNS important for domains?
7. What do domains within the same tree share?
8. What resources are shared across a forest?
9. Is a forest considered a security boundary?
10. When is a single-domain design preferable?

---

# References

- Microsoft Learn – Active Directory Domains and Forests
- Microsoft Windows Server Documentation
- Microsoft Identity Documentation
- Windows Internals
- Microsoft Security Best Practices

---

# 03-Domain-and-Forest.md

# Part 2 — Domain Namespace, Trust Relationships, Functional Levels, Forest Design Models, and Enterprise Planning

---

# Learning Objectives

By the end of this part, you will be able to:

- Understand DNS namespaces in Active Directory.
- Explain contiguous and disjoint namespaces.
- Learn how trust relationships work at a high level.
- Understand Domain Functional Levels (DFL) and Forest Functional Levels (FFL).
- Compare common forest design models.
- Learn enterprise planning considerations before deploying multiple domains or forests.

---

# Active Directory Namespace

A **namespace** is the naming structure used to uniquely identify objects and domains.

Example:

```text
company.com

↓

sales.company.com

↓

user@sales.company.com
```

Namespaces make it possible for users, computers, and services to be uniquely identified throughout the enterprise.

---

# DNS Namespace Hierarchy

```text
company.com

│

├── hr.company.com

├── finance.company.com

├── sales.company.com

└── it.company.com
```

Each child domain extends the parent DNS namespace.

---

# Contiguous Namespace

A **contiguous namespace** means child domains inherit the parent's DNS naming hierarchy.

Example:

```text
company.com

│

├── europe.company.com

├── asia.company.com

└── america.company.com
```

Characteristics:

- Parent-child relationship
- Continuous DNS naming
- Common forest
- Automatic transitive trusts

---

# Disjoint Namespace

A forest can also contain multiple trees with different DNS namespaces.

Example:

```text
Forest

│

├── company.com

└── fabrikam.com
```

Although the namespaces differ, both trees belong to the same forest and share:

- Schema
- Configuration partition
- Global Catalog
- Forest-wide trust infrastructure

---

# UPN vs DNS Name

Users often log in with a **User Principal Name (UPN)**.

Example:

```text
Username:

alice@company.com
```

This resembles an email address but serves as a logon name.

The DNS domain name might be:

```text
company.com
```

While often identical, UPN suffixes can be customized to improve usability.

---

# Parent and Child Domains

Example:

```text
company.com

│

└── europe.company.com

       │

       └── germany.europe.company.com
```

Characteristics:

- Shared forest
- Shared schema
- Automatic trust
- Separate domain administration
- Separate domain partition

---

# Why Create Child Domains?

Historically, organizations created child domains for:

- Geographic administration
- Large organizational structures
- Different password or account policies (before fine-grained password policies became available)
- Administrative separation
- Legacy requirements

Today, many organizations instead use Organizational Units (OUs) and delegated administration unless separate domains are truly necessary.

---

# Trust Relationships (High-Level)

A **trust** allows authenticated users in one domain to access resources in another domain, subject to permissions.

```text
Domain A

     ⇄

Domain B
```

Trust **does not automatically grant permissions**.

It enables authentication to be recognized across boundaries.

---

# Automatic Trusts

Within a forest:

- Parent-child trusts are created automatically.
- Trusts are transitive by default.

Example:

```text
company.com

│

├── hr.company.com

└── sales.company.com
```

Users in one domain can be authenticated in another domain if appropriate permissions exist.

A dedicated chapter will cover trusts in depth.

---

# Authentication Across Domains

Simplified example:

```text
User

↓

HR Domain

↓

Trust Relationship

↓

Finance Domain

↓

Permission Check

↓

Access Granted or Denied
```

Authentication and authorization remain separate processes.

---

# Domain Functional Level (DFL)

The **Domain Functional Level** determines which Active Directory features are available within a domain.

It depends on the Windows Server versions supported by the Domain Controllers in that domain.

Higher functional levels can enable newer capabilities once all Domain Controllers meet the required version.

---

# Forest Functional Level (FFL)

The **Forest Functional Level** controls features available across the entire forest.

Characteristics:

- Applies forest-wide
- Depends on supported Domain Controller versions throughout the forest
- Enables advanced Active Directory functionality

DFL applies to one domain, while FFL applies to the entire forest.

---

# Functional Level Overview

```text
Forest

↓

Forest Functional Level

↓

Domain A

↓

Domain Functional Level

↓

Domain Controllers
```

Administrators should plan upgrades carefully before raising functional levels.

---

# Why Functional Levels Matter

Benefits include:

- Access to newer Active Directory features
- Improved security capabilities
- Better replication behavior
- Modern authentication enhancements
- Support for newer management capabilities

Raising functional levels should be performed only after validating compatibility with existing infrastructure and applications.

---

# Forest Design Models

Organizations generally choose one of several logical models.

---

## Model 1 — Single Forest, Single Domain

```text
Forest

│

└── company.com
```

Advantages:

- Simplest administration
- Lower operational cost
- Easier Group Policy management
- Fewer Domain Controllers

Suitable for many small and medium organizations.

---

## Model 2 — Single Forest, Multiple Domains

```text
Forest

│

├── company.com

├── europe.company.com

└── asia.company.com
```

Advantages:

- Regional administration
- Business-unit separation
- Shared forest infrastructure

Trade-offs:

- Greater administrative complexity
- Additional replication considerations
- More Domain Controllers

---

## Model 3 — Multiple Forests

```text
Forest A

│

└── company.com


Forest B

│

└── partner.com
```

Reasons organizations may deploy multiple forests include:

- Regulatory separation
- Organizational independence
- Mergers and acquisitions
- Security isolation requirements

Multiple forests significantly increase management complexity.

---

# Choosing the Right Design

| Organization | Typical Design |
|--------------|----------------|
| Small business | Single forest, single domain |
| Medium enterprise | Usually single forest, single domain or limited multi-domain |
| Large global enterprise | Single forest with multiple domains, or multiple forests when justified |

Business requirements—not organization size alone—should drive the design.

---

# Enterprise Planning Considerations

Before creating additional domains or forests, consider:

- Number of users
- Geographic locations
- Administrative model
- Regulatory requirements
- Disaster recovery
- Replication traffic
- DNS design
- Future growth
- Application compatibility
- Security requirements

Careful planning reduces long-term operational overhead.

---

# Naming Best Practices

Use:

```text
company.com
```

Rather than inconsistent names such as:

```text
company123.local

mydomain

serverdomain
```

Recommendations:

- Follow organizational naming standards.
- Keep names concise.
- Avoid unnecessary complexity.
- Document namespace decisions.
- Coordinate with DNS planning.

---

# Enterprise Example

A multinational company has:

- 30,000 employees
- Offices in 20 countries
- Central IT governance
- Regional administration

Possible design:

```text
Forest

│

└── company.com

       ├── americas.company.com

       ├── europe.company.com

       ├── asia.company.com

       └── africa.company.com
```

Each region has delegated administration while sharing a common forest.

---

# Cybersecurity Perspective

Domains and forests affect identity security across the enterprise.

Security recommendations:

- Minimize the number of forests unless required.
- Limit forest-wide administrative privileges.
- Review trust relationships regularly.
- Monitor privileged authentication across domains.
- Document domain boundaries and ownership.
- Apply least privilege consistently.

Poor forest design can increase administrative complexity and broaden the impact of privileged account compromise.

---

# Hands-on Lab

## Objective

Compare different Active Directory design models.

### Tasks

1. Draw:
   - Single forest, single domain
   - Single forest, multiple domains
   - Multiple forests
2. Identify advantages and disadvantages of each.
3. Determine which model best fits:
   - 100 users
   - 2,000 users across three offices
   - 50,000 users across multiple legal entities
4. Justify your design choices.

---

# Key Takeaways

- Active Directory uses DNS namespaces to organize domains.
- Contiguous namespaces form parent-child domain hierarchies.
- Multiple trees can exist within the same forest.
- Trusts enable authentication across domains but do not grant permissions.
- Domain and Forest Functional Levels control available Active Directory features.
- Most organizations benefit from simpler designs unless business requirements dictate otherwise.
- Forest and domain planning should prioritize scalability, manageability, and security.

---

# Interview Questions

1. What is a namespace in Active Directory?
2. What is the difference between a contiguous and disjoint namespace?
3. What is a User Principal Name (UPN)?
4. Why were child domains commonly used historically?
5. What is a trust relationship?
6. What is the difference between Domain Functional Level and Forest Functional Level?
7. When would an organization deploy multiple forests?
8. Why is a single-domain model often recommended?
9. What planning factors should be considered before adding a new domain?
10. Does a trust automatically grant access to resources? Why or why not?

---

# References

- Microsoft Learn – Active Directory Domains and Forests
- Microsoft Windows Server Documentation
- Microsoft Identity Documentation
- Windows Internals
- Microsoft Security Best Practices

---

# 03-Domain-and-Forest.md

# Part 3 — Forest-Wide Components, Global Catalog Placement, Domain Boundaries, Administrative Models, and Enterprise Architecture

---

# Learning Objectives

After completing this part, you will be able to:

- Understand forest-wide Active Directory components.
- Learn how domains interact inside a forest.
- Understand Global Catalog placement strategies.
- Compare administrative models.
- Learn enterprise domain design principles.
- Understand forest boundaries from both operational and cybersecurity perspectives.

---

# Forest-Wide Components

Certain Active Directory components are shared across the entire forest.

These include:

- Active Directory Schema
- Configuration Partition
- Global Catalog
- Trust Infrastructure
- Forest Functional Level
- Enterprise Administrative Groups
- Forest-wide replication of schema and configuration data

These shared components allow domains to operate as a unified directory service.

---

# Forest Architecture

```text
                    Forest

        ┌────────────┼────────────┐

        │            │            │

   Schema      Configuration   Global Catalog

        │            │            │

        └────────────┼────────────┘

                Domains

        ┌────────┼────────┐

        │        │        │

     Domain A Domain B Domain C
```

---

# Schema Sharing

Every domain inside a forest uses the **same Active Directory Schema**.

Example:

```text
Forest

│

Schema

│

├── Domain A

├── Domain B

└── Domain C
```

Advantages:

- Consistent object definitions
- Standardized attributes
- Simplified application integration

Because the schema is shared, schema modifications affect the entire forest and should be carefully planned.

---

# Configuration Partition

The Configuration Partition stores forest-wide information such as:

- Active Directory Sites
- Site Links
- Services
- Replication topology
- Forest configuration

Example:

```text
Configuration

│

├── Sites

├── Services

├── Subnets

└── Site Links
```

All Domain Controllers within the forest receive this partition through replication.

---

# Global Catalog Placement

The Global Catalog (GC) improves search efficiency and supports certain authentication scenarios.

Example:

```text
Forest

│

├── Domain A

│      └── GC01

│

├── Domain B

│      └── GC02

│

└── Domain C

       └── GC03
```

---

# Why Place Multiple Global Catalog Servers?

Benefits include:

- Faster directory searches
- Reduced authentication latency
- Improved redundancy
- Better performance for distributed environments
- Higher availability

Large organizations typically deploy multiple Global Catalog servers across major locations.

---

# Choosing Global Catalog Locations

Factors to consider:

- Number of users
- Number of sites
- WAN bandwidth
- Authentication requirements
- Disaster recovery
- Business-critical applications

Avoid placing all Global Catalog servers in a single location.

---

# Administrative Boundaries

Domains provide administrative boundaries that allow organizations to:

- Delegate management
- Separate operational responsibilities
- Organize identities
- Manage Group Policies
- Apply security controls

However, enterprise governance should remain consistent across the forest where appropriate.

---

# Administrative Models

Several administration models are commonly used.

---

## Centralized Administration

```text
Corporate IT

│

├── Domain A

├── Domain B

└── Domain C
```

Characteristics:

- Single IT team
- Standardized policies
- Simplified governance
- Consistent security

---

## Delegated Administration

```text
Corporate IT

│

├── Region A Admins

├── Region B Admins

└── Region C Admins
```

Characteristics:

- Regional management
- Local operational control
- Reduced central workload
- Requires clearly defined delegation

---

## Hybrid Administration

```text
Corporate IT

│

├── Security

├── Infrastructure

├── Regional IT

└── Help Desk
```

Responsibilities are shared between central and regional teams.

This model is common in large enterprises.

---

# Administrative Delegation

Instead of granting Domain Admin privileges broadly:

Use delegation.

Example:

| Team | Delegated Permissions |
|------|-----------------------|
| Help Desk | Reset passwords |
| Desktop Team | Manage computer accounts |
| HR IT | Create user accounts |
| Server Team | Manage servers |
| Security Team | Audit privileged activity |

Delegation follows the principle of least privilege.

---

# Domain Boundaries

Each domain has its own:

- Domain partition
- Domain Controllers
- Authentication database copy
- Administrative scope
- Group Policy hierarchy

Forest-wide components remain shared.

---

# Example Enterprise Structure

```text
Forest

│

├── company.com

│

├── europe.company.com

│

├── asia.company.com

│

└── americas.company.com
```

Each domain can have:

- Regional administrators
- Local Domain Controllers
- Regional Organizational Units
- Local Group Policies

All share the same forest infrastructure.

---

# Enterprise Identity Flow

```text
User

↓

Regional Domain

↓

Forest Services

↓

Global Catalog

↓

Authentication

↓

Authorization

↓

Enterprise Resources
```

---

# Resource Access Across Domains

Example:

```text
User

↓

HR Domain

↓

Trust Relationship

↓

Finance Domain

↓

ACL Evaluation

↓

Access Granted
```

Even though authentication can cross domains, permissions must still be explicitly granted.

---

# Forest Growth

As organizations expand, forests may include:

- Additional domains
- New geographic regions
- New business units
- Acquired organizations
- Additional Domain Controllers
- Additional Sites

Growth should be planned rather than reactive.

---

# Designing for Scalability

Consider:

- Expected user growth
- Office expansion
- Cloud integration
- Identity lifecycle management
- Disaster recovery
- WAN connectivity
- Replication traffic
- Administrative workload

A scalable design minimizes future restructuring.

---

# Operational Best Practices

- Standardize naming conventions.
- Document domain ownership.
- Review delegated permissions regularly.
- Monitor replication health.
- Deploy redundant Domain Controllers.
- Validate Global Catalog placement.
- Test disaster recovery plans.
- Keep architecture documentation current.

---

# Common Design Mistakes

Avoid:

- Creating unnecessary child domains
- Excessive administrative privileges
- Poor OU planning
- Weak documentation
- Ignoring future growth
- Poor Global Catalog placement
- Insufficient Domain Controllers
- Inconsistent naming standards

Simple, well-governed designs are usually easier to secure and maintain.

---

# Enterprise Case Study

Organization:

- 45,000 employees
- 25 countries
- 40 Domain Controllers
- 8 Global Catalog servers
- Hybrid identity
- Regional IT teams

Design:

```text
Forest

│

└── company.com

       ├── americas.company.com

       ├── europe.company.com

       ├── asia.company.com

       └── middleeast.company.com
```

Benefits:

- Regional administration
- Shared schema
- Consistent governance
- Efficient authentication
- Simplified enterprise search

---

# Cybersecurity Perspective

The forest is the highest level of trust within Active Directory.

Security priorities include:

- Protecting Enterprise Admin accounts
- Limiting forest-wide administrative privileges
- Monitoring trust relationships
- Auditing Global Catalog servers
- Restricting interactive logon to Domain Controllers
- Securing replication traffic
- Maintaining accurate documentation

Compromise of forest-level administrative accounts can have organization-wide consequences.

---

# Hands-on Lab

## Objective

Design a scalable forest architecture.

### Scenario

Organization:

- 12,000 users
- Four geographic regions
- One central IT team
- Regional help desk staff

### Tasks

1. Design the forest hierarchy.
2. Decide whether multiple domains are required.
3. Determine Global Catalog placement.
4. Define delegated administrative roles.
5. Explain your design decisions.

---

# Key Takeaways

- The Schema and Configuration partitions are shared across the forest.
- The Global Catalog enables forest-wide searches and supports authentication.
- Administrative delegation reduces the need for highly privileged accounts.
- Domain boundaries organize administration while the forest provides shared infrastructure.
- Good planning improves scalability, availability, and security.

---

# Interview Questions

1. Which components are shared across an Active Directory forest?
2. Why is the Schema considered a forest-wide component?
3. What information is stored in the Configuration Partition?
4. Why are Global Catalog servers important?
5. How should Global Catalog placement be planned?
6. What is administrative delegation?
7. Why should Domain Admin privileges be minimized?
8. What are the advantages of centralized versus delegated administration?
9. How does a forest support enterprise scalability?
10. Why is the forest considered a critical security boundary?

---

# References

- Microsoft Learn – Active Directory Forest Design
- Microsoft Windows Server Documentation
- Microsoft Identity Documentation
- Windows Internals
- Microsoft Security Best Practices
- CIS Microsoft Windows Benchmarks

---

**Next:** **Part 4 — Forest Design Best Practices, Domain Lifecycle, Common Misconceptions, Architecture Review, Final Revision, and Chapter Summary**