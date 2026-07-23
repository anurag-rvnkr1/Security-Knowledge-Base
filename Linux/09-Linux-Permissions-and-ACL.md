# 09 - Linux Permissions and ACL

# Part 1 — Linux Permission Model, Ownership, Read/Write/Execute Permissions, Symbolic & Numeric Permissions, `chmod`, `chown`, and `chgrp`

---

# Introduction

One of Linux's strongest security features is its **permission-based access control model**.

Every file and directory on a Linux system has:

- An owner
- An associated group
- Permission bits

These attributes determine:

- Who can read data
- Who can modify files
- Who can execute programs
- Who can access directories
- Who can administer resources

The Linux permission model forms the foundation for:

- Operating System Security
- Multi-user Computing
- Enterprise Access Control
- Application Isolation
- Compliance Requirements
- Cybersecurity Defense

---

# Learning Objectives

By the end of this chapter, you will understand:

- Linux ownership
- Permission model
- Read, write, execute permissions
- Symbolic permissions
- Numeric (octal) permissions
- File ownership
- Directory permissions
- Permission modification
- Enterprise security practices

---

# Why Permissions Matter

Consider a production server hosting:

- Customer databases
- Financial records
- SSH keys
- Source code
- Backup archives
- Application configurations

If every user had unrestricted access:

- Data confidentiality would be lost.
- Files could be modified accidentally.
- Malware could spread easily.
- Compliance requirements would fail.
- Insider threats would increase.

Permissions help enforce the **Principle of Least Privilege**.

---

# Linux Permission Architecture

```text
                     Linux File

                           │

        ┌──────────────────┴──────────────────┐

        │                                     │

    Ownership                          Permissions

        │                                     │

   Owner      Group                    r  w  x

        │                                     │

        └───────────────┬─────────────────────┘

                        │

                  Kernel Decision

                        │

                 Allow / Deny Access
```

---

# Every File Has Three Ownership Classes

Linux evaluates permissions for three classes.

| Class | Description |
|---------|-------------|
| User (Owner) | File owner |
| Group | Members of associated group |
| Others | Everyone else |

Example:

```text
Owner

↓

alice

Group

↓

developers

Others

↓

Everyone Else
```

---

# Viewing Permissions

Use:

```bash
ls -l
```

Example:

```text
-rwxr-xr-- 1 alice developers 2048 Jul 20 report.sh
```

---

# Understanding the Output

```text
-rwxr-xr--
```

Breakdown:

```text
-

rwx

r-x

r--
```

Meaning:

| Section | Purpose |
|----------|----------|
| First Character | File type |
| Next 3 | Owner permissions |
| Next 3 | Group permissions |
| Last 3 | Others permissions |

---

# File Types

First character meanings:

| Symbol | File Type |
|----------|------------|
| `-` | Regular file |
| `d` | Directory |
| `l` | Symbolic link |
| `c` | Character device |
| `b` | Block device |
| `p` | Named pipe |
| `s` | Socket |

Example:

```text
drwxr-xr-x
```

The leading `d` indicates a directory.

---

# Read Permission (r)

Read permission allows viewing file contents.

Examples:

```bash
cat report.txt

less report.txt

head report.txt
```

Without read permission:

```text
Permission denied
```

---

# Write Permission (w)

Write permission allows modification.

Examples:

- Edit file
- Delete contents
- Append text
- Truncate file

Typical commands:

```bash
echo "Hello" >> notes.txt

nano notes.txt
```

---

# Execute Permission (x)

Execute permission allows running a file as a program or script.

Example:

```bash
./backup.sh
```

Without execute permission:

```text
Permission denied
```

---

# Directory Permissions

Permissions behave differently for directories.

| Permission | Meaning |
|------------|----------|
| Read | List directory contents |
| Write | Create, rename, or delete entries (subject to directory ownership and other constraints) |
| Execute | Enter/traverse the directory and access items by name |

---

# Directory Read Permission

Allows listing files.

Example:

```bash
ls projects/
```

Without read permission:

Directory contents cannot be listed.

---

# Directory Write Permission

Allows:

- Create files
- Delete files
- Rename files

Example:

```bash
touch test.txt

rm old.txt
```

> **Note:** Deleting a file depends primarily on permissions of the containing directory rather than permissions on the file itself.

---

# Directory Execute Permission

Allows traversal.

Example:

```bash
cd projects
```

Without execute permission:

```text
Permission denied
```

---

# Permission Matrix

| Permission | File | Directory |
|-------------|------|-----------|
| Read | View contents | List entries |
| Write | Modify contents | Create/Delete/Rename entries |
| Execute | Run program | Traverse directory |

---

# Permission Representation

Permissions are represented in two ways.

## Symbolic

```text
rwxr-xr--
```

## Numeric

```text
754
```

Both describe the same permissions.

---

# Numeric Permission Values

Each permission has a numeric value.

| Permission | Value |
|------------|-------|
| Read | 4 |
| Write | 2 |
| Execute | 1 |

Sum the values to calculate the permission digit.

---

# Common Permission Values

| Number | Meaning |
|---------|----------|
| 7 | rwx |
| 6 | rw- |
| 5 | r-x |
| 4 | r-- |
| 3 | -wx |
| 2 | -w- |
| 1 | --x |
| 0 | --- |

---

# Example Calculation

Permissions:

```text
rwx
```

Calculation:

```text
4 + 2 + 1 = 7
```

---

Permissions:

```text
rw-
```

Calculation:

```text
4 + 2 = 6
```

---

Permissions:

```text
r-x
```

Calculation:

```text
4 + 1 = 5
```

---

Example:

```text
rwxr-xr--

↓

7 5 4
```

---

# Common Permission Sets

| Numeric | Symbolic | Typical Usage |
|----------|----------|---------------|
| 777 | rwxrwxrwx | Rarely appropriate; generally insecure |
| 755 | rwxr-xr-x | Executables and many directories |
| 750 | rwxr-x--- | Team-shared directories |
| 700 | rwx------ | Private directories |
| 644 | rw-r--r-- | Standard text files |
| 640 | rw-r----- | Sensitive shared files |
| 600 | rw------- | Private keys and confidential files |
| 400 | r-------- | Read-only owner access |

---

# chmod

`chmod` changes permissions.

Syntax:

```bash
chmod MODE file
```

Example:

```bash
chmod 644 notes.txt
```

---

# Numeric chmod

Grant:

```text
Owner

↓

Read + Write

Group

↓

Read

Others

↓

Read
```

Command:

```bash
chmod 644 file.txt
```

---

# Make a Script Executable

```bash
chmod 755 backup.sh
```

Now:

```bash
./backup.sh
```

can be executed by users with execute permission.

---

# Symbolic chmod

Syntax:

```bash
chmod [who][operator][permission]
```

Where:

| Symbol | Meaning |
|---------|----------|
| `u` | User (owner) |
| `g` | Group |
| `o` | Others |
| `a` | All |

Operators:

| Symbol | Meaning |
|---------|----------|
| `+` | Add permission |
| `-` | Remove permission |
| `=` | Set exact permission |

---

# Examples

Add execute permission for owner:

```bash
chmod u+x script.sh
```

Remove write permission from group:

```bash
chmod g-w file.txt
```

Grant read permission to others:

```bash
chmod o+r report.txt
```

Remove execute permission for everyone:

```bash
chmod a-x script.sh
```

---

# Recursive chmod

Apply permissions recursively.

```bash
chmod -R 755 website/
```

> **Warning:** Recursive permission changes can unintentionally alter large numbers of files. Review the target path carefully before using `-R`.

---

# chown

Change file ownership.

Syntax:

```bash
chown OWNER file
```

Example:

```bash
sudo chown alice report.txt
```

---

# Change Owner and Group

```bash
sudo chown alice:developers report.txt
```

Both owner and group are updated.

---

# Recursive Ownership Change

```bash
sudo chown -R alice:developers project/
```

Useful after restoring backups or migrating application data.

---

# chgrp

Change only the group.

Syntax:

```bash
chgrp GROUP file
```

Example:

```bash
chgrp developers report.txt
```

Ownership remains unchanged.

---

# Viewing Ownership

```bash
ls -l
```

Example:

```text
-rw-r----- 1 alice developers report.txt
```

Owner:

```text
alice
```

Group:

```text
developers
```

---

# Ownership Decision Flow

```text
User Requests Access

        │

        ▼

Is User Owner?

      │        │

     Yes       No

      │        │

 Owner Bits   Group Member?

               │      │

              Yes     No

               │      │

         Group Bits  Others Bits

               │

               ▼

        Allow / Deny
```

The kernel evaluates owner, then group, then others, stopping at the first applicable class.

---

# Enterprise Example

A web application stores files in:

```text
/var/www/html
```

Ownership:

```text
Owner

↓

www-data

Group

↓

webadmins
```

Permissions:

```text
750
```

Result:

- Web service can access files.
- Web administrators can manage content according to group permissions.
- Other users have no access.

This supports least-privilege access to web content.

---

# Cybersecurity Perspective

Weak permissions are a common cause of security incidents.

Examples include:

- World-writable configuration files.
- Executable scripts writable by untrusted users.
- Sensitive data readable by all users.
- Misconfigured ownership after software installation.
- Overly permissive shared directories.

Security teams regularly audit permissions to identify these issues.

---

# Business Impact

Proper permission management helps organizations:

- Protect sensitive information.
- Prevent unauthorized changes.
- Reduce accidental data loss.
- Support regulatory compliance.
- Improve system stability.
- Strengthen access control.

---

# Enterprise Best Practices

- Grant the minimum permissions required.
- Prefer group-based access instead of granting permissions to everyone.
- Avoid `777` permissions except in carefully justified, controlled scenarios.
- Protect private keys with restrictive permissions (for example, `600`).
- Review ownership after migrations and restores.
- Audit critical directories for unexpected permission changes.
- Apply recursive permission changes only after verifying their impact.

---

# Key Takeaways

- Every Linux file has an owner, group, and permission set.
- Read, write, and execute permissions have different meanings for files and directories.
- Permissions can be expressed symbolically or numerically.
- `chmod`, `chown`, and `chgrp` are the primary tools for permission management.
- Correct ownership and permissions are essential for secure multi-user systems.

---


