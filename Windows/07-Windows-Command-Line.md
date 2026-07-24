# 07-Windows-Command-Line.md

# Part 1 — Introduction to Windows Command Line, Command Prompt (CMD), Console Basics, Navigation, File System Commands, and Environment Variables

---

# Introduction

The **Windows Command Line** is a text-based interface that allows users and administrators to interact directly with the Windows operating system.

Unlike graphical interfaces, the command line enables:

- Faster administration
- Task automation
- Remote management
- Troubleshooting
- System configuration
- Scripting
- Enterprise-scale operations

It remains an essential skill for:

- Windows Administrators
- System Engineers
- Cybersecurity Professionals
- SOC Analysts
- Penetration Testers
- Incident Responders
- DevOps Engineers
- Cloud Engineers

Although many modern administrative tasks are performed using **PowerShell**, understanding the traditional **Command Prompt (CMD)** remains important because numerous legacy tools, scripts, installers, and troubleshooting procedures still depend on it.

---

# Learning Objectives

By the end of this part, you will understand:

- Windows command-line architecture
- Command Prompt (CMD)
- Windows Console
- Opening CMD
- Administrative Command Prompt
- Current working directory
- Navigation commands
- File system commands
- Environment variables
- Command syntax
- Help system

---

# What is the Command Line?

The command line allows users to issue text commands that Windows executes directly.

Example:

```text
User

↓

Types Command

↓

Command Interpreter

↓

Windows Kernel

↓

Result Returned
```

Instead of clicking buttons, users execute commands to perform operations.

---

# Graphical Interface vs Command Line

| Graphical User Interface (GUI) | Command Line Interface (CLI) |
|--------------------------------|------------------------------|
| Mouse-driven | Keyboard-driven |
| Easier for beginners | Faster for experienced users |
| Visual navigation | Text-based navigation |
| Suitable for occasional tasks | Ideal for automation and administration |
| Limited bulk operations | Excellent for repetitive tasks |

Most enterprise administrators use both interfaces depending on the task.

---

# Windows Command-Line Components

```text
User

↓

Windows Console

↓

Command Interpreter (CMD)

↓

Windows API

↓

Operating System
```

The console hosts the command interpreter and displays input and output.

---

# Command Prompt (CMD)

**Command Prompt**, also called **CMD**, is the traditional Windows command interpreter.

Executable:

```text
cmd.exe
```

Location:

```text
C:\Windows\System32\cmd.exe
```

CMD interprets user commands and executes internal or external programs.

---

# Windows Console

The Windows Console provides the interface for text-based applications.

Responsibilities include:

- Displaying output
- Accepting keyboard input
- Managing command history
- Supporting copy and paste
- Handling console windows

---

# Opening Command Prompt

Common methods:

- Start Menu → **Command Prompt**
- Search for **cmd**
- Press **Win + R**, type `cmd`, then press **Enter**
- Launch from Windows Terminal (if installed)
- Open from File Explorer's address bar by typing `cmd`

---

# Opening an Administrative Command Prompt

Some commands require elevated privileges.

Methods:

```text
Start

↓

Search "cmd"

↓

Run as Administrator
```

or

```text
Win + X

↓

Terminal (Admin)

or

Command Prompt (Admin)
```

Administrative access is required for many system configuration tasks.

---

# Standard vs Administrative CMD

| Standard CMD | Administrative CMD |
|--------------|--------------------|
| Normal user permissions | Elevated privileges |
| Limited system changes | Full administrative operations |
| Safer for everyday use | Required for protected resources |

Always use the lowest privilege necessary to perform a task.

---

# CMD Window Components

```text
+------------------------------------------------+

Title Bar

↓

Command Prompt

↓

Cursor

↓

Output Area

↓

Scroll Buffer

+------------------------------------------------+
```

---

# Command Prompt Format

Typical prompt:

```cmd
C:\Users\Alice>
```

Meaning:

| Component | Description |
|-----------|-------------|
| `C:` | Current drive |
| `\Users\Alice` | Current directory |
| `>` | Ready to accept a command |

---

# Current Working Directory (CWD)

The **Current Working Directory** is the folder in which commands operate by default.

Example:

```cmd
C:\Users\Alice\Documents>
```

Relative paths are interpreted from this location.

---

# Command Syntax

General format:

```text
Command

↓

Option

↓

Argument
```

Example:

```cmd
dir /a C:\Users
```

Where:

| Part | Meaning |
|------|---------|
| `dir` | Command |
| `/a` | Option (show files with attributes) |
| `C:\Users` | Argument (target path) |

---

# Internal vs External Commands

CMD supports two categories of commands.

| Internal Commands | External Commands |
|-------------------|-------------------|
| Built into `cmd.exe` | Separate executable files |
| Always available in CMD | Stored as executable programs |
| Example: `cd` | Example: `ipconfig.exe` |

---

# Viewing Help

Most commands provide built-in help.

Example:

```cmd
help
```

Specific command help:

```cmd
dir /?
```

or

```cmd
copy /?
```

Learning to use built-in help is an important troubleshooting skill.

---

# Command History

CMD stores previously entered commands.

Useful keys:

| Key | Function |
|-----|----------|
| ↑ | Previous command |
| ↓ | Next command |
| F7 | Command history window |
| Tab | Auto-complete file and folder names |

---

# Auto-Completion

Example:

```cmd
cd Doc
```

Press:

```text
Tab
```

Result:

```cmd
cd Documents
```

Tab completion reduces typing errors and speeds navigation.

---

# Changing Directories

Command:

```cmd
cd
```

Example:

```cmd
cd Documents
```

Move to parent directory:

```cmd
cd ..
```

Return to root:

```cmd
cd \
```

---

# Changing Drives

Example:

```cmd
D:
```

Switches from:

```cmd
C:
```

to:

```cmd
D:
```

To change both the drive and directory simultaneously:

```cmd
cd /d D:\Projects
```

---

# Display Current Directory

Command:

```cmd
cd
```

or

```cmd
chdir
```

Without arguments, the command displays the current working directory.

---

# Listing Directory Contents

Command:

```cmd
dir
```

Example output:

```text
Projects

Reports

notes.txt

budget.xlsx
```

---

# Useful DIR Options

| Command | Purpose |
|----------|----------|
| `dir` | Standard listing |
| `dir /w` | Wide format |
| `dir /p` | Pause after each screen |
| `dir /a` | Show files with attributes |
| `dir /o:n` | Sort by name |
| `dir /s` | Include subdirectories |
| `dir /b` | Bare format |

---

# Directory Navigation Example

```text
C:\

↓

Users

↓

Alice

↓

Documents

↓

Projects
```

Commands:

```cmd
cd Users
cd Alice
cd Documents
cd Projects
```

---

# Creating Directories

Command:

```cmd
mkdir Reports
```

or

```cmd
md Reports
```

Result:

```text
Reports

Created
```

---

# Removing Directories

Command:

```cmd
rmdir Reports
```

or

```cmd
rd Reports
```

A directory generally must be empty before it can be removed without additional options.

---

# Creating Files

One simple method:

```cmd
type nul > demo.txt
```

This creates an empty file named:

```text
demo.txt
```

---

# Display File Contents

Command:

```cmd
type notes.txt
```

Example:

```text
Meeting at 10:00

Review firewall logs

Submit report
```

---

# Clearing the Screen

Command:

```cmd
cls
```

Result:

```text
Console Cleared
```

This affects only the display, not command history or system state.

---

# Exiting Command Prompt

Command:

```cmd
exit
```

Result:

```text
CMD Window Closed
```

---

# Environment Variables

Environment variables store information used by Windows and applications.

Examples:

| Variable | Purpose |
|-----------|----------|
| `%PATH%` | Executable search paths |
| `%TEMP%` | Temporary directory |
| `%USERNAME%` | Current user |
| `%COMPUTERNAME%` | Device name |
| `%USERPROFILE%` | User profile path |
| `%SYSTEMROOT%` | Windows installation directory |

---

# Viewing Environment Variables

Display all variables:

```cmd
set
```

Display a specific variable:

```cmd
echo %USERNAME%
```

Example output:

```text
Alice
```

---

# PATH Variable

The **PATH** variable tells Windows where to search for executable programs.

```text
Command

↓

Search PATH

↓

Executable Found

↓

Program Runs
```

Without PATH, many commands would require their full file paths.

---

# Enterprise Example

A help desk technician needs to verify a user's profile directory.

Instead of browsing through File Explorer, they use:

```cmd
echo %USERPROFILE%
```

Output:

```text
C:\Users\Alice
```

This allows quick verification during remote support sessions.

---

# Cybersecurity Perspective

Command Prompt is frequently used by both defenders and attackers.

Legitimate administrative activities include:

- File management
- Troubleshooting
- Software installation
- Network diagnostics

Threat actors may also use CMD to:

- Execute malicious scripts
- Enumerate system information
- Launch built-in utilities
- Delete logs
- Download payloads

Security teams should monitor suspicious command execution using:

- Microsoft Defender for Endpoint
- SIEM solutions
- Endpoint Detection and Response (EDR)
- Windows Event Logs
- Sysmon (when deployed)

---

# Business Impact

Command-line proficiency enables organizations to:

- Resolve issues faster
- Automate repetitive tasks
- Reduce administrative effort
- Improve operational consistency
- Support large-scale Windows deployments

Administrators who understand the command line can often diagnose issues more quickly than relying solely on graphical tools.

---

# Enterprise Best Practices

- Use administrative CMD only when required.
- Prefer full paths in administrative scripts.
- Validate commands before executing them on production systems.
- Document administrative procedures.
- Audit privileged command execution where appropriate.
- Restrict administrative access using the principle of least privilege.

---

# Practical Labs

## Lab 1 — Explore the Current Directory

Open **Command Prompt** and run:

```cmd
cd
```

Then navigate using:

```cmd
cd ..

cd \
```

Observe how the current working directory changes.

---

## Lab 2 — Create and View a File

Run:

```cmd
mkdir Demo

cd Demo

type nul > notes.txt

dir

type notes.txt
```

Record the results after each command.

---

## Lab 3 — Explore Environment Variables

Run:

```cmd
echo %USERNAME%

echo %USERPROFILE%

echo %SYSTEMROOT%

set
```

Identify the values for your current system.

---

# Key Takeaways

- CMD is the traditional Windows command interpreter.
- Commands consist of a command name, optional switches, and arguments.
- The current working directory determines how relative paths are resolved.
- Environment variables provide dynamic system information.
- Built-in help (`/?`) is an essential learning and troubleshooting resource.
- Command Prompt remains widely used for administration, automation, and incident response.

---

# Interview Questions

1. What is `cmd.exe`?
2. What is the difference between CMD and PowerShell?
3. What is the current working directory?
4. What is the purpose of the `PATH` environment variable?
5. What is the difference between internal and external commands?
6. How do you change directories in CMD?
7. What does the `dir` command do?
8. How do you display environment variables?
9. Why should administrative CMD sessions be limited?
10. Why is command-line knowledge valuable in cybersecurity?

---

# References

- Microsoft Learn
- Microsoft Windows Command-Line Reference
- Microsoft CMD Documentation
- Microsoft Sysinternals Documentation
- *Windows Internals* (Mark Russinovich, David Solomon, Alex Ionescu)

---

# 07-Windows-Command-Line.md

# Part 2 — Advanced CMD Commands, File Operations, Process Management, Networking Utilities, Batch Files, Redirection, Pipes, and Command Chaining

---

# Introduction

After learning the fundamentals of Command Prompt (CMD), the next step is understanding how administrators automate work, troubleshoot systems, manage processes, and perform network diagnostics.

In enterprise environments, CMD is commonly used for:

- System troubleshooting
- File management
- Network diagnostics
- Process management
- Software deployment
- Batch automation
- Log collection
- Remote administration

Although PowerShell has become Microsoft's primary automation platform, many Windows utilities still rely on CMD syntax and batch scripts.

---

# Advanced Command Categories

```text
Windows CMD

├── File Management
├── Directory Management
├── Process Management
├── System Information
├── Network Diagnostics
├── Environment Variables
├── Batch Automation
├── Redirection
├── Pipes
└── Command Chaining
```

---

# Copy Command

Copies one or more files.

Syntax

```cmd
copy Source Destination
```

Example

```cmd
copy report.txt D:\Backup\
```

Result

```text
report.txt

↓

Copied

↓

D:\Backup\
```

---

# XCOPY

`xcopy` is an enhanced version of the `copy` command.

Example

```cmd
xcopy C:\Projects D:\Backup /E
```

Common options

| Option | Description |
|---------|-------------|
| `/E` | Copy all subdirectories including empty ones |
| `/H` | Copy hidden and system files |
| `/Y` | Suppress overwrite confirmation |
| `/D` | Copy newer files only |

Although still available, **Robocopy** is generally recommended for enterprise-scale operations.

---

# ROBOCOPY

Robocopy (Robust File Copy) is Microsoft's enterprise file-copy utility.

Example

```cmd
robocopy C:\Projects D:\Backup /MIR
```

Common features

- Resume interrupted copies
- Preserve permissions
- Retry failed transfers
- Logging
- Mirror directories
- Copy large datasets efficiently

---

# Move Command

Moves files or folders.

Example

```cmd
move report.docx D:\Archive\
```

Workflow

```text
Original Location

↓

Move

↓

Destination

↓

File Relocated
```

---

# Rename Command

Rename files or folders.

Example

```cmd
ren draft.docx final.docx
```

Only the name changes.

The file contents remain unchanged.

---

# Delete Files

Delete a file

```cmd
del report.txt
```

Delete all text files

```cmd
del *.txt
```

Delete confirmation

```cmd
del /P report.txt
```

Always verify wildcard usage before execution.

---

# Remove Directories

Delete an empty folder

```cmd
rd Test
```

Delete a folder and its contents

```cmd
rd /S Test
```

Quiet mode

```cmd
rd /S /Q Test
```

Be cautious when using `/S` and `/Q` because they can remove large directory trees.

---

# Wildcards

CMD supports wildcard characters.

| Wildcard | Meaning |
|-----------|----------|
| `*` | Multiple characters |
| `?` | Single character |

Examples

```cmd
dir *.txt
```

```cmd
copy *.pdf D:\PDF\
```

---

# Tree Command

Display directory hierarchy.

```cmd
tree
```

Example

```text
Projects

├── Reports

├── Images

└── Source
```

Useful for documentation and troubleshooting.

---

# Finding Files

Locate files using:

```cmd
dir report.docx /S
```

Search recursively

```cmd
dir *.log /S
```

---

# File Comparison

Compare two files.

```cmd
fc file1.txt file2.txt
```

Useful for:

- Configuration comparison
- Script verification
- Log analysis

---

# Display Text Files

```cmd
type notes.txt
```

Display multiple files

```cmd
type *.txt
```

---

# More Command

Large output can be paged.

Example

```cmd
type logfile.txt | more
```

Instead of scrolling rapidly, output pauses one screen at a time.

---

# Sort Command

Sort text alphabetically.

Example

```cmd
sort names.txt
```

Combined example

```cmd
type users.txt | sort
```

---

# Find Command

Search for text.

Example

```cmd
find "Administrator" users.txt
```

Returns matching lines.

---

# Findstr Command

`findstr` is more powerful than `find`.

Example

```cmd
findstr ERROR server.log
```

Supports:

- Pattern matching
- Multiple search terms
- Case-insensitive searches
- Regular-expression style searches

Widely used in log analysis.

---

# System Information

Display detailed system information.

```cmd
systeminfo
```

Information includes:

- Windows version
- Build number
- Installed RAM
- Processor
- Domain membership
- Boot time
- Hotfixes

---

# Hostname

Display computer name.

```cmd
hostname
```

Example

```text
HR-LAPTOP-021
```

---

# Who Am I

Display current user.

```cmd
whoami
```

Example

```text
CORP\Alice
```

Additional information

```cmd
whoami /groups
```

```cmd
whoami /priv
```

These commands are valuable during privilege analysis.

---

# Tasklist

Display running processes.

```cmd
tasklist
```

Example

```text
explorer.exe

chrome.exe

notepad.exe
```

---

# Taskkill

Terminate a process.

Example

```cmd
taskkill /PID 4256
```

Terminate by image name

```cmd
taskkill /IM notepad.exe
```

Force termination

```cmd
taskkill /F /IM notepad.exe
```

Use force termination carefully because unsaved work may be lost.

---

# Shutdown Command

Shutdown system

```cmd
shutdown /s
```

Restart

```cmd
shutdown /r
```

Cancel pending shutdown

```cmd
shutdown /a
```

Schedule restart after 60 seconds

```cmd
shutdown /r /t 60
```

---

# Networking Utilities

Common networking commands include:

| Command | Purpose |
|----------|----------|
| `ipconfig` | Display IP configuration |
| `ping` | Connectivity testing |
| `tracert` | Trace packet path |
| `pathping` | Route and packet-loss analysis |
| `arp` | View ARP cache |
| `netstat` | Network connections |
| `nslookup` | DNS queries |
| `route` | Routing table |
| `net` | Network administration |

These commands are covered in greater detail in the Windows Networking chapter.

---

# IPCONFIG

Display IP configuration.

```cmd
ipconfig
```

Detailed output

```cmd
ipconfig /all
```

Release DHCP lease

```cmd
ipconfig /release
```

Renew lease

```cmd
ipconfig /renew
```

Flush DNS cache

```cmd
ipconfig /flushdns
```

---

# PING

Test connectivity.

```cmd
ping google.com
```

Example workflow

```text
Host

↓

ICMP Echo Request

↓

Reply

↓

Latency Displayed
```

---

# NETSTAT

View active connections.

```cmd
netstat
```

Display listening ports

```cmd
netstat -an
```

Display executable names (requires elevation)

```cmd
netstat -ab
```

---

# NSLOOKUP

Query DNS.

```cmd
nslookup openai.com
```

Useful for:

- DNS troubleshooting
- Name resolution verification
- Server diagnostics

---

# Batch Files

Batch files automate CMD commands.

Extension

```text
.bat

or

.cmd
```

Example

```bat
@echo off
echo Hello World
pause
```

---

# Echo Command

Display text.

```cmd
echo Hello
```

Display environment variable

```cmd
echo %USERNAME%
```

---

# Pause

Wait for user input.

```cmd
pause
```

Example output

```text
Press any key to continue . . .
```

---

# Comments

Batch comments

```bat
REM Backup Script
```

Alternative

```bat
:: Backup Script
```

---

# Variables

Create variable

```bat
set NAME=Alice
```

Use variable

```bat
echo %NAME%
```

---

# Input

Prompt the user.

```bat
set /P USER=Enter username:
```

---

# IF Statement

Example

```bat
IF EXIST report.txt echo Found
```

Conditional execution is fundamental to batch scripting.

---

# FOR Loop

Example

```bat
FOR %%F IN (*.txt) DO echo %%F
```

Useful for processing multiple files.

---

# GOTO

Jump to another section.

```bat
goto END

:END
echo Finished
```

---

# Redirection

Redirect output.

Overwrite

```cmd
dir > files.txt
```

Append

```cmd
dir >> files.txt
```

Workflow

```text
Command

↓

Output

↓

Text File
```

---

# Input Redirection

```cmd
sort < names.txt
```

The command reads input from a file instead of the keyboard.

---

# Error Redirection

Redirect errors.

```cmd
dir MissingFolder 2> errors.txt
```

Redirect standard output and errors

```cmd
dir C:\ 1>output.txt 2>errors.txt
```

---

# Pipes

A pipe passes output from one command directly into another.

Syntax

```cmd
Command1 | Command2
```

Example

```cmd
tasklist | find "chrome"
```

Workflow

```text
Command Output

↓

Pipe

↓

Second Command

↓

Filtered Result
```

---

# Command Chaining

Execute multiple commands.

Run second command only if the first succeeds

```cmd
mkdir Logs && cd Logs
```

Run second command only if the first fails

```cmd
mkdir Logs || echo Failed
```

Run commands regardless of success

```cmd
echo Start & dir & echo Finished
```

---

# Enterprise Example

A help desk engineer collects diagnostic information.

```text
systeminfo

↓

ipconfig /all

↓

tasklist

↓

netstat -an

↓

Redirect Results

↓

diagnostics.txt
```

The collected information is attached to a support ticket for troubleshooting.

---

# Cybersecurity Perspective

Attackers frequently use built-in CMD utilities because they are trusted Windows components.

Examples include:

- System enumeration (`systeminfo`, `whoami`)
- Process discovery (`tasklist`)
- Network discovery (`ipconfig`, `arp`, `netstat`)
- File searching (`dir`, `findstr`)
- Batch script execution
- Command chaining for automation

Security teams should monitor:

- Suspicious command execution
- Privileged batch scripts
- Unexpected process termination
- Mass file operations
- Network enumeration
- Unusual command-line arguments

Monitoring command-line activity is an important component of Endpoint Detection and Response (EDR).

---

# Business Impact

CMD enables organizations to:

- Automate repetitive tasks
- Standardize administrative procedures
- Reduce troubleshooting time
- Improve operational consistency
- Support remote administration
- Simplify diagnostics

Well-designed automation reduces operational costs and human error.

---

# Enterprise Best Practices

- Test batch scripts in non-production environments.
- Use descriptive script names and comments.
- Validate user input before processing.
- Log important administrative actions.
- Review scripts regularly for security and accuracy.
- Restrict execution of unauthorized scripts using organizational security policies.

---

# Practical Labs

## Lab 1 — File Operations

Create a test folder and perform:

```cmd
mkdir Demo

copy file.txt Demo

move file.txt Backup

dir
```

Observe the changes after each command.

---

## Lab 2 — Process Management

Run:

```cmd
tasklist

whoami

hostname

systeminfo
```

Identify:

- Current user
- Computer name
- Operating system version
- Running processes

---

## Lab 3 — Redirection and Pipes

Execute:

```cmd
systeminfo > system.txt

tasklist | find "explorer"

ipconfig /all > network.txt
```

Review the generated files and filtered output.

---

# Key Takeaways

- CMD provides powerful administrative capabilities beyond basic navigation.
- Built-in utilities support process, file, and network management.
- Batch files automate repetitive administrative tasks.
- Redirection and pipes enable flexible command processing.
- Command chaining simplifies complex workflows.
- Proper monitoring of command-line activity strengthens enterprise security.

---

# Interview Questions

1. What is the difference between `copy`, `xcopy`, and `robocopy`?
2. What does the `tasklist` command display?
3. How do `find` and `findstr` differ?
4. What is the purpose of `systeminfo`?
5. Explain output redirection using `>`.
6. What is a pipe (`|`) in CMD?
7. What is the difference between `&&`, `||`, and `&`?
8. How do batch files automate administration?
9. Why is `whoami /priv` useful during security investigations?
10. Why do attackers frequently use built-in Windows command-line utilities?

---

# References

- Microsoft Learn
- Microsoft Windows Command Reference
- Microsoft Robocopy Documentation
- Microsoft Sysinternals Documentation
- *Windows Internals* (Mark Russinovich, David Solomon, Alex Ionescu)

---

# 07-Windows-Command-Line.md

# Part 3 — Windows Networking Commands, Disk Utilities, System Administration Commands, Scheduling, Services, Registry Tools, and Troubleshooting

---

# Introduction

The Windows Command Line provides numerous built-in utilities that enable administrators to manage networking, storage, services, scheduled tasks, user accounts, the Windows Registry, and system troubleshooting.

In enterprise environments, these tools are essential for:

- Network diagnostics
- Storage management
- User administration
- Service management
- Scheduled automation
- System maintenance
- Incident response
- Digital forensics
- Security investigations

Many of these commands require **administrative privileges** because they modify critical operating system components.

---

# Windows Administrative Command Categories

```text
Windows CMD

├── Network Commands
├── Disk Utilities
├── Service Management
├── User Management
├── Scheduled Tasks
├── Registry Tools
├── Driver Management
├── System Maintenance
├── Event Log Utilities
└── Troubleshooting Tools
```

---

# Network Configuration Commands

Windows includes several networking utilities.

| Command | Purpose |
|----------|----------|
| `ipconfig` | IP configuration |
| `ping` | Connectivity testing |
| `tracert` | Route tracing |
| `pathping` | Packet loss analysis |
| `netstat` | Active connections |
| `arp` | ARP cache |
| `route` | Routing table |
| `nslookup` | DNS lookup |
| `hostname` | Computer name |
| `net` | Network administration |

---

# IPCONFIG Review

Display IP configuration.

```cmd
ipconfig
```

Detailed configuration.

```cmd
ipconfig /all
```

Release DHCP lease.

```cmd
ipconfig /release
```

Renew DHCP lease.

```cmd
ipconfig /renew
```

Flush DNS cache.

```cmd
ipconfig /flushdns
```

Display DNS cache.

```cmd
ipconfig /displaydns
```

---

# PING

Tests network connectivity using ICMP Echo Requests.

```cmd
ping 8.8.8.8
```

or

```cmd
ping microsoft.com
```

Typical output:

```text
Reply from ...

Time=14ms

TTL=127
```

---

# TRACERT

Displays the path packets take to a destination.

```cmd
tracert google.com
```

Example workflow:

```text
Computer

↓

Router

↓

ISP

↓

Internet

↓

Destination
```

Useful for identifying routing issues.

---

# PATHPING

Combines the functionality of `ping` and `tracert`.

```cmd
pathping google.com
```

Provides:

- Route information
- Packet loss statistics
- Latency measurements

---

# ARP

Displays the Address Resolution Protocol cache.

```cmd
arp -a
```

Example output:

```text
IP Address

↓

MAC Address
```

Useful during network troubleshooting and incident investigations.

---

# NETSTAT

Displays network statistics.

```cmd
netstat -an
```

Common options:

| Option | Purpose |
|---------|----------|
| `-a` | All connections |
| `-n` | Numeric addresses |
| `-o` | Include Process ID (PID) |
| `-b` | Show executable (requires admin) |

---

# Example NETSTAT Output

```text
Local Address

↓

Foreign Address

↓

State

↓

PID
```

Administrators often correlate the PID with `tasklist` during investigations.

---

# ROUTE

View routing table.

```cmd
route print
```

Example:

```text
Network

↓

Gateway

↓

Interface

↓

Metric
```

Improper routes can prevent communication between networks.

---

# NSLOOKUP

DNS query utility.

```cmd
nslookup openai.com
```

Specify DNS server:

```cmd
nslookup openai.com 8.8.8.8
```

Useful for diagnosing DNS resolution issues.

---

# NET Command

The `net` command manages numerous Windows networking functions.

Examples:

```cmd
net user
```

```cmd
net localgroup
```

```cmd
net share
```

```cmd
net use
```

Each subcommand serves a different administrative purpose.

---

# NET USER

List local users.

```cmd
net user
```

View a user.

```cmd
net user Alice
```

Create a user.

```cmd
net user Alice Password123! /add
```

Delete a user.

```cmd
net user Alice /delete
```

Administrative privileges are required for account management.

---

# NET LOCALGROUP

Display local groups.

```cmd
net localgroup
```

Add a user to Administrators.

```cmd
net localgroup Administrators Alice /add
```

Membership changes should follow organizational approval processes.

---

# NET SHARE

Display shared folders.

```cmd
net share
```

Create a share.

```cmd
net share Public=C:\Public
```

Improperly configured shares can expose sensitive information.

---

# NET USE

Connect to a network share.

```cmd
net use Z: \\FileServer\Finance
```

Disconnect.

```cmd
net use Z: /delete
```

---

# Task Scheduler

Windows schedules tasks using:

```text
Task Scheduler
```

CMD interface:

```cmd
schtasks
```

---

# SCHTASKS

Display scheduled tasks.

```cmd
schtasks
```

Query a task.

```cmd
schtasks /query
```

Create a task.

```cmd
schtasks /create ...
```

Run a task immediately.

```cmd
schtasks /run /tn "TaskName"
```

Scheduled tasks are commonly used for automation and maintenance.

---

# Service Management

Windows services can be managed from CMD.

Utilities include:

- `sc`
- `net start`
- `net stop`

---

# NET START

Display running services.

```cmd
net start
```

Start a service.

```cmd
net start Spooler
```

---

# NET STOP

Stop a service.

```cmd
net stop Spooler
```

Stopping critical services may affect system functionality.

---

# SC Command

Service Controller utility.

Query service.

```cmd
sc query
```

Query specific service.

```cmd
sc query WinDefend
```

Start service.

```cmd
sc start WinDefend
```

Stop service.

```cmd
sc stop WinDefend
```

Display configuration.

```cmd
sc qc WinDefend
```

---

# Driver Query

Display installed drivers.

```cmd
driverquery
```

Verbose output.

```cmd
driverquery /v
```

CSV export.

```cmd
driverquery /fo csv
```

Useful during troubleshooting and forensic investigations.

---

# Driver Signing

Windows can display information about signed drivers.

Administrators use:

```cmd
sigverif
```

This launches the File Signature Verification utility.

---

# Registry Command

The Windows Registry can be managed using:

```cmd
reg
```

Examples:

```cmd
reg query
```

```cmd
reg add
```

```cmd
reg delete
```

```cmd
reg export
```

```cmd
reg import
```

Always back up the Registry before making changes.

---

# Registry Query Example

```cmd
reg query HKLM\Software
```

Output:

```text
Registry Keys

↓

Values

↓

Data
```

---

# Event Log Utility

Windows includes:

```cmd
wevtutil
```

Examples:

List logs.

```cmd
wevtutil el
```

Query a log.

```cmd
wevtutil qe System
```

Export a log.

```cmd
wevtutil epl System System.evtx
```

Useful during incident response and troubleshooting.

---

# System File Checker

Verify protected Windows system files.

```cmd
sfc /scannow
```

Workflow:

```text
Scan System Files

↓

Verify Integrity

↓

Repair if Possible

↓

Generate Results
```

---

# DISM

Deployment Image Servicing and Management.

Check image health.

```cmd
DISM /Online /Cleanup-Image /CheckHealth
```

Scan image.

```cmd
DISM /Online /Cleanup-Image /ScanHealth
```

Restore health.

```cmd
DISM /Online /Cleanup-Image /RestoreHealth
```

DISM is commonly used before or alongside `sfc` when repairing Windows installations.

---

# CHKDSK

Check disk integrity.

```cmd
chkdsk C:
```

Repair file system.

```cmd
chkdsk C: /F
```

Locate bad sectors.

```cmd
chkdsk C: /R
```

Some operations require a reboot because the system volume is in use.

---

# FSUTIL

Advanced file system management.

Examples:

```cmd
fsutil fsinfo drives
```

```cmd
fsutil fsinfo ntfsinfo C:
```

`fsutil` is intended primarily for advanced administrative tasks.

---

# Shutdown Utility

Shutdown.

```cmd
shutdown /s
```

Restart.

```cmd
shutdown /r
```

Log off.

```cmd
shutdown /l
```

Abort pending shutdown.

```cmd
shutdown /a
```

---

# System Diagnostics Workflow

```text
Problem Report

↓

systeminfo

↓

driverquery

↓

ipconfig

↓

netstat

↓

Event Logs

↓

SFC

↓

DISM

↓

Resolution
```

---

# Enterprise Example

A workstation cannot reach a file server.

The administrator performs:

```text
ping

↓

tracert

↓

nslookup

↓

route print

↓

net use

↓

Resolution
```

If connectivity exists but authentication fails, the administrator continues with user, share, and permission troubleshooting.

---

# Cybersecurity Perspective

Security analysts frequently use CMD during investigations.

Common commands include:

| Command | Investigation Purpose |
|----------|-----------------------|
| `whoami` | Identify current user |
| `hostname` | Identify system |
| `systeminfo` | Collect system details |
| `ipconfig /all` | Network configuration |
| `arp -a` | Local network mapping |
| `netstat -ano` | Active connections and PIDs |
| `tasklist` | Running processes |
| `driverquery` | Installed drivers |
| `wevtutil` | Collect event logs |
| `reg query` | Inspect Registry |
| `schtasks` | Review scheduled tasks |
| `sc query` | Review running services |

Attackers also use many of these utilities because they are legitimate Windows binaries ("living off the land"). Security teams should correlate command execution with user context, process ancestry, and endpoint telemetry.

---

# Business Impact

These command-line utilities enable organizations to:

- Diagnose network failures
- Automate maintenance
- Repair operating systems
- Manage users and services
- Collect forensic evidence
- Improve operational efficiency
- Reduce downtime

---

# Enterprise Best Practices

- Use administrative privileges only when necessary.
- Export Registry data before modifying it.
- Review scheduled tasks periodically.
- Audit local administrator membership.
- Monitor service creation and modification.
- Log administrative command execution.
- Test repair commands in accordance with organizational change management procedures.

---

# Practical Labs

## Lab 1 — Network Diagnostics

Run:

```cmd
hostname

ipconfig /all

ping localhost

nslookup microsoft.com

route print
```

Record:

- Computer name
- IPv4 address
- Default gateway
- DNS server
- Route summary

---

## Lab 2 — System Health

Execute:

```cmd
systeminfo

driverquery

sfc /scannow
```

Observe:

- Operating system information
- Installed drivers
- System File Checker results

---

## Lab 3 — Services and Tasks

Run:

```cmd
sc query

net start

schtasks /query
```

Identify:

- Running services
- Scheduled tasks
- Service states

Do not stop or modify production services unless authorized.

---

# Key Takeaways

- Windows provides extensive command-line tools for networking, storage, services, and troubleshooting.
- `net`, `sc`, and `schtasks` are core administrative utilities.
- `sfc` and `DISM` help repair Windows system files and images.
- `wevtutil` enables command-line event log management.
- Administrative commands should be used carefully and audited in enterprise environments.

---

# Interview Questions

1. What is the difference between `ping`, `tracert`, and `pathping`?
2. What information does `netstat -ano` provide?
3. How do you list local user accounts using CMD?
4. What is the purpose of the `sc` command?
5. How do `sfc` and `DISM` differ?
6. What is the purpose of `driverquery`?
7. How do you export Windows Event Logs using `wevtutil`?
8. Why should the Windows Registry be backed up before modification?
9. What is the purpose of `schtasks`?
10. Why are built-in Windows administrative tools important in cybersecurity investigations?

---

# References

- Microsoft Learn
- Microsoft Windows Command Reference
- Microsoft Task Scheduler Documentation
- Microsoft DISM Documentation
- Microsoft SFC Documentation
- Microsoft Sysinternals Documentation
- *Windows Internals* (Mark Russinovich, David Solomon, Alex Ionescu)

---

# 07-Windows-Command-Line.md

# Part 4 — Advanced CMD Administration, Security, Enterprise Automation, Best Practices, Chapter Review, and Interview Preparation

---

# Introduction

Windows Command Prompt (CMD) remains one of the most valuable administrative tools in Windows.

Although PowerShell has become Microsoft's primary automation platform, CMD continues to be used for:

- Legacy application support
- Enterprise deployment scripts
- Operating system recovery
- Windows Preinstallation Environment (WinPE)
- Startup troubleshooting
- Software installation
- Incident response
- Digital forensics
- Security investigations

Understanding how CMD fits into modern enterprise administration helps professionals choose the appropriate tool for each task.

---

# Enterprise Command-Line Workflow

```text
Administrator

↓

Command Prompt

↓

Built-in Windows Utilities

↓

Operating System

↓

Logs

↓

Monitoring

↓

Enterprise SIEM
```

Every administrative action should be documented, monitored, and performed using the principle of least privilege.

---

# CMD in Enterprise Administration

CMD is commonly used for:

| Administrative Task | Example Tool |
|---------------------|--------------|
| User Management | `net user` |
| Service Management | `sc` |
| Network Troubleshooting | `ipconfig`, `ping`, `netstat` |
| File Management | `copy`, `robocopy`, `dir` |
| Disk Maintenance | `chkdsk` |
| System Repair | `sfc`, `DISM` |
| Event Collection | `wevtutil` |
| Scheduled Automation | `schtasks` |

---

# Windows Recovery Environment (WinRE)

Command Prompt is available within **Windows Recovery Environment (WinRE)**.

Typical uses include:

- Repairing boot issues
- Running `bootrec`
- Running `bcdedit`
- Repairing system files
- Accessing offline files
- Copying important data
- Troubleshooting startup failures

Example workflow:

```text
Boot Failure

↓

WinRE

↓

Command Prompt

↓

Repair Commands

↓

Successful Boot
```

---

# Windows PE (WinPE)

Windows Preinstallation Environment (WinPE) is a lightweight Windows environment used for:

- Operating system deployment
- Disk partitioning
- Image deployment
- Recovery
- Hardware diagnostics

CMD is the primary interface in many WinPE scenarios.

---

# Safe Mode with Command Prompt

Windows can boot into:

```text
Safe Mode

↓

Command Prompt

↓

Minimal Drivers

↓

Troubleshooting
```

This mode is useful when graphical components fail to load correctly.

---

# Administrative Automation

Many organizations automate routine maintenance using CMD scripts.

Example workflow:

```text
Nightly Task

↓

Batch Script

↓

Robocopy

↓

Cleanup

↓

Log Generation

↓

Email Notification
```

Automation reduces repetitive manual work and improves consistency.

---

# Logging Administrative Activity

Administrative scripts should generate logs whenever possible.

Typical log contents include:

- Script name
- Start time
- End time
- User account
- Computer name
- Commands executed
- Successes
- Errors
- Exit code

Example:

```text
Backup Started

↓

Files Copied

↓

Verification Completed

↓

Backup Successful
```

Logs simplify troubleshooting and auditing.

---

# Exit Codes

Most Windows commands return an **exit code** indicating success or failure.

Common values:

| Exit Code | Meaning |
|-----------|---------|
| `0` | Success |
| Non-zero | Warning or error (depends on the command) |

Batch scripts often evaluate `%ERRORLEVEL%`.

Example:

```cmd
echo %ERRORLEVEL%
```

---

# Using ERRORLEVEL

Example:

```bat
copy report.txt D:\Backup

IF ERRORLEVEL 1 (
    echo Copy Failed
) ELSE (
    echo Copy Successful
)
```

Checking exit codes improves the reliability of automation.

---

# Batch Script Structure

Example:

```bat
@echo off

REM Initialize

echo Starting Backup

robocopy C:\Data D:\Backup

echo Backup Complete

pause
```

A well-structured script is easier to maintain and troubleshoot.

---

# Defensive Scripting Practices

Administrators should:

- Validate input
- Check exit codes
- Log important actions
- Avoid hard-coded credentials
- Use absolute paths where practical
- Test scripts before deployment
- Document script behavior

---

# Common Administrative Mistakes

Examples include:

- Running commands without elevation when required
- Deleting incorrect directories
- Misusing wildcard characters
- Executing unverified scripts
- Ignoring command output
- Failing to check exit codes
- Running destructive commands in the wrong directory

Careful verification reduces operational risk.

---

# CMD Security Considerations

Because CMD can execute powerful system commands, organizations should protect administrative access.

Recommended controls:

- Least privilege
- Multi-factor authentication (where applicable)
- Administrative approval processes
- Endpoint monitoring
- Application control
- Command-line auditing

---

# Living Off the Land (LotL)

Many legitimate Windows executables can be used for both administration and malicious purposes.

Examples include:

| Utility | Legitimate Use | Potential Abuse |
|----------|----------------|-----------------|
| `cmd.exe` | Administration | Script execution |
| `certutil.exe` | Certificate management | File download/encoding |
| `bitsadmin.exe` *(legacy)* | Background transfers | Payload transfer |
| `reg.exe` | Registry management | Persistence changes |
| `schtasks.exe` | Scheduled automation | Persistence |
| `sc.exe` | Service management | Malicious service creation |
| `wevtutil.exe` | Event log management | Log clearing or export |

The presence of these tools alone is **not** an indicator of malicious activity. Security analysts evaluate how, when, and by whom they are used.

---

# Command-Line Logging

Enterprise security solutions often record:

- Executed commands
- Parent process
- Child process
- User account
- Timestamp
- Device name
- Process ID
- Command-line arguments

These records support incident response and threat hunting.

---

# Example Investigation

SOC analysts observe the following sequence:

```text
powershell.exe

↓

cmd.exe

↓

whoami

↓

net user

↓

ipconfig /all

↓

netstat -ano
```

Possible interpretation:

- System enumeration
- Network discovery
- User discovery

This activity may be legitimate administration or part of attacker reconnaissance. Analysts correlate additional telemetry before reaching conclusions.

---

# Enterprise Automation Example

Nightly maintenance script:

```text
Verify Free Space

↓

Robocopy

↓

Delete Temporary Files

↓

Generate Log

↓

Check ERRORLEVEL

↓

Notify Administrator
```

This approach minimizes manual intervention while maintaining accountability.

---

# Incident Response Example

A workstation reports suspicious activity.

Administrator collects:

```cmd
hostname

whoami

systeminfo

tasklist

netstat -ano

driverquery

wevtutil epl System System.evtx
```

The collected information is preserved for further investigation.

---

# Disaster Recovery Example

A Windows server fails to boot.

Recovery steps:

```text
WinRE

↓

Command Prompt

↓

bootrec

↓

bcdedit

↓

chkdsk

↓

sfc

↓

DISM

↓

Successful Recovery
```

The exact repair sequence depends on the root cause of the failure.

---

# CMD vs PowerShell

| Feature | CMD | PowerShell |
|----------|-----|------------|
| Primary Interface | Text-based | Object-based |
| Legacy Support | Excellent | Excellent |
| Automation | Basic | Advanced |
| Pipeline | Text | .NET Objects |
| Scripting | Batch | PowerShell |
| Enterprise Administration | Supported | Preferred |
| Modern Microsoft Management | Limited | Extensive |

PowerShell is generally recommended for new automation projects, while CMD remains valuable for compatibility and troubleshooting.

---

# Enterprise Example

A financial institution automates nightly log collection.

```text
Scheduled Task

↓

Batch Script

↓

Collect Event Logs

↓

Compress Files

↓

Copy to Secure Server

↓

Verify Success

↓

Generate Audit Log
```

The process runs unattended and produces a detailed execution log.

---

# Cybersecurity Perspective

Command-line activity is a high-value source of security telemetry.

Security teams monitor for:

- Suspicious script execution
- Unexpected administrative tools
- Privilege escalation attempts
- Unauthorized scheduled tasks
- Registry modifications
- Service creation
- Network reconnaissance
- Large-scale file operations

Context is essential. Many commands used by attackers are also used daily by system administrators.

---

# Business Impact

Effective command-line administration enables organizations to:

- Automate repetitive tasks
- Improve operational efficiency
- Reduce downtime
- Standardize maintenance
- Support disaster recovery
- Accelerate incident response
- Lower administrative costs

---

# Enterprise Best Practices

- Prefer PowerShell for new automation while maintaining CMD compatibility where required.
- Execute administrative commands using least privilege.
- Store scripts in version-controlled repositories.
- Digitally sign scripts when organizational policy requires.
- Test scripts in development or staging environments before production use.
- Enable centralized logging and monitoring of administrative activities.
- Review scheduled tasks, services, and startup scripts regularly.
- Document recovery procedures for common operational issues.

---

# Practical Labs

## Lab 1 — Collect System Information

Open **Command Prompt** and run:

```cmd
hostname

whoami

systeminfo > systeminfo.txt

ipconfig /all > network.txt
```

Review the generated reports.

---

## Lab 2 — Create a Simple Batch Script

Create a file named:

```text
maintenance.bat
```

Contents:

```bat
@echo off
echo Starting Maintenance...
hostname
whoami
systeminfo
echo Maintenance Complete.
pause
```

Run the script and observe the output.

---

## Lab 3 — Check Exit Codes

Execute:

```cmd
dir C:\Windows

echo %ERRORLEVEL%

dir C:\FolderThatDoesNotExist

echo %ERRORLEVEL%
```

Compare the exit codes after a successful and unsuccessful command.

---

# Chapter Summary

In this chapter, you learned:

- Windows Command Prompt architecture
- Command syntax
- Internal and external commands
- Navigation commands
- File and directory management
- Environment variables
- Process management
- Networking utilities
- Batch scripting
- Redirection
- Pipes
- Command chaining
- Disk utilities
- Service management
- User management
- Registry commands
- Scheduled tasks
- System repair utilities
- Enterprise automation
- Security monitoring
- Best practices for administrative scripting

These skills provide a strong foundation for Windows administration, troubleshooting, enterprise operations, and cybersecurity.

---

# Key Takeaways

- CMD remains an essential Windows administration tool despite the growth of PowerShell.
- Batch scripts automate repetitive administrative tasks.
- Exit codes improve script reliability.
- Enterprise automation should include logging, validation, and error handling.
- Command-line activity is valuable for both system administration and security monitoring.
- Administrative commands should be executed responsibly and audited where appropriate.

---

# Interview Questions

1. What is `%ERRORLEVEL%`, and why is it important?
2. When would you use CMD instead of PowerShell?
3. What is the purpose of WinRE?
4. How does WinPE differ from WinRE?
5. Why should scripts generate logs?
6. What is the principle of least privilege, and how does it apply to CMD?
7. Explain the difference between text-based pipelines in CMD and object-based pipelines in PowerShell.
8. What is "Living Off the Land" (LotL), and why is it important in cybersecurity?
9. Why should administrators validate exit codes in automation scripts?
10. What types of command-line activity should security teams monitor?

---

# References

- Microsoft Learn
- Microsoft Windows Command Reference
- Microsoft Windows Recovery Environment Documentation
- Microsoft Windows PE Documentation
- Microsoft PowerShell Documentation
- Microsoft Sysinternals Documentation
- *Windows Internals* (Mark Russinovich, David Solomon, Alex Ionescu)

---

# Congratulations!

You have successfully completed **Chapter 7 – Windows Command Line**.

You now understand how to use Command Prompt for navigation, administration, troubleshooting, automation, networking, system repair, and enterprise operations. These skills provide a solid foundation for more advanced Windows management topics, including user administration, security, and PowerShell scripting.

---
