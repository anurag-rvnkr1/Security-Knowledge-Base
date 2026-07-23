# 07 - Linux Text Processing

# Part 1 — Standard Input, Standard Output, Standard Error, Redirection, Pipes, and Introduction to Text Processing

---

# Introduction

Almost everything in Linux can be represented as text.

Examples include:

- System logs
- Configuration files
- Source code
- Command output
- Network information
- Security alerts
- Process information
- Audit records

Because of this philosophy, Linux provides powerful tools that allow administrators to process, filter, transform, and analyze text efficiently.

Text processing is one of the most valuable skills for:

- Linux Administrators
- DevOps Engineers
- Cloud Engineers
- Site Reliability Engineers (SRE)
- SOC Analysts
- DFIR Analysts
- Penetration Testers
- Security Engineers

---

# Learning Objectives

After completing this chapter, you will understand:

- Standard streams
- Input and output redirection
- Pipes
- Linux text processing philosophy
- Command chaining
- Building processing pipelines
- Enterprise log processing basics

---

# Why Text Processing Matters

Consider a production Linux server generating:

```text
Application Logs

↓

10 GB/day

↓

Millions of Log Entries

↓

Security Events

↓

Performance Metrics

↓

Audit Records
```

Reading such data manually is impossible.

Linux solves this problem using command-line text processing tools.

---

# Linux Philosophy

One of the Unix design principles is:

> **Write programs that do one thing well.**

Instead of creating one large application, Linux provides many small utilities that can be connected together.

Example:

```text
cat

↓

grep

↓

sort

↓

uniq

↓

wc
```

Each command performs a specific task, and the output of one command becomes the input of the next.

---

# Standard Streams

Every Linux process starts with three standard data streams.

| Stream | Number | Purpose |
|----------|---------|----------|
| Standard Input | 0 | Receives input |
| Standard Output | 1 | Produces normal output |
| Standard Error | 2 | Produces error messages |

These streams enable flexible redirection and automation.

---

# Standard Stream Diagram

```text
             Keyboard
                 │
                 ▼
        Standard Input (0)
                 │
                 ▼
            Application
          ┌──────────────┐
          │              │
          └──────────────┘
          │              │
          ▼              ▼
 Standard Output     Standard Error
       (1)                 (2)
          │                 │
          ▼                 ▼
      Terminal         Terminal
```

---

# Standard Input (stdin)

Standard Input is the source from which a program receives data.

Common sources include:

- Keyboard
- File
- Pipe
- Another command

Example:

```bash
cat
```

Typing:

```text
Hello Linux
```

Output:

```text
Hello Linux
```

The `cat` command reads from standard input until interrupted or an end-of-file signal is received.

---

# Standard Output (stdout)

Standard Output contains the normal results produced by a command.

Example:

```bash
date
```

Output:

```text
Thu Jul 23 10:30:00 IST 2026
```

By default, stdout is displayed on the terminal.

---

# Standard Error (stderr)

Errors are written to Standard Error.

Example:

```bash
ls missingfile
```

Output:

```text
ls: cannot access 'missingfile': No such file or directory
```

Separating normal output from error messages allows each stream to be handled independently.

---

# Why Separate stdout and stderr?

Suppose a backup script generates:

```text
Successful Files

↓

stdout

Failed Files

↓

stderr
```

Administrators can:

- Save successful results.
- Record errors separately.
- Monitor failures automatically.

This separation improves automation and troubleshooting.

---

# Output Redirection

Linux allows command output to be written somewhere other than the terminal.

General syntax:

```bash
command > file
```

Instead of displaying output, it is written to the specified file.

---

# Redirect stdout

Example:

```bash
date > today.txt
```

Result:

```text
today.txt
```

Contents:

```text
Thu Jul 23 10:30:00 IST 2026
```

If the file does not exist, it is created.

---

# Overwrite Behavior

Using:

```bash
>
```

overwrites the destination file.

Example:

```bash
echo "Linux" > notes.txt
```

Then:

```bash
echo "Security" > notes.txt
```

Final content:

```text
Security
```

The previous contents are replaced.

---

# Append Output

Use:

```bash
>>
```

Example:

```bash
echo "Linux" > notes.txt

echo "Security" >> notes.txt
```

Result:

```text
Linux

Security
```

The existing contents are preserved and new data is appended.

---

# Redirect Standard Error

Redirect only error messages:

```bash
ls missingfile 2> errors.log
```

Terminal:

```text
(no error displayed)
```

File:

```text
errors.log
```

Contains:

```text
ls: cannot access 'missingfile': No such file or directory
```

---

# Append Standard Error

```bash
command 2>> errors.log
```

This appends new error messages without overwriting the existing log.

---

# Redirect Both stdout and stderr

One common approach:

```bash
command > output.log 2> errors.log
```

Normal output:

```text
output.log
```

Errors:

```text
errors.log
```

Keeping these separate simplifies troubleshooting.

---

# Combine stdout and stderr

Redirect both streams into one file:

```bash
command > complete.log 2>&1
```

Explanation:

```text
stdout

↓

complete.log

stderr

↓

complete.log
```

Both streams are stored together in execution order.

---

# Discard Output

Linux provides a special device:

```text
/dev/null
```

Anything written to `/dev/null` is discarded.

Suppress stdout:

```bash
command > /dev/null
```

Suppress stderr:

```bash
command 2> /dev/null
```

Suppress both:

```bash
command > /dev/null 2>&1
```

This is useful for scripts where specific output is intentionally ignored.

---

# Input Redirection

Programs can receive input from a file instead of the keyboard.

Example:

```bash
sort < names.txt
```

Workflow:

```text
names.txt

↓

stdin

↓

sort

↓

stdout
```

---

# Pipes

One of Linux's most powerful features is the pipe operator.

Symbol:

```text
|
```

A pipe sends the output of one command directly to another command.

---

# Pipe Workflow

```text
Command A

↓

stdout

↓

Pipe

↓

stdin

↓

Command B
```

No temporary files are required.

---

# Basic Pipe Example

```bash
ls -l | less
```

Workflow:

```text
ls -l

↓

less
```

Useful when command output is longer than one screen.

---

# Another Pipe Example

```bash
cat access.log | wc
```

Workflow:

```text
Log File

↓

cat

↓

wc
```

The `wc` command counts information from the incoming text stream.

---

# Multi-Command Pipeline

Linux pipelines can contain many commands.

Example:

```text
Command

↓

Filter

↓

Transform

↓

Sort

↓

Count

↓

Report
```

Complex processing can often be performed without writing custom programs.

---

# Advantages of Pipes

Benefits include:

- Reduced temporary files
- Improved readability
- Efficient processing
- Easy automation
- Modular workflows
- Reusable command combinations

---

# Command Chaining vs Pipes

These concepts are related but different.

| Feature | Pipe (`|`) | Command Chaining (`&&`, `;`, `||`) |
|----------|------------|-------------------------------------|
| Passes output | Yes | No |
| Controls execution | No | Yes |
| Shares data | Yes | No |

Pipes transfer data, while command chaining controls execution flow.

---

# Command Chaining Examples

Run sequentially:

```bash
pwd ; ls
```

Run second command only if the first succeeds:

```bash
mkdir Backup && cd Backup
```

Run second command only if the first fails:

```bash
ls missingfile || echo "File not found"
```

---

# Enterprise Log Processing Workflow

```text
Application

↓

Log File

↓

Text Processing

↓

Filtering

↓

Alert Detection

↓

Dashboard

↓

Security Team
```

This pipeline is common in SIEM and centralized logging environments.

---

# Cybersecurity Perspective

Security teams rely heavily on standard streams and pipelines to:

- Filter authentication logs.
- Process firewall events.
- Analyze web server logs.
- Identify failed login attempts.
- Investigate incidents.
- Automate detection workflows.

Many security tools are designed to integrate into Unix-style pipelines.

---

# Business Impact

Efficient text processing enables organizations to:

- Analyze large datasets quickly.
- Automate operational tasks.
- Improve troubleshooting.
- Accelerate incident response.
- Reduce manual effort.
- Support scalable log analysis.

---

# Enterprise Best Practices

- Redirect output intentionally; avoid overwriting important files.
- Separate standard output from standard error during automation.
- Use pipes to build modular processing workflows.
- Suppress unnecessary output only when appropriate.
- Document complex command pipelines in operational runbooks.
- Validate command results before using them in production scripts.

---

# Key Takeaways

- Linux processes communicate using standard input, output, and error streams.
- Redirection changes where data is read from or written to.
- Pipes connect commands into efficient processing pipelines.
- Command chaining controls execution flow, while pipes transfer data.
- These concepts form the foundation for advanced Linux text processing.

---


