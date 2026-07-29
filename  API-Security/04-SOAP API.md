# 04 - SOAP API

# Introduction

Simple Object Access Protocol (SOAP) is a protocol specification for exchanging structured information between applications over a network.

Before REST became the dominant architecture for web APIs, SOAP was the primary standard used by enterprise organizations for building secure, reliable, and interoperable web services.

Today, SOAP remains widely deployed in industries where:

- High security
- Transaction integrity
- Compliance
- Reliability
- Formal contracts

are more important than simplicity.

Common industries using SOAP include:

- Banking
- Financial Services
- Insurance
- Government
- Healthcare
- Telecommunications
- Aviation
- Enterprise ERP Systems

Major enterprise products such as Oracle, SAP, IBM WebSphere, Microsoft Dynamics, Salesforce integrations, and many legacy banking platforms continue to expose SOAP web services.

Understanding SOAP is important because cybersecurity professionals frequently encounter legacy enterprise environments where SOAP services are still critical business assets.

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand SOAP fundamentals.
- Explain SOAP architecture.
- Understand XML messaging.
- Learn SOAP communication flow.
- Understand SOAP envelopes.
- Explain SOAP headers and body.
- Understand WSDL.
- Differentiate SOAP and REST.
- Recognize enterprise SOAP deployments.
- Identify SOAP security mechanisms.
- Understand common SOAP attack surfaces.

---

# What is SOAP?

SOAP stands for:

> **Simple Object Access Protocol**

SOAP is a standardized messaging protocol used for communication between distributed applications.

Unlike REST, SOAP is:

- Protocol-based
- XML-only
- Contract-driven
- Highly standardized

SOAP defines:

- Message structure
- Communication rules
- Error handling
- Security extensions
- Reliable messaging

---

# SOAP Definition

SOAP is an XML-based messaging protocol that enables applications running on different operating systems, programming languages, and hardware platforms to exchange structured information.

Example

```
Java Application

        │

SOAP XML

        │

.NET Application
```

The applications do not need to understand each other's internal implementation.

SOAP provides interoperability through standardized XML messages.

---

# Evolution of SOAP

Before SOAP, distributed systems relied on technologies such as:

- CORBA
- DCOM
- Java RMI
- RPC

These approaches suffered from:

- Platform dependency
- Vendor lock-in
- Complex networking
- Limited interoperability

SOAP introduced a platform-independent, XML-based communication protocol built on open standards.

---

# SOAP Timeline

```
RPC

   │

   ▼

CORBA

   │

   ▼

SOAP 1.1

   │

   ▼

SOAP 1.2

   │

   ▼

REST

   │

   ▼

GraphQL

   │

   ▼

gRPC
```

Although newer API styles have become popular, SOAP continues to power many enterprise systems.

---

# Why SOAP Was Created

SOAP addressed several enterprise challenges.

Organizations required:

- Platform independence
- Standardized messaging
- Reliable communication
- Security
- Transaction management
- Formal service contracts

SOAP provided standardized solutions for each requirement.

---

# SOAP Communication Model

```
Client Application

        │

SOAP Request

        ▼

SOAP Server

        │

Business Logic

        │

Database

        │

SOAP Response

        ▼

Client
```

Both requests and responses use XML.

---

# SOAP Architecture

A typical SOAP architecture consists of:

```
+---------------------------+
| Client Application        |
+------------+--------------+
             │
             ▼
+---------------------------+
| SOAP Client Library       |
+------------+--------------+
             │
             ▼
+---------------------------+
| HTTP / SMTP / JMS         |
+------------+--------------+
             │
             ▼
+---------------------------+
| SOAP Server               |
+------------+--------------+
             │
             ▼
+---------------------------+
| Business Logic            |
+------------+--------------+
             │
             ▼
+---------------------------+
| Database                  |
+---------------------------+
```

Unlike REST, SOAP is transport-independent and can operate over multiple protocols.

---

# SOAP Components

SOAP consists of several core components.

- SOAP Envelope
- SOAP Header
- SOAP Body
- SOAP Fault

Every SOAP message follows this structure.

---

# SOAP Message Structure

```
SOAP Message

│

├────────► Envelope

│

├────────► Header (Optional)

│

├────────► Body

│

└────────► Fault (Optional)
```

The envelope acts as the root element of every SOAP message.

---

# XML in SOAP

SOAP exclusively uses XML.

Example

```xml
<?xml version="1.0"?>

<soap:Envelope>

    ...

</soap:Envelope>
```

Advantages

- Platform independent
- Self-describing
- Standardized
- Human readable

Disadvantages

- Larger payloads
- Slower parsing
- Higher bandwidth usage

---

# SOAP Envelope

The envelope defines the beginning and end of the SOAP message.

Example

```xml
<soap:Envelope>

</soap:Envelope>
```

Every SOAP message must contain exactly one envelope.

---

# SOAP Header

The header contains metadata.

Examples

- Authentication
- Authorization
- Routing
- Digital signatures
- Encryption information
- Transaction identifiers

Example

```xml
<soap:Header>

    <Authentication>

        ...

    </Authentication>

</soap:Header>
```

Headers are optional but widely used in enterprise deployments.

---

# SOAP Body

The body contains the actual business request.

Example

```xml
<soap:Body>

    <GetCustomer>

        ...

    </GetCustomer>

</soap:Body>
```

Business operations are represented as XML elements.

---

# SOAP Fault

SOAP Fault provides standardized error handling.

Example

```xml
<soap:Fault>

    ...

</soap:Fault>
```

Typical information includes:

- Error code
- Error message
- Error details
- Fault actor

SOAP Faults provide significantly richer error information than many REST APIs.

---

# SOAP Request Example

```xml
POST /CustomerService HTTP/1.1

Content-Type: text/xml

SOAPAction: "GetCustomer"

<?xml version="1.0"?>

<soap:Envelope>

    <soap:Body>

        <GetCustomer>

            <CustomerID>100</CustomerID>

        </GetCustomer>

    </soap:Body>

</soap:Envelope>
```

The request body contains the XML message enclosed within a SOAP envelope.

---

# SOAP Response Example

```xml
HTTP/1.1 200 OK

Content-Type: text/xml

<soap:Envelope>

    <soap:Body>

        <GetCustomerResponse>

            <Name>Alice</Name>

        </GetCustomerResponse>

    </soap:Body>

</soap:Envelope>
```

The response also uses XML.

---

# SOAP Transport Protocols

Although HTTP is the most common transport, SOAP supports multiple protocols.

Examples

- HTTP
- HTTPS
- SMTP
- JMS
- TCP
- MQ

This flexibility made SOAP attractive for enterprise integration.

---

# SOAP over HTTP

Most SOAP services communicate using HTTP or HTTPS.

```
SOAP Client

     │

HTTP POST

     ▼

SOAP Server

     │

XML Response

     ▼

Client
```

Unlike REST, SOAP generally uses **POST** for most operations.

---

# Enterprise Use Cases

SOAP is commonly used for:

Financial Services

- Fund transfers
- Payment processing
- Regulatory reporting

Healthcare

- Patient records
- Insurance claims
- Laboratory integration

Government

- Citizen services
- Identity verification
- Tax systems

Enterprise

- ERP integration
- CRM integration
- HR systems

Telecommunications

- Billing
- Subscriber management
- Service provisioning

---

# Advantages of SOAP

SOAP provides several enterprise benefits.

- Platform independent
- Strong standards
- Built-in extensibility
- Reliable messaging
- Advanced security
- Formal service contracts
- Transaction support
- Vendor interoperability

These features make SOAP suitable for mission-critical systems.

---

# Disadvantages of SOAP

SOAP also has limitations.

- Large XML payloads
- Higher bandwidth consumption
- Slower performance
- Complex implementation
- Difficult debugging
- Steeper learning curve
- Less suitable for lightweight mobile applications

These limitations contributed to the widespread adoption of REST for modern web APIs.

---

# Enterprise Example

A multinational bank integrates its core banking system with external payment processors using SOAP.

Architecture

```
ATM

 │

 ▼

Bank Gateway

 │

 ▼

SOAP Service

 │

 ▼

Authentication

 │

 ▼

Core Banking

 │

 ▼

Transaction Database
```

SOAP provides:

- Reliable messaging
- Transaction consistency
- Strong security
- Formal contracts
- Regulatory compliance

These characteristics are essential for financial systems where correctness and reliability outweigh payload size.

---

# Key Takeaways

- SOAP is a protocol for exchanging structured XML messages between distributed applications.
- It is contract-driven, standardized, and designed for enterprise interoperability.
- Every SOAP message consists of an Envelope, optional Header, Body, and optional Fault.
- SOAP commonly operates over HTTP/HTTPS but supports multiple transport protocols.
- XML is the only supported message format in SOAP.
- SOAP remains widely used in banking, healthcare, government, telecommunications, and enterprise integration scenarios.
- Its strengths include security, reliability, extensibility, and formal contracts, while its primary drawbacks are complexity and larger message sizes.

---

# XML Namespaces

SOAP messages rely heavily on **XML Namespaces** to uniquely identify XML elements and prevent naming conflicts.

Without namespaces, different XML documents may define elements with identical names, making it difficult for applications to determine which element belongs to which schema.

Example:

```
<Customer>

<Name>

</Name>

</Customer>
```

If another application also defines a `<Customer>` element, conflicts occur.

Namespaces solve this problem.

---

# What is an XML Namespace?

An XML namespace uniquely identifies XML elements using a Uniform Resource Identifier (URI).

Example

```xml
<soap:Envelope
xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
```

Here,

```
soap
```

is the namespace prefix, while

```
http://schemas.xmlsoap.org/soap/envelope/
```

identifies the SOAP specification.

---

# Namespace Structure

```
Prefix

↓

Namespace URI

↓

Element
```

Example

```xml
<soap:Body>
```

Where

```
soap

↓

Namespace Prefix

↓

SOAP Specification
```

---

# Multiple Namespaces

A SOAP message often uses multiple namespaces.

Example

```xml
<soap:Envelope

xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"

xmlns:cus="http://company.com/customer">

<soap:Body>

<cus:GetCustomer>

<cus:CustomerID>100</cus:CustomerID>

</cus:GetCustomer>

</soap:Body>

</soap:Envelope>
```

Here:

```
soap

↓

SOAP Namespace
```

```
cus

↓

Business Namespace
```

---

# Why Namespaces Matter

Benefits include:

- Prevent naming conflicts
- Improve interoperability
- Enable schema validation
- Separate business elements from protocol elements
- Improve XML readability

Namespaces are mandatory for interoperable SOAP services.

---

# SOAP Namespace Example

```
SOAP Envelope

↓

soap Namespace
```

```
Business Request

↓

Application Namespace
```

Example

```xml
<soap:Body>

<bank:TransferFunds>

...

</bank:TransferFunds>

</soap:Body>
```

---

# XML Schema (XSD)

SOAP messages frequently rely on **XML Schema Definition (XSD)**.

XSD defines:

- Data types
- Required elements
- Optional elements
- Constraints
- Validation rules

Example

```
CustomerID

↓

Integer
```

```
Email

↓

String
```

Applications validate incoming XML against these schemas before processing requests.

---

# Web Services Description Language (WSDL)

One of SOAP's defining characteristics is the use of **WSDL**.

WSDL stands for:

> **Web Services Description Language**

It is an XML document that formally describes a SOAP web service.

It defines:

- Available operations
- Input parameters
- Output parameters
- Message formats
- Transport protocols
- Service endpoints

Unlike REST, where documentation is often external (such as OpenAPI), WSDL acts as a machine-readable service contract.

---

# Why WSDL Exists

Before invoking a SOAP service, clients need to know:

- Which operations exist?
- Which parameters are required?
- What data types are expected?
- Which endpoint should be used?
- Which protocol should be used?

WSDL answers all of these questions.

---

# WSDL Architecture

```
Client

    │

Read WSDL

    │

Generate Client

    │

SOAP Request

    ▼

SOAP Service
```

Many development tools automatically generate client libraries directly from a WSDL document.

---

# WSDL Components

A WSDL document consists of several major sections.

```
WSDL

│

├────────► Types

├────────► Messages

├────────► Port Types

├────────► Bindings

└────────► Service
```

Each component has a specific responsibility.

---

# Types

The **Types** section defines data structures.

Example

```
Customer

Order

Invoice

Payment
```

These are usually described using XML Schema (XSD).

---

# Messages

Messages define data exchanged between client and server.

Example

```
GetCustomerRequest
```

```
GetCustomerResponse
```

Each message specifies the required XML elements.

---

# Port Types

Port Types define available operations.

Example

```
Customer Service

↓

GetCustomer()

CreateCustomer()

DeleteCustomer()
```

A Port Type is conceptually similar to an interface in object-oriented programming.

---

# Bindings

Bindings specify:

- Transport protocol
- Encoding style
- SOAP version

Example

```
SOAP 1.2

↓

HTTPS

↓

Document Style
```

---

# Service

The Service section identifies the actual endpoint.

Example

```
https://api.company.com/customer
```

Clients connect to this endpoint when invoking SOAP operations.

---

# WSDL Workflow

```
Developer

     │

Publish WSDL

     ▼

Client Downloads WSDL

     │

Generate Client Library

     │

Invoke SOAP Service
```

This significantly reduces manual development effort.

---

# SOAP Operations

SOAP supports several operation types.

```
One-Way

Request-Response

Solicit-Response

Notification
```

Each defines how messages flow between client and server.

---

# One-Way Operation

The client sends a request.

No response is expected.

```
Client

 │

SOAP Request

 ▼

Server
```

Example:

- Audit logging
- Event notification
- Fire-and-forget processing

---

# Request-Response

Most common SOAP operation.

```
Client

 │

SOAP Request

 ▼

Server

 │

SOAP Response

 ▼

Client
```

Used for:

- Banking
- Authentication
- Customer lookup
- Payment processing

---

# Solicit-Response

The server initiates communication.

```
Server

 │

Request

 ▼

Client

 │

Response

 ▼

Server
```

Rarely implemented in modern enterprise systems.

---

# Notification

The server sends information without expecting a reply.

```
Server

 │

Notification

 ▼

Client
```

Example

- Event alerts
- Monitoring systems
- Enterprise notifications

---

# RPC Style vs Document Style

SOAP supports two messaging styles.

```
RPC Style
```

and

```
Document Style
```

---

# RPC Style

RPC (Remote Procedure Call) focuses on invoking methods.

Example

```
GetCustomer()
```

Request

```xml
<GetCustomer>

<CustomerID>100</CustomerID>

</GetCustomer>
```

Advantages

- Familiar programming model
- Simple for developers

Disadvantages

- Tight coupling
- Limited flexibility
- Less interoperable

---

# Document Style

Document Style exchanges XML documents instead of procedure calls.

Example

```xml
<CustomerRequest>

<CustomerID>100</CustomerID>

</CustomerRequest>
```

Advantages

- Better interoperability
- Looser coupling
- Easier validation
- Enterprise preferred

Today, most enterprise SOAP services use **Document/Literal** style.

---

# Literal vs Encoded

SOAP also defines encoding styles.

Literal

```
XML follows Schema

↓

Exact Validation
```

Encoded

```
SOAP Encoding Rules

↓

Less Common Today
```

Document/Literal is considered the industry best practice.

---

# Message Exchange Pattern

```
Application

 │

Generate XML

 │

SOAP Envelope

 │

HTTP POST

 │

SOAP Server

 │

Business Logic

 │

SOAP Response

 │

Client
```

Every SOAP transaction follows this general flow.

---

# Enterprise SOAP Workflow

A banking transaction illustrates the complete lifecycle.

```
ATM

 │

SOAP Request

 ▼

API Gateway

 │

Authentication

 ▼

SOAP Service

 │

Fraud Detection

 ▼

Core Banking

 │

Transaction Database

 │

SOAP Response

 ▼

ATM
```

Each stage validates and processes the XML message before returning a response.

---

# Enterprise Design Principles

Well-designed SOAP services follow these principles:

- Strong contracts using WSDL
- Schema validation using XSD
- Document/Literal messaging
- Secure transport using HTTPS
- Versioned service contracts
- Loose coupling
- Consistent namespaces
- Comprehensive error handling
- Centralized authentication
- Detailed logging and monitoring

These practices improve interoperability and long-term maintainability.

---

# Common Mistakes

Avoid:

- Missing namespaces
- Invalid XML
- Ignoring schema validation
- Mixing business logic into transport details
- Using RPC style for complex enterprise integrations
- Hardcoding endpoint URLs
- Weak version management
- Poor WSDL documentation

---

# Key Takeaways

- XML namespaces uniquely identify XML elements and prevent naming conflicts.
- XML Schema (XSD) validates SOAP message structure and data types.
- WSDL acts as a formal, machine-readable contract describing SOAP services.
- SOAP supports multiple operation types, including Request-Response and One-Way messaging.
- Document/Literal messaging is the preferred style for enterprise interoperability.
- Strong contracts, schema validation, and standardized messaging are key strengths of SOAP-based systems.

---

# WS-Security

One of the biggest strengths of SOAP is its standardized security framework.

Unlike REST, which typically relies on HTTPS, JWT, OAuth 2.0, or API Gateways for security, SOAP includes an extensive specification called **WS-Security**.

WS-Security provides standardized mechanisms for:

- Authentication
- Authorization
- Confidentiality
- Integrity
- Non-repudiation
- Secure message exchange

It protects the **SOAP message itself**, not just the transport channel.

---

# What is WS-Security?

WS-Security (Web Services Security) is an extension to SOAP that adds security information to SOAP headers.

Instead of relying solely on HTTPS, security information travels inside the SOAP message.

Architecture

```
SOAP Message

│

├────────► Security Header

│              │

│              ├── Username Token

│              ├── Digital Signature

│              ├── Encryption

│              └── Timestamp

│

└────────► SOAP Body
```

This enables end-to-end security across multiple intermediaries.

---

# Why WS-Security?

HTTPS protects data **only while it travels across the network**.

```
Client

 │

HTTPS

 ▼

Gateway

 │

HTTP

 ▼

Application
```

If messages pass through intermediaries, encryption may terminate before reaching the final destination.

WS-Security protects the SOAP message itself.

```
SOAP Message

↓

Encrypted

↓

Gateway

↓

Still Encrypted

↓

SOAP Service
```

This provides **message-level security**.

---

# WS-Security Components

WS-Security consists of several security mechanisms.

```
WS-Security

│

├────────► Username Token

├────────► Binary Security Token

├────────► Digital Signature

├────────► XML Encryption

├────────► Timestamp

└────────► Security Token References
```

Each mechanism addresses different security requirements.

---

# Username Token

Username Tokens provide authentication credentials.

Example

```xml
<wsse:UsernameToken>

    <wsse:Username>Alice</wsse:Username>

    <wsse:Password>******</wsse:Password>

</wsse:UsernameToken>
```

Instead of transmitting plain-text passwords, secure implementations typically use password digests.

---

# Binary Security Tokens

Binary Security Tokens carry certificates.

Examples include:

- X.509 Certificates
- Kerberos Tickets
- SAML Tokens

Architecture

```
Client

 │

Certificate

 ▼

SOAP Header

 │

Server Validation
```

These tokens enable strong identity verification.

---

# XML Digital Signature

Digital signatures provide:

- Integrity
- Authentication
- Non-repudiation

Workflow

```
SOAP Message

 │

Generate Hash

 │

Private Key

 │

Digital Signature

 ▼

Transmit
```

The receiver verifies the signature using the sender's public key.

---

# Digital Signature Verification

```
Sender

 │

Private Key

 ▼

Sign Message

 │

SOAP

 ▼

Receiver

 │

Public Key

 ▼

Verify Signature
```

If the message changes during transit, signature verification fails.

---

# XML Encryption

Encryption protects sensitive message contents.

Example

```
Customer Data

↓

Encrypt

↓

SOAP Message

↓

Decrypt

↓

Receiver
```

Unlike HTTPS, XML Encryption allows only specific XML elements to be encrypted.

Example:

- Credit Card Number
- Account Balance
- Personal Information

while leaving the remainder of the message readable.

---

# Timestamp

Timestamps help prevent replay attacks.

Example

```xml
<wsu:Timestamp>

    <Created>

        2026-07-29T10:00:00Z

    </Created>

    <Expires>

        2026-07-29T10:05:00Z

    </Expires>

</wsu:Timestamp>
```

Expired messages are rejected.

---

# Security Token Reference

Security Token References identify authentication credentials.

Example

```
Certificate

↓

Security Token Reference

↓

SOAP Header
```

This avoids repeatedly transmitting certificates.

---

# WS-Security Workflow

```
Client

 │

Create SOAP Message

 │

Add Timestamp

 │

Add Username Token

 │

Sign XML

 │

Encrypt XML

 ▼

Transmit

 ▼

SOAP Server

 │

Decrypt

 │

Verify Signature

 │

Validate Token

 │

Process Request

 ▼

Response
```

This layered workflow ensures confidentiality, integrity, and authenticity.

---

# Message-Level Security

Unlike HTTPS, WS-Security protects individual message elements.

```
SOAP Envelope

│

├────────► Header

│

├────────► Encrypted Customer Data

│

├────────► Signed Payment Details

│

└────────► Timestamp
```

Even if the transport changes, protected elements remain secure.

---

# Transport-Level vs Message-Level Security

| Transport Security | Message Security |
|--------------------|------------------|
| HTTPS | WS-Security |
| Protects connection | Protects message |
| Session-based | End-to-end |
| Easier implementation | More complex |
| Lower overhead | Higher processing cost |
| Widely used | Enterprise-focused |

Many enterprise SOAP systems use **both** HTTPS and WS-Security together.

---

# SOAP Fault

SOAP provides standardized error handling using **SOAP Faults**.

Structure

```
SOAP Envelope

│

└────────► Fault
```

Faults communicate errors in a structured format.

---

# SOAP Fault Components

```
Fault

│

├────────► Code

├────────► Reason

├────────► Node

├────────► Role

└────────► Detail
```

Each element provides information about the error.

---

# SOAP Fault Example

```xml
<soap:Fault>

    <Code>

        soap:Sender

    </Code>

    <Reason>

        Invalid Customer ID

    </Reason>

</soap:Fault>
```

Clients can process these standardized responses programmatically.

---

# Common SOAP Fault Codes

| Fault Code | Meaning |
|------------|----------|
| VersionMismatch | Unsupported SOAP version |
| MustUnderstand | Required header missing |
| Sender | Client request error |
| Receiver | Server processing error |
| DataEncodingUnknown | Unsupported encoding |

These standardized fault codes improve interoperability.

---

# SOAP Security Threats

Although SOAP provides strong security capabilities, it is still vulnerable to attacks when improperly configured.

Common threats include:

- XML Injection
- XXE (XML External Entity)
- SOAP Injection
- Replay Attacks
- XML Signature Wrapping
- XML Bomb (Billion Laughs)
- Weak Authentication
- Broken Authorization
- Information Disclosure
- Insecure WSDL Exposure

Proper configuration and validation are essential.

---

# XML External Entity (XXE)

One of the most common SOAP vulnerabilities.

```
Attacker

 │

Malicious XML

 ▼

SOAP Parser

 │

Read Local File

 ▼

Sensitive Data
```

Mitigations:

- Disable external entities
- Disable DTD processing
- Use secure XML parsers
- Keep XML libraries updated

---

# XML Signature Wrapping

Attackers manipulate XML structure while preserving valid signatures.

Example

```
Original Signed Element

↓

Move Signed Element

↓

Insert Malicious Element

↓

Application Processes Wrong Data
```

Mitigation:

- Validate XML structure
- Verify signed elements
- Use secure XML libraries

---

# SOAP Injection

SOAP Injection is similar to other injection attacks.

Example

```
Malicious XML

↓

SOAP Parser

↓

Business Logic

↓

Unexpected Execution
```

Mitigations:

- Input validation
- Schema validation
- Parameterized database queries
- Output encoding

---

# Enterprise SOAP Security Architecture

```
                 Internet

                     │

                     ▼

             Web Application Firewall

                     │

                     ▼

                 API Gateway

                     │

                     ▼

              HTTPS + TLS 1.3

                     │

                     ▼

               SOAP Service

                     │

                     ▼

               WS-Security

         ┌──────────┼──────────┐

         ▼          ▼          ▼

 Authentication Encryption Signature

                     │

                     ▼

              Business Logic

                     │

                     ▼

                 Database

                     │

                     ▼

            Logging & Monitoring

                     │

                     ▼

                 SIEM / SOC
```

This layered architecture combines transport security, message security, and operational monitoring.

---

# REST vs SOAP

| Feature | REST | SOAP |
|----------|------|------|
| Type | Architectural Style | Protocol |
| Data Format | JSON, XML, YAML, etc. | XML Only |
| Performance | Lightweight | Heavier |
| Standardization | Flexible | Highly Standardized |
| WSDL | Optional | Required |
| Security | HTTPS, JWT, OAuth | WS-Security |
| Message Size | Small | Large |
| Caching | Native HTTP Support | Limited |
| Learning Curve | Easier | Steeper |
| Enterprise Integration | Excellent | Excellent |
| Mobile Friendly | Yes | Less Suitable |
| Formal Contracts | Optional | Built-in |

---

# When to Choose SOAP

SOAP is well suited for:

- Banking systems
- Insurance platforms
- Government services
- Healthcare integrations
- Enterprise ERP systems
- B2B integrations
- Regulatory environments
- Mission-critical transactions

Choose SOAP when:

- Strong contracts are required
- Advanced security is mandatory
- Reliable messaging is critical
- Formal standards are required

---

# Enterprise Case Study

A multinational insurance company integrates policy management systems across multiple countries.

Architecture

```
Insurance Portal

       │

       ▼

API Gateway

       │

       ▼

SOAP Service

       │

       ▼

WS-Security

       │

 ┌─────┼────────────┐

 ▼     ▼            ▼

Signature Encryption Timestamp

       │

       ▼

Policy Engine

       │

       ▼

Claims Database

       │

       ▼

Enterprise SIEM
```

Security Features

- HTTPS
- Mutual TLS
- X.509 Certificates
- XML Digital Signatures
- XML Encryption
- Timestamp Validation
- Centralized Logging
- Continuous Monitoring

This architecture enables secure, compliant communication between internal systems and external partners.

---

# Hands-on Lab 1 – Inspect a SOAP Message

Objective

Understand the structure of a SOAP request.

Steps

1. Capture a SOAP request using a proxy tool such as Burp Suite.
2. Identify:
   - Envelope
   - Header
   - Body
   - Namespaces
3. Determine whether WS-Security headers are present.

Learning Outcomes

- SOAP message anatomy
- XML parsing
- Security header identification

---

# Hands-on Lab 2 – Analyze a WSDL

Objective

Understand how SOAP services are documented.

Steps

1. Obtain a publicly available WSDL.
2. Identify:
   - Operations
   - Messages
   - Bindings
   - Service endpoint
3. Map one operation to its request and response structure.

Learning Outcomes

- WSDL interpretation
- Service contracts
- SOAP operation discovery

---

# Hands-on Lab 3 – Security Assessment

Objective

Identify common SOAP security controls.

Verify whether the service:

- Uses HTTPS
- Implements WS-Security
- Signs messages
- Encrypts sensitive elements
- Returns standardized SOAP Faults
- Protects against XXE

Document observations and recommend improvements.

---

# Common SOAP Security Mistakes

Avoid:

- Allowing XML External Entities (XXE)
- Missing schema validation
- Weak certificate management
- Unsigned messages
- Unencrypted sensitive data
- Exposing internal stack traces
- Outdated TLS versions
- Poor WSDL access controls
- Weak authentication
- Missing replay protection

---

# Troubleshooting

## Invalid SOAP Envelope

Possible causes:

- Malformed XML
- Missing namespace
- Incorrect SOAP version

---

## Authentication Failure

Possible causes:

- Invalid Username Token
- Expired certificate
- Incorrect credentials
- Missing WS-Security header

---

## Signature Validation Failure

Possible causes:

- Modified message
- Incorrect certificate
- Expired signing key
- Canonicalization mismatch

---

## XML Parsing Errors

Possible causes:

- Invalid XML
- Schema validation failure
- Unsupported encoding
- Namespace mismatch

---

## Service Unavailable

Possible causes:

- Endpoint unavailable
- Backend application failure
- Network connectivity issue
- Incorrect WSDL endpoint

---

# Interview Questions

## Fundamental

1. What is SOAP?
2. How does SOAP differ from REST?
3. What is a SOAP Envelope?
4. What is WSDL?
5. What is WS-Security?
6. Why does SOAP use XML?
7. What is a SOAP Fault?
8. What is the purpose of XML namespaces?
9. What is the difference between transport-level and message-level security?
10. Why is Document/Literal preferred over RPC style?

---

## Intermediate

11. Explain the components of a WSDL document.
12. How does XML Digital Signature work?
13. What is XML Encryption?
14. Why are timestamps important in WS-Security?
15. Explain XML Schema validation.
16. What is XML Signature Wrapping?
17. How would you secure a SOAP web service?
18. Why is SOAP still used in enterprise environments?
19. Compare SOAP Faults with HTTP status codes.
20. What security controls would you implement for a public SOAP service?

---

## Scenario-Based

**Scenario 1**

A banking SOAP service begins rejecting valid requests with signature verification errors.

- Which parts of the WS-Security implementation would you investigate first?
- How would you determine whether the issue is related to certificates, canonicalization, or message modification?

---

**Scenario 2**

During a security assessment, you discover that the SOAP parser accepts external entities.

- What are the associated risks?
- Which parser configurations would you change to mitigate the issue?

---

**Scenario 3**

A legacy enterprise application must integrate securely with an external partner using SOAP.

- Which WS-Security features would you enable?
- How would you protect both the transport channel and the SOAP message itself?

---

# Chapter Summary

In this chapter, we explored SOAP as a protocol for enterprise web services.

We covered:

- SOAP fundamentals
- XML namespaces
- SOAP message structure
- WSDL
- SOAP operations
- Document and RPC styles
- WS-Security
- XML Digital Signatures
- XML Encryption
- SOAP Faults
- Enterprise security architecture
- SOAP security threats
- REST vs SOAP comparison
- Hands-on exercises
- Troubleshooting
- Interview preparation

Although REST dominates modern public APIs, SOAP remains an essential technology in many enterprise environments where security, reliability, formal contracts, and interoperability are critical.

---

# Chapter Review

You should now be able to answer:

- What is SOAP and how does it differ from REST?
- How are SOAP messages structured?
- What role do XML namespaces and WSDL play?
- How does WS-Security protect SOAP messages?
- What is the difference between transport-level and message-level security?
- How do SOAP Faults communicate errors?
- What are the most common SOAP security threats?
- How would you secure an enterprise SOAP service?
- When should SOAP be chosen instead of REST?
- How would you troubleshoot common SOAP issues?

If you can confidently explain these topics, you are ready to continue to GraphQL and understand how its architecture, flexibility, and security model differ from both REST and SOAP.

---

# References

## Standards

- SOAP 1.2 Specification (W3C)
- Web Services Description Language (WSDL) 2.0
- WS-Security 1.1
- XML Signature Syntax and Processing
- XML Encryption Syntax and Processing
- XML Schema Definition (XSD)

## Security Standards

- OWASP API Security Top 10
- OWASP Web Security Testing Guide (WSTG)
- NIST Cybersecurity Framework (CSF)
- NIST SP 800-53
- NIST SP 800-204

## Further Reading

- W3C SOAP Specifications
- W3C XML Namespaces
- W3C XML Schema
- WS-I Basic Profile
- OASIS WS-Security Specifications

---

# What's Next?

➡️ **Chapter 05 – GraphQL Security**

In the next chapter, we will explore:

- GraphQL architecture
- Queries, mutations, and subscriptions
- Schema and type system
- Resolvers
- Introspection
- Authentication and authorization
- GraphQL-specific attack vectors
- Security best practices
- Enterprise deployments
- Hands-on labs and interview questions