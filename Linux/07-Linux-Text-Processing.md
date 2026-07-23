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


# Part 2 — grep, egrep, Regular Expressions, sort, uniq, cut, paste, tr, and wc

---

# Introduction

Once text is flowing through pipelines, Linux provides utilities to:

- Search text
- Filter information
- Count entries
- Extract fields
- Remove duplicates
- Transform characters
- Combine files
- Generate statistics

These commands are used daily by:

- Linux Administrators
- DevOps Engineers
- Cloud Engineers
- SOC Analysts
- DFIR Analysts
- Threat Hunters
- Security Engineers

Mastering these utilities allows administrators to analyze gigabytes of logs using only a few commands.

---

# Linux Text Processing Pipeline

```text
Raw File

↓

grep

↓

cut

↓

sort

↓

uniq

↓

wc

↓

Report
```

Each utility performs one focused task, making pipelines modular and reusable.

---

# grep

**grep** (Global Regular Expression Print) searches text for matching patterns.

General syntax:

```bash
grep "pattern" filename
```

Example:

```bash
grep "error" system.log
```

This displays every line containing the word `error`.

---

# Case-Insensitive Search

Ignore letter case:

```bash
grep -i "failed" auth.log
```

Matches:

```text
FAILED

Failed

failed
```

---

# Show Line Numbers

```bash
grep -n "root" passwd
```

Example output:

```text
1:root:x:0:0:root:/root:/bin/bash
```

Useful when reviewing configuration files.

---

# Count Matches

Instead of displaying matching lines:

```bash
grep -c "ERROR" app.log
```

Example:

```text
24
```

Returns the number of matching lines.

---

# Invert Search

Display lines **not** matching a pattern:

```bash
grep -v "^#" sshd_config
```

Common use:

- Ignore comments
- Display active configuration entries

---

# Recursive Search

Search an entire directory tree:

```bash
grep -r "password" /etc
```

Typical applications:

- Configuration audits
- Source code review
- Security investigations

---

# Multiple Patterns

Search for several alternatives:

```bash
grep -E "error|warning|critical" system.log
```

The `-E` option enables extended regular expressions.

---

# egrep

Historically:

```bash
egrep
```

was used for extended regular expressions.

Modern Linux systems generally recommend:

```bash
grep -E
```

Both perform equivalent pattern matching in most environments.

---

# What Are Regular Expressions?

A **regular expression (regex)** describes a search pattern rather than literal text.

Instead of searching only for:

```text
error
```

Regex allows matching many related strings.

---

# Basic Regular Expression Symbols

| Symbol | Meaning |
|----------|----------|
| `.` | Any single character |
| `*` | Zero or more occurrences |
| `^` | Beginning of line |
| `$` | End of line |
| `[]` | Character class |
| `[^ ]` | Negated character class |
| `+` | One or more occurrences (extended regex) |
| `?` | Zero or one occurrence (extended regex) |
| `|` | Alternation (OR) |

---

# Beginning of Line

Match lines beginning with `root`:

```bash
grep "^root" /etc/passwd
```

Example:

```text
root:x:0:0:root:/root:/bin/bash
```

---

# End of Line

Match lines ending with `/bin/bash`:

```bash
grep "/bin/bash$" /etc/passwd
```

---

# Wildcard Character

Example:

```bash
grep "r..t"
```

Matches:

```text
root

rust

rAAt
```

The period (`.`) matches any single character.

---

# Character Classes

Example:

```bash
grep "[0-9]"
```

Matches any line containing at least one digit.

Examples:

```text
user1

eth0

2026
```

---

# Negated Character Classes

Example:

```bash
grep "^[^#]"
```

Matches lines that do **not** begin with `#`.

Commonly used to display active configuration settings.

---

# Practical grep Examples

Find failed SSH logins:

```bash
grep "Failed password" auth.log
```

Find successful SSH logins:

```bash
grep "Accepted password" auth.log
```

Locate IPv4 addresses (simple example):

```bash
grep -E "[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+" access.log
```

---

# sort

The `sort` command arranges text in a specified order.

Example:

```bash
sort users.txt
```

Input:

```text
Charlie

Alice

Bob
```

Output:

```text
Alice

Bob

Charlie
```

---

# Reverse Sort

```bash
sort -r users.txt
```

Output:

```text
Charlie

Bob

Alice
```

---

# Numeric Sort

```bash
sort -n scores.txt
```

Input:

```text
20

3

100
```

Output:

```text
3

20

100
```

Without `-n`, values are sorted alphabetically.

---

# Remove Duplicate Lines

Use:

```bash
sort users.txt | uniq
```

Since `uniq` compares adjacent lines, sorting first is a common practice.

---

# uniq

The `uniq` command removes consecutive duplicate lines.

Example:

Input:

```text
Alice

Alice

Bob

Bob

Charlie
```

Command:

```bash
uniq names.txt
```

Output:

```text
Alice

Bob

Charlie
```

---

# Count Duplicates

```bash
uniq -c names.txt
```

Example:

```text
2 Alice

2 Bob

1 Charlie
```

Useful for summarizing repeated values.

---

# Display Only Repeated Lines

```bash
uniq -d names.txt
```

Displays only duplicated entries.

---

# cut

The `cut` command extracts selected portions of each line.

Typical uses:

- CSV files
- Log analysis
- Delimited text
- User databases

---

# Extract Characters

```bash
cut -c1-5 file.txt
```

Displays characters 1 through 5 from each line.

---

# Extract Fields

Given:

```text
Alice,HR

Bob,IT

Charlie,Finance
```

Command:

```bash
cut -d "," -f1 employees.csv
```

Output:

```text
Alice

Bob

Charlie
```

Explanation:

| Option | Purpose |
|----------|----------|
| `-d` | Delimiter |
| `-f` | Field number |

---

# Extract Multiple Fields

```bash
cut -d ":" -f1,7 /etc/passwd
```

Displays:

- Username
- Login shell

This is useful for reviewing account configurations.

---

# paste

The `paste` command merges lines from multiple files.

Example:

File 1:

```text
Alice

Bob
```

File 2:

```text
HR

IT
```

Command:

```bash
paste names.txt departments.txt
```

Output:

```text
Alice    HR

Bob      IT
```

---

# Change Delimiter

Example:

```bash
paste -d "," file1 file2
```

Output:

```text
Alice,HR

Bob,IT
```

---

# tr

The `tr` command translates or deletes characters.

Common uses:

- Case conversion
- Character replacement
- Removing unwanted characters

---

# Convert Lowercase to Uppercase

```bash
echo "linux" | tr 'a-z' 'A-Z'
```

Output:

```text
LINUX
```

---

# Convert Uppercase to Lowercase

```bash
echo "SECURITY" | tr 'A-Z' 'a-z'
```

Output:

```text
security
```

---

# Delete Characters

Remove digits:

```bash
echo "abc123" | tr -d '0-9'
```

Output:

```text
abc
```

---

# Replace Characters

Replace spaces with underscores:

```bash
echo "Linux Security" | tr ' ' '_'
```

Output:

```text
Linux_Security
```

---

# wc

The `wc` (word count) utility summarizes text.

Example:

```bash
wc notes.txt
```

Output:

```text
15 120 980 notes.txt
```

Meaning:

| Value | Description |
|----------|-------------|
| First | Lines |
| Second | Words |
| Third | Bytes |

---

# Count Lines Only

```bash
wc -l access.log
```

---

# Count Words

```bash
wc -w article.txt
```

---

# Count Characters

```bash
wc -m notes.txt
```

---

# Enterprise Example

Count failed SSH logins:

```bash
grep "Failed password" auth.log | wc -l
```

Workflow:

```text
Authentication Log

↓

grep

↓

Failed Entries

↓

wc

↓

Total Failed Logins
```

This type of pipeline is common in security monitoring.

---

# Combining Multiple Commands

Example:

```bash
cat access.log \
| grep "404" \
| cut -d " " -f1 \
| sort \
| uniq -c \
| sort -nr
```

Workflow:

```text
Access Log

↓

grep

↓

cut

↓

sort

↓

uniq

↓

sort

↓

Ranked Report
```

This identifies the IP addresses generating the most HTTP 404 responses.

---

# Cybersecurity Perspective

Security teams frequently use these tools to:

- Detect repeated authentication failures.
- Analyze firewall logs.
- Search indicators of compromise (IOCs).
- Count suspicious events.
- Extract IP addresses.
- Identify unusual activity patterns.
- Build lightweight detection pipelines.

These commands are foundational for SOC investigations and threat hunting.

---

# Business Impact

Efficient text processing enables organizations to:

- Analyze large log volumes quickly.
- Improve troubleshooting.
- Automate reporting.
- Reduce manual effort.
- Accelerate incident response.
- Support compliance and audit activities.

---

# Enterprise Best Practices

- Use `grep -E` instead of legacy `egrep` in new scripts.
- Prefer pipelines over temporary intermediate files when practical.
- Sort data before using `uniq` unless the input is already grouped.
- Validate regular expressions against representative sample data.
- Document complex command pipelines used in operational procedures.
- Test text-processing commands on non-production data before running them on critical systems.

---

# Key Takeaways

- `grep` is the primary tool for searching text.
- Regular expressions provide flexible and powerful pattern matching.
- `sort` and `uniq` organize and summarize data.
- `cut`, `paste`, and `tr` extract, combine, and transform text.
- `wc` generates useful statistics for text files and command output.
- Combining small tools into pipelines is a core strength of Linux text processing.

---


