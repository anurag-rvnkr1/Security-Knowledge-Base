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

**Next:** Part 2