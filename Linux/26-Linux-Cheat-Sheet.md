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

# 26 - Linux Cheat Sheet

# Part 2 — Users & Groups, Permissions, Processes, Services, System Monitoring, and Package Management

---

# Introduction

This section contains the commands Linux administrators, DevOps engineers, cloud engineers, SOC analysts, and cybersecurity professionals use daily.

Focus areas:

- User management
- Permissions
- Process management
- Services
- System monitoring
- Package management

---

# Users & Groups

## Current User

```bash
whoami
```

---

## Logged-in Users

```bash
who
```

Detailed login information:

```bash
w
```

---

## User Identity

```bash
id username
```

Example:

```bash
id alice
```

Displays:

- UID
- Primary GID
- Supplementary groups

---

## Create User

```bash
sudo useradd username
```

Create home directory (if required by your distribution):

```bash
sudo useradd -m username
```

---

## Set Password

```bash
sudo passwd username
```

---

## Delete User

Delete account only:

```bash
sudo userdel username
```

Delete account and home directory:

```bash
sudo userdel -r username
```

---

## Modify User

Change login shell:

```bash
sudo usermod -s /bin/bash username
```

Lock account:

```bash
sudo usermod -L username
```

Unlock account:

```bash
sudo usermod -U username
```

---

## Groups

Create group:

```bash
sudo groupadd developers
```

Delete group:

```bash
sudo groupdel developers
```

Add user to group:

```bash
sudo usermod -aG developers username
```

Display group membership:

```bash
groups username
```

---

# Important User Files

| File | Purpose |
|------|----------|
| `/etc/passwd` | User accounts |
| `/etc/shadow` | Password hashes (restricted access) |
| `/etc/group` | Group information |
| `/etc/gshadow` | Group passwords and administration |

---

# Permissions

---

## View Permissions

```bash
ls -l
```

Example:

```text
-rwxr-xr--
```

---

## Change Permissions

Numeric mode:

```bash
chmod 755 script.sh
```

Symbolic mode:

```bash
chmod u+x script.sh
```

Remove write permission:

```bash
chmod go-w file.txt
```

---

## Change Ownership

Owner:

```bash
sudo chown alice file.txt
```

Owner and group:

```bash
sudo chown alice:developers file.txt
```

---

## Change Group

```bash
sudo chgrp developers file.txt
```

---

## Default Permissions

View current umask:

```bash
umask
```

Set temporary umask:

```bash
umask 022
```

---

# Special Permissions

SetUID:

```bash
chmod u+s filename
```

SetGID:

```bash
chmod g+s directory
```

Sticky Bit:

```bash
chmod +t directory
```

---

# ACL (Access Control Lists)

View ACL:

```bash
getfacl file.txt
```

Grant ACL permission:

```bash
setfacl -m u:alice:rwx file.txt
```

Remove ACL:

```bash
setfacl -b file.txt
```

---

# Processes

---

## Display Running Processes

```bash
ps aux
```

Process tree:

```bash
ps -ef --forest
```

---

## Interactive Monitoring

```bash
top
```

Alternative:

```bash
htop
```

(if installed)

---

## Search for a Process

```bash
pgrep ssh
```

or

```bash
ps aux | grep ssh
```

---

## Kill Process

Graceful termination:

```bash
kill PID
```

Force termination:

```bash
kill -9 PID
```

Kill by process name:

```bash
pkill process_name
```

---

## Background Jobs

Run in background:

```bash
command &
```

View jobs:

```bash
jobs
```

Bring job to foreground:

```bash
fg
```

Resume in background:

```bash
bg
```

---

# Services

---

## Service Status

```bash
systemctl status ssh
```

---

## Start Service

```bash
sudo systemctl start ssh
```

---

## Stop Service

```bash
sudo systemctl stop ssh
```

---

## Restart Service

```bash
sudo systemctl restart ssh
```

---

## Reload Configuration

```bash
sudo systemctl reload ssh
```

---

## Enable at Boot

```bash
sudo systemctl enable ssh
```

Disable:

```bash
sudo systemctl disable ssh
```

---

## Failed Services

```bash
systemctl --failed
```

---

## List Running Services

```bash
systemctl list-units --type=service
```

---

# Logs

View complete journal:

```bash
journalctl
```

Current boot:

```bash
journalctl -b
```

Previous boot:

```bash
journalctl -b -1
```

Follow logs:

```bash
journalctl -f
```

Service logs:

```bash
journalctl -u ssh
```

---

# System Monitoring

---

## CPU Information

```bash
lscpu
```

---

## Memory Usage

```bash
free -h
```

---

## Disk Usage

```bash
df -h
```

---

## Directory Usage

```bash
du -sh *
```

---

## Block Devices

```bash
lsblk
```

---

## Mounted Filesystems

```bash
mount
```

---

## Filesystem UUIDs

```bash
blkid
```

---

## Open Files

```bash
lsof
```

---

## System Load

```bash
uptime
```

---

## Kernel Messages

```bash
dmesg
```

---

## Process Resource Usage

Sort by CPU:

```bash
ps aux --sort=-%cpu | head
```

Sort by memory:

```bash
ps aux --sort=-%mem | head
```

---

# Package Management

---

## Debian / Ubuntu (APT)

Update package index:

```bash
sudo apt update
```

Upgrade installed packages:

```bash
sudo apt upgrade
```

Install package:

```bash
sudo apt install package_name
```

Remove package:

```bash
sudo apt remove package_name
```

Remove package and configuration:

```bash
sudo apt purge package_name
```

Search packages:

```bash
apt search keyword
```

List installed packages:

```bash
apt list --installed
```

---

## RHEL / Rocky / AlmaLinux / Fedora

Install:

```bash
sudo dnf install package_name
```

Update:

```bash
sudo dnf update
```

Remove:

```bash
sudo dnf remove package_name
```

Search:

```bash
dnf search keyword
```

List installed:

```bash
dnf list installed
```

---

## Verify Installed Package

Debian-based:

```bash
dpkg -l
```

RHEL-based:

```bash
rpm -qa
```

---

# Quick Command Reference

| Task | Command |
|------|---------|
| Current user | `whoami` |
| User info | `id` |
| Add user | `useradd` |
| Change password | `passwd` |
| Add group | `groupadd` |
| Change permissions | `chmod` |
| Change owner | `chown` |
| Running processes | `ps aux` |
| Interactive monitor | `top` |
| Kill process | `kill` |
| Service status | `systemctl status` |
| Logs | `journalctl` |
| Memory | `free -h` |
| Disk | `df -h` |
| Packages | `apt`, `dnf` |

---

# Enterprise Best Practices

- Grant users only the permissions they require.
- Prefer groups over assigning permissions individually.
- Use `sudo` instead of logging in directly as `root`.
- Validate service configuration before restarting production services.
- Monitor CPU, memory, storage, and logs proactively.
- Keep systems updated using your distribution's package manager.
- Review failed services after updates or configuration changes.

---

# Cybersecurity Perspective

These commands support:

- User and privilege auditing
- Incident response
- Malware investigations
- Log review
- Process analysis
- Service validation
- Patch management
- Compliance assessments

---

# Key Takeaways

- User and permission management are fundamental administrative skills.
- Processes and services should be monitored continuously.
- Package management keeps systems secure and up to date.
- Logs and monitoring commands are essential for troubleshooting and incident response.

---

# 26 - Linux Cheat Sheet

# Part 3 — Networking, Storage, Security, SSH, Shell Scripting, Troubleshooting, One-Liners, and Enterprise Administration

---

# Introduction

This section contains the Linux commands most frequently used in:

- System Administration
- DevOps
- Cloud Engineering
- Site Reliability Engineering (SRE)
- SOC Operations
- Incident Response
- Digital Forensics
- Penetration Testing
- Enterprise Production Support

Think of this as your **day-to-day operational cheat sheet**.

---

# Networking

---

## Display IP Addresses

```bash
ip addr
```

Short form:

```bash
ip a
```

---

## Display Routing Table

```bash
ip route
```

Short form:

```bash
ip r
```

---

## Display Network Interfaces

```bash
ip link
```

---

## Enable Network Interface

```bash
sudo ip link set eth0 up
```

---

## Disable Network Interface

```bash
sudo ip link set eth0 down
```

---

## Test Connectivity

```bash
ping google.com
```

Limit packets:

```bash
ping -c 4 google.com
```

---

## Trace Network Path

```bash
traceroute google.com
```

Alternative:

```bash
tracepath google.com
```

---

## DNS Lookup

Using `dig`:

```bash
dig example.com
```

Using `host`:

```bash
host example.com
```

Using `nslookup`:

```bash
nslookup example.com
```

---

## Display Listening Ports

```bash
ss -tulpn
```

TCP only:

```bash
ss -tlpn
```

UDP only:

```bash
ss -ulpn
```

---

## Network Connections

```bash
ss -tunap
```

---

## View ARP Table

```bash
ip neigh
```

---

## Download Files

Using `wget`:

```bash
wget https://example.com/file.zip
```

Using `curl`:

```bash
curl -O https://example.com/file.zip
```

---

# Storage & Filesystems

---

## Block Devices

```bash
lsblk
```

---

## Filesystem Usage

```bash
df -h
```

---

## Directory Usage

```bash
du -sh *
```

---

## Filesystem UUIDs

```bash
blkid
```

---

## Mounted Filesystems

```bash
mount
```

---

## Mount Filesystem

```bash
sudo mount /dev/sdb1 /mnt
```

---

## Unmount Filesystem

```bash
sudo umount /mnt
```

---

## View `/etc/fstab`

```bash
cat /etc/fstab
```

---

## Open Files

```bash
lsof
```

---

# SSH

---

## Connect to Remote Server

```bash
ssh user@host
```

---

## Connect Using Specific Port

```bash
ssh -p 2222 user@host
```

---

## Copy File to Remote Host

```bash
scp file.txt user@host:/tmp/
```

---

## Copy Directory

```bash
scp -r directory user@host:/tmp/
```

---

## Copy File from Remote Host

```bash
scp user@host:/tmp/file.txt .
```

---

## Generate SSH Key Pair

```bash
ssh-keygen
```

---

## Copy Public Key

```bash
ssh-copy-id user@host
```

---

## SSH Configuration

System-wide:

```text
/etc/ssh/sshd_config
```

Client:

```text
~/.ssh/config
```

---

# Security

---

## Current User

```bash
whoami
```

---

## User Identity

```bash
id
```

---

## Current Groups

```bash
groups
```

---

## View Failed Login Attempts

Ubuntu/Debian:

```bash
grep "Failed password" /var/log/auth.log
```

RHEL-family:

```bash
grep "Failed password" /var/log/secure
```

---

## View Logged-in Users

```bash
who
```

Detailed view:

```bash
w
```

---

## File Permissions

```bash
ls -l
```

---

## Change Permissions

```bash
chmod
```

---

## Change Ownership

```bash
chown
```

---

## Access Control Lists

Display:

```bash
getfacl file
```

Modify:

```bash
setfacl
```

---

# Shell Scripting

---

## Script Header

```bash
#!/bin/bash
```

---

## Execute Script

```bash
./script.sh
```

---

## Variables

```bash
NAME="Linux"

echo "$NAME"
```

---

## Positional Parameters

```text
$0
```

Script name

```text
$1
```

First argument

```text
$#
```

Argument count

---

## Conditional

```bash
if
```

---

## Loop

```bash
for
```

---

## While Loop

```bash
while
```

---

## Case Statement

```bash
case
```

---

# Troubleshooting

---

## System Information

```bash
hostnamectl
```

---

## Kernel Version

```bash
uname -r
```

---

## Current Boot Logs

```bash
journalctl -b
```

---

## Previous Boot

```bash
journalctl -b -1
```

---

## Kernel Messages

```bash
dmesg
```

---

## Failed Services

```bash
systemctl --failed
```

---

## Service Status

```bash
systemctl status service
```

---

## Process List

```bash
ps aux
```

---

## Interactive Monitor

```bash
top
```

---

## Memory

```bash
free -h
```

---

## Storage

```bash
df -h
```

---

## Largest Directories

```bash
du -sh /*
```

---

## Search Logs

```bash
grep "error" logfile
```

---

## Follow Logs

```bash
journalctl -f
```

---

# Enterprise One-Liners

---

## Top CPU Consumers

```bash
ps aux --sort=-%cpu | head
```

---

## Top Memory Consumers

```bash
ps aux --sort=-%mem | head
```

---

## Largest Files

```bash
find / -type f -exec du -h {} + | sort -hr | head
```

---

## Largest Directories

```bash
du -sh /* | sort -hr
```

---

## Find Empty Files

```bash
find . -type f -empty
```

---

## Find Empty Directories

```bash
find . -type d -empty
```

---

## Find Files Modified Today

```bash
find . -mtime 0
```

---

## Find Files Larger Than 100 MB

```bash
find / -type f -size +100M
```

---

## Count Files in Current Directory

```bash
find . -maxdepth 1 -type f | wc -l
```

---

## Display Open Ports

```bash
ss -tulpn
```

---

## Check DNS

```bash
dig google.com
```

---

## Test HTTPS Response

```bash
curl -I https://example.com
```

---

## Generate SHA-256 Checksum

```bash
sha256sum file.iso
```

---

# Enterprise Administration Workflow

```text
Monitoring

↓

Alert

↓

Investigation

↓

Logs

↓

Root Cause Analysis

↓

Resolution

↓

Validation

↓

Documentation

↓

Preventive Improvement
```

---

# Common Linux Log Locations

| Location | Purpose |
|----------|---------|
| `/var/log/auth.log` | Authentication (Debian/Ubuntu) |
| `/var/log/secure` | Authentication (RHEL-family) |
| `/var/log/syslog` | General system logs (Debian/Ubuntu) |
| `/var/log/messages` | General system logs (RHEL-family) |
| `/var/log/kern.log` | Kernel logs (Debian/Ubuntu) |
| `journalctl` | systemd journal |
| `/var/log/nginx/` | NGINX logs |
| `/var/log/httpd/` | Apache logs (RHEL-family) |
| `/var/log/apache2/` | Apache logs (Debian/Ubuntu) |

---

# Enterprise Best Practices

- Verify network connectivity before investigating applications.
- Monitor disk usage proactively to avoid outages.
- Use SSH key authentication instead of passwords where appropriate.
- Review logs regularly and centralize them when possible.
- Use shell scripts to automate repetitive administrative tasks.
- Validate changes before applying them to production systems.
- Document incidents, resolutions, and preventive actions.

---

# Cybersecurity Perspective

These commands are heavily used during:

- Incident response
- Threat hunting
- Malware analysis
- Privilege auditing
- Vulnerability assessments
- Log correlation
- Forensic investigations
- Security monitoring

---

# Key Takeaways

- Networking and storage commands are essential for production troubleshooting.
- SSH is the primary tool for secure remote administration.
- Security and troubleshooting commands should be part of every administrator's toolkit.
- Enterprise one-liners improve efficiency during investigations and operations.

---

