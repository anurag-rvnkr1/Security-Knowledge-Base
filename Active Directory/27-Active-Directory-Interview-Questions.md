# 27-Active-Directory-Interview-Questions.md

# Part 1 — Active Directory Interview Questions (Beginner to Intermediate)

> **Important Note**
>
> This chapter is designed for **System Administrator, Windows Administrator, Active Directory Administrator, Infrastructure Engineer, SOC Analyst, Blue Team, IAM, Help Desk, and Cybersecurity interviews**. The questions focus on **enterprise administration and defensive security**, not offensive techniques.

---

# Learning Objectives

After completing this part, you will be able to:

- Answer common Active Directory interview questions
- Explain AD concepts clearly
- Differentiate similar technologies
- Handle scenario-based interviews
- Prepare for HR + Technical rounds
- Build confidence for enterprise interviews

---

# Interview Preparation Strategy

Most companies evaluate candidates in four stages:

```
Fundamentals

↓

Architecture

↓

Administration

↓

Scenario Questions
```

A strong candidate explains **why**, not just **what**.

---

# Section 1 — Active Directory Fundamentals

## Q1. What is Active Directory?

**Answer:**

Active Directory (AD) is Microsoft's centralized directory service that stores and manages users, computers, groups, printers, and other network resources. It provides authentication, authorization, and centralized administration within Windows domains.

---

## Q2. What are the primary functions of Active Directory?

**Answer:**

- Centralized authentication
- Authorization
- Resource management
- Group Policy management
- Identity management
- Security administration
- Single Sign-On (SSO)

---

## Q3. What is a Domain?

**Answer:**

A domain is a logical security boundary that contains users, computers, groups, and other directory objects managed by Active Directory.

---

## Q4. What is a Domain Controller?

**Answer:**

A Domain Controller (DC) is a server running Active Directory Domain Services (AD DS) that authenticates users, stores directory information, and enforces security policies.

---

## Q5. What is a Forest?

**Answer:**

A forest is the highest logical structure in Active Directory. It can contain one or more domains sharing a common schema and global catalog.

---

## Q6. What is a Tree?

**Answer:**

A tree is a collection of domains that share a contiguous DNS namespace.

---

## Q7. What is an Organizational Unit (OU)?

**Answer:**

An Organizational Unit is a container used to organize directory objects and delegate administration or apply Group Policies.

---

## Q8. Difference between OU and Group?

| OU | Group |
|----|-------|
| Organizes objects | Grants permissions |
| Supports delegation | Supports access control |
| Used for GPOs | Used for authorization |

---

## Q9. What is LDAP?

**Answer:**

LDAP (Lightweight Directory Access Protocol) is the protocol used to query and manage directory services such as Active Directory.

---

## Q10. What is Kerberos?

**Answer:**

Kerberos is the default authentication protocol used by Active Directory. It uses tickets to securely authenticate users without repeatedly transmitting passwords.

---

# Section 2 — Active Directory Objects

## Q11. Which objects are stored in Active Directory?

Examples include:

- Users
- Groups
- Computers
- Printers
- Contacts
- Organizational Units
- Shared folders
- Service accounts

---

## Q12. What is a Security Group?

**Answer:**

A Security Group is used to assign permissions to users and computers for accessing resources.

---

## Q13. What is a Distribution Group?

**Answer:**

A Distribution Group is used for email distribution and cannot be used to assign security permissions.

---

## Q14. Difference between Security Group and Distribution Group?

| Security Group | Distribution Group |
|---------------|--------------------|
| Permission management | Email distribution |
| Access control | Messaging only |
| Used by Windows security | Used by mail systems |

---

## Q15. What is a Computer Account?

**Answer:**

A computer account represents a device joined to the domain and allows it to participate securely in domain authentication and management.

---

# Section 3 — Authentication

## Q16. What is Authentication?

**Answer:**

Authentication verifies the identity of a user, computer, or service before access is granted.

---

## Q17. What is Authorization?

**Answer:**

Authorization determines what authenticated users are permitted to access or perform.

---

## Q18. Difference between Authentication and Authorization?

| Authentication | Authorization |
|---------------|---------------|
| Verifies identity | Determines permissions |
| Happens first | Happens after authentication |

---

## Q19. What is Single Sign-On (SSO)?

**Answer:**

Single Sign-On allows users to authenticate once and access multiple authorized systems without signing in repeatedly.

---

## Q20. Why is DNS important for Active Directory?

**Answer:**

Active Directory relies on DNS to locate Domain Controllers and directory services. Without healthy DNS, authentication and many AD services may fail.

---

# Section 4 — Group Policy

## Q21. What is Group Policy?

**Answer:**

Group Policy is a centralized management feature used to configure operating system, user, and security settings across domain-joined devices.

---

## Q22. Where can Group Policy be applied?

It can be linked to:

- Sites
- Domains
- Organizational Units

---

## Q23. What is Group Policy inheritance?

**Answer:**

Inheritance allows policies applied at higher levels to flow down to child containers unless otherwise configured.

---

## Q24. Why use Group Policy?

Benefits include:

- Security configuration
- Software deployment
- Desktop standardization
- Password policies
- Administrative control

---

## Q25. Can multiple GPOs apply to one computer?

**Answer:**

Yes. Multiple Group Policy Objects may apply based on scope and processing order.

---

# Section 5 — Domain Controllers

## Q26. What services does a Domain Controller provide?

- Authentication
- Authorization
- Directory services
- Replication
- Policy enforcement
- DNS integration (when configured)

---

## Q27. Why deploy multiple Domain Controllers?

**Answer:**

To improve availability, redundancy, load distribution, and fault tolerance.

---

## Q28. What happens if one Domain Controller becomes unavailable?

**Answer:**

Other healthy Domain Controllers can continue providing authentication and directory services, assuming the environment is properly designed.

---

## Q29. What is Active Directory replication?

**Answer:**

Replication synchronizes directory changes between Domain Controllers to maintain a consistent directory.

---

## Q30. Why is replication important?

**Answer:**

It ensures directory updates are available across the enterprise and supports reliable authentication and administration.

---

# Mini Scenario Questions

### Scenario 1

A user cannot log in.

What would you verify first?

**Suggested Answer:**

- Username
- Account status
- Password validity
- DNS
- Domain Controller availability
- Time synchronization

---

### Scenario 2

Group Policy is not applying.

What would you check?

**Suggested Answer:**

- GPO linkage
- OU placement
- Replication
- Client policy processing
- Event logs

---

### Scenario 3

Users in one office experience slow authentication.

What areas would you investigate?

**Suggested Answer:**

- Site connectivity
- DNS
- Domain Controller health
- Replication
- Network performance

---

# Interview Tips

- Explain concepts in simple language.
- Use enterprise examples.
- Distinguish similar terms (Authentication vs Authorization, OU vs Group, Forest vs Domain).
- Describe troubleshooting steps logically.
- If unsure, explain how you would investigate instead of guessing.

---

# Hands-on Practice

Create answers in your own words for:

- What is Active Directory?
- How does Kerberos work at a high level?
- Why is DNS critical for AD?
- What is Group Policy?
- How would you troubleshoot a user logon issue?

---

# Key Takeaways

- Master the fundamentals before advanced topics.
- Structure answers clearly: **Definition → Purpose → Example**.
- Be prepared for scenario-based questions.
- Demonstrate a systematic troubleshooting mindset.

---

**Next:** Part 2