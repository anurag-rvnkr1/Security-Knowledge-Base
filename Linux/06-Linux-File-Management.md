# 06 - Linux File Management

# Part 1 — File Management Fundamentals, Creating Files & Directories, Copying, Moving, Renaming, Deleting, and File Discovery

---

# Introduction

Managing files efficiently is one of the most fundamental Linux administration skills.

Whether administering enterprise servers, cloud infrastructure, or security appliances, administrators constantly perform operations such as:

- Creating files
- Organizing directories
- Copying data
- Moving files
- Renaming resources
- Removing obsolete content
- Searching for important files
- Maintaining directory structures

Poor file management can result in:

- Data loss
- Misconfigurations
- Security vulnerabilities
- Storage exhaustion
- Operational downtime

Understanding Linux file management is therefore essential for every Linux professional.

---

# Learning Objectives

After completing this chapter, you will be able to:

- Create and organize files and directories.
- Copy, move, rename, and delete files safely.
- Navigate large directory structures.
- Search for files efficiently.
- Understand recursive operations.
- Apply enterprise file management best practices.

---

# File Management Workflow

```text
Create

↓

Modify

↓

Copy

↓

Move

↓

Rename

↓

Backup

↓

Archive

↓

Delete
```

Every file typically passes through a lifecycle from creation to eventual removal or archival.

---

# Creating Files

Linux provides several methods to create files.

Common commands include:

- `touch`
- `cat`
- `echo`
- Text editors
- Redirection operators

---

# touch Command

Create an empty file:

```bash
touch notes.txt
```

Create multiple files:

```bash
touch file1.txt file2.txt file3.txt
```

If the file already exists, `touch` updates its timestamp without modifying its contents.

---

# Verify File Creation

Display file information:

```bash
ls -l notes.txt
```

Display inode information:

```bash
stat notes.txt
```

---

# Creating Directories

Create a directory:

```bash
mkdir Projects
```

Result:

```text
Projects/
```

Directories organize files into logical structures.

---

# Create Multiple Directories

```bash
mkdir Docs Images Scripts
```

Result:

```text
Docs/

Images/

Scripts/
```

---

# Parent Directory Creation

Use:

```bash
mkdir -p
```

Example:

```bash
mkdir -p Projects/Linux/Chapter01
```

Without `-p`, parent directories must already exist.

---

# Directory Structure Example

```text
Projects

└── Linux

    └── Chapter01

        ├── Notes

        └── Labs
```

This approach is useful for organizing documentation, projects, and automation scripts.

---

# Copying Files

Use:

```bash
cp
```

Example:

```bash
cp report.txt backup.txt
```

Result:

```text
report.txt

backup.txt
```

The contents are duplicated into a new file.

---

# Copy Multiple Files

Example:

```bash
cp file1 file2 file3 Backup/
```

All specified files are copied into the destination directory.

---

# Copy Directories

Directories require recursive copying.

Example:

```bash
cp -r Projects Backup/
```

Result:

```text
Backup/

└── Projects
```

The `-r` (or `-R`) option copies directories and their contents recursively.

---

# Preserve Metadata During Copy

Example:

```bash
cp -a Projects Backup/
```

The `-a` (archive) option preserves attributes such as:

- Permissions
- Ownership
- Timestamps
- Symbolic links (where applicable)

This is commonly used for backups and migrations.

---

# Interactive Copy

Prompt before overwriting:

```bash
cp -i report.txt Backup/
```

This helps prevent accidental replacement of existing files.

---

# Moving Files

Move a file:

```bash
mv report.txt Documents/
```

The file is relocated to the target directory.

---

# Rename Files

The `mv` command is also used to rename files.

Example:

```bash
mv report.txt final_report.txt
```

Result:

```text
final_report.txt
```

No duplicate copy is created; the directory entry is updated.

---

# Move Multiple Files

Example:

```bash
mv *.txt Archive/
```

All matching text files are moved into the `Archive` directory.

---

# Renaming Directories

Example:

```bash
mv OldProject NewProject
```

The directory name changes while its contents remain intact.

---

# Deleting Files

Remove a file:

```bash
rm report.txt
```

Once removed, recovery may be difficult or impossible depending on the filesystem and subsequent disk activity.

---

# Interactive Deletion

Prompt before deletion:

```bash
rm -i report.txt
```

Useful when working with important files.

---

# Delete Multiple Files

Example:

```bash
rm file1 file2 file3
```

Each specified file is removed.

---

# Remove Directories

Empty directory:

```bash
rmdir EmptyDirectory
```

`rmdir` works only if the directory contains no files or subdirectories.

---

# Remove Non-Empty Directories

Recursive removal:

```bash
rm -r Projects
```

This removes:

- Directory
- Files
- Subdirectories

Use this command with care.

---

# Force Removal

Example:

```bash
rm -rf Projects
```

Options:

- `-r` — Recursive
- `-f` — Force (suppress prompts and certain errors)

⚠ **Warning:** `rm -rf` can permanently remove large portions of the filesystem if used incorrectly. Always verify the target path before execution, especially when operating with administrative privileges.

---

# Safe Removal Practices

Before deleting:

- Confirm the current directory with `pwd`.
- Verify targets using `ls`.
- Prefer interactive mode for sensitive files.
- Ensure backups exist for important data.

Enterprise environments often require change approval before deleting production files.

---

# Viewing Directory Contents

Basic listing:

```bash
ls
```

Long format:

```bash
ls -l
```

Show hidden files:

```bash
ls -la
```

These commands are used constantly in Linux administration.

---

# File Listing Example

```text
-rw-r--r-- report.txt

drwxr-xr-x Projects

lrwxrwxrwx python -> python3
```

The first character identifies the file type.

---

# Tree View

Display directory hierarchy:

```bash
tree
```

Example:

```text
Projects

├── Linux

├── Python

└── Security
```

> **Note:** The `tree` utility may need to be installed separately on some distributions.

---

# Current Working Directory

Display current location:

```bash
pwd
```

Example:

```text
/home/anurag/Documents
```

Knowing the current working directory helps avoid operating on unintended files.

---

# Searching for Files

Linux offers multiple search utilities.

Common tools:

- `find`
- `locate`
- `which`
- `whereis`

Each serves a different purpose.

---

# find Command

Search by name:

```bash
find /home -name "*.txt"
```

Searches recursively for matching text files.

---

# Case-Insensitive Search

```bash
find . -iname "*.pdf"
```

The `-iname` option ignores letter case.

---

# Search by Type

Files only:

```bash
find . -type f
```

Directories only:

```bash
find . -type d
```

This helps narrow search results.

---

# Search by Size

Example:

```bash
find /var -size +100M
```

Finds files larger than 100 MB.

Useful for storage management and investigations.

---

# Search by Modification Time

Modified within the last seven days:

```bash
find /home -mtime -7
```

This is useful for identifying recently changed files.

---

# locate Command

Example:

```bash
locate passwd
```

`locate` searches an indexed database and is generally faster than `find` for broad searches.

If the database is outdated, search results may not reflect recent changes.

---

# which Command

Locate executable in the user's `PATH`:

```bash
which python3
```

Example output:

```text
/usr/bin/python3
```

Useful for determining which executable will run.

---

# whereis Command

Example:

```bash
whereis ssh
```

May display:

- Binary
- Source
- Manual page locations

This provides more context than `which`.

---

# Cybersecurity Perspective

File management knowledge assists security teams in:

- Locating malicious files.
- Investigating unauthorized changes.
- Identifying suspicious executables.
- Managing incident response artifacts.
- Organizing forensic evidence.

Search commands such as `find` are frequently used during investigations.

---

# Business Impact

Efficient file management enables organizations to:

- Improve administrator productivity.
- Reduce operational errors.
- Simplify automation.
- Enhance backup strategies.
- Maintain organized infrastructure.

---

# Enterprise Best Practices

- Use meaningful directory structures.
- Avoid unnecessary duplication of large files.
- Preserve metadata when performing backups or migrations.
- Verify deletion targets before removing files.
- Restrict write permissions on critical directories.
- Regularly review storage utilization.
- Standardize directory layouts across servers.

---

# Key Takeaways

- `touch` and `mkdir` create files and directories.
- `cp` copies files and directories, while `mv` moves or renames them.
- `rm` removes files, and recursive deletion should be used with caution.
- `find`, `locate`, `which`, and `whereis` provide different methods for locating files.
- Consistent file management practices improve reliability, security, and maintainability.

---

# Part 2 — Viewing Files, Editing Files, Wildcards, Globbing, File Comparison, Checksums, and File Integrity

---

# Introduction

Creating and organizing files is only one aspect of Linux file management.

Administrators, developers, security analysts, and DevOps engineers spend much of their time:

- Viewing file contents
- Editing configuration files
- Comparing different file versions
- Searching inside files
- Using wildcard patterns
- Verifying file integrity
- Detecting unauthorized modifications

Efficient use of these tools is essential for troubleshooting, automation, security operations, and system administration.

---

# File Viewing Workflow

```text
Create File
      │
      ▼
Open File
      │
      ▼
View Contents
      │
      ▼
Search Information
      │
      ▼
Edit File
      │
      ▼
Save Changes
      │
      ▼
Verify Integrity
```

---

# Viewing File Contents

Linux provides several utilities for reading files without modifying them.

Common commands include:

- `cat`
- `less`
- `more`
- `head`
- `tail`
- `nl`

Each is suited to different scenarios.

---

# cat Command

Display an entire file:

```bash
cat notes.txt
```

Example output:

```text
Linux Fundamentals
Linux File Management
Linux Networking
```

`cat` is best suited for relatively small files.

---

# Number Lines

Display line numbers:

```bash
cat -n notes.txt
```

Example:

```text
1 Linux Fundamentals

2 Linux File Management

3 Linux Networking
```

Useful when reviewing configuration files or log excerpts.

---

# less Command

Open a file interactively:

```bash
less /var/log/syslog
```

Features:

- Scroll forward and backward
- Search within the file
- Handle very large files efficiently

Navigation:

| Key | Action |
|------|--------|
| `Space` | Next page |
| `b` | Previous page |
| `/` | Search |
| `q` | Quit |

`less` is generally preferred over `more` because it provides more functionality.

---

# more Command

Example:

```bash
more notes.txt
```

Displays file contents one page at a time.

Compared with `less`, navigation capabilities are more limited.

---

# head Command

Display the first lines of a file.

Default:

```bash
head notes.txt
```

Show the first five lines:

```bash
head -n 5 notes.txt
```

Useful for previewing files without opening them completely.

---

# tail Command

Display the last lines:

```bash
tail notes.txt
```

Display the last twenty lines:

```bash
tail -n 20 notes.txt
```

This command is commonly used when reviewing logs.

---

# Follow Log Files

Monitor a growing log file:

```bash
tail -f /var/log/syslog
```

Typical uses:

- Server monitoring
- Application debugging
- Security investigations

Press `Ctrl + C` to stop following the file.

---

# nl Command

Display numbered lines:

```bash
nl notes.txt
```

Unlike `cat -n`, `nl` provides additional formatting options for line numbering.

---

# Creating Files with Output Redirection

Create a file:

```bash
echo "Linux" > file.txt
```

Append additional content:

```bash
echo "Security" >> file.txt
```

Difference:

| Operator | Action |
|-----------|--------|
| `>` | Create or overwrite |
| `>>` | Append |

---

# Editing Files

Common text editors include:

| Editor | Characteristics |
|---------|-----------------|
| `nano` | Beginner-friendly |
| `vim` | Powerful and widely used |
| `vi` | Traditional Unix editor |
| `emacs` | Highly extensible |

The choice often depends on administrator preference and environment.

---

# nano Editor

Open a file:

```bash
nano notes.txt
```

Basic workflow:

```text
Open

↓

Edit

↓

Save

↓

Exit
```

Common shortcuts:

| Shortcut | Action |
|-----------|--------|
| `Ctrl + O` | Save |
| `Ctrl + X` | Exit |
| `Ctrl + K` | Cut line |
| `Ctrl + U` | Paste line |

---

# vi / vim Overview

Open:

```bash
vim notes.txt
```

Basic modes:

```text
Normal Mode

↓

Insert Mode

↓

Command Mode
```

Frequently used commands:

| Command | Purpose |
|----------|----------|
| `i` | Insert mode |
| `Esc` | Return to normal mode |
| `:w` | Save |
| `:q` | Quit |
| `:wq` | Save and quit |
| `:q!` | Quit without saving |

`vim` is commonly available on enterprise Linux servers.

---

# Wildcards (Globbing)

Wildcards allow commands to operate on multiple files matching a pattern.

Common wildcard characters:

| Wildcard | Meaning |
|-----------|----------|
| `*` | Zero or more characters |
| `?` | Exactly one character |
| `[]` | Character set or range |

This process is known as **filename expansion (globbing)** and is typically performed by the shell before the command executes.

---

# Asterisk (`*`)

Example:

```bash
ls *.txt
```

Matches:

```text
notes.txt

report.txt

todo.txt
```

The asterisk is the most frequently used wildcard.

---

# Question Mark (`?`)

Example:

```bash
ls file?.txt
```

Matches:

```text
file1.txt

file2.txt
```

Does not match:

```text
file10.txt
```

Because `?` represents exactly one character.

---

# Character Sets

Example:

```bash
ls report[12].txt
```

Matches:

```text
report1.txt

report2.txt
```

Character ranges:

```bash
ls file[a-z].txt
```

This matches filenames with a single lowercase letter in the specified position.

---

# Brace Expansion

Generate multiple filenames:

```bash
touch file{1..5}.txt
```

Creates:

```text
file1.txt

file2.txt

file3.txt

file4.txt

file5.txt
```

Brace expansion is performed by the shell and is distinct from wildcard matching.

---

# File Comparison

Linux provides several tools to compare files.

Common commands:

- `diff`
- `cmp`
- `comm`

Each presents differences differently.

---

# diff Command

Example:

```bash
diff old.conf new.conf
```

Displays line-by-line differences between two text files.

Common use cases:

- Configuration reviews
- Software development
- Change verification

---

# cmp Command

Example:

```bash
cmp file1 file2
```

Reports the first byte and line where two files differ.

Often used for binary comparisons.

---

# comm Command

Example:

```bash
comm file1 file2
```

Compares two **sorted** text files and identifies:

- Lines unique to the first file
- Lines unique to the second file
- Lines common to both

---

# File Integrity

Ensuring that files have not been modified unexpectedly is critical for:

- Security
- Compliance
- Software distribution
- Incident response

Integrity verification commonly relies on cryptographic hash functions.

---

# Checksums

A checksum (hash) is a fixed-length value calculated from file contents.

Common algorithms:

| Algorithm | Typical Use |
|------------|-------------|
| MD5 | Legacy compatibility (not suitable for security-sensitive integrity verification) |
| SHA-1 | Legacy compatibility (collision weaknesses) |
| SHA-256 | Widely recommended |
| SHA-512 | Strong cryptographic integrity verification |

---

# Generate SHA-256 Checksum

Example:

```bash
sha256sum file.iso
```

Example output:

```text
e3b0c44298fc...

file.iso
```

The hash uniquely represents the file contents with extremely high probability.

---

# Verify File Integrity

Compare a newly generated checksum with a trusted checksum provided by the software vendor.

Workflow:

```text
Download File

↓

Generate SHA-256

↓

Compare with Trusted Hash

↓

Match?

↓

Yes → Integrity Verified
```

A mismatch indicates that the file may be corrupted or altered.

---

# Why Hashes Matter

Hash verification helps detect:

- Corruption during download
- Accidental modification
- Unauthorized changes
- Supply chain attacks
- Tampered installation media

Hashes verify integrity but do not identify *who* modified a file.

---

# Practical Use Cases

Administrators use hashes to verify:

- Linux ISO images
- Backup archives
- Software packages
- Configuration snapshots
- Security evidence
- Digital forensic images

---

# Cybersecurity Perspective

Security professionals routinely:

- Verify downloaded software before installation.
- Compare hashes during malware analysis.
- Detect unauthorized file modifications.
- Validate forensic evidence.
- Monitor critical system files for integrity changes.

Hash-based integrity verification is a fundamental component of incident response workflows.

---

# Business Impact

Effective file viewing, editing, and integrity verification help organizations:

- Reduce configuration errors.
- Improve operational efficiency.
- Strengthen software supply chain security.
- Detect unauthorized modifications.
- Support regulatory compliance and auditing.

---

# Enterprise Best Practices

- Use `less` for viewing large files.
- Limit direct editing of production configuration files without backups or version control.
- Verify software downloads using vendor-provided SHA-256 or stronger hashes.
- Store baseline hashes securely.
- Review configuration differences before deployment.
- Use wildcard patterns carefully to avoid unintended file operations.
- Validate changes through testing before applying them in production.

---

# Key Takeaways

- Linux provides multiple tools for viewing and editing files, each suited to different tasks.
- Wildcards and shell globbing simplify operations on groups of files.
- `diff`, `cmp`, and `comm` compare files in different ways.
- Cryptographic hashes provide a practical mechanism for verifying file integrity.
- Careful file handling and integrity verification are essential for secure and reliable system administration.

---

