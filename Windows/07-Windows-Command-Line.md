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

