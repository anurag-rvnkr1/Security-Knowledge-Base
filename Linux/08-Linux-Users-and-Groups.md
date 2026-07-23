# 08 - Linux Users and Groups

# Part 1 — Linux User Management Fundamentals, User IDs (UID), Group IDs (GID), User Types, `/etc/passwd`, `/etc/shadow`, and `/etc/group`

---

# Introduction

Linux is a **multi-user operating system**, meaning multiple users can access and use the same system simultaneously while remaining isolated from one another.

Every file, process, service, and network connection is associated with a user identity. This identity determines:

- Ownership
- Permissions
- Resource access
- Process privileges
- Audit records
- Security policies

Proper user and group management is fundamental to:

- Linux Administration
- DevOps
- Cloud Computing
- Cybersecurity
- Compliance
- Enterprise Identity Management

---

# Learning Objectives

After completing this chapter, you will understand:

- Linux user architecture
- User accounts
- User IDs (UID)
- Group IDs (GID)
- User types
- Primary and supplementary groups
- Authentication databases
- Account information storage

---

# Why User Management Matters

Every enterprise Linux server may have:

- System administrators
- Developers
- Database administrators
- DevOps engineers
- Security analysts
- Service accounts
- Applications
- Automated jobs

Each requires different privileges.

Without proper account management:

- Unauthorized access increases.
- Accountability is reduced.
- Security policies become difficult to enforce.
- Compliance requirements may not be met.

---

# Linux User Architecture

```text
                Linux System
                     │
        ┌────────────┴────────────┐
        │                         │
   Human Users              Service Accounts
        │                         │
        ├──────────────┐          │
        │              │          │
 Administrator     Standard User  Database
        │              │          │
        └──────────────┴──────────┘
                     │
                     ▼
              Linux Kernel
```

The kernel uses numeric user and group identifiers to enforce access control.

---

# What is a User?

A **user** represents an identity recognized by the operating system.

A user account typically includes:

- Username
- Password (stored securely)
- UID
- Primary group
- Home directory
- Login shell

Example:

```text
Username: alice

UID: 1001

Home: /home/alice

Shell: /bin/bash
```

---

# User Types

Linux systems generally contain three categories of users.

| User Type | Purpose |
|------------|----------|
| Root User | Full administrative privileges |
| Regular User | Daily work and application usage |
| System/Service User | Runs operating system or application services |

---

# Root User

The **root** account is the most privileged account on a Linux system.

Characteristics:

- UID 0
- Unrestricted access
- Can modify any file
- Can manage users
- Can install software
- Can control services
- Can change security settings

Example:

```text
Username: root

UID: 0
```

> **Security Note:** Routine administrative work should generally be performed using delegated privileges (such as `sudo`) instead of logging in directly as the root user.

---

# Regular Users

Regular users perform everyday tasks.

Typical permissions:

- Access personal files.
- Run applications.
- Create documents.
- Execute authorized programs.

Regular users generally cannot:

- Modify system files.
- Install system-wide software without authorization.
- Change kernel configuration.
- Access other users' private files.

---

# System Users

Many Linux services run under dedicated service accounts.

Examples:

```text
www-data

mysql

postgres

nginx

sshd

daemon

nobody
```

Benefits:

- Least privilege
- Process isolation
- Reduced attack surface
- Improved auditing

Running each service under its own account limits the impact of compromise.

---

# User Identification

Linux identifies users internally by **User ID (UID)** rather than username.

Example:

```text
Username

↓

alice

↓

UID

↓

1001
```

The kernel makes authorization decisions based on numeric IDs.

---

# User ID (UID)

Each user has a unique numeric identifier.

Typical ranges (may vary by distribution):

| UID Range | Typical Purpose |
|------------|-----------------|
| 0 | Root |
| 1–999 | System and service accounts |
| 1000+ | Regular users |

> **Note:** UID allocation policies differ among Linux distributions and enterprise environments.

---

# Why UID Matters

The filesystem stores ownership using numeric IDs.

Example:

```text
report.txt

↓

Owner UID

↓

1001
```

The username displayed by tools such as `ls` is derived by mapping the UID to an entry in the user database.

---

# Group IDs (GID)

Every group also has a numeric identifier.

Example:

```text
developers

↓

GID

↓

1002
```

Like UIDs, GIDs are used internally by the kernel.

---

# What is a Group?

A group is a collection of users who share permissions.

Example:

```text
Developers

├── Alice

├── Bob

└── Charlie
```

Groups simplify permission management by assigning access to multiple users collectively.

---

# Why Groups Exist

Without groups:

```text
Administrator

↓

Configure Permissions

↓

User A

User B

User C

User D
```

With groups:

```text
Administrator

↓

Developers Group

↓

All Members
```

Managing permissions becomes significantly simpler.

---

# Primary Group

Each user has one **primary group**.

Example:

```text
User

↓

alice

↓

Primary Group

↓

developers
```

New files created by the user typically inherit the user's primary group, subject to directory settings and filesystem behavior.

---

# Supplementary Groups

Users may belong to multiple additional groups.

Example:

```text
Alice

├── developers

├── docker

├── security

└── sudo
```

This allows a single account to receive permissions for multiple roles.

---

# Viewing Current User

Display the current username:

```bash
whoami
```

Example output:

```text
alice
```

---

# Display User Information

Show UID, GID, and group memberships:

```bash
id
```

Example:

```text
uid=1001(alice)

gid=1001(alice)

groups=1001(alice),27(sudo),998(docker)
```

---

# Display Logged-In Users

List active sessions:

```bash
who
```

Additional information:

```bash
w
```

The `w` command also displays system load and user activity.

---

# The `/etc/passwd` File

User account information is stored in:

```text
/etc/passwd
```

Despite its name, modern Linux systems do **not** store password hashes in this file.

---

# Example Entry

```text
alice:x:1001:1001:Alice:/home/alice:/bin/bash
```

Each field is separated by a colon (`:`).

---

# `/etc/passwd` Structure

| Field | Description |
|----------|-------------|
| Username | Login name |
| Password Placeholder | Usually `x` |
| UID | User ID |
| GID | Primary Group ID |
| GECOS | User description/comment |
| Home Directory | User's home directory |
| Login Shell | Default shell |

---

# Password Placeholder

Example:

```text
x
```

The `x` indicates that the password hash is stored separately in:

```text
/etc/shadow
```

This separation improves security.

---

# Home Directory

Example:

```text
/home/alice
```

The home directory stores:

- Documents
- Configuration files
- Shell history
- SSH keys
- Personal application data

Each user typically has a dedicated home directory.

---

# Login Shell

Example:

```text
/bin/bash
```

Common shells:

| Shell | Description |
|---------|-------------|
| `/bin/bash` | Bourne Again Shell |
| `/bin/sh` | POSIX-compatible shell |
| `/bin/zsh` | Z Shell |
| `/usr/sbin/nologin` | Prevent interactive login |
| `/bin/false` | Immediately exits |

Service accounts often use non-interactive shells.

---

# The `/etc/shadow` File

Password hashes are stored in:

```text
/etc/shadow
```

Example:

```text
alice:$6$...:19840:0:99999:7:::
```

Unlike `/etc/passwd`, access to this file is restricted because it contains sensitive authentication data.

---

# `/etc/shadow` Fields

| Field | Description |
|----------|-------------|
| Username | Login name |
| Password Hash | Encrypted password representation |
| Last Password Change | Days since epoch |
| Minimum Password Age | Minimum days before change |
| Maximum Password Age | Maximum password lifetime |
| Warning Period | Days before expiration warning |
| Inactive Period | Days after expiration before account becomes inactive |
| Expiration Date | Account expiration |
| Reserved | Reserved for future use |

---

# Password Hashes

Modern Linux systems typically use strong password hashing algorithms such as:

- SHA-512 (common on many distributions)
- yescrypt (default on several newer distributions)

The exact algorithm depends on the Linux distribution and system configuration.

Password hashes are designed to make recovering the original password computationally difficult.

---

# The `/etc/group` File

Group information is stored in:

```text
/etc/group
```

Example:

```text
developers:x:1002:alice,bob,charlie
```

---

# `/etc/group` Structure

| Field | Description |
|----------|-------------|
| Group Name | Name of the group |
| Password Placeholder | Usually `x` |
| GID | Group ID |
| Members | Supplementary group members |

---

# Relationship Between User Files

```text
           User Login
                │
                ▼
         /etc/passwd
                │
                ▼
         /etc/shadow
                │
                ▼
          Authentication
                │
                ▼
          User Session
                │
                ▼
           /etc/group
                │
                ▼
         Permission Checks
```

Together, these files define user identities, authentication information, and group memberships.

---

# Cybersecurity Perspective

User accounts are a primary target during attacks.

Common attacker objectives include:

- Credential theft
- Privilege escalation
- Creation of unauthorized accounts
- Abuse of service accounts
- Modification of authentication databases

Security teams should:

- Monitor privileged accounts.
- Audit group memberships.
- Protect authentication files.
- Review inactive or unnecessary accounts.

---

# Business Impact

Proper user management helps organizations:

- Enforce least privilege.
- Improve accountability.
- Support compliance requirements.
- Reduce insider risk.
- Simplify access management.
- Strengthen overall system security.

---

# Enterprise Best Practices

- Assign unique accounts to each user.
- Avoid sharing privileged accounts.
- Use service accounts only for their intended applications.
- Restrict access to `/etc/shadow`.
- Review user and group memberships regularly.
- Disable or remove unused accounts.
- Prefer delegated administrative access over direct root logins.

---

# Key Takeaways

- Linux identifies users and groups using numeric UIDs and GIDs.
- Root, regular users, and service accounts serve different purposes.
- `/etc/passwd` stores account information, while `/etc/shadow` stores password hashes.
- Groups simplify permission management across multiple users.
- Strong identity management is foundational to Linux security.

---


# Part 2 — User Creation, User Modification, User Deletion, Group Management, Password Management, and Account Administration

---

# Introduction

Creating and managing user accounts is one of the primary responsibilities of a Linux administrator.

In enterprise environments, administrators routinely:

- Create employee accounts
- Modify user information
- Assign groups
- Reset passwords
- Lock compromised accounts
- Disable inactive users
- Remove departing employees
- Audit account configurations

Proper account lifecycle management is critical for both security and operational efficiency.

---

# User Lifecycle

```text
Create User

↓

Assign Groups

↓

Set Password

↓

Configure Access

↓

Monitor Activity

↓

Modify Account

↓

Disable Account

↓

Delete Account
```

A structured lifecycle ensures that user access aligns with organizational policies.

---

# Creating Users

Linux provides dedicated utilities for user creation.

Common commands:

- `useradd`
- `adduser` (available on many distributions)

> **Note:** `adduser` is often a higher-level, interactive utility provided by specific distributions, while `useradd` is the standard low-level command available on most Linux systems.

---

# Create a User

Example:

```bash
sudo useradd alice
```

This creates a basic user account.

Depending on system defaults, a home directory may not be created automatically.

---

# Create Home Directory

Create a user with a home directory:

```bash
sudo useradd -m alice
```

Result:

```text
/home/alice
```

The `-m` option creates the user's home directory if it does not already exist.

---

# Specify Login Shell

Example:

```bash
sudo useradd -m -s /bin/bash alice
```

Options:

| Option | Purpose |
|----------|----------|
| `-m` | Create home directory |
| `-s` | Specify login shell |

---

# Specify User ID

Example:

```bash
sudo useradd -u 1050 alice
```

Useful when migrating systems or maintaining consistent UIDs across servers.

Unique UIDs should be maintained to avoid ownership conflicts.

---

# Specify Primary Group

Example:

```bash
sudo useradd -g developers alice
```

The specified group becomes the user's primary group.

---

# Add Supplementary Groups

Example:

```bash
sudo useradd -G docker,sudo,security alice
```

The user joins multiple additional groups.

---

# Complete User Creation Example

```bash
sudo useradd \
-m \
-s /bin/bash \
-g developers \
-G docker,sudo \
alice
```

This creates:

- Home directory
- Bash shell
- Primary group
- Supplementary groups

---

# Set Password

Assign or change a password:

```bash
sudo passwd alice
```

The administrator is prompted to enter and confirm the new password.

---

# Password Workflow

```text
Administrator

↓

passwd

↓

Password Hash

↓

/etc/shadow

↓

Authentication
```

Passwords are stored as hashes rather than plaintext.

---

# Force Password Change

Require a password change at next login:

```bash
sudo passwd -e alice
```

Useful after password resets.

---

# Lock a Password

Disable password authentication:

```bash
sudo passwd -l alice
```

The account remains present, but password-based login is prevented.

---

# Unlock a Password

Re-enable password authentication:

```bash
sudo passwd -u alice
```

This reverses a previous password lock.

---

# View Password Status

```bash
sudo passwd -S alice
```

Example output:

```text
alice P 07/23/2026 0 99999 7 -1
```

The exact format may vary by distribution.

---

# Modify User Accounts

Use:

```bash
sudo usermod
```

This command updates existing user account settings.

---

# Change Login Shell

Example:

```bash
sudo usermod -s /bin/zsh alice
```

The user's default shell becomes:

```text
/bin/zsh
```

---

# Change Home Directory

Example:

```bash
sudo usermod -d /home/newalice alice
```

To move existing files as well:

```bash
sudo usermod -d /home/newalice -m alice
```

The `-m` option moves the contents of the old home directory.

---

# Rename a User

Example:

```bash
sudo usermod -l alice_new alice
```

The username changes, while the UID remains unchanged.

Additional updates (such as renaming the home directory) may be required separately.

---

# Add User to a Group

Example:

```bash
sudo usermod -aG docker alice
```

Explanation:

| Option | Purpose |
|----------|----------|
| `-a` | Append |
| `-G` | Supplementary groups |

> **Important:** Use `-aG` together. Omitting `-a` replaces the user's existing supplementary group list.

---

# Remove User from Group

Example:

```bash
sudo gpasswd -d alice docker
```

The user is removed from the specified supplementary group.

---

# View Group Membership

Display current user's groups:

```bash
groups
```

Display another user's groups:

```bash
groups alice
```

---

# Create Groups

Create a group:

```bash
sudo groupadd developers
```

The system assigns an available GID.

---

# Specify Group ID

Example:

```bash
sudo groupadd -g 1050 developers
```

Useful for consistent group IDs across multiple systems.

---

# Modify Group Name

Rename a group:

```bash
sudo groupmod -n engineers developers
```

The group's GID remains the same.

---

# Delete Group

Example:

```bash
sudo groupdel developers
```

Groups should generally not be deleted while still serving as primary groups for active users.

---

# Delete User

Remove a user account:

```bash
sudo userdel alice
```

The account is deleted, but the home directory is typically retained unless additional options are used.

---

# Delete User and Home Directory

Example:

```bash
sudo userdel -r alice
```

The `-r` option removes:

- Home directory
- Mail spool (where applicable)

Exercise caution before deleting user data.

---

# User Account Verification

Confirm account information:

```bash
id alice
```

Check home directory:

```bash
ls -ld /home/alice
```

Review account entry:

```bash
grep "^alice:" /etc/passwd
```

---

# Account Expiration

Set an expiration date:

```bash
sudo chage -E 2026-12-31 alice
```

After this date, the account cannot be used for login.

---

# View Password Aging

Display password aging information:

```bash
sudo chage -l alice
```

Example output includes:

- Last password change
- Password expiration
- Warning period
- Account expiration

---

# Configure Password Aging

Set maximum password age:

```bash
sudo chage -M 90 alice
```

Set minimum password age:

```bash
sudo chage -m 1 alice
```

Set warning period:

```bash
sudo chage -W 7 alice
```

These settings help enforce organizational password policies.

---

# Disable an Account

Expire the account immediately:

```bash
sudo chage -E 0 alice
```

Alternatively, administrators may lock the account and disable login access according to organizational policy.

---

# Verify Logged-In Users

Display active sessions:

```bash
who
```

Detailed information:

```bash
w
```

These commands assist with user activity monitoring.

---

# Enterprise User Provisioning Workflow

```text
HR Approval

↓

Create User

↓

Assign UID

↓

Assign Groups

↓

Create Home Directory

↓

Set Password

↓

Apply Security Policies

↓

Provide Access
```

Automated provisioning is commonly integrated with centralized identity management systems.

---

# Enterprise User Deprovisioning Workflow

```text
Employee Departure

↓

Disable Account

↓

Lock Password

↓

Archive Data

↓

Remove Access

↓

Delete Account

↓

Audit Completion
```

Timely deprovisioning reduces the risk of unauthorized access.

---

# Cybersecurity Perspective

Attackers often attempt to:

- Create unauthorized accounts.
- Add themselves to privileged groups.
- Reset passwords.
- Modify login shells.
- Establish persistent access through service accounts.

Security teams should:

- Audit account changes.
- Monitor privileged group memberships.
- Review password policy compliance.
- Alert on unexpected account creation or modification.

---

# Business Impact

Well-managed user administration enables organizations to:

- Improve operational efficiency.
- Enforce least privilege.
- Meet regulatory compliance requirements.
- Reduce insider threats.
- Simplify onboarding and offboarding.
- Strengthen identity governance.

---

# Enterprise Best Practices

- Create individual accounts for every user.
- Assign the minimum required privileges.
- Use supplementary groups instead of granting excessive permissions directly.
- Require password changes after administrative resets.
- Review inactive accounts regularly.
- Implement password aging policies appropriate to organizational requirements.
- Automate provisioning and deprovisioning wherever possible.
- Maintain audit logs of account administration activities.

---

# Key Takeaways

- `useradd`, `usermod`, and `userdel` manage user accounts.
- `groupadd`, `groupmod`, and `groupdel` manage groups.
- `passwd` and `chage` control passwords and password aging.
- Proper lifecycle management improves security and operational consistency.
- Auditing user and group changes is essential in enterprise environments.

---

