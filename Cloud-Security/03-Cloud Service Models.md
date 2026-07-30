# 03 - Cloud Service Models

# Introduction

Cloud computing has revolutionized the way organizations consume technology. Rather than purchasing expensive hardware, installing operating systems, maintaining physical infrastructure, and managing every component manually, organizations can now consume IT resources as services.

These services are known as **Cloud Service Models**.

A cloud service model defines:

- What services the cloud provider offers.
- Which infrastructure components the provider manages.
- Which responsibilities remain with the customer.
- The level of control the customer has.
- The amount of operational effort required.
- The security responsibilities of both parties.

Choosing the appropriate service model is one of the most important architectural decisions made by organizations because it directly affects:

- Cost
- Scalability
- Security
- Compliance
- Performance
- Flexibility
- Operational overhead
- Disaster Recovery
- Automation
- Governance

Every cloud platform—including AWS, Microsoft Azure, Google Cloud Platform (GCP), Oracle Cloud Infrastructure (OCI), IBM Cloud, and Alibaba Cloud—offers multiple service models designed to meet different business needs.

Understanding these models is fundamental before learning advanced cloud security concepts because the **security responsibilities change depending on the chosen service model**.

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand Cloud Service Models.
- Differentiate between IaaS, PaaS, SaaS, FaaS, and BaaS.
- Learn enterprise use cases for each model.
- Understand advantages and disadvantages.
- Learn security responsibilities.
- Compare operational responsibilities.
- Understand pricing models.
- Learn real-world enterprise deployments.
- Understand architectural decision-making.
- Build a foundation for the Shared Responsibility Model.

---

# Why Cloud Service Models Exist

Not every organization has identical requirements.

Consider three different organizations.

### Organization A

A startup wants to launch a website quickly.

They do not want to manage:

- Servers
- Databases
- Networking
- Operating systems

Instead, they simply want a platform where they can upload their application.

---

### Organization B

A cybersecurity company requires complete control over its infrastructure.

It wants to:

- Configure custom firewalls
- Install intrusion detection systems
- Deploy specialized software
- Tune operating systems
- Perform penetration testing

This organization needs maximum flexibility.

---

### Organization C

A university simply wants employees to use email and office productivity software.

It has no interest in managing:

- Servers
- Databases
- Storage
- Updates
- Security patches

Instead, it simply wants to subscribe to a service.

---

Each organization has different operational needs.

Cloud Service Models allow providers to satisfy these different requirements.

---

# Evolution of IT Services

Cloud service models evolved over several decades.

```
Traditional Computing

↓

Virtualization

↓

Infrastructure as a Service

↓

Platform as a Service

↓

Software as a Service

↓

Serverless Computing

↓

Cloud Native Services
```

As cloud technology matured, providers assumed greater operational responsibility, allowing customers to focus increasingly on their business objectives.

---

# Overview of Cloud Service Models

Modern cloud computing generally consists of five major service models.

```
+------------------------------------------------------+
| Software as a Service (SaaS)                         |
+------------------------------------------------------+
| Platform as a Service (PaaS)                         |
+------------------------------------------------------+
| Infrastructure as a Service (IaaS)                   |
+------------------------------------------------------+
| Physical Infrastructure                              |
+------------------------------------------------------+
```

Modern cloud providers have expanded beyond these traditional models to include:

- Function as a Service (FaaS)
- Backend as a Service (BaaS)
- Container as a Service (CaaS)
- Database as a Service (DBaaS)
- AI as a Service (AIaaS)

These specialized services are built upon the core service models.

---

# The Cloud Responsibility Stack

Before discussing individual service models, it is important to understand the layers involved in delivering cloud services.

```
Applications

↓

Data

↓

Runtime

↓

Middleware

↓

Operating System

↓

Virtualization

↓

Servers

↓

Storage

↓

Networking
```

Each service model determines who is responsible for securing and managing these layers.

---

# Categories of Cloud Service Models

Cloud services can generally be categorized according to how much control is provided to customers.

| Service Model | Customer Control | Operational Effort |
|---------------|-----------------|--------------------|
| On-Premises | Very High | Very High |
| IaaS | High | High |
| PaaS | Medium | Medium |
| CaaS | Medium | Medium |
| FaaS | Low | Low |
| SaaS | Very Low | Very Low |

As operational responsibility decreases, provider responsibility increases.

---

# Understanding the Service Model Pyramid

```
             SaaS

              ▲

             PaaS

              ▲

             CaaS

              ▲

             IaaS

              ▲

      Physical Infrastructure
```

Moving upward:

- Less infrastructure management
- Faster deployment
- Less customization
- Lower operational overhead

Moving downward:

- More flexibility
- Greater administrative control
- Higher security responsibility
- Greater operational complexity

---

# What is Infrastructure as a Service (IaaS)?

Infrastructure as a Service provides virtualized computing infrastructure over the internet.

Instead of purchasing physical hardware, customers rent virtual infrastructure.

Typical IaaS services include:

- Virtual Machines
- Virtual Networks
- Firewalls
- Storage
- Load Balancers
- IP Addresses
- VPN Gateways
- DNS
- Snapshots

Customers manage the operating system and everything above it.

---

# IaaS Architecture

```
Customer

│

Applications

│

Runtime

│

Operating System

────────────────────────

Cloud Provider

────────────────────────

Hypervisor

Servers

Storage

Networking

Physical Data Center
```

The customer has significant flexibility but also significant responsibility.

---

# Characteristics of IaaS

Infrastructure as a Service provides:

- Virtualized infrastructure
- Root administrative access
- Custom operating systems
- Flexible networking
- Elastic scaling
- Consumption-based billing
- High customization

This model resembles traditional data centers but eliminates the need to own physical hardware.

---

# IaaS Example Workflow

```
Developer

↓

Cloud Portal

↓

Launch VM

↓

Install Linux

↓

Configure Firewall

↓

Install Database

↓

Deploy Application

↓

Production
```

Every software component above virtualization is managed by the customer.

---

# Advantages of IaaS

Organizations choose IaaS because it offers:

- Maximum flexibility
- Complete OS control
- Custom networking
- Legacy application support
- Full administrative access
- Support for specialized software
- Better migration from on-premises environments

IaaS is particularly suitable for organizations that require extensive infrastructure customization.

---

# Limitations of IaaS

Although flexible, IaaS requires customers to manage many operational tasks.

Examples include:

- OS patching
- Security hardening
- Malware protection
- Backup configuration
- Monitoring
- Log management
- User management
- Vulnerability remediation

Failure to perform these tasks can lead to security incidents.

---

# Common IaaS Services

Examples include:

- Virtual Machines
- Elastic Compute
- Managed Networking
- Virtual Firewalls
- Virtual Routers
- Block Storage
- Object Storage
- Virtual Private Clouds

Every major cloud provider offers these capabilities under different product names.

---

# Real-World IaaS Use Cases

Organizations commonly use IaaS for:

- Enterprise applications
- Legacy software migration
- ERP systems
- Security laboratories
- Penetration testing environments
- Development environments
- Disaster recovery
- High-performance computing

Cybersecurity professionals frequently use IaaS because it provides low-level infrastructure control.

---

# Security Responsibilities in IaaS

Customer responsibilities typically include:

- Operating systems
- Applications
- User accounts
- IAM policies
- Firewalls
- Data encryption
- Patch management
- Endpoint protection

The cloud provider is responsible for:

- Physical infrastructure
- Networking hardware
- Hypervisors
- Storage hardware
- Physical security

This division of responsibilities is explored in depth in Chapter 06.

---

# What is Platform as a Service (PaaS)?

Platform as a Service provides a managed application platform.

Instead of managing operating systems and infrastructure, customers focus on developing and deploying applications.

The provider manages:

- Servers
- Operating systems
- Runtime environments
- Middleware
- Scaling
- Infrastructure maintenance

Customers manage only:

- Applications
- Business logic
- Data
- Configurations

---

# PaaS Architecture

```
Customer

│

Application

Data

────────────────────────

Cloud Provider

────────────────────────

Runtime

Middleware

Operating System

Virtualization

Servers

Storage

Networking
```

PaaS accelerates software development by reducing operational complexity.

---

# Why PaaS is Popular

Developers can deploy applications without worrying about infrastructure.

Typical workflow:

```
Write Code

↓

Push Code

↓

Cloud Platform

↓

Automatic Build

↓

Deployment

↓

Application Online
```

This significantly shortens development cycles.

---

# Advantages of PaaS

- Faster development
- Automatic scaling
- Managed operating systems
- Built-in monitoring
- Simplified deployments
- Reduced operational effort
- Integrated development tools

PaaS enables developers to focus primarily on application functionality.

---

# Limitations of PaaS

Potential disadvantages include:

- Less operating system control
- Limited customization
- Vendor-specific features
- Platform lock-in
- Restricted administrative access

Organizations requiring extensive system-level customization may prefer IaaS.

---

# Common PaaS Use Cases

PaaS is widely used for:

- Web applications
- REST APIs
- Enterprise portals
- Mobile backends
- SaaS products
- Microservices
- Internal business applications

---

# Security Considerations for PaaS

Although infrastructure management is reduced, customers remain responsible for securing:

- Application code
- User authentication
- Authorization
- APIs
- Secrets
- Sensitive data
- Business logic

Application security remains critical regardless of the underlying platform.

---

# Key Takeaways

- Cloud Service Models define how computing resources are delivered and how responsibilities are divided between the cloud provider and the customer.
- Infrastructure as a Service (IaaS) offers maximum flexibility and control but requires customers to manage operating systems, applications, and much of the security stack.
- Platform as a Service (PaaS) abstracts infrastructure management, enabling developers to focus on building and deploying applications while the provider manages the underlying platform.
- The choice of service model directly influences operational complexity, customization, scalability, and security responsibilities.
- Understanding these foundational service models is essential before exploring Software as a Service (SaaS), Function as a Service (FaaS), Backend as a Service (BaaS), Container as a Service (CaaS), and the Shared Responsibility Model in the following sections.

---

