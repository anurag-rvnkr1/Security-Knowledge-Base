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

# 25 - Linux Interview Questions

# Part 2 — Processes, Services, Networking, Storage, Shell Scripting, and Security Interview Questions

---

# Introduction

After verifying Linux fundamentals, interviewers typically assess your ability to manage:

- Processes
- Services
- Networking
- Storage
- Shell scripting
- Security

These topics are frequently asked in interviews for:

- Linux Administrator
- System Administrator
- DevOps Engineer
- Cloud Engineer
- Site Reliability Engineer (SRE)
- SOC Analyst
- Security Analyst
- VAPT / Penetration Tester
- Cybersecurity Engineer

---

# Section 1 — Process Management

---

# Q31. What is a process?

### Answer

A process is an instance of a running program.

Each process has:

- Process ID (PID)
- Parent Process ID (PPID)
- Memory allocation
- CPU state
- Open file descriptors
- Execution context

Example:

```text
Program (nginx)

↓

Executed

↓

Running Process (PID 1234)
```

---

# Q32. Difference between a process and a thread?

| Process | Thread |
|----------|--------|
| Independent execution unit | Lightweight execution unit within a process |
| Separate memory space | Shares memory with other threads in the same process |
| Higher resource usage | Lower resource usage |
| Better isolation | Faster communication |

---

# Q33. How do you view running processes?

### Answer

```bash
ps aux
```

Interactive monitoring:

```bash
top
```

or

```bash
htop
```

(if installed)

---

# Q34. What is a zombie process?

### Answer

A zombie process has completed execution, but its parent process has not yet collected its exit status.

Characteristics:

- No CPU usage
- Minimal memory usage
- Remains in the process table
- Displayed with the `Z` state

---

# Q35. How do you terminate a process?

Graceful termination:

```bash
kill PID
```

Force termination:

```bash
kill -9 PID
```

Best practice:

Use `SIGTERM` (`kill`) first and `SIGKILL` (`kill -9`) only when necessary.

---

# Q36. What is the difference between SIGTERM and SIGKILL?

| SIGTERM | SIGKILL |
|----------|----------|
| Signal 15 | Signal 9 |
| Can be handled by the application | Cannot be intercepted or ignored |
| Allows graceful shutdown | Immediately terminates the process |

---

# Section 2 — Services

---

# Q37. What is a service?

### Answer

A service (daemon) is a background process that provides functionality such as:

- SSH
- Web servers
- Databases
- DNS
- Monitoring agents

---

# Q38. How do you check service status?

```bash
systemctl status ssh
```

---

# Q39. How do you start, stop, and restart a service?

Start:

```bash
systemctl start service-name
```

Stop:

```bash
systemctl stop service-name
```

Restart:

```bash
systemctl restart service-name
```

Reload configuration (when supported):

```bash
systemctl reload service-name
```

---

# Q40. How do you enable a service at boot?

```bash
systemctl enable service-name
```

Disable:

```bash
systemctl disable service-name
```

---

# Q41. How do you list failed services?

```bash
systemctl --failed
```

---

# Q42. Where do you check service logs?

```bash
journalctl -u service-name
```

---

# Section 3 — Networking

---

# Q43. How do you display IP addresses?

```bash
ip addr
```

---

# Q44. How do you display the routing table?

```bash
ip route
```

---

# Q45. Difference between TCP and UDP?

| TCP | UDP |
|------|------|
| Connection-oriented | Connectionless |
| Reliable delivery | Best-effort delivery |
| Ordered packets | No delivery order guarantee |
| Higher overhead | Lower overhead |
| Used for SSH, HTTP(S), SMTP | Used for DNS, DHCP, VoIP, streaming |

---

# Q46. How do you test connectivity?

```bash
ping hostname
```

---

# Q47. How do you trace the network path?

```bash
traceroute hostname
```

or

```bash
tracepath hostname
```

---

# Q48. How do you view listening ports?

```bash
ss -tulpn
```

---

# Q49. How do you troubleshoot DNS?

Typical steps:

1. Check `/etc/resolv.conf`
2. Verify network connectivity
3. Query DNS using `dig`, `host`, or `nslookup`
4. Review local `/etc/hosts`
5. Confirm DNS server availability

---

# Q50. Difference between public IP and private IP?

| Public IP | Private IP |
|------------|------------|
| Internet routable | Internal network only |
| Globally unique | Reused in private networks |
| Assigned by ISP or cloud provider | Assigned locally |

Private IPv4 ranges:

- 10.0.0.0/8
- 172.16.0.0/12
- 192.168.0.0/16

---

# Section 4 — Storage

---

# Q51. How do you check disk usage?

Filesystem usage:

```bash
df -h
```

Directory usage:

```bash
du -sh directory
```

---

# Q52. What is a mount point?

### Answer

A mount point is a directory where a filesystem is attached to the directory tree.

Example:

```text
/

↓

/mnt

↓

Mounted Filesystem
```

---

# Q53. What is `/etc/fstab`?

### Answer

`/etc/fstab` defines filesystems that should be mounted automatically during boot.

It typically includes:

- Device or UUID
- Mount point
- Filesystem type
- Mount options
- Dump/pass values

---

# Q54. What is an inode?

### Answer

An inode stores metadata about a file, such as:

- Permissions
- Owner
- Group
- File size
- Timestamps
- Block locations

---

# Q55. What causes "No space left on device" even when disk space appears available?

Possible causes include:

- Inode exhaustion
- Deleted-but-open files
- Reserved filesystem blocks
- Quotas

Interview tip:

Mention both disk space (`df -h`) and inode usage (`df -i`).

---

# Section 5 — Shell Scripting

---

# Q56. What is a shell script?

### Answer

A shell script is a text file containing shell commands executed sequentially.

Example:

```bash
#!/bin/bash
echo "Hello, Linux!"
```

---

# Q57. How do you make a script executable?

```bash
chmod +x script.sh
```

Execute:

```bash
./script.sh
```

---

# Q58. Difference between `$0`, `$1`, and `$#`?

| Variable | Meaning |
|-----------|----------|
| `$0` | Script name |
| `$1` | First positional argument |
| `$#` | Number of arguments |

---

# Q59. How do you use variables?

```bash
NAME="Anurag"

echo "$NAME"
```

---

# Q60. What are common control structures in Bash?

Examples:

Conditional:

```bash
if
```

Loop:

```bash
for
```

Loop:

```bash
while
```

Selection:

```bash
case
```

---

# Section 6 — Security

---

# Q61. What is the principle of least privilege?

### Answer

Users and processes should receive only the permissions required to perform their tasks.

Benefits:

- Reduces attack surface
- Limits accidental changes
- Restricts privilege escalation opportunities

---

# Q62. What is `sudo`?

### Answer

`sudo` allows authorized users to execute commands with elevated privileges according to defined policies.

---

# Q63. Difference between authentication and authorization?

| Authentication | Authorization |
|----------------|---------------|
| Verifies identity | Determines permissions |
| "Who are you?" | "What can you do?" |

---

# Q64. What is SSH?

### Answer

Secure Shell (SSH) provides encrypted remote administration and secure file transfer.

Common uses:

- Remote login
- Secure command execution
- File transfer (SCP/SFTP)
- Port forwarding

---

# Q65. How do you view failed SSH login attempts?

Ubuntu/Debian:

```bash
grep "Failed password" /var/log/auth.log
```

RHEL-family:

```bash
grep "Failed password" /var/log/secure
```

---

# Q66. What is a firewall?

### Answer

A firewall filters network traffic according to defined security rules.

Common Linux firewall frameworks:

- nftables
- firewalld
- iptables (legacy)

---

# Q67. Why should you avoid logging in directly as root?

Reasons:

- Reduced accountability
- Increased risk of accidental system changes
- Larger impact if credentials are compromised

Preferred approach:

- Log in as a standard user.
- Use `sudo` when administrative access is required.

---

# Q68. What is log analysis?

### Answer

Log analysis is the process of reviewing system and application logs to identify:

- Errors
- Performance issues
- Security events
- Configuration problems
- Operational trends

---

# Q69. What is root cause analysis (RCA)?

### Answer

Root cause analysis identifies the underlying cause of an incident rather than only addressing its symptoms.

Typical workflow:

```text
Problem

↓

Evidence

↓

Analysis

↓

Root Cause

↓

Resolution

↓

Prevention
```

---

# Q70. Why is documentation important after troubleshooting?

Documentation helps:

- Build organizational knowledge
- Speed future incident response
- Support audits and compliance
- Improve operational consistency
- Reduce Mean Time to Resolution (MTTR)

---

# Interview Tips

- Explain your reasoning before listing commands.
- Mention validation steps after making changes.
- Distinguish between temporary fixes and permanent solutions.
- Relate answers to production environments and best practices.
- Demonstrate an understanding of security implications when discussing administration tasks.

---

# Key Takeaways

- Process and service management are foundational Linux administration skills.
- Networking and storage questions often assess troubleshooting ability.
- Shell scripting demonstrates automation capabilities.
- Security questions evaluate operational maturity and safe administration practices.
- Strong interview answers combine concepts, commands, and real-world context.

---


