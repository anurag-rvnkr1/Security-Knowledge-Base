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

# 15-Windows-PowerShell-and-Scripting.md

# Part 2 — Variables, Data Types, Operators, Control Flow, Functions, Error Handling, and Advanced Scripting

---

# Introduction

PowerShell becomes truly powerful when commands are combined into reusable scripts.

Instead of manually executing hundreds of commands, administrators can write scripts that:

- Automate repetitive tasks
- Configure systems
- Generate reports
- Monitor infrastructure
- Manage Active Directory
- Collect logs
- Perform security audits

This section introduces the core scripting concepts required to build reliable PowerShell automation.

---

# Script Execution Flow

A PowerShell script generally follows this workflow.

```text
Start

↓

Read Input

↓

Process Data

↓

Decision Making

↓

Execute Commands

↓

Display or Save Results

↓

End
```

Understanding this flow helps in designing readable and maintainable scripts.

---

# Variables

Variables store values in memory.

Syntax:

```powershell
$VariableName = Value
```

Examples:

```powershell
$Name = "John"

$Age = 25

$Enabled = $true
```

Variables can hold almost any .NET object.

---

# Variable Naming

Good naming conventions improve readability.

Good examples:

```powershell
$ComputerName

$ServiceStatus

$IPAddress

$LogPath
```

Poor examples:

```powershell
$x

$a

$temp1

$abc
```

Meaningful names make scripts easier to maintain.

---

# Displaying Variables

```powershell
$User = "Alice"

Write-Output $User
```

Output:

```text
Alice
```

Variables can also be embedded within strings.

```powershell
"Current User: $User"
```

---

# Variable Scope

Variables exist within different scopes.

| Scope | Description |
|--------|-------------|
| Local | Current function or script |
| Script | Entire script |
| Global | Current PowerShell session |
| Private | Accessible only within the current scope |

Example:

```powershell
$Global:Company = "Contoso"
```

Use broader scopes only when necessary.

---

# Built-in Variables

Common automatic variables include:

| Variable | Description |
|----------|-------------|
| `$PSVersionTable` | PowerShell version information |
| `$HOME` | User profile directory |
| `$PWD` | Current working directory |
| `$Error` | Error collection |
| `$True` | Boolean true |
| `$False` | Boolean false |
| `$Null` | Null value |

Example:

```powershell
$PSVersionTable
```

---

# Data Types

PowerShell supports many data types.

Common examples:

| Type | Example |
|------|----------|
| String | `"Windows"` |
| Integer | `100` |
| Double | `10.25` |
| Boolean | `$true` |
| DateTime | `Get-Date` |
| Array | `@(1,2,3)` |
| Hashtable | `@{}` |

PowerShell automatically converts types when appropriate.

---

# Strings

```powershell
$Message = "Hello World"
```

Access length:

```powershell
$Message.Length
```

Concatenate strings:

```powershell
$First = "Windows"

$Second = "PowerShell"

"$First $Second"
```

---

# Numbers

```powershell
$A = 10

$B = 5
```

Arithmetic:

```powershell
$A + $B

$A - $B

$A * $B

$A / $B
```

---

# Arrays

Arrays store multiple values.

```powershell
$Servers = @(
"DC01",
"WEB01",
"SQL01"
)
```

Access an element:

```powershell
$Servers[0]
```

Count elements:

```powershell
$Servers.Count
```

---

# Hashtables

Hashtables store key-value pairs.

```powershell
$Employee = @{
Name = "Alice"
Department = "Finance"
City = "Bangalore"
}
```

Retrieve a value:

```powershell
$Employee.Name
```

Hashtables are frequently used for configuration data.

---

# Operators

PowerShell supports several categories of operators.

| Category | Examples |
|-----------|----------|
| Arithmetic | `+ - * / %` |
| Assignment | `=` `+=` |
| Comparison | `-eq` `-ne` |
| Logical | `-and` `-or` |
| Matching | `-like` `-match` |

---

# Comparison Operators

| Operator | Meaning |
|----------|---------|
| `-eq` | Equal |
| `-ne` | Not Equal |
| `-gt` | Greater Than |
| `-lt` | Less Than |
| `-ge` | Greater Than or Equal |
| `-le` | Less Than or Equal |

Example:

```powershell
5 -gt 3
```

Returns:

```text
True
```

---

# Logical Operators

Examples:

```powershell
$true -and $true

$true -or $false

-not $false
```

Logical operators combine multiple conditions.

---

# If Statement

Basic syntax:

```powershell
if ($Condition)
{
    Commands
}
```

Example:

```powershell
$Age = 20

if ($Age -ge 18)
{
    "Adult"
}
```

---

# If-Else Statement

```powershell
if ($Status -eq "Running")
{
    "Service is running"
}
else
{
    "Service is stopped"
}
```

This allows scripts to take different actions based on conditions.

---

# ElseIf

```powershell
if ($Score -ge 90)
{
    "Grade A"
}
elseif ($Score -ge 75)
{
    "Grade B"
}
else
{
    "Grade C"
}
```

Useful when multiple conditions must be evaluated.

---

# Switch Statement

`switch` simplifies evaluation of multiple possible values.

Example:

```powershell
switch ($Day)
{
    "Monday" { "Start of Week" }
    "Friday" { "Weekend Soon" }
    Default  { "Regular Day" }
}
```

---

# Loops

PowerShell supports several loop types.

| Loop | Purpose |
|------|----------|
| For | Known number of iterations |
| Foreach | Iterate through a collection |
| While | Repeat while condition is true |
| Do-While | Execute at least once |

---

# For Loop

```powershell
for ($i = 1; $i -le 5; $i++)
{
    $i
}
```

Output:

```text
1
2
3
4
5
```

---

# Foreach Loop

```powershell
$Servers = @("DC01","WEB01","SQL01")

foreach ($Server in $Servers)
{
    $Server
}
```

`foreach` is one of the most frequently used loops in administrative scripts.

---

# While Loop

```powershell
$i = 1

while ($i -le 5)
{
    $i
    $i++
}
```

The condition is checked before each iteration.

---

# Do-While Loop

```powershell
$i = 1

do
{
    $i
    $i++
}
while ($i -le 5)
```

The loop executes at least once, regardless of the condition.

---

# Functions

Functions package reusable code.

Basic syntax:

```powershell
function Get-Greeting
{
    "Hello"
}
```

Call the function:

```powershell
Get-Greeting
```

---

# Function Parameters

```powershell
function Get-Welcome
{
    param(
        $Name
    )

    "Welcome $Name"
}
```

Usage:

```powershell
Get-Welcome "Alice"
```

Parameters make functions flexible and reusable.

---

# Returning Values

```powershell
function Get-Square
{
    param($Number)

    return ($Number * $Number)
}
```

Example:

```powershell
Get-Square 5
```

Returns:

```text
25
```

---

# Script Parameters

Scripts can also accept parameters.

Example:

```powershell
param(
    $ComputerName
)

Get-Service -ComputerName $ComputerName
```

Execute:

```powershell
.\ServiceCheck.ps1 -ComputerName DC01
```

---

# Error Handling

Unexpected errors occur in automation.

Examples:

- Missing files
- Permission issues
- Offline computers
- Invalid user input
- Network failures

Proper error handling makes scripts more reliable.

---

# Try-Catch

```powershell
try
{
    Get-Content "C:\Data\File.txt"
}
catch
{
    "An error occurred."
}
```

`try` contains code that may fail.

`catch` handles exceptions gracefully.

---

# Finally Block

```powershell
try
{
    Commands
}
catch
{
    Error Handling
}
finally
{
    Cleanup
}
```

The `finally` block executes whether an error occurs or not.

---

# Throw

Generate a custom error.

```powershell
throw "Invalid Input"
```

Useful for validating user input and enforcing business logic.

---

# Error Variable

View recent errors:

```powershell
$Error
```

Most recent error:

```powershell
$Error[0]
```

The `$Error` collection helps troubleshoot script failures.

---

# Reading User Input

```powershell
$Name = Read-Host "Enter Name"
```

Example:

```text
Enter Name:
```

The entered value is stored in `$Name`.

---

# Writing Output

Display information:

```powershell
Write-Output "Completed"
```

Display informational messages:

```powershell
Write-Host "Starting..."
```

For scripts intended to be reused or piped into other commands, prefer `Write-Output` over `Write-Host`.

---

# Reading Files

Read a text file:

```powershell
Get-Content C:\Logs\App.log
```

Each line becomes an object in the output collection.

---

# Writing Files

Write content:

```powershell
Set-Content Report.txt "Completed"
```

Append content:

```powershell
Add-Content Report.txt "Finished Successfully"
```

---

# Enterprise Example

A systems administrator needs to verify disk space on multiple servers.

Workflow:

```text
Read Server List

↓

Loop Through Servers

↓

Collect Disk Usage

↓

Handle Errors

↓

Generate Report

↓

Save Results
```

This approach automates a repetitive operational task.

---

# Cybersecurity Perspective

PowerShell scripts are frequently used to:

- Collect forensic artifacts
- Audit local users
- Review running services
- Enumerate installed software
- Check security configurations
- Generate compliance reports

Security teams should ensure scripts include proper validation, logging, and error handling.

---

# Business Impact

Well-written PowerShell scripts provide:

- Consistent administration
- Reduced operational effort
- Faster deployments
- Improved reporting
- Lower risk of manual errors
- Better scalability

Reusable automation contributes to operational efficiency across the enterprise.

---

# Enterprise Best Practices

- Use descriptive variable names.
- Modularize scripts using functions.
- Validate input before processing.
- Implement `try/catch` for expected failures.
- Avoid hard-coded values where possible.
- Store configuration separately from code.
- Include comments and documentation.
- Test scripts in a non-production environment.

---

# Practical Labs

## Lab 1 — Create Variables

Write a script that stores:

- Computer name
- Current date
- Logged-on username

Display all values.

---

## Lab 2 — Practice Loops

Create an array containing five server names.

Use a `foreach` loop to display each name.

---

## Lab 3 — Build a Function

Create a function that accepts a username and displays:

```text
Welcome <username>
```

Test it with multiple values.

---

## Lab 4 — Handle Errors

Write a script that attempts to read a file that does not exist.

Use `try/catch` to display a friendly error message instead of terminating unexpectedly.

---

# Key Takeaways

- Variables store data and objects.
- Arrays and hashtables organize collections of information.
- Conditional statements control script execution.
- Loops automate repetitive tasks.
- Functions promote code reuse and readability.
- Error handling improves script reliability.
- Input validation and modular design are essential for enterprise automation.

---

# Interview Questions

1. What is the difference between an array and a hashtable?
2. What are PowerShell automatic variables?
3. Explain the purpose of `foreach`.
4. When would you use a `switch` statement instead of multiple `if` statements?
5. What is the purpose of a function?
6. How do script parameters improve reusability?
7. Explain `try`, `catch`, and `finally`.
8. What does `throw` do?
9. What is the difference between `Write-Host` and `Write-Output`?
10. Why should enterprise scripts validate user input?

---

# References

- Microsoft Learn
- Microsoft PowerShell Documentation
- PowerShell Language Specification
- *PowerShell in Action* (Bruce Payette)
- *Learn PowerShell Scripting in a Month of Lunches* (Don Jones & Jeff Hicks)

---

**Next:** **Part 3 — PowerShell Remoting, CIM/WMI, Jobs, Modules, Security, Automation, and Enterprise Administration**