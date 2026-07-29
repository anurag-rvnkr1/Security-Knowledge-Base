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

**Next:** XML Namespaces, WSDL, SOAP Operations, RPC vs Document Style, Message Exchange Patterns, and Enterprise SOAP Service Design.