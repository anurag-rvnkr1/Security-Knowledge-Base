# 25 - Linux Interview Questions

# Part 1 — Linux Fundamentals Interview Questions (Beginner to Intermediate)

---

# Introduction

Linux interview questions are designed to evaluate:

- Linux fundamentals
- Command-line proficiency
- System administration knowledge
- Troubleshooting ability
- Security awareness
- Problem-solving skills

This chapter covers interview questions from **fresher to enterprise-level Linux administrator, DevOps, Cloud, SOC, and Cybersecurity roles**.

---

# Interview Preparation Strategy

Enterprise interviewers generally evaluate candidates in this order:

```text
Linux Basics

↓

Command Line

↓

Filesystem

↓

Permissions

↓

Processes

↓

Networking

↓

Security

↓

Troubleshooting

↓

Scenario-Based Questions

↓

Hands-on Assessment
```

---

# Types of Linux Interview Questions

| Level | Focus |
|--------|-------|
| Beginner | Basic Linux concepts |
| Intermediate | Administration and troubleshooting |
| Advanced | Enterprise architecture and security |
| Practical | Hands-on command execution |
| Scenario-Based | Real-world production issues |

---

# Q1. What is Linux?

### Answer

Linux is an open-source, Unix-like operating system kernel created by **Linus Torvalds** in 1991.

A Linux operating system consists of:

- Kernel
- Shell
- System libraries
- Utilities
- Package manager
- Applications

Linux is widely used for:

- Servers
- Cloud computing
- Embedded systems
- Supercomputers
- Containers
- Cybersecurity

---

# Q2. What is the Linux Kernel?

### Answer

The kernel is the core component of the operating system.

Responsibilities include:

- Process management
- Memory management
- Device management
- Filesystem management
- System call handling
- Network management

Architecture:

```text
Applications

↓

Shell

↓

Kernel

↓

Hardware
```

---

# Q3. What is the Shell?

### Answer

The shell is a command interpreter that allows users to communicate with the Linux kernel.

Popular shells include:

- Bash
- Zsh
- Fish
- Ksh
- Tcsh

---

# Q4. What is the difference between Linux and Unix?

| Linux | Unix |
|--------|------|
| Open source | Mostly proprietary |
| Community driven | Vendor driven |
| Multiple distributions | Vendor-specific implementations |
| Highly customizable | Less flexible |

---

# Q5. What are Linux distributions?

### Answer

A Linux distribution combines the Linux kernel with software packages and tools.

Examples:

- Ubuntu
- Debian
- Red Hat Enterprise Linux (RHEL)
- Rocky Linux
- AlmaLinux
- Fedora
- Arch Linux
- openSUSE

---

# Q6. Explain the Linux boot process.

### Answer

```text
BIOS/UEFI

↓

Bootloader (GRUB)

↓

Kernel

↓

initramfs

↓

systemd

↓

Services

↓

Login Prompt
```

---

# Q7. What is systemd?

### Answer

`systemd` is the initialization system used by most modern Linux distributions.

Responsibilities:

- Starts services
- Manages targets
- Controls system startup
- Handles logging through `journalctl`
- Manages timers

Useful commands:

```bash
systemctl status ssh
```

```bash
systemctl restart ssh
```

---

# Q8. What is the Linux filesystem?

### Answer

Linux uses a hierarchical directory structure beginning at the root directory:

```text
/
```

Important directories:

| Directory | Purpose |
|-----------|----------|
| / | Root |
| /home | User home directories |
| /etc | Configuration files |
| /var | Variable data |
| /usr | User programs |
| /bin | Essential binaries |
| /tmp | Temporary files |
| /opt | Optional software |

---

# Q9. What is an inode?

### Answer

An inode stores metadata about a file, including:

- Ownership
- Permissions
- File size
- Timestamps
- Data block locations

The filename itself is stored in the directory entry, not in the inode.

---

# Q10. What is the difference between a hard link and a symbolic link?

| Hard Link | Symbolic Link |
|------------|---------------|
| Shares the same inode | Has its own inode |
| Cannot span filesystems | Can span filesystems |
| Usually cannot reference directories | Can reference directories |
| Remains valid if original filename is removed (while at least one hard link exists) | Becomes broken if the target is removed |

---

# Q11. What are file permissions?

### Answer

Linux permissions determine who can:

- Read
- Write
- Execute

Permission groups:

```text
Owner

Group

Others
```

Example:

```text
-rwxr-xr--
```

---

# Q12. Explain chmod.

### Answer

`chmod` changes file permissions.

Example:

```bash
chmod 755 script.sh
```

Meaning:

```text
Owner

↓

Read + Write + Execute

Group

↓

Read + Execute

Others

↓

Read + Execute
```

---

# Q13. Explain chown.

### Answer

`chown` changes file ownership.

Example:

```bash
sudo chown user:group file.txt
```

---

# Q14. Difference between chmod and chown?

| chmod | chown |
|--------|--------|
| Changes permissions | Changes ownership |
| Controls access rights | Controls owner and group |

---

# Q15. What is sudo?

### Answer

`sudo` allows authorized users to execute commands with elevated privileges according to system policy.

Example:

```bash
sudo apt update
```

---

# Q16. What is the root user?

### Answer

The `root` user is the superuser with unrestricted administrative privileges.

Enterprise best practice:

- Use individual user accounts.
- Elevate privileges with `sudo`.
- Avoid routine interactive use of the root account.

---

# Q17. What is PATH?

### Answer

`PATH` is an environment variable containing directories searched for executable commands.

View it:

```bash
echo $PATH
```

---

# Q18. What is the difference between absolute and relative paths?

| Absolute Path | Relative Path |
|---------------|---------------|
| Starts from `/` | Starts from current directory |
| Independent of current location | Depends on current location |

Examples:

Absolute:

```text
/home/user/file.txt
```

Relative:

```text
documents/file.txt
```

---

# Q19. How do you display the current working directory?

### Answer

```bash
pwd
```

---

# Q20. How do you list files?

### Answer

```bash
ls
```

Detailed listing:

```bash
ls -l
```

Include hidden files:

```bash
ls -la
```

---

# Q21. How do you create directories?

### Answer

```bash
mkdir directory_name
```

Create nested directories:

```bash
mkdir -p parent/child
```

---

# Q22. How do you copy, move, and remove files?

Copy:

```bash
cp source destination
```

Move:

```bash
mv source destination
```

Remove:

```bash
rm filename
```

Remove directory recursively:

```bash
rm -r directory
```

Use recursive deletion carefully, especially with elevated privileges.

---

# Q23. How do you search for files?

### Answer

```bash
find /path -name filename
```

Example:

```bash
find /home -name report.txt
```

---

# Q24. How do you search inside files?

### Answer

```bash
grep "pattern" filename
```

Recursive search:

```bash
grep -R "pattern" directory
```

---

# Q25. How do you display file contents?

Commands:

```bash
cat
```

```bash
less
```

```bash
more
```

```bash
head
```

```bash
tail
```

---

# Q26. What is the difference between cat and less?

| cat | less |
|------|-------|
| Displays entire file | Allows interactive navigation |
| Best for small files | Better for large files |

---

# Q27. How do you check disk usage?

Filesystem usage:

```bash
df -h
```

Directory usage:

```bash
du -sh directory
```

---

# Q28. How do you check memory usage?

```bash
free -h
```

---

# Q29. How do you check CPU and process usage?

Interactive:

```bash
top
```

or

```bash
htop
```

(if installed)

---

# Q30. How do you check system uptime?

```bash
uptime
```

---

# Interview Tips

- Explain concepts before giving commands.
- Mention practical use cases.
- Avoid memorized one-line answers.
- Relate answers to production environments where appropriate.
- If unsure, explain how you would investigate rather than guessing.

---

# Key Takeaways

- Master Linux fundamentals before advanced topics.
- Understand both concepts and commands.
- Explain *why* a command is used, not just *how*.
- Enterprise interviews value structured thinking and troubleshooting skills as much as memorization.

---


