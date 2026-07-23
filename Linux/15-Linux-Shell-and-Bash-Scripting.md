# 15 - Linux Shell and Bash Scripting

# Part 1 — Shell Fundamentals, Types of Shells, Bash Basics, Environment Variables, Shell Expansion, and Command-Line Essentials

---

# Introduction

The Linux shell is one of the most powerful interfaces available to system administrators, DevOps engineers, cloud engineers, and cybersecurity professionals.

Unlike graphical interfaces (GUIs), the shell provides:

- Complete system control
- Automation capabilities
- Remote administration
- Script execution
- Process management
- System monitoring
- Rapid troubleshooting

In enterprise environments, nearly every administrative task can be performed through the shell.

---

# Learning Objectives

After completing this chapter, you will understand:

- What a shell is
- Types of Linux shells
- Bash fundamentals
- Command syntax
- Environment variables
- Shell expansion
- Command history
- Aliases
- Shell initialization files

---

# What is a Shell?

A **shell** is a command-line interpreter that acts as an interface between the user and the Linux kernel.

It accepts commands from the user, interprets them, and requests the kernel to perform the required operations.

---

# Shell Architecture

```text
User

↓

Shell (Bash)

↓

Kernel

↓

Hardware
```

---

# Shell Responsibilities

The shell is responsible for:

- Reading commands
- Parsing input
- Expanding variables
- Executing programs
- Managing jobs
- Handling redirection
- Creating pipelines
- Running scripts

---

# Why Use the Shell?

Advantages include:

- Faster administration
- Automation of repetitive tasks
- Remote management through SSH
- Low resource consumption
- Fine-grained system control
- Powerful scripting capabilities

---

# GUI vs Shell

| GUI | Shell |
|------|-------|
| Mouse-driven | Keyboard-driven |
| Easy for beginners | Powerful for advanced users |
| Limited automation | Extensive automation |
| Higher resource usage | Lightweight |
| Best for occasional tasks | Best for repetitive and enterprise tasks |

---

# Common Linux Shells

| Shell | Description |
|--------|-------------|
| Bash | Bourne Again Shell (default on many distributions) |
| Sh | Bourne Shell |
| Zsh | Extended interactive shell |
| Ksh | Korn Shell |
| Fish | Friendly Interactive Shell |
| Tcsh | Enhanced C Shell |

---

# Bash (Bourne Again Shell)

Bash is the most widely used Linux shell.

Features include:

- Command history
- Tab completion
- Variables
- Aliases
- Scripting
- Job control
- Arithmetic operations
- Shell expansion

Bash is the standard shell on many enterprise Linux systems.

---

# Checking the Current Shell

Display the current shell:

```bash
echo $SHELL
```

Example:

```text
/bin/bash
```

Display the current process shell:

```bash
ps -p $$
```

---

# Changing the Default Shell

View available shells:

```bash
cat /etc/shells
```

Change your login shell:

```bash
chsh
```

> Changes typically take effect after logging out and back in.

---

# Command Syntax

Most Linux commands follow this format:

```text
command [options] [arguments]
```

Example:

```bash
ls -l /home
```

Where:

| Component | Meaning |
|-----------|---------|
| `ls` | Command |
| `-l` | Option |
| `/home` | Argument |

---

# Understanding Options

Short option:

```bash
ls -a
```

Long option:

```bash
ls --all
```

Multiple short options:

```bash
ls -lah
```

Equivalent:

```bash
ls -l -a -h
```

---

# Built-in Commands vs External Commands

| Built-in | External |
|-----------|-----------|
| Executed by the shell | Separate executable |
| Faster | Located in the filesystem |
| Example: `cd` | Example: `ls` |

Determine command type:

```bash
type ls
```

Example:

```bash
type cd
```

---

# Finding Executables

Locate an executable:

```bash
which python3
```

Search executable paths:

```bash
whereis bash
```

Display command information:

```bash
type grep
```

---

# Getting Help

View a command's manual:

```bash
man ls
```

Quick help:

```bash
ls --help
```

Command summary:

```bash
whatis ls
```

Search manual pages:

```bash
apropos network
```

---

# Command History

Display history:

```bash
history
```

Execute the previous command:

```bash
!!
```

Execute a specific command by history number:

```bash
!125
```

Search interactively:

Press:

```text
Ctrl + R
```

---

# Clearing the Terminal

```bash
clear
```

Shortcut:

```text
Ctrl + L
```

---

# Environment Variables

Environment variables store configuration information used by the shell and applications.

Examples include:

- User information
- Home directory
- Current shell
- Search paths
- Language settings

---

# Viewing Environment Variables

Display all variables:

```bash
printenv
```

Or:

```bash
env
```

Display a specific variable:

```bash
echo $HOME
```

---

# Common Environment Variables

| Variable | Purpose |
|----------|----------|
| `HOME` | User's home directory |
| `PATH` | Search path for executables |
| `USER` | Current username |
| `PWD` | Current working directory |
| `SHELL` | Current login shell |
| `HOSTNAME` | System hostname |
| `LANG` | Language and locale |
| `TERM` | Terminal type |

---

# The PATH Variable

The `PATH` variable tells the shell where to search for executable programs.

Display it:

```bash
echo $PATH
```

Example:

```text
/usr/local/bin:/usr/bin:/bin
```

The shell searches these directories from left to right.

---

# Modifying PATH (Current Session)

Temporarily append a directory:

```bash
export PATH=$PATH:/opt/scripts
```

Verify:

```bash
echo $PATH
```

Changes affect only the current shell session unless added to a shell startup file.

---

# Creating Environment Variables

Create a shell variable:

```bash
PROJECT=LinuxGuide
```

Display it:

```bash
echo $PROJECT
```

Export it to child processes:

```bash
export PROJECT
```

---

# Shell Variables vs Environment Variables

| Shell Variable | Environment Variable |
|----------------|----------------------|
| Available only in current shell | Inherited by child processes after export |
| Created without `export` | Created or promoted with `export` |
| Local scope | Broader process scope |

---

# Quoting in Bash

## Single Quotes

Treat all enclosed characters literally:

```bash
echo '$HOME'
```

Output:

```text
$HOME
```

---

## Double Quotes

Allow variable expansion:

```bash
echo "$HOME"
```

Output:

```text
/home/user
```

---

## No Quotes

The shell performs word splitting and expansion where applicable.

Example:

```bash
echo $USER
```

---

# Shell Expansion

Before executing a command, Bash performs several expansions.

Common types include:

- Variable expansion
- Command substitution
- Arithmetic expansion
- Brace expansion
- Filename (glob) expansion
- Tilde expansion

---

# Variable Expansion

```bash
echo $USER
```

Output:

```text
alice
```

---

# Tilde Expansion

```bash
cd ~
```

Equivalent to:

```bash
cd $HOME
```

---

# Brace Expansion

```bash
echo file{1..5}.txt
```

Output:

```text
file1.txt file2.txt file3.txt file4.txt file5.txt
```

Useful for creating multiple files:

```bash
touch report{1..10}.log
```

---

# Wildcard (Glob) Expansion

| Pattern | Matches |
|----------|----------|
| `*` | Zero or more characters |
| `?` | Exactly one character |
| `[abc]` | One character from the set |
| `[0-9]` | Any digit |
| `[a-z]` | Lowercase letters |

Example:

```bash
ls *.txt
```

---

# Arithmetic Expansion

```bash
echo $((5 + 7))
```

Output:

```text
12
```

Another example:

```bash
echo $((10 * 3))
```

---

# Command Substitution

Execute a command and substitute its output.

Preferred syntax:

```bash
echo $(date)
```

Legacy syntax:

```bash
echo `date`
```

The `$(...)` form is recommended for readability and nesting.

---

# Aliases

Aliases create shortcuts for frequently used commands.

Create:

```bash
alias ll='ls -lah'
```

Use:

```bash
ll
```

List aliases:

```bash
alias
```

Remove:

```bash
unalias ll
```

---

# Shell Initialization Files

These files configure the shell environment.

| File | Purpose |
|------|----------|
| `~/.bashrc` | Interactive shell configuration |
| `~/.bash_profile` | Login shell configuration (common on some systems) |
| `~/.profile` | Generic login configuration |
| `/etc/profile` | System-wide login configuration |
| `/etc/bash.bashrc` or distribution equivalent | System-wide interactive Bash configuration (distribution-dependent) |

---

# Reloading Configuration

Apply changes without logging out:

```bash
source ~/.bashrc
```

Equivalent:

```bash
. ~/.bashrc
```

---

# Enterprise Shell Workflow

```text
Administrator

↓

Bash Shell

↓

Command Parsing

↓

Expansion

↓

Execution

↓

Kernel

↓

System Resources
```

---

# Cybersecurity Perspective

The shell is a primary interface for both defenders and attackers.

Security teams use Bash to:

- Analyze logs
- Collect forensic artifacts
- Monitor processes
- Automate incident response
- Audit permissions
- Investigate network activity

Because shell commands can significantly impact a system, administrators should:

- Follow the principle of least privilege.
- Validate commands before execution.
- Avoid running unknown scripts.
- Record and audit administrative activity where appropriate.

---

# Business Impact

Efficient shell usage provides:

- Faster administration
- Reduced operational costs
- Improved automation
- Better consistency
- Faster troubleshooting
- Greater operational efficiency

Organizations relying on automation often use shell scripts as a foundation for deployment and maintenance workflows.

---

# Enterprise Best Practices

- Use descriptive aliases sparingly and document them.
- Prefer `$(...)` for command substitution.
- Store persistent customizations in appropriate shell initialization files.
- Avoid modifying `PATH` unnecessarily.
- Quote variables unless unquoted behavior is explicitly required.
- Review shell history before sharing terminals or screenshots.
- Test commands in non-production environments when possible.

---

# Key Takeaways

- The shell provides the primary command-line interface to Linux.
- Bash is the most widely used Linux shell.
- Environment variables control many aspects of the shell environment.
- Shell expansion occurs before command execution.
- Aliases and initialization files improve productivity and consistency.
- Strong shell skills are essential for Linux administration, DevOps, and cybersecurity.

---


# 15 - Linux Shell and Bash Scripting

# Part 2 — Input/Output Redirection, Pipes, Variables, User Input, Command Substitution, and Bash Scripting Fundamentals

---

# Introduction

The true power of Bash comes from combining commands, redirecting input and output, using variables, and automating tasks through scripts.

Instead of manually performing repetitive tasks, administrators write Bash scripts to:

- Provision servers
- Monitor services
- Rotate logs
- Deploy applications
- Perform backups
- Analyze security events
- Generate reports
- Automate incident response

Almost every enterprise Linux environment relies heavily on shell scripting.

---

# Bash Scripting Workflow

```text
Script

↓

Bash Interpreter

↓

Commands

↓

Kernel

↓

System Resources

↓

Output
```

---

# Standard Streams

Every Linux process starts with three standard streams.

| Stream | Number | Purpose |
|---------|--------|----------|
| Standard Input | 0 | Input to program |
| Standard Output | 1 | Normal output |
| Standard Error | 2 | Error messages |

---

# Standard Stream Diagram

```text
             Keyboard
                │
                ▼
      Standard Input (0)
                │
                ▼
            Program
          ▲         ▲
          │         │
          │         │
 Std Output(1)  Std Error(2)
          │         │
          ▼         ▼
       Terminal   Terminal
```

---

# Input Redirection

Input can come from files instead of the keyboard.

Example:

```bash
sort < names.txt
```

Workflow:

```text
File

↓

Program

↓

Output
```

---

# Output Redirection

Overwrite output:

```bash
ls > files.txt
```

The file is created if it does not exist.

If it exists, its previous contents are replaced.

---

# Append Output

Append instead of overwrite:

```bash
date >> log.txt
```

Example:

```text
Run 1

Run 2

Run 3
```

---

# Redirecting Errors

Redirect only errors:

```bash
find /root 2> errors.log
```

Useful when collecting error information separately.

---

# Append Errors

```bash
find /root 2>> errors.log
```

---

# Redirect Both Output and Errors

```bash
command > output.log 2>&1
```

Modern Bash syntax:

```bash
command &> output.log
```

---

# Discard Output

Linux provides a special device:

```text
/dev/null
```

Ignore output:

```bash
command > /dev/null
```

Ignore errors:

```bash
command 2> /dev/null
```

Ignore both:

```bash
command &> /dev/null
```

---

# Redirection Summary

| Operator | Meaning |
|-----------|----------|
| `>` | Overwrite output |
| `>>` | Append output |
| `<` | Read input |
| `2>` | Redirect errors |
| `2>>` | Append errors |
| `&>` | Redirect output and errors |
| `/dev/null` | Discard data |

---

# Pipes

A pipe (`|`) sends the output of one command directly into another.

Instead of storing intermediate results in a file, data flows between commands.

---

# Pipe Workflow

```text
Command A

↓

Pipe

↓

Command B
```

---

# Example

```bash
ls -l | less
```

Workflow:

```text
Directory Listing

↓

less

↓

Scrollable Output
```

---

# Counting Files

```bash
ls | wc -l
```

Meaning:

```text
List Files

↓

Count Lines

↓

Number of Files
```

---

# Searching Output

```bash
ps -ef | grep ssh
```

Workflow:

```text
Running Processes

↓

grep ssh

↓

Matching Processes
```

---

# Multiple Pipes

```bash
cat access.log | grep ERROR | sort | uniq
```

Workflow:

```text
Log File

↓

Filter

↓

Sort

↓

Remove Duplicates
```

---

# Tee Command

Display output while saving it.

```bash
ls | tee files.txt
```

Workflow:

```text
Program

↓

tee

├── Terminal

└── File
```

Useful for:

- Logging
- Debugging
- Reports

---

# Xargs

Convert standard input into command arguments.

Example:

```bash
find . -name "*.log" | xargs rm
```

Safer alternative for filenames containing spaces:

```bash
find . -name "*.log" -print0 | xargs -0 rm
```

Always review the results before deleting files, especially in production systems.

---

# Command Substitution

Use the output of one command inside another.

Preferred syntax:

```bash
echo "Today is $(date)"
```

Output:

```text
Today is Tue Jul 21
```

Nested example:

```bash
echo "$(whoami) logged in from $(hostname)"
```

---

# Arithmetic Expansion

```bash
echo $((25 + 10))
```

Output:

```text
35
```

Additional examples:

```bash
echo $((20 * 4))
```

```bash
echo $((100 / 5))
```

---

# Creating Bash Scripts

Create a file:

```bash
nano hello.sh
```

Example:

```bash
#!/bin/bash

echo "Hello Linux"
```

---

# Shebang

Every Bash script usually begins with:

```bash
#!/bin/bash
```

or, for improved portability:

```bash
#!/usr/bin/env bash
```

The shebang specifies the interpreter used to execute the script.

---

# Making Scripts Executable

Grant execute permission:

```bash
chmod +x hello.sh
```

Run:

```bash
./hello.sh
```

Or:

```bash
bash hello.sh
```

---

# Script Execution Flow

```text
Script

↓

Bash Interpreter

↓

Execute Commands

↓

Output
```

---

# Comments

Single-line comment:

```bash
# This is a comment
```

Comments improve readability and maintainability.

---

# Variables

Assign a variable:

```bash
NAME="Anurag"
```

Display:

```bash
echo "$NAME"
```

---

# Variable Rules

Valid:

```bash
USER_NAME
```

```bash
count
```

```bash
PORT1
```

Invalid:

```text
1NAME

USER-NAME

MY VALUE
```

---

# Variable Example

```bash
SERVER="web01"

echo "$SERVER"
```

Output:

```text
web01
```

---

# Read User Input

```bash
read NAME
```

Example:

```bash
echo "Enter your name:"

read NAME

echo "Hello $NAME"
```

---

# Prompt with `read`

```bash
read -p "Username: " USER
```

Example:

```text
Username:
```

---

# Hidden Password Input

```bash
read -s PASSWORD
```

No characters are displayed while typing.

---

# Positional Parameters

Arguments passed to scripts.

Example:

```bash
./backup.sh home
```

Inside the script:

```bash
echo "$1"
```

Output:

```text
home
```

---

# Common Positional Parameters

| Parameter | Meaning |
|------------|----------|
| `$0` | Script name |
| `$1` | First argument |
| `$2` | Second argument |
| `$#` | Number of arguments |
| `$@` | All arguments (recommended for iteration) |
| `$*` | All arguments as a single word in some contexts |
| `$$` | Current shell process ID |
| `$?` | Exit status of the previous command |

---

# Exit Status

Every command returns an exit code.

```text
0 = Success

Non-zero = Failure or specific condition
```

Example:

```bash
ls

echo $?
```

---

# Testing Exit Status

```bash
mkdir project

echo $?
```

A successful command returns:

```text
0
```

Checking exit codes is essential for reliable automation.

---

# Quoting Variables

Recommended:

```bash
echo "$HOME"
```

Avoid unquoted variables when they may contain spaces or special characters.

Example:

```bash
FILE="My Report.txt"

cat "$FILE"
```

---

# Basic Script Example

```bash
#!/bin/bash

echo "System Information"

echo "Hostname: $(hostname)"

echo "User: $(whoami)"

echo "Date: $(date)"
```

---

# Backup Script Example

```bash
#!/bin/bash

cp report.txt report.bak

echo "Backup Complete"
```

---

# Enterprise Script Workflow

```text
Administrator

↓

Run Script

↓

Collect Data

↓

Execute Commands

↓

Generate Report

↓

Log Results
```

---

# Common Beginner Mistakes

| Mistake | Correct Practice |
|----------|------------------|
| Missing shebang | Add a shebang at the top of the script |
| Forgetting execute permission | Use `chmod +x` |
| Unquoted variables | Quote variables when appropriate |
| Ignoring exit codes | Check `$?` or use conditional logic |
| Overwriting files unintentionally | Use `>>` when appending is intended |
| Deleting without validation | Review commands before execution |

---

# Cybersecurity Perspective

Bash scripting is widely used in security operations.

Typical use cases include:

- Log collection
- IOC searches
- User auditing
- Network monitoring
- Malware triage
- File integrity checks
- Backup verification
- Security reporting

Scripts should be reviewed carefully to avoid:

- Command injection
- Unsafe handling of user input
- Hard-coded secrets
- Excessive privileges

---

# Business Impact

Automation with Bash provides:

- Faster operations
- Consistent system administration
- Reduced human error
- Lower operational costs
- Rapid incident response
- Improved compliance through repeatable processes

---

# Enterprise Best Practices

- Use meaningful variable names.
- Prefer `#!/usr/bin/env bash` for portability unless a fixed interpreter path is required.
- Quote variables unless unquoted expansion is intentional.
- Validate user input.
- Log important actions and errors.
- Test scripts in non-production environments first.
- Keep scripts modular and well documented.
- Use version control for production scripts.

---

# Key Takeaways

- Linux programs communicate using standard input, output, and error streams.
- Redirection and pipes allow commands to be combined into powerful workflows.
- Variables and positional parameters make scripts reusable.
- Command substitution and arithmetic expansion simplify automation.
- Exit codes are fundamental for writing reliable scripts.
- Bash scripting is an essential enterprise automation skill.

---


# 15 - Linux Shell and Bash Scripting

# Part 3 — Conditional Statements, Loops, Functions, Arrays, Error Handling, Debugging, and Advanced Bash Scripting

---

# Introduction

Enterprise Bash scripts rarely consist of a few simple commands.

Production scripts commonly include:

- Decision making
- Repeated execution
- Functions
- Arrays
- Error handling
- Logging
- Debugging
- Defensive programming

These features make scripts reliable, maintainable, and scalable.

---

# Advanced Script Workflow

```text
Start

↓

Initialize Variables

↓

Validate Input

↓

Execute Functions

↓

Handle Errors

↓

Generate Output

↓

Log Results

↓

Exit
```

---

# Conditional Statements

Conditional statements allow scripts to execute different actions depending on conditions.

Common constructs:

- `if`
- `if-else`
- `elif`
- `case`

---

# Basic `if` Statement

Syntax:

```bash
if condition
then
    commands
fi
```

Example:

```bash
#!/usr/bin/env bash

NUMBER=10

if [ "$NUMBER" -gt 5 ]
then
    echo "Greater than 5"
fi
```

---

# `if-else`

```bash
#!/usr/bin/env bash

AGE=16

if [ "$AGE" -ge 18 ]
then
    echo "Adult"
else
    echo "Minor"
fi
```

---

# `elif`

```bash
#!/usr/bin/env bash

MARKS=82

if [ "$MARKS" -ge 90 ]
then
    echo "Grade A"
elif [ "$MARKS" -ge 75 ]
then
    echo "Grade B"
else
    echo "Grade C"
fi
```

---

# Comparison Operators

## Numeric Operators

| Operator | Meaning |
|-----------|----------|
| `-eq` | Equal |
| `-ne` | Not equal |
| `-gt` | Greater than |
| `-lt` | Less than |
| `-ge` | Greater than or equal |
| `-le` | Less than or equal |

Example:

```bash
[ "$A" -gt "$B" ]
```

---

## String Operators

| Operator | Meaning |
|-----------|----------|
| `=` | Equal |
| `!=` | Not equal |
| `-z` | Empty string |
| `-n` | Non-empty string |

Example:

```bash
[ "$USER" = "root" ]
```

---

## File Test Operators

| Operator | Meaning |
|-----------|----------|
| `-f` | Regular file exists |
| `-d` | Directory exists |
| `-r` | Readable |
| `-w` | Writable |
| `-x` | Executable |
| `-e` | Path exists |
| `-s` | File exists and is not empty |

Example:

```bash
if [ -f "/etc/passwd" ]
then
    echo "File exists"
fi
```

---

# Logical Operators

AND:

```bash
[ "$A" -gt 5 ] && [ "$A" -lt 20 ]
```

OR:

```bash
[ "$USER" = "root" ] || [ "$USER" = "admin" ]
```

NOT:

```bash
[ ! -f secret.txt ]
```

---

# `case` Statement

Useful when evaluating multiple fixed options.

Example:

```bash
#!/usr/bin/env bash

read -p "Choose (start|stop): " ACTION

case "$ACTION" in
    start)
        echo "Starting service"
        ;;
    stop)
        echo "Stopping service"
        ;;
    *)
        echo "Invalid option"
        ;;
esac
```

---

# Loops

Loops repeat commands until a condition changes.

Types:

- `for`
- `while`
- `until`
- Nested loops

---

# `for` Loop

```bash
for i in 1 2 3 4 5
do
    echo "$i"
done
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

# Range Loop

```bash
for i in {1..10}
do
    echo "$i"
done
```

---

# Loop Through Files

```bash
for FILE in *.txt
do
    echo "$FILE"
done
```

---

# C-Style `for` Loop

```bash
for ((i=1; i<=5; i++))
do
    echo "$i"
done
```

---

# `while` Loop

```bash
COUNT=1

while [ "$COUNT" -le 5 ]
do
    echo "$COUNT"
    COUNT=$((COUNT + 1))
done
```

---

# `until` Loop

Runs until the condition becomes true.

```bash
COUNT=1

until [ "$COUNT" -gt 5 ]
do
    echo "$COUNT"
    COUNT=$((COUNT + 1))
done
```

---

# `break`

Terminate a loop immediately.

```bash
for i in {1..10}
do
    if [ "$i" -eq 5 ]
    then
        break
    fi

    echo "$i"
done
```

---

# `continue`

Skip the current iteration.

```bash
for i in {1..5}
do
    if [ "$i" -eq 3 ]
    then
        continue
    fi

    echo "$i"
done
```

---

# Arrays

Arrays store multiple values.

Declare:

```bash
FRUITS=("Apple" "Orange" "Banana")
```

Access first element:

```bash
echo "${FRUITS[0]}"
```

---

# Array Operations

Display all values:

```bash
echo "${FRUITS[@]}"
```

Display array size:

```bash
echo "${#FRUITS[@]}"
```

Add an element:

```bash
FRUITS+=("Mango")
```

---

# Loop Through Arrays

```bash
for ITEM in "${FRUITS[@]}"
do
    echo "$ITEM"
done
```

---

# Functions

Functions group reusable commands.

Syntax:

```bash
function_name() {

    commands

}
```

---

# Function Example

```bash
greet() {

    echo "Welcome to Linux"

}

greet
```

---

# Function with Arguments

```bash
greet() {

    echo "Hello $1"

}

greet "Anurag"
```

---

# Returning Values

Functions return exit codes using `return`.

Example:

```bash
check_file() {

    [ -f "$1" ]

}

check_file "/etc/passwd"

echo $?
```

For textual output, use `echo` inside the function and capture it with command substitution if needed.

---

# Local Variables

Limit variable scope:

```bash
example() {

    local NAME="Linux"

    echo "$NAME"

}
```

---

# Reading Command-Line Arguments

```bash
#!/usr/bin/env bash

echo "Script: $0"

echo "First: $1"

echo "Second: $2"
```

---

# Processing All Arguments

```bash
for ARG in "$@"
do
    echo "$ARG"
done
```

`"$@"` preserves individual arguments, including those containing spaces.

---

# Exit Codes

Exit successfully:

```bash
exit 0
```

Failure example:

```bash
exit 1
```

---

# Defensive Error Handling

Example:

```bash
cp report.txt backup/

if [ $? -eq 0 ]
then
    echo "Backup successful"
else
    echo "Backup failed"
fi
```

A more concise approach:

```bash
if cp report.txt backup/
then
    echo "Backup successful"
else
    echo "Backup failed"
fi
```

---

# Strict Mode

Many production scripts begin with:

```bash
set -euo pipefail
```

Meaning:

| Option | Purpose |
|---------|----------|
| `-e` | Exit on command failure |
| `-u` | Treat unset variables as errors |
| `pipefail` | Fail a pipeline if any command fails |

These options help catch common scripting mistakes early.

---

# Traps

Execute cleanup before exiting.

Example:

```bash
cleanup() {

    echo "Cleaning temporary files"

}

trap cleanup EXIT
```

Useful for:

- Removing temporary files
- Releasing locks
- Cleaning resources

---

# Debugging Scripts

Run with debugging enabled:

```bash
bash -x script.sh
```

Or inside the script:

```bash
set -x
```

Disable debugging:

```bash
set +x
```

---

# Syntax Checking

Verify script syntax without execution:

```bash
bash -n script.sh
```

This detects syntax errors before running the script.

---

# Logging

Append log messages:

```bash
echo "$(date): Backup completed" >> backup.log
```

Production scripts often include:

- Timestamp
- Hostname
- User
- Script name
- Status
- Error details

---

# Example Log Function

```bash
log() {

    echo "$(date): $1"

}

log "Deployment started"
```

To persist logs:

```bash
log() {
    echo "$(date): $1" >> script.log
}
```

---

# Temporary Files

Create securely:

```bash
TEMP_FILE=$(mktemp)
```

Remove during cleanup:

```bash
rm -f "$TEMP_FILE"
```

---

# ShellCheck

ShellCheck is a widely used static analysis tool for shell scripts.

Example:

```bash
shellcheck script.sh
```

It detects:

- Quoting issues
- Unused variables
- Common logic mistakes
- Portability concerns

---

# Enterprise Script Structure

```text
Shebang

↓

Strict Mode

↓

Variables

↓

Functions

↓

Input Validation

↓

Main Logic

↓

Logging

↓

Cleanup

↓

Exit
```

---

# Enterprise Example

## User Account Audit

Workflow:

```text
Read User List

↓

Check Account

↓

Verify Home Directory

↓

Verify Shell

↓

Generate Report

↓

Save Log
```

---

# Enterprise Example

## Log Monitoring Script

Workflow:

```text
Read Log

↓

Search Errors

↓

Count Matches

↓

Generate Alert

↓

Notify Administrator
```

---

# Common Bash Mistakes

| Mistake | Better Practice |
|----------|-----------------|
| Unquoted variables | Quote variables unless unquoted expansion is required |
| Ignoring exit codes | Check command success |
| Using temporary filenames manually | Use `mktemp` |
| Hard-coded paths | Store paths in variables |
| Repeated code | Create reusable functions |
| Missing cleanup | Use `trap` |

---

# Cybersecurity Perspective

Security teams frequently use Bash for:

- User audits
- File integrity checks
- IOC searches
- Log analysis
- Service verification
- Automated response
- Scheduled security tasks
- Evidence collection

When writing security scripts:

- Validate all external input.
- Avoid executing untrusted data.
- Run with the minimum required privileges.
- Protect sensitive logs and output.
- Review scripts before deploying them to production.

---

# Business Impact

Well-designed Bash scripts provide:

- Consistent administration
- Reduced manual effort
- Faster deployments
- Reliable monitoring
- Improved operational efficiency
- Lower risk of repetitive human errors

---

# Enterprise Best Practices

- Use descriptive function and variable names.
- Enable strict mode where appropriate.
- Quote variables consistently.
- Validate all user input.
- Handle failures gracefully.
- Log meaningful events.
- Remove temporary files automatically.
- Review scripts with ShellCheck.
- Store production scripts in version control.
- Peer-review automation before deployment.

---

# Key Takeaways

- Conditional statements control script execution paths.
- Loops automate repetitive tasks.
- Functions improve modularity and reuse.
- Arrays simplify handling multiple values.
- Strict mode, logging, and traps increase script reliability.
- Debugging and static analysis tools improve script quality.

---

