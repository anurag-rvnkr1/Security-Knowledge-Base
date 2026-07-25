# 13-Active-Directory-Certificate-Services.md

# Part 1 — Introduction to Active Directory Certificate Services (AD CS), Public Key Infrastructure (PKI), Certificate Authorities, and Enterprise Fundamentals

---

# Learning Objectives

After completing this part, you will be able to:

- Understand Active Directory Certificate Services (AD CS).
- Learn Public Key Infrastructure (PKI).
- Understand digital certificates.
- Learn Certificate Authorities (CAs).
- Understand public/private key cryptography.
- Learn certificate trust chains.
- Prepare for enterprise PKI deployment.

---

# Introduction

Modern enterprise environments require more than usernames and passwords.

Organizations need secure mechanisms for:

- User authentication
- Device authentication
- Website security
- Email encryption
- Digital signatures
- VPN authentication
- Wi-Fi authentication
- Smart card logon
- Code signing

Active Directory provides these capabilities through **Active Directory Certificate Services (AD CS)**.

---

# What is Active Directory Certificate Services (AD CS)?

**Active Directory Certificate Services (AD CS)** is a Windows Server role that enables organizations to build and manage a **Public Key Infrastructure (PKI)**.

It issues, manages, renews, and revokes digital certificates used to establish trust between users, devices, applications, and services.

---

# Why Do We Need AD CS?

Imagine an employee accessing:

- VPN
- Internal websites
- Wi-Fi
- Remote Desktop
- Email

Without certificates:

```text
Username

↓

Password

↓

Authentication
```

With AD CS:

```text
Certificate

↓

Cryptographic Verification

↓

Trusted Authentication
```

Certificates provide stronger identity verification than passwords alone in many scenarios.

---

# Real-World Analogy

Think of a passport.

A passport contains:

- Identity
- Issuing authority
- Expiration date
- Security features

A digital certificate serves a similar purpose.

It proves:

- Identity
- Ownership
- Trustworthiness

---

# What is PKI?

**Public Key Infrastructure (PKI)** is the framework that manages:

- Digital certificates
- Public keys
- Private keys
- Certificate Authorities
- Trust relationships
- Certificate lifecycle

PKI is the foundation that allows secure communication across enterprise networks.

---

# PKI Components

A typical PKI includes:

```text
Certificate Authority

↓

Issues Certificate

↓

User / Computer

↓

Uses Certificate

↓

Application

↓

Verifies Certificate
```

---

# Core PKI Components

| Component | Purpose |
|-----------|---------|
| Certificate Authority (CA) | Issues and manages certificates |
| Digital Certificate | Identity document |
| Public Key | Shared openly |
| Private Key | Secret cryptographic key |
| Certificate Revocation List (CRL) | Lists revoked certificates |
| Registration Authority (RA) | Validates enrollment requests (optional) |
| Certificate Store | Stores certificates |

---

# What is a Digital Certificate?

A **digital certificate** is an electronic credential that binds an identity to a public key.

It is digitally signed by a trusted Certificate Authority.

Certificates help systems verify that an identity is genuine.

---

# Information Inside a Certificate

A certificate typically contains:

- Subject name
- Public key
- Serial number
- Issuing CA
- Validity period
- Signature algorithm
- Thumbprint
- Extensions
- Key usage
- Enhanced Key Usage (EKU)

---

# Simplified Certificate Structure

```text
Certificate

├── Subject

├── Issuer

├── Public Key

├── Serial Number

├── Valid From

├── Valid Until

├── Signature

└── Extensions
```

---

# Public Key Cryptography

PKI relies on **asymmetric cryptography**.

Each identity receives:

- One Public Key
- One Private Key

Example:

```text
Public Key

↓

Can Be Shared
```

```text
Private Key

↓

Must Remain Secret
```

---

# Key Pair Concept

```text
User

│

├── Public Key

└── Private Key
```

The two keys are mathematically related, but the private key cannot practically be derived from the public key.

---

# Public Key Usage

Public keys are used for operations such as:

- Encryption
- Signature verification
- Certificate validation

Anyone can obtain the public key.

---

# Private Key Usage

Private keys are used for:

- Decryption (depending on the protocol)
- Creating digital signatures
- Authentication
- Identity proof

Private keys must never be shared.

---

# Why Two Keys?

Instead of using one shared secret:

```text
Single Secret

↓

High Risk
```

PKI uses:

```text
Public Key

↓

Everyone Can Know
```

```text
Private Key

↓

Only Owner Knows
```

This enables secure communication without exposing secret keys.

---

# What is a Certificate Authority (CA)?

A **Certificate Authority (CA)** is a trusted entity that issues digital certificates.

Its responsibilities include:

- Verifying identity
- Issuing certificates
- Renewing certificates
- Revoking certificates
- Publishing revocation information
- Maintaining trust

---

# CA Workflow

```text
Certificate Request

↓

Certificate Authority

↓

Identity Verification

↓

Certificate Issued

↓

User Receives Certificate
```

---

# Trusting the CA

Applications generally trust certificates issued by trusted CAs.

Example:

```text
Browser

↓

Website Certificate

↓

Trusted CA

↓

Secure Connection
```

If the issuing CA is not trusted, users receive warnings or the connection may fail.

---

# Root Certificate Authority

The **Root CA** is the highest trust authority in a PKI.

```text
Root CA

↓

Signs

↓

Subordinate CA

↓

Signs

↓

User Certificates
```

The Root CA serves as the trust anchor.

---

# Certificate Chain

Certificates are validated through a **certificate chain**.

Example:

```text
User Certificate

↓

Issuing CA

↓

Intermediate CA

↓

Root CA
```

If every certificate in the chain is trusted and valid, the certificate is considered trustworthy.

---

# Trust Chain Diagram

```text
Root CA

↓

Intermediate CA

↓

Issuing CA

↓

Computer Certificate

↓

Application Trusts Certificate
```

---

# Enterprise Example

Company:

```text
GlobalTech
```

PKI deployment:

```text
Offline Root CA

↓

Enterprise Issuing CA

↓

Employee Certificates

↓

Laptop Certificates

↓

Web Server Certificates

↓

VPN Certificates
```

Benefits:

- Centralized trust
- Strong authentication
- Secure communications
- Simplified certificate management

---

# Common Uses of AD CS

Organizations commonly issue certificates for:

- Domain Controllers
- User authentication
- Computer authentication
- HTTPS websites
- VPN servers
- Wi-Fi (802.1X)
- Email encryption
- Smart cards
- Code signing
- Remote Desktop Services

---

# Cybersecurity Perspective

Certificates are foundational to enterprise security.

Security teams should:

- Protect Certificate Authorities.
- Secure private keys.
- Use strong cryptographic algorithms.
- Monitor certificate issuance.
- Audit CA administrators.
- Secure backup copies of CA databases and keys.

Compromise of a Certificate Authority can undermine trust across the entire PKI.

---

# Common Mistakes

Avoid:

- Sharing private keys.
- Leaving private keys unprotected.
- Trusting unknown Certificate Authorities.
- Treating certificates as permanent.
- Ignoring certificate expiration.

---

# Hands-on Lab

## Objective

Explore the basics of certificates.

### Tasks

1. Open:

```text
certlm.msc
```

2. Browse:

- Personal
- Trusted Root Certification Authorities
- Intermediate Certification Authorities

3. Open any certificate.

4. Record:

- Subject
- Issuer
- Validity period
- Thumbprint
- Public Key Algorithm

5. Draw the certificate chain.

---

# Interview Questions

1. What is Active Directory Certificate Services?
2. What is PKI?
3. What is a digital certificate?
4. What is the difference between a public key and a private key?
5. What is a Certificate Authority?
6. What is a Root CA?
7. What is a certificate chain?
8. Why must private keys remain secret?
9. What information is stored in a certificate?
10. Why is AD CS important in enterprise environments?

---

# Key Takeaways

- Active Directory Certificate Services (AD CS) enables organizations to build and manage a Public Key Infrastructure (PKI).
- PKI uses public and private key cryptography to provide secure authentication, encryption, and digital signatures.
- Digital certificates bind an identity to a public key and are issued by trusted Certificate Authorities.
- The Root CA acts as the trust anchor, while subordinate CAs issue certificates to users, devices, and services.
- Protecting Certificate Authorities and private keys is critical because they establish trust throughout the enterprise.

---

# 13-Active-Directory-Certificate-Services.md

# Part 2 — Certificate Authorities, AD CS Role Services, Certificate Templates, Enrollment Methods, Certificate Stores, and Enterprise PKI Architecture

---

# Learning Objectives

After completing this part, you will be able to:

- Understand different Certificate Authority (CA) types.
- Learn AD CS role services.
- Understand Enterprise and Standalone CAs.
- Learn certificate templates.
- Understand certificate enrollment methods.
- Learn certificate stores.
- Design enterprise PKI architecture.

---

# Types of Certificate Authorities

Active Directory Certificate Services supports multiple types of Certificate Authorities.

The major types are:

- Root CA
- Subordinate (Intermediate) CA
- Enterprise CA
- Standalone CA
- Issuing CA

Each serves a different purpose within a PKI hierarchy.

---

# Root Certificate Authority

The **Root CA** is the highest level of trust.

Characteristics:

- Trust anchor
- Self-signed certificate
- Signs subordinate CA certificates
- Usually kept offline
- Highly protected

Architecture:

```text
Root CA

↓

Subordinate CA

↓

Issuing CA

↓

Certificates
```

---

# Why Keep the Root CA Offline?

An enterprise Root CA is rarely used after initial deployment.

Example:

```text
Install Root CA

↓

Issue Subordinate CA Certificate

↓

Shutdown

↓

Store Securely
```

Benefits:

- Smaller attack surface
- Better protection of the root private key
- Reduced compromise risk

---

# Offline Root CA Best Practices

Recommended:

✔ Not domain joined

✔ Powered on only when required

✔ Stored securely

✔ Strong administrator controls

✔ Hardware-backed key protection if available

✔ Offline backups

---

# Subordinate Certificate Authority

A **Subordinate CA** receives its certificate from another CA.

Example:

```text
Root CA

↓

Signs

↓

Subordinate CA
```

The subordinate CA inherits trust from the Root CA.

---

# Intermediate CA

An **Intermediate CA** sits between the Root CA and the Issuing CA.

Example:

```text
Root CA

↓

Intermediate CA

↓

Issuing CA

↓

Users
```

Benefits:

- Better security
- Flexible certificate management
- Simplified key rollover
- Reduced exposure of the Root CA

---

# Issuing Certificate Authority

An **Issuing CA** performs day-to-day certificate issuance.

It issues certificates for:

- Users
- Computers
- Servers
- VPN
- Wi-Fi
- Smart Cards
- Applications

Example:

```text
User Request

↓

Issuing CA

↓

Certificate Issued
```

---

# Enterprise CA

An **Enterprise CA** integrates with Active Directory.

Features:

- Uses Active Directory
- Supports certificate templates
- Automatic enrollment
- User and computer discovery
- Simplified certificate management

---

# Enterprise CA Workflow

```text
Computer Joins Domain

↓

Group Policy

↓

Auto Enrollment

↓

Enterprise CA

↓

Certificate Installed
```

Minimal administrator intervention is required after configuration.

---

# Advantages of Enterprise CA

Advantages include:

- Active Directory integration
- Automatic certificate issuance
- Template support
- Auto-enrollment
- Easier lifecycle management
- Centralized administration

---

# Standalone CA

A **Standalone CA** operates independently of Active Directory.

Characteristics:

- Does not require domain membership
- Manual approval can be used
- No certificate templates
- Suitable for isolated environments

---

# Enterprise CA vs Standalone CA

| Feature | Enterprise CA | Standalone CA |
|----------|---------------|---------------|
| Active Directory Integration | Yes | No |
| Certificate Templates | Yes | No |
| Auto Enrollment | Yes | No |
| Manual Requests | Optional | Common |
| Domain Membership | Required | Not required |

---

# Enterprise PKI Hierarchy

Example:

```text
Offline Root CA

↓

Intermediate CA

↓

Enterprise Issuing CA

↓

Users

↓

Computers

↓

Servers
```

This is a common enterprise design.

---

# AD CS Role Services

The Active Directory Certificate Services role contains several role services.

Common role services include:

- Certification Authority
- Certificate Enrollment Web Service
- Certificate Enrollment Policy Web Service
- Online Responder
- Network Device Enrollment Service (NDES)

Organizations install only the services they require.

---

# Certification Authority Role

Purpose:

- Issue certificates
- Renew certificates
- Revoke certificates
- Publish Certificate Revocation Lists (CRLs)

Without this role, no certificates can be issued.

---

# Online Responder

The **Online Responder** supports the **Online Certificate Status Protocol (OCSP)**.

Instead of downloading an entire CRL:

```text
Client

↓

OCSP Request

↓

Online Responder

↓

Certificate Status
```

Benefits:

- Faster validation
- Lower bandwidth
- Near real-time status checking

---

# Certificate Enrollment Web Services

These services allow certificate enrollment for clients that may not have direct connectivity to the CA.

Example:

```text
Remote Computer

↓

Enrollment Web Service

↓

Enterprise CA

↓

Certificate Issued
```

---

# Network Device Enrollment Service (NDES)

NDES enables certificate enrollment for devices that support the **Simple Certificate Enrollment Protocol (SCEP)**.

Typical devices:

- Routers
- Switches
- Firewalls
- Mobile Device Management (MDM) solutions
- IoT devices

---

# Certificate Templates

A **Certificate Template** defines how certificates should be issued.

Templates specify:

- Intended purpose
- Key length
- Validity period
- Renewal period
- Subject name format
- Key usage
- Enhanced Key Usage (EKU)
- Security permissions

---

# Template Workflow

```text
Certificate Request

↓

Template

↓

CA

↓

Certificate
```

The template ensures certificates are issued consistently.

---

# Common Certificate Templates

| Template | Typical Usage |
|-----------|---------------|
| User | User authentication |
| Computer | Computer authentication |
| Domain Controller | Kerberos and LDAP |
| Web Server | HTTPS |
| Smart Card Logon | Smart card authentication |
| Code Signing | Software signing |
| EFS | Encrypting File System |

---

# Template Permissions

Templates include security permissions that determine:

- Who can enroll
- Who can auto-enroll
- Who can read the template
- Who can manage the template

Example:

```text
Domain Computers

↓

Auto Enroll

↓

Computer Certificate
```

---

# Certificate Enrollment

Enrollment is the process of obtaining a certificate.

Methods include:

- Manual enrollment
- Auto-enrollment
- Web enrollment
- SCEP enrollment
- API or application enrollment

---

# Manual Enrollment

Administrator:

```text
Open MMC

↓

Request Certificate

↓

CA Approval

↓

Certificate Installed
```

Suitable for:

- Testing
- Special-purpose certificates
- Small environments

---

# Auto Enrollment

Auto-enrollment is controlled through **Group Policy**.

Example:

```text
Group Policy

↓

Domain Computer

↓

Enterprise CA

↓

Certificate Automatically Installed
```

Ideal for large enterprise environments.

---

# Web Enrollment

Users submit certificate requests through a web interface.

Example:

```text
Browser

↓

Enrollment Website

↓

Certificate Request

↓

CA

↓

Certificate Issued
```

---

# Certificate Stores

Windows stores certificates in logical certificate stores.

Common stores include:

| Store | Purpose |
|--------|----------|
| Personal | User or computer certificates |
| Trusted Root Certification Authorities | Trusted Root CAs |
| Intermediate Certification Authorities | Intermediate CAs |
| Trusted Publishers | Software publishers |
| Enterprise Trust | Enterprise trust information |

---

# User vs Computer Store

```text
User Store

↓

User Certificates
```

```text
Computer Store

↓

Machine Certificates
```

Applications select the appropriate store depending on their authentication requirements.

---

# Enterprise Architecture Example

Large Organization:

```text
Offline Root CA

↓

Intermediate CA

↓

Enterprise Issuing CA

↓

Auto Enrollment

↓

100,000 Computers

↓

50,000 Users

↓

Internal Applications
```

Benefits:

- Centralized certificate management
- Automated deployment
- Consistent security policies
- Scalable PKI

---

# Cybersecurity Perspective

PKI components should be protected with the same care as Domain Controllers.

Recommendations:

- Keep the Root CA offline.
- Restrict CA administrators.
- Audit certificate issuance.
- Protect CA private keys.
- Limit template permissions.
- Regularly review published templates.

Misconfigured certificate templates can create significant security risks.

---

# Common Mistakes

Avoid:

- Using an online Root CA in production.
- Granting excessive enrollment permissions.
- Publishing unnecessary certificate templates.
- Leaving expired templates active.
- Ignoring CA backup procedures.

---

# Hands-on Lab

## Objective

Explore AD CS components.

### Tasks

1. Open:

```text
Certification Authority
```

2. Review:

- Certificate Templates
- Issued Certificates
- Pending Requests
- Revoked Certificates

3. Open:

```text
certtmpl.msc
```

4. Examine:

- User Template
- Computer Template
- Web Server Template

5. Record:

- Validity period
- Key length
- Intended purposes (EKUs)
- Enrollment permissions

---

# Interview Questions

1. What is the difference between a Root CA and an Issuing CA?
2. Why is an Offline Root CA recommended?
3. What is an Enterprise CA?
4. How does a Standalone CA differ from an Enterprise CA?
5. What is a certificate template?
6. What role does auto-enrollment play in enterprise PKI?
7. What is the purpose of the Online Responder (OCSP)?
8. What is NDES used for?
9. What information is defined by a certificate template?
10. Where are certificates stored in Windows?

---

# Key Takeaways

- Enterprise PKI typically uses an Offline Root CA with one or more subordinate or issuing CAs.
- Enterprise CAs integrate with Active Directory and support templates and auto-enrollment, while Standalone CAs operate independently.
- AD CS role services provide capabilities such as certificate issuance, OCSP responses, web enrollment, and SCEP enrollment.
- Certificate templates standardize certificate issuance by defining security, usage, validity, and enrollment settings.
- Proper CA hierarchy, template permissions, and private key protection are essential for a secure enterprise PKI.

---

**Next:** Part 3