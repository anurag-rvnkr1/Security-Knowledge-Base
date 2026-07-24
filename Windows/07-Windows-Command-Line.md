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

