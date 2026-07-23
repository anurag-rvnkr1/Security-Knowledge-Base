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


# Part 2 — Special Permissions (SUID, SGID, Sticky Bit), Default Permissions (`umask`), and Access Control Lists (ACLs)

---

# Introduction

Traditional Linux permissions (Owner, Group, Others) are sufficient for many situations, but enterprise environments often require more advanced access control.

Examples include:

- Shared project directories
- Secure application execution
- Collaborative development
- Multi-team file sharing
- Enterprise storage servers
- Application service accounts

Linux provides additional mechanisms:

- SUID (Set User ID)
- SGID (Set Group ID)
- Sticky Bit
- Default permissions (`umask`)
- Access Control Lists (ACLs)

These features allow administrators to implement more flexible and secure access policies.

---

# Linux Permission Hierarchy

```text
                Linux Permissions

                        │

        ┌───────────────┴───────────────┐

        │                               │

 Standard Permissions          Special Permissions

        │                               │

     rwx bits                  SUID  SGID  Sticky

                        │

                        ▼

                Access Control Lists

                        │

                        ▼

                Fine-Grained Access
```

---

# Review of Standard Permissions

Every object begins with:

```text
Owner

↓

Group

↓

Others
```

Example:

```text
rwxr-x---
```

These permissions apply to three identity classes only.

ACLs extend this model by allowing permissions for specific additional users and groups.

---

# Special Permissions

Linux provides three special permission bits.

| Permission | Numeric Value | Symbol |
|------------|---------------|---------|
| SUID | 4 | s |
| SGID | 2 | s |
| Sticky Bit | 1 | t |

These values occupy an additional leading digit in numeric permission notation.

---

# Permission Format

Normal permissions:

```text
755
```

Special permissions:

```text
4755

2755

1777
```

The first digit represents special permission bits.

---

# SUID (Set User ID)

SUID allows an executable to run with the privileges of its **owner**, rather than the privileges of the user executing it.

Workflow:

```text
User Executes Program

        │

        ▼

Program Has SUID?

        │

      Yes

        │

        ▼

Runs as File Owner

        │

        ▼

Returns to User
```

---

# Why SUID Exists

Some operations require elevated privileges.

Example:

Changing your password.

A regular user cannot modify:

```text
/etc/shadow
```

However, the `passwd` program can update it because it executes with the privileges of its owner (typically `root`) when the SUID bit is set.

---

# Example

Display permissions:

```bash
ls -l /usr/bin/passwd
```

Example:

```text
-rwsr-xr-x
```

Notice:

```text
rws
```

The `s` replaces the owner's execute bit, indicating SUID is enabled.

---

# Setting SUID

Numeric:

```bash
chmod 4755 program
```

Symbolic:

```bash
chmod u+s program
```

---

# Removing SUID

```bash
chmod u-s program
```

---

# Security Considerations for SUID

Improperly configured SUID programs may:

- Increase the attack surface
- Allow privilege escalation
- Expose sensitive system resources

Enterprise administrators should:

- Limit the number of SUID binaries.
- Audit them regularly.
- Remove unnecessary SUID permissions.

---

# Finding SUID Files

```bash
find / -perm -4000 -type f
```

Example output:

```text
/usr/bin/passwd

/usr/bin/su
```

Regular reviews help identify unexpected privileged executables.

---

# SGID (Set Group ID)

SGID behaves differently for files and directories.

For executable files:

- The program runs with the file's group privileges.

For directories:

- Newly created files inherit the directory's group instead of the creator's primary group.

---

# SGID on Directories

Example:

```text
Project Directory

Group:

developers
```

Without SGID:

```text
Alice creates file

↓

Group = alice
```

With SGID:

```text
Alice creates file

↓

Group = developers
```

This simplifies collaboration.

---

# Enable SGID

Numeric:

```bash
chmod 2755 project
```

Symbolic:

```bash
chmod g+s project
```

---

# SGID Example

Display:

```bash
ls -ld project
```

Example:

```text
drwxr-sr-x
```

The `s` appears in the group execute position.

---

# Finding SGID Files

```bash
find / -perm -2000
```

This identifies files and directories with the SGID bit set.

---

# Sticky Bit

The Sticky Bit is primarily used on **directories**.

It prevents users from deleting or renaming files owned by other users, even when the directory is writable.

---

# Why Sticky Bit Exists

Consider:

```text
/tmp
```

Everyone needs write access.

Without Sticky Bit:

```text
Alice

↓

Deletes Bob's File
```

With Sticky Bit:

```text
Alice

↓

Cannot Delete Bob's File
```

Only the file owner, directory owner, or root can remove the file.

---

# Example

Display:

```bash
ls -ld /tmp
```

Typical output:

```text
drwxrwxrwt
```

Notice:

```text
t
```

The `t` indicates the Sticky Bit.

---

# Enable Sticky Bit

Numeric:

```bash
chmod 1777 shared
```

Symbolic:

```bash
chmod +t shared
```

---

# Remove Sticky Bit

```bash
chmod -t shared
```

---

# Summary of Special Permissions

| Permission | Applies To | Primary Purpose |
|------------|------------|-----------------|
| SUID | Executable files | Run with owner's privileges |
| SGID | Files & directories | Group inheritance or group execution |
| Sticky Bit | Directories | Prevent deletion of others' files |

---

# Understanding umask

When a file is created, Linux begins with default permission values.

Typical defaults:

| Object | Base Permission |
|----------|-----------------|
| File | 666 |
| Directory | 777 |

The **umask** removes permission bits from these defaults.

---

# View Current umask

```bash
umask
```

Example:

```text
0022
```

---

# Example Calculation

Default file permission:

```text
666
```

umask:

```text
022
```

Typical result:

```text
644
```

Directory:

```text
777

↓

022

↓

755
```

---

# Common umask Values

| umask | Files | Directories | Typical Use |
|--------|-------|-------------|-------------|
| 022 | 644 | 755 | Standard multi-user systems |
| 027 | 640 | 750 | Restricted enterprise environments |
| 077 | 600 | 700 | Highly sensitive systems |

---

# Temporarily Change umask

```bash
umask 027
```

This affects new files created in the current shell session.

---

# Access Control Lists (ACLs)

Traditional permissions allow only:

- Owner
- Group
- Others

ACLs allow permissions for additional individual users and groups.

Example:

```text
Owner

↓

alice

↓

ACL

↓

bob

↓

charlie

↓

security-team
```

---

# Why ACLs?

Scenario:

```text
report.pdf

Owner:

alice

Group:

developers
```

Requirement:

Grant **Bob** read access without changing:

- Owner
- Group
- Others

ACLs solve this problem cleanly.

---

# ACL Workflow

```text
Permission Check

        │

        ▼

Owner?

        │

        ▼

Named User ACL?

        │

        ▼

Group ACL?

        │

        ▼

Others
```

ACL evaluation extends the traditional permission model.

---

# Viewing ACLs

Display ACL information:

```bash
getfacl report.txt
```

Example:

```text
user::rw-

user:bob:r--

group::r--

mask::r--

other::---
```

---

# Grant ACL Permission

Grant Bob read access:

```bash
setfacl -m u:bob:r report.txt
```

Explanation:

| Option | Meaning |
|----------|----------|
| `-m` | Modify ACL |
| `u:` | User ACL |

---

# Grant Multiple Permissions

Grant Bob read and write:

```bash
setfacl -m u:bob:rw report.txt
```

---

# Grant Group ACL

```bash
setfacl -m g:security:r report.txt
```

The `security` group receives read access.

---

# Remove ACL Entry

```bash
setfacl -x u:bob report.txt
```

---

# Remove All ACLs

```bash
setfacl -b report.txt
```

This removes all extended ACL entries while leaving standard permissions intact.

---

# Default ACLs

Default ACLs apply automatically to newly created files within a directory.

Example:

```bash
setfacl -d -m g:developers:rwx project/
```

Files created inside `project/` inherit the default ACL according to filesystem support and applicable masks.

---

# Display Files with ACLs

```bash
ls -l
```

Example:

```text
-rw-r-----+
```

The `+` indicates that extended ACL entries exist.

---

# Enterprise Collaboration Example

```text
Engineering Directory

Owner:

engineering

↓

ACL

↓

QA Team

↓

Security Team

↓

Auditors
```

Each team receives only the permissions required for its role.

---

# Cybersecurity Perspective

Security teams frequently audit for:

- Unexpected SUID binaries
- Unauthorized SGID directories
- World-writable directories without Sticky Bit
- Excessive ACL permissions
- Privilege escalation opportunities
- Misconfigured shared storage

Regular permission reviews reduce the likelihood of unauthorized access.

---

# Business Impact

Advanced permission features enable organizations to:

- Support secure collaboration
- Reduce permission management overhead
- Enforce least privilege
- Protect shared resources
- Improve operational flexibility
- Meet compliance requirements

---

# Enterprise Best Practices

- Minimize the number of SUID executables.
- Use SGID on shared project directories where appropriate.
- Ensure publicly writable directories use the Sticky Bit.
- Prefer ACLs over creating unnecessary groups for one-off access requirements.
- Review ACLs periodically to prevent permission sprawl.
- Apply restrictive `umask` values consistent with organizational security policies.
- Document exceptions to standard permission models.

---

# Key Takeaways

- SUID allows executables to run with the owner's privileges.
- SGID supports shared group ownership and group-based execution.
- Sticky Bit protects files in shared writable directories.
- `umask` influences default permissions for newly created files and directories.
- ACLs provide fine-grained access beyond the traditional owner/group/others model.

---

# Part 3 — Permission Troubleshooting, Enterprise Scenarios, Security Auditing, Practical Examples, and Real-World Permission Management

---

# Introduction

In enterprise environments, permission problems are among the most common causes of:

- Application failures
- Service outages
- Deployment issues
- Security incidents
- Compliance violations

A Linux administrator must be able to quickly determine:

- Who owns a file
- Who should have access
- Why access is denied
- Whether permissions are too permissive
- How to safely correct the issue

Permission troubleshooting requires understanding both Linux authorization logic and security best practices.

---

# Permission Evaluation Process

Whenever a process attempts to access a file or directory, the Linux kernel evaluates permissions in a specific order.

```text
            Access Request
                  │
                  ▼
        Is Process Running as Root?
          │                 │
        Yes                No
          │                 │
      Access Allowed        ▼
                     Is User Owner?
                      │          │
                    Yes         No
                      │          │
              Check Owner Bits   ▼
                          Is User in Group?
                           │           │
                         Yes          No
                           │           │
                   Check Group Bits    ▼
                               Check Others Bits
                                       │
                                       ▼
                              Allow or Deny
```

> **Note:** Processes with elevated capabilities or mandatory access control systems (such as SELinux or AppArmor) may follow additional authorization rules beyond traditional Unix permissions.

---

# Understanding "Permission Denied"

One of the most common Linux errors:

```text
Permission denied
```

Possible causes include:

- Missing read permission
- Missing write permission
- Missing execute permission
- Incorrect ownership
- Incorrect group membership
- Missing execute permission on a parent directory
- Filesystem mounted read-only
- Additional security controls (ACLs, SELinux, AppArmor)

---

# Troubleshooting Workflow

```text
Access Failure

      │

      ▼

Check File Exists

      │

      ▼

Check Ownership

      │

      ▼

Check Permissions

      │

      ▼

Check Group Membership

      │

      ▼

Check ACL

      │

      ▼

Check Security Modules

      │

      ▼

Resolve Issue
```

Following a consistent workflow reduces troubleshooting time.

---

# Step 1 — Verify File Exists

```bash
ls -l report.txt
```

If the file does not exist:

```text
No such file or directory
```

The problem is not related to permissions.

---

# Step 2 — Check Ownership

```bash
ls -l report.txt
```

Example:

```text
-rw-r----- 1 alice developers report.txt
```

Determine:

- Owner
- Group
- Permissions

---

# Step 3 — Verify User Identity

Display current user:

```bash
whoami
```

Display identity:

```bash
id
```

Example:

```text
uid=1001(alice)

gid=1001(alice)

groups=developers,docker
```

Compare this information with the file's ownership.

---

# Step 4 — Check Group Membership

Display groups:

```bash
groups
```

or

```bash
id username
```

Example:

```text
alice developers docker security
```

If the required group is missing, group permissions will not apply.

---

# Step 5 — Check ACLs

Display ACL entries:

```bash
getfacl report.txt
```

Example:

```text
user::rw-

user:bob:r--

group::r--

other::---
```

ACLs may grant or restrict access beyond the standard permission bits.

---

# Step 6 — Verify Parent Directory

Users require execute (`x`) permission on every directory in the path.

Example:

```text
/home

↓

projects

↓

reports

↓

report.txt
```

Check:

```bash
ls -ld /home/projects/reports
```

A missing execute bit on a parent directory can prevent access even when the file permissions appear correct.

---

# Diagnosing Common Permission Issues

| Problem | Likely Cause | Suggested Check |
|----------|--------------|-----------------|
| Cannot read file | Missing `r` permission | `ls -l` |
| Cannot edit file | Missing `w` permission | `ls -l` |
| Cannot execute script | Missing `x` permission | `chmod +x` |
| Cannot enter directory | Missing directory execute permission | `ls -ld` |
| Group access not working | Incorrect group membership | `groups`, `id` |
| ACL behaving unexpectedly | Extended ACL present | `getfacl` |
| Changes fail despite correct permissions | Read-only filesystem or security policy | `mount`, SELinux/AppArmor tools |

---

# Example 1 — Script Will Not Execute

Permissions:

```text
-rw-r--r--
```

Attempt:

```bash
./backup.sh
```

Result:

```text
Permission denied
```

Resolution:

```bash
chmod +x backup.sh
```

Verify:

```bash
ls -l backup.sh
```

---

# Example 2 — User Cannot Modify File

Permissions:

```text
-rw-r--r--
```

Owner:

```text
root
```

User:

```text
alice
```

Solution options include:

- Change ownership (when appropriate):

```bash
sudo chown alice file.txt
```

- Grant write access through group permissions or ACLs if ownership should remain unchanged.

Choose the approach that aligns with organizational policy.

---

# Example 3 — Shared Directory Collaboration

Problem:

Developers create files that other team members cannot modify.

Current directory:

```text
drwxrwxr-x
```

Solution:

Enable SGID:

```bash
chmod g+s project
```

Result:

```text
New Files

↓

Inherited Group

↓

developers
```

This ensures consistent group ownership.

---

# Example 4 — Public Upload Directory

Requirements:

- Everyone can upload files.
- Users cannot delete each other's files.

Configuration:

```bash
chmod 1777 uploads
```

Result:

```text
World Writable

+

Sticky Bit

=

Protected Shared Directory
```

---

# Example 5 — Confidential SSH Key

Private key:

```text
id_rsa
```

Recommended permissions:

```bash
chmod 600 ~/.ssh/id_rsa
```

Owner:

- Read
- Write

Group:

- None

Others:

- None

This protects sensitive authentication material.

---

# Example 6 — Shared Report Access

Scenario:

Alice owns:

```text
report.pdf
```

Bob requires read-only access.

Instead of changing group ownership:

```bash
setfacl -m u:bob:r report.pdf
```

Benefits:

- Fine-grained access
- No ownership changes
- Minimal privilege

---

# Enterprise Scenario 1 — Web Server

Directory:

```text
/var/www/html
```

Recommended ownership:

```text
Owner:

root

Group:

www-data
```

Example permissions:

```text
Directories: 750

Files: 640
```

Benefits:

- Administrators retain ownership.
- Web service accesses required content.
- Other users are denied access.

---

# Enterprise Scenario 2 — Database Server

Sensitive directory:

```text
/var/lib/mysql
```

Typical ownership:

```text
mysql:mysql
```

Access should generally be limited to the database service account and authorized administrators.

---

# Enterprise Scenario 3 — Shared Engineering Repository

```text
engineering/

↓

Owner:

engineering

↓

SGID Enabled

↓

ACL:

QA

↓

Security

↓

Auditors
```

This approach supports collaboration while maintaining least privilege.

---

# Enterprise Scenario 4 — Secure Backup Storage

Backup directory:

```text
/backups
```

Example:

```text
Owner:

backup

Group:

backupadmins
```

Typical characteristics:

- Restricted access
- Limited write permissions
- Regular permission audits

---

# Permission Auditing

Administrators should regularly review:

- World-writable files
- World-writable directories
- SUID binaries
- SGID directories
- Files with extended ACLs
- Sensitive ownership changes

Routine audits help detect misconfigurations before they become security issues.

---

# Find World-Writable Files

```bash
find / -type f -perm -002
```

Review the results carefully before making changes.

---

# Find World-Writable Directories

```bash
find / -type d -perm -002
```

Verify that publicly writable directories use the Sticky Bit where appropriate.

---

# Find SUID Programs

```bash
find / -type f -perm -4000
```

Unexpected results should be investigated.

---

# Find SGID Objects

```bash
find / -perm -2000
```

Review whether SGID is required for each result.

---

# Find Files with ACLs

```bash
getfacl filename
```

or identify files displaying:

```text
+
```

in the permission listing:

```bash
ls -l
```

---

# Permission Audit Checklist

| Audit Item | Verify |
|------------|---------|
| Ownership | Correct owner |
| Group | Appropriate group |
| World write | Avoid unless required |
| SUID | Only approved binaries |
| SGID | Only approved shared directories/files |
| Sticky Bit | Enabled on public writable directories |
| ACLs | Minimal required permissions |
| Private keys | Restricted permissions |
| Configuration files | Protected from unauthorized modification |

---

# Permission Troubleshooting Flowchart

```text
Permission Denied

        │

        ▼

File Exists?

        │

        ▼

Correct Owner?

        │

        ▼

Correct Group?

        │

        ▼

Permission Bits Correct?

        │

        ▼

ACL Correct?

        │

        ▼

Security Policies?

        │

        ▼

Access Granted
```

---

# Cybersecurity Perspective

Attackers frequently abuse permission weaknesses such as:

- World-writable configuration files
- Incorrect SUID binaries
- Writable application scripts
- Weak permissions on SSH keys
- Overly permissive shared directories
- Privilege escalation through misconfigured ownership

Security teams routinely monitor:

- Permission changes
- Ownership modifications
- Unexpected SUID binaries
- ACL changes
- Unauthorized privilege assignments

Permission reviews are a core component of system hardening.

---

# Business Impact

Effective permission management enables organizations to:

- Protect confidential information.
- Reduce accidental changes.
- Improve application reliability.
- Support compliance frameworks.
- Simplify audits.
- Strengthen overall security posture.

---

# Enterprise Best Practices

- Apply the Principle of Least Privilege.
- Prefer group-based access over broad "others" permissions.
- Review SUID and SGID objects periodically.
- Restrict world-writable locations and use the Sticky Bit where necessary.
- Use ACLs for exceptional access rather than permanently expanding group membership.
- Validate permissions after deployments, backups, and data migrations.
- Automate permission audits for critical systems.

---

# Key Takeaways

- Permission troubleshooting follows a structured process.
- Ownership, groups, permission bits, ACLs, and security policies all influence access decisions.
- SUID, SGID, and Sticky Bit require regular review due to their security implications.
- Routine permission auditing reduces the likelihood of privilege escalation and unauthorized access.
- Consistent permission management improves both security and operational reliability.

---



