# 26 - Linux Cheat Sheet

# Part 1 — Essential Linux Commands, File & Directory Management, Text Processing, and Navigation

---

# Introduction

This chapter is designed as a **quick-reference guide** for Linux users, system administrators, DevOps engineers, cloud engineers, SOC analysts, penetration testers, and cybersecurity professionals.

Unlike previous chapters, this chapter is intended for **rapid revision** and **daily operational use**.

---

# Linux Command Structure

```text
command [options] [arguments]
```

Example:

```bash
ls -la /home
```

Where:

- `ls` → Command
- `-la` → Options
- `/home` → Argument

---

# Keyboard Shortcuts

| Shortcut | Purpose |
|-----------|---------|
| `Ctrl + C` | Stop current process |
| `Ctrl + Z` | Suspend process |
| `Ctrl + D` | Logout / End input (EOF) |
| `Ctrl + L` | Clear terminal screen |
| `Ctrl + A` | Move cursor to beginning of line |
| `Ctrl + E` | Move cursor to end of line |
| `Ctrl + U` | Delete to beginning of line |
| `Ctrl + K` | Delete to end of line |
| `Ctrl + R` | Search command history |
| `Tab` | Auto-complete commands/files |
| `!!` | Repeat previous command |
| `history` | Show command history |

---

# System Information

| Task | Command |
|------|---------|
| Hostname | `hostname` |
| Detailed hostname | `hostnamectl` |
| Kernel version | `uname -r` |
| Kernel & architecture | `uname -a` |
| Current user | `whoami` |
| Logged-in users | `who` |
| Uptime | `uptime` |
| Current date | `date` |
| Current calendar | `cal` |

---

# Directory Navigation

| Task | Command |
|------|---------|
| Current directory | `pwd` |
| Home directory | `cd` |
| Root directory | `cd /` |
| Parent directory | `cd ..` |
| Previous directory | `cd -` |
| User's home | `cd ~` |

---

# Listing Files

| Command | Purpose |
|----------|---------|
| `ls` | List files |
| `ls -l` | Long listing |
| `ls -a` | Include hidden files |
| `ls -la` | Long listing with hidden files |
| `ls -lh` | Human-readable sizes |
| `ls -R` | Recursive listing |

---

# Hidden Files

Hidden files begin with:

```text
.
```

Example:

```text
.bashrc
.profile
.gitignore
```

Display hidden files:

```bash
ls -la
```

---

# Creating Files

Create an empty file:

```bash
touch file.txt
```

Create multiple files:

```bash
touch file1 file2 file3
```

---

# Creating Directories

Create directory:

```bash
mkdir project
```

Create nested directories:

```bash
mkdir -p projects/linux/scripts
```

---

# Copying Files

Copy file:

```bash
cp source destination
```

Copy recursively:

```bash
cp -r directory backup/
```

Preserve attributes:

```bash
cp -a source destination
```

---

# Moving Files

Move:

```bash
mv file.txt Documents/
```

Rename:

```bash
mv old.txt new.txt
```

---

# Removing Files

Delete file:

```bash
rm file.txt
```

Delete directory recursively:

```bash
rm -r directory
```

Force deletion:

```bash
rm -rf directory
```

> **Warning:** `rm -rf` permanently deletes data without moving it to a recycle bin. Verify the target path carefully before executing.

---

# Viewing File Contents

Display entire file:

```bash
cat file.txt
```

View interactively:

```bash
less file.txt
```

First lines:

```bash
head file.txt
```

Last lines:

```bash
tail file.txt
```

Follow updates:

```bash
tail -f logfile.log
```

---

# Searching Files

Search by name:

```bash
find /home -name report.txt
```

Case-insensitive search:

```bash
find . -iname "*.pdf"
```

Search by type:

```bash
find . -type d
```

---

# Searching Text

Basic search:

```bash
grep "error" logfile
```

Recursive search:

```bash
grep -R "password" .
```

Ignore case:

```bash
grep -i "linux" notes.txt
```

Show line numbers:

```bash
grep -n "TODO" script.sh
```

---

# Text Processing Commands

| Command | Purpose |
|----------|---------|
| `grep` | Search text |
| `sed` | Stream editor |
| `awk` | Pattern scanning and processing |
| `cut` | Extract fields |
| `sort` | Sort lines |
| `uniq` | Remove adjacent duplicates |
| `wc` | Count lines, words, characters |
| `tr` | Translate characters |
| `paste` | Merge files line by line |

---

# Word Count

Count lines, words, and bytes:

```bash
wc file.txt
```

Count only lines:

```bash
wc -l file.txt
```

---

# Sorting

Sort alphabetically:

```bash
sort names.txt
```

Sort numerically:

```bash
sort -n numbers.txt
```

Reverse order:

```bash
sort -r names.txt
```

---

# Remove Duplicate Lines

```bash
uniq file.txt
```

For complete duplicate removal, sort first:

```bash
sort file.txt | uniq
```

---

# Cut Fields

Extract the first field separated by `:`:

```bash
cut -d: -f1 /etc/passwd
```

---

# Translate Characters

Convert lowercase to uppercase:

```bash
echo "linux" | tr 'a-z' 'A-Z'
```

---

# File Comparison

Compare two files:

```bash
diff file1.txt file2.txt
```

Side-by-side comparison:

```bash
diff -y file1.txt file2.txt
```

---

# File Information

Display file type:

```bash
file filename
```

Display detailed statistics:

```bash
stat filename
```

---

# Archive Files

Create a tar archive:

```bash
tar -cvf archive.tar directory/
```

Extract:

```bash
tar -xvf archive.tar
```

Create compressed archive:

```bash
tar -czvf archive.tar.gz directory/
```

Extract compressed archive:

```bash
tar -xzvf archive.tar.gz
```

---

# Compression

Compress:

```bash
gzip file.txt
```

Decompress:

```bash
gunzip file.txt.gz
```

View compressed file without extracting:

```bash
zcat file.txt.gz
```

---

# File Permissions (Quick View)

Display permissions:

```bash
ls -l
```

Example:

```text
-rwxr-xr--
```

Meaning:

```text
Owner  → rwx

Group  → r-x

Others → r--
```

---

# Useful One-Liners

Current user:

```bash
whoami
```

Current directory:

```bash
pwd
```

Current date:

```bash
date
```

Current shell:

```bash
echo $SHELL
```

Display PATH:

```bash
echo $PATH
```

---

# Enterprise Productivity Tips

- Use `Tab` completion to reduce typing errors.
- Use `history` and `Ctrl + R` to quickly recall commands.
- Prefer `less` over `cat` for large files.
- Validate file paths before using destructive commands such as `rm`.
- Use recursive operations (`cp -r`, `rm -r`) only when necessary.

---

# Cybersecurity Perspective

These commands are frequently used during:

- Log review
- Malware investigation
- Incident response
- Digital forensics
- Vulnerability assessments
- Configuration auditing

Accurate command usage reduces operational mistakes and preserves evidence.

---

# Key Takeaways

- Navigation and file management are foundational Linux skills.
- Text-processing tools enable efficient log and configuration analysis.
- Archive and compression commands are essential for backups and data transfer.
- Safe command usage is critical in production and security environments.

---

