# 15-PowerShell-and-Scripting.md

# Part 1 — PowerShell Fundamentals, Architecture, Syntax, Cmdlets, Pipeline, Objects, and Basic Scripting

---

# Introduction

PowerShell is Microsoft's modern command-line shell and scripting language built on the **.NET platform**. It is designed specifically for system administration, automation, configuration management, cloud administration, cybersecurity, and DevOps.

Unlike traditional command-line interpreters that work primarily with plain text, PowerShell works with **objects**.

PowerShell is one of the most important skills for:

- Windows Administrators
- System Engineers
- SOC Analysts
- Incident Responders
- Cloud Engineers
- DevOps Engineers
- Penetration Testers
- Security Engineers

Almost every enterprise Windows environment relies on PowerShell for automation.

---

# Learning Objectives

By the end of this section, you will understand:

- What PowerShell is
- Windows PowerShell vs PowerShell
- PowerShell architecture
- Console basics
- Cmdlets
- Modules
- Aliases
- Variables
- Objects
- Pipeline
- Help system
- Basic scripting
- PowerShell security fundamentals

---

# What is PowerShell?

PowerShell is:

- A command-line shell
- A scripting language
- An automation framework
- A configuration management tool

It allows administrators to manage:

- Windows
- Active Directory
- Azure
- Microsoft 365
- Hyper-V
- Exchange
- SQL Server
- File systems
- Processes
- Services
- Networking

---

# Why PowerShell is Important

Enterprise administrators may manage:

- Hundreds of servers
- Thousands of endpoints
- Millions of files
- Hundreds of user accounts

Manual administration becomes impossible.

PowerShell enables:

```text
Administrator

↓

PowerShell Script

↓

Thousands of Computers

↓

Automated Tasks
```

Automation saves time, improves consistency, and reduces human error.

---

# Windows PowerShell vs PowerShell

| Windows PowerShell | PowerShell |
|--------------------|------------|
| Built on .NET Framework | Built on .NET |
| Windows only | Cross-platform |
| Version 5.1 | Version 7+ |
| Legacy administration | Modern administration |

Modern environments increasingly adopt PowerShell 7 while maintaining compatibility with Windows PowerShell where required.

---

# PowerShell Architecture

```text
Administrator

↓

PowerShell Console

↓

PowerShell Engine

↓

Cmdlets

↓

.NET

↓

Windows Operating System
```

PowerShell uses the .NET runtime to expose Windows functionality through consistent commands.

---

# Starting PowerShell

Common methods:

```text
Start Menu

↓

PowerShell
```

or

```text
Windows Terminal

↓

PowerShell
```

or

```text
Win + X

↓

Windows PowerShell
```

Running PowerShell as Administrator is required for many system-level operations.

---

# Interactive Shell

PowerShell can execute commands interactively.

Example:

```powershell
Get-Date
```

Output:

```text
Thursday, July 30, 2026
```

Interactive mode is useful for administration and troubleshooting.

---

# What is a Cmdlet?

A **cmdlet** (pronounced *command-let*) is a lightweight PowerShell command.

Naming convention:

```text
Verb-Noun
```

Examples:

```powershell
Get-Process

Get-Service

Get-ChildItem

Stop-Service

Restart-Computer
```

The consistent naming convention makes PowerShell easier to learn.

---

# Approved Verbs

PowerShell uses standardized verbs.

Examples:

| Verb | Purpose |
|-------|----------|
| Get | Retrieve information |
| Set | Modify information |
| New | Create |
| Remove | Delete |
| Start | Start a resource |
| Stop | Stop a resource |
| Restart | Restart |
| Test | Validate |
| Enable | Enable functionality |
| Disable | Disable functionality |

Using approved verbs improves script readability and consistency.

---

# Nouns

The noun identifies the resource being managed.

Examples:

```powershell
Get-Service

Get-Process

Get-EventLog

Get-NetAdapter

Get-Help
```

Together, the verb and noun clearly describe the action.

---

# Discovering Commands

Find commands:

```powershell
Get-Command
```

Search for process-related commands:

```powershell
Get-Command *process*
```

Search for networking commands:

```powershell
Get-Command *net*
```

This is often the first step when learning a new module.

---

# Getting Help

PowerShell includes an extensive help system.

View help:

```powershell
Get-Help Get-Service
```

View examples:

```powershell
Get-Help Get-Service -Examples
```

Open the online documentation:

```powershell
Get-Help Get-Service -Online
```

---

# Updating Help

Download the latest help files:

```powershell
Update-Help
```

Administrative privileges and Internet access may be required.

Keeping help files current ensures access to the latest documentation.

---

# PowerShell Modules

Modules package related cmdlets.

Examples:

- Microsoft.PowerShell.Management
- Microsoft.PowerShell.Utility
- NetTCPIP
- Hyper-V
- ActiveDirectory

List installed modules:

```powershell
Get-Module -ListAvailable
```

Modules extend PowerShell's capabilities.

---

# Importing Modules

Load a module manually:

```powershell
Import-Module Hyper-V
```

PowerShell often imports modules automatically when needed.

---

# Aliases

Aliases are shortcuts for cmdlets.

Examples:

| Alias | Cmdlet |
|--------|---------|
| ls | Get-ChildItem |
| dir | Get-ChildItem |
| pwd | Get-Location |
| cat | Get-Content |
| ps | Get-Process |

View aliases:

```powershell
Get-Alias
```

Although convenient interactively, full cmdlet names are recommended in production scripts.

---

# Variables

Variables store information.

Example:

```powershell
$name = "Alice"
```

Display the value:

```powershell
$name
```

Variables begin with the `$` symbol.

---

# Variable Examples

Store numbers:

```powershell
$count = 10
```

Store strings:

```powershell
$city = "Bangalore"
```

Store dates:

```powershell
$today = Get-Date
```

Variables can also store complex objects.

---

# Comments

Single-line comment:

```powershell
# This is a comment
```

Multi-line comment:

```powershell
<#
This script
contains
multiple comments.
#>
```

Comments improve readability and maintainability.

---

# Objects

Unlike traditional shells, PowerShell works with **objects**, not plain text.

Example:

```powershell
Get-Process
```

Returns process objects containing properties such as:

- ProcessName
- Id
- CPU
- WorkingSet
- StartTime (when available)

Objects enable powerful filtering and automation.

---

# Properties

Display object properties:

```powershell
Get-Process | Get-Member
```

Sample properties:

```text
Name

Id

CPU

HandleCount

WorkingSet
```

Understanding object properties is fundamental to effective scripting.

---

# Methods

Objects also contain methods.

Example:

```powershell
Get-Service | Get-Member
```

Methods represent actions an object can perform.

Examples include:

- Start()
- Stop()
- Refresh()

Availability depends on the object type.

---

# The Pipeline

The pipeline (`|`) passes objects from one command to another.

```powershell
Command A

↓

Pipeline

↓

Command B
```

This is one of PowerShell's most powerful features.

---

# Pipeline Example

```powershell
Get-Service | Sort-Object Status
```

Workflow:

```text
Get Services

↓

Pass Objects

↓

Sort Results
```

Objects retain their properties throughout the pipeline.

---

# Selecting Data

Display selected properties:

```powershell
Get-Process |
Select-Object Name, Id
```

Output is easier to read and focuses on relevant information.

---

# Sorting Data

Example:

```powershell
Get-Process |
Sort-Object CPU -Descending
```

This lists processes using the most CPU time first.

---

# Filtering Data

Filter running services:

```powershell
Get-Service |
Where-Object Status -eq Running
```

Filtering reduces unnecessary output and improves script efficiency.

---

# Formatting Output

Display information as a table:

```powershell
Get-Service |
Format-Table
```

Display information as a list:

```powershell
Get-Service |
Format-List
```

Formatting is intended for display, not further processing.

---

# Redirecting Output

Save output to a file:

```powershell
Get-Service >
services.txt
```

Append to an existing file:

```powershell
Get-Service >>
services.txt
```

Output redirection is useful for reporting and documentation.

---

# Running Scripts

PowerShell scripts use the extension:

```text
.ps1
```

Example:

```powershell
.\Inventory.ps1
```

Scripts can automate repetitive administrative tasks.

---

# Execution Policy

PowerShell includes an execution policy to help prevent accidental script execution.

View the current policy:

```powershell
Get-ExecutionPolicy
```

Common policies include:

| Policy | Description |
|---------|-------------|
| Restricted | No script execution |
| RemoteSigned | Local scripts allowed; downloaded scripts require a trusted signature |
| AllSigned | All scripts must be signed |
| Unrestricted | Scripts allowed with minimal restrictions |

Execution Policy is **not** a security boundary; it is a safety feature.

---

# Enterprise Example

A systems administrator needs to verify that a critical service is running on multiple servers.

Instead of manually checking each server:

```text
Administrator

↓

PowerShell Script

↓

Check Services

↓

Generate Report

↓

Email Results
```

Automation reduces manual effort and provides consistent reporting.

---

# Cybersecurity Perspective

PowerShell is widely used by:

- Blue Teams
- Red Teams
- Incident Responders
- Threat Hunters
- System Administrators

Legitimate uses include:

- Log collection
- System inventory
- Security auditing
- Automation
- Configuration management

Because PowerShell is powerful, attackers may also abuse it. Organizations should implement logging, monitoring, and least-privilege controls.

---

# Business Impact

PowerShell enables organizations to:

- Reduce administrative effort
- Improve operational consistency
- Standardize deployments
- Automate repetitive tasks
- Improve reporting
- Reduce human error

Automation increases efficiency and scalability across enterprise environments.

---

# Enterprise Best Practices

- Use full cmdlet names in production scripts.
- Include comments and documentation.
- Store scripts in version control.
- Test scripts in non-production environments.
- Validate user input.
- Use the help system frequently.
- Apply the Principle of Least Privilege.
- Enable PowerShell logging in enterprise environments.

---

# Practical Labs

## Lab 1 — Explore Available Cmdlets

Run:

```powershell
Get-Command
```

Then search for:

```powershell
Get-Command *service*
```

Identify at least five service-related cmdlets.

---

## Lab 2 — Explore Objects

Run:

```powershell
Get-Process | Get-Member
```

Identify:

- Properties
- Methods

Observe how PowerShell represents process information as objects.

---

## Lab 3 — Practice the Pipeline

Run:

```powershell
Get-Service |
Where-Object Status -eq Running |
Sort-Object Name
```

Review the filtered and sorted output.

---

## Lab 4 — Use the Help System

Run:

```powershell
Get-Help Get-Process -Examples
```

Study the provided examples and experiment with one in a test environment.

---

# Key Takeaways

- PowerShell is Microsoft's automation and scripting platform.
- Cmdlets follow a consistent Verb-Noun naming convention.
- PowerShell processes objects rather than plain text.
- The pipeline is central to combining commands.
- Modules extend PowerShell functionality.
- Execution Policy helps prevent accidental script execution but is not a security boundary.
- Automation improves efficiency, consistency, and scalability.

---

# Interview Questions

1. What is PowerShell?
2. What is the difference between Windows PowerShell and PowerShell 7?
3. What is a cmdlet?
4. Explain the Verb-Noun naming convention.
5. What is the PowerShell pipeline?
6. Why are PowerShell objects more powerful than plain text?
7. What is the purpose of `Get-Help`?
8. What are PowerShell modules?
9. What is an execution policy?
10. Why should production scripts use full cmdlet names instead of aliases?

---

# References

- Microsoft Learn
- Microsoft PowerShell Documentation
- Microsoft PowerShell Gallery
- PowerShell Team Blog
- *PowerShell in Action* (Bruce Payette)
- *Learn PowerShell in a Month of Lunches* (Don Jones & Jeff Hicks)

---

**Next:** **Part 2 — Variables, Data Types, Operators, Control Flow, Functions, Error Handling, and Advanced Scripting**