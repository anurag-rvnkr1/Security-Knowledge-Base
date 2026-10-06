# Reverse Engineering

> A structured, practical and enterprise-oriented guide to understanding compiled software, binaries, executable formats, machine code, program behavior, vulnerabilities and low-level system operation.

---

## Overview

Reverse engineering is the disciplined process of analyzing software when its original source code, design documentation or internal implementation is unavailable or incomplete.

It involves moving from:

```text
Compiled Binary
      │
      ▼
Executable Format
      │
      ▼
Machine Code
      │
      ▼
Assembly
      │
      ▼
Functions
      │
      ▼
Control Flow
      │
      ▼
Program Logic
      │
      ▼
Behavior
      │
      ▼
Security Understanding
```

This knowledge base approaches reverse engineering from both **security engineering** and **software-analysis** perspectives.

It covers:

- Computer architecture
- Assembly language
- Binary internals
- PE and ELF
- Linking and loading
- Disassembly
- Decompilation
- Function analysis
- Control-flow analysis
- Debugging
- Runtime analysis
- Obfuscation
- Packing
- Anti-debugging
- Anti-analysis
- Vulnerability research
- Patch analysis
- Binary diffing
- Automation
- Reverse-engineering tooling
- Malware and security research
- Advanced case studies

---

# Why Reverse Engineering Matters

Modern security professionals frequently encounter software without source code.

Examples include:

```text
Malware
      │
      ├── Suspicious executable
      │
      ├── Packed payload
      │
      ├── Unknown DLL
      │
      └── Memory-resident code
```

But reverse engineering is much broader than malware.

It is useful for:

```text
Vulnerability Research
Software Security
Incident Response
Malware Analysis
Digital Forensics
Threat Research
Product Security
Application Security
Firmware Analysis
IoT Security
Exploit Development
Patch Analysis
Software Compatibility
```

A strong reverse engineer can answer:

> **What does this program actually do, how does it do it, and where are its security-relevant assumptions?**

---

# Reverse Engineering vs Malware Analysis

These areas overlap, but they have different goals.

## Malware Analysis

Primarily asks:

```text
Is it malicious?
What does it do?
How does it persist?
What infrastructure does it use?
How can we detect it?
```

## Reverse Engineering

Can ask:

```text
How is this functionality implemented?
What instructions perform it?
How are data structures represented?
How does the binary interact with the operating system?
Where are security boundaries?
Why does this vulnerability exist?
```

Therefore:

```text
Malware Analysis
       +
Reverse Engineering
       +
Vulnerability Research
       ↓
Deep Software Understanding
```

---

# Core Reverse Engineering Workflow

A professional investigation commonly follows:

```text
              Binary
                │
                ▼
          Evidence Intake
                │
                ▼
        File Identification
                │
                ▼
          Static Triage
                │
        ┌───────┴───────┐
        ▼               ▼
    Disassembly     Metadata
        │               │
        └───────┬───────┘
                ▼
          Function Analysis
                │
                ▼
         Control-Flow Analysis
                │
                ▼
          Data-Flow Analysis
                │
                ▼
         Decompilation
                │
                ▼
          Runtime Analysis
                │
                ▼
       Debugging / Validation
                │
                ▼
       Behavioral Understanding
                │
                ▼
          Security Assessment
```

---

# Reverse Engineering Objectives

Depending on the investigation, objectives may include:

### Software Understanding

```text
Program architecture
Functions
Dependencies
Data structures
Control flow
Algorithms
```

### Security Analysis

```text
Attack surface
Input validation
Trust boundaries
Memory safety
Authentication logic
Cryptographic implementation
Privilege boundaries
```

### Malware Research

```text
Payload behavior
Persistence
C2
Configuration
Anti-analysis
Injection
```

### Vulnerability Research

```text
Crash
Root cause
Affected function
Memory corruption
Patch difference
Exploitability
```

---

# Reverse Engineering Mindset

Reverse engineering requires an evidence-driven mindset.

Do not begin with:

> "I know what this function does."

Instead begin with:

```text
What do I know?
        │
        ▼
What evidence supports it?
        │
        ▼
What remains unknown?
        │
        ▼
What experiment can answer it?
```

---

# Observation vs Inference

A professional reverse-engineering report should distinguish:

### Observation

```text
The function calls CreateFileW.
```

### Inference

```text
The function likely opens a file.
```

### Confirmed Behavior

```text
Runtime execution shows the function opening C:\example.txt.
```

These are different levels of confidence.

---

# Binary Analysis Layers

Reverse engineering can be viewed as multiple layers:

```text
┌─────────────────────────────┐
│ Application Behavior        │
├─────────────────────────────┤
│ Program Logic               │
├─────────────────────────────┤
│ Functions / Data Structures │
├─────────────────────────────┤
│ Assembly                    │
├─────────────────────────────┤
│ Machine Instructions        │
├─────────────────────────────┤
│ CPU Architecture            │
├─────────────────────────────┤
│ Hardware                    │
└─────────────────────────────┘
```

The analyst moves between layers as necessary.

---

# Computer Architecture Foundation

Reverse engineering requires understanding how computers execute instructions.

Core concepts include:

```text
CPU
Registers
Instruction Pointer
Stack
Heap
Virtual Memory
Caches
Processes
Threads
System Calls
```

Important architectures include:

```text
x86
x86-64
ARM
ARM64
MIPS
RISC-V
```

This repository focuses primarily on:

```text
x86-64
ARM64
```

while introducing concepts transferable to other architectures.

---

# Assembly Language

Assembly provides a human-readable representation of machine instructions.

Example:

```asm
mov eax, 5
add eax, 3
ret
```

Conceptually:

```text
EAX = 5
EAX = EAX + 3
return
```

Reverse engineering is the process of reconstructing higher-level meaning from instructions like these.

---

# Registers

Registers store small pieces of CPU state.

For x86-64:

```text
RAX
RBX
RCX
RDX
RSI
RDI
RSP
RBP
RIP
```

Some registers have special roles.

For example:

```text
RSP
 ↓
Stack Pointer

RBP
 ↓
Frame/Base Pointer

RIP
 ↓
Instruction Pointer
```

---

# Stack

The stack commonly contains:

```text
Function arguments
Return addresses
Saved registers
Local variables
Temporary data
```

Conceptually:

```text
High Address
┌──────────────────┐
│ Function Data    │
├──────────────────┤
│ Return Address   │
├──────────────────┤
│ Saved Registers  │
├──────────────────┤
│ Local Variables  │
└──────────────────┘
Low Address
```

Understanding the stack is essential for:

- Debugging
- Function analysis
- Calling conventions
- Memory corruption research

---

# Heap

The heap is commonly used for dynamically allocated memory.

Conceptually:

```text
Program
  │
  ├── Stack
  │
  └── Heap
       │
       ├── Object
       ├── Buffer
       └── Structure
```

Heap behavior is particularly important for vulnerability research.

---

# Virtual Memory

Modern operating systems provide processes with virtual address spaces.

```text
Process A
┌─────────────────┐
│ Code            │
│ Libraries       │
│ Heap            │
│ Stack           │
└─────────────────┘

Process B
┌─────────────────┐
│ Code            │
│ Libraries       │
│ Heap            │
│ Stack           │
└─────────────────┘
```

The processes generally operate in separate virtual address spaces.

---

# Executable Formats

Reverse engineers must understand how operating systems represent executable files.

Major formats include:

```text
Windows
  ↓
PE / PE32+

Linux / Unix
  ↓
ELF
```

These formats describe:

```text
Code
Data
Imports
Exports
Relocations
Sections
Metadata
Dependencies
Entry Point
```

---

# PE

The Portable Executable format is used by Windows.

Important structures include:

```text
DOS Header
PE Signature
COFF Header
Optional Header
Section Table
Import Directory
Export Directory
Relocations
Resources
TLS
Debug Information
```

---

# ELF

Executable and Linkable Format is common on Linux and Unix-like systems.

Important structures include:

```text
ELF Header
Program Headers
Section Headers
Segments
Dynamic Section
Symbol Tables
Relocations
```

---

# Static Analysis

Static analysis examines software without executing it.

Common techniques:

```text
Strings
Imports
Exports
Disassembly
Decompilation
Control-flow analysis
Cross-references
Data-flow analysis
Binary diffing
```

---

# Dynamic Analysis

Dynamic analysis examines software while it executes.

Common techniques:

```text
Debugging
Breakpoints
Tracing
API monitoring
Memory inspection
System-call tracing
Network observation
```

---

# Static + Dynamic

The strongest analysis often combines both.

```text
Static
  ↓
Hypothesis
  ↓
Dynamic
  ↓
Validation
  ↓
Static
  ↓
Deeper Understanding
```

---

# Disassembly

Disassembly converts machine code into assembly instructions.

For example:

```bash
objdump -d sample
```

Other tools include:

```text
Ghidra
IDA
Binary Ninja
radare2
rizin
llvm-objdump
```

---

# Decompilation

Decompilers attempt to reconstruct source-like code.

Example conceptual output:

```c
if (value == 0) {
    return;
}

process_data(value);
```

The original source code may have looked completely different.

Therefore decompiled code should be treated as an approximation.

---

# Control-Flow Graph

A Control-Flow Graph (CFG) represents possible execution paths.

```text
        Start
          │
          ▼
       Check
       /   \
     Yes    No
      │      │
      ▼      ▼
   Process  Exit
      │
      ▼
     End
```

CFGs are fundamental to:

- Malware analysis
- Vulnerability research
- Binary optimization
- Program understanding

---

# Call Graph

A call graph represents function relationships.

```text
main()
 │
 ├── initialize()
 │
 ├── authenticate()
 │      └── verify()
 │
 └── process()
        ├── parse()
        └── save()
```

This helps identify high-value functions quickly.

---

# Debugging

Debuggers allow analysts to observe program execution.

Important capabilities include:

```text
Run
Pause
Step
Step Over
Step Into
Step Out
Breakpoints
Watchpoints
Register inspection
Memory inspection
Thread inspection
```

Common tools:

```text
x64dbg
WinDbg
GDB
LLDB
```

---

# Obfuscation

Obfuscation attempts to make code harder to understand.

Examples include:

```text
String encryption
Control-flow obfuscation
Opaque predicates
API hashing
Junk instructions
Dynamic code generation
```

Obfuscation is not exclusive to malware.

Commercial software may also use it for intellectual-property protection.

---

# Packing

Packers transform a binary into a representation that reconstructs the original code at runtime.

Conceptually:

```text
Packed Binary
      │
      ▼
Unpacking Stub
      │
      ▼
Original Code
      │
      ▼
Execution
```

Reverse engineering often requires identifying the unpacked code.

---

# Anti-Reverse-Engineering

Programs may attempt to detect:

```text
Debugger
VM
Sandbox
Analysis tools
Breakpoints
Instrumentation
```

The analyst should identify the detection mechanism and understand its impact on observed behavior.

---

# Vulnerability Research

Reverse engineering is also fundamental to vulnerability research.

Typical workflow:

```text
Binary
  ↓
Crash
  ↓
Reproduce
  ↓
Root Cause
  ↓
Affected Function
  ↓
Memory Corruption
  ↓
Exploitability
  ↓
Mitigation
```

The goal is not merely to reproduce a crash.

The goal is to understand why it occurs and what security boundary it affects.

---

# Patch Diffing

When a vendor releases a security update:

```text
Old Binary
     │
     ├─────────┐
     │         │
     ▼         ▼
New Binary  Diff
     │         │
     └────┬────┘
          ▼
    Changed Functions
          │
          ▼
    Security Analysis
```

Patch diffing can help identify vulnerability fixes and understand affected code.

---

# Reverse Engineering Automation

Automation can assist with:

```text
Function extraction
String extraction
Cross-reference analysis
Binary comparison
IOC extraction
Symbol processing
API analysis
Report generation
```

Python is commonly used to extend reverse-engineering workflows.

---

# Tool Categories

| Category | Examples |
|---|---|
| Disassembler | Ghidra, IDA, Binary Ninja |
| Debugger | x64dbg, WinDbg, GDB, LLDB |
| Binary inspection | objdump, readelf, rabin2 |
| Decompiler | Ghidra, IDA, Hex-Rays |
| Memory analysis | Volatility |
| Binary diffing | Diaphora, BinDiff |
| Scripting | Python |
| Static analysis | Ghidra, angr |
| Firmware analysis | binwalk |
| Fuzzing | AFL++, libFuzzer |

Tool capabilities and support vary by architecture and file type.

---

# Ethical and Legal Considerations

Reverse engineering must respect:

- Authorization
- Licensing
- Intellectual property
- Privacy
- Responsible disclosure
- Organizational policy
- Applicable law

Security research should be performed only on software and systems you are authorized to analyze.

---

# Repository Structure

```text
Reverse-Engineering/
│
├── README.md
│
├── 01-Reverse-Engineering-Fundamentals.md
├── 02-Computer-Architecture-and-Assembly.md
├── 03-Executable-Formats-PE-ELF-and-Binary-Internals.md
├── 04-Static-Code-Analysis-and-Disassembly.md
├── 05-Decompilation-Functions-and-Control-Flow.md
├── 06-Debugging-Dynamic-Reverse-Engineering.md
├── 07-Obfuscation-Packing-and-Anti-Reverse-Engineering.md
├── 08-Software-Vulnerability-Research-and-Exploit-Reversing.md
├── 09-Reverse-Engineering-Automation-and-Tooling.md
└── 10-Advanced-Reverse-Engineering-Case-Studies.md
```

---

# Chapter Roadmap

## 01 — Reverse Engineering Fundamentals

Covers:

- Reverse-engineering methodology
- Analysis workflows
- Evidence handling
- Tool selection
- Static vs dynamic analysis
- Analyst mindset
- Documentation

---

## 02 — Computer Architecture and Assembly

Covers:

- CPU architecture
- Registers
- Memory
- Stack
- Heap
- Instructions
- Calling conventions
- x86/x64
- ARM64
- System calls

---

## 03 — Executable Formats: PE, ELF and Binary Internals

Covers:

- PE
- ELF
- Headers
- Sections
- Segments
- Imports
- Exports
- Relocations
- Linking
- Loading
- Symbols
- Resources

---

## 04 — Static Code Analysis and Disassembly

Covers:

- Disassembly
- Strings
- Imports
- Cross-references
- API analysis
- Data-flow analysis
- Static heuristics
- Binary inspection

---

## 05 — Decompilation, Functions and Control Flow

Covers:

- Decompilers
- Function identification
- CFGs
- Call graphs
- Variables
- Structures
- Types
- Algorithms
- Program reconstruction

---

## 06 — Debugging and Dynamic Reverse Engineering

Covers:

- Debuggers
- Breakpoints
- Watchpoints
- Registers
- Stack
- Memory
- Threads
- API tracing
- Runtime validation

---

## 07 — Obfuscation, Packing and Anti-Reverse-Engineering

Covers:

- Packers
- Encryption
- String obfuscation
- Control-flow obfuscation
- API hashing
- Anti-debugging
- Anti-VM
- Anti-analysis
- Unpacking methodology

---

## 08 — Software Vulnerability Research and Exploit Reversing

Covers:

- Crash analysis
- Memory corruption
- Stack vulnerabilities
- Heap vulnerabilities
- Integer issues
- Use-after-free
- Patch diffing
- Root cause
- Exploitability
- Mitigations

---

## 09 — Reverse Engineering Automation and Tooling

Covers:

- Python
- Ghidra scripting
- IDA scripting concepts
- Binary parsing
- Automation
- Binary diffing
- Function similarity
- Plugin development
- Large-scale analysis

---

## 10 — Advanced Reverse Engineering Case Studies

Covers:

- Complete binary investigations
- Malware reversing
- Vulnerability analysis
- Patch analysis
- Complex obfuscation
- Firmware/binary investigations
- Detection engineering
- Reporting
- Professional case studies

---

# Skills Matrix

| Skill | Beginner | Intermediate | Advanced |
|---|---:|---:|---:|
| Binary formats | ✓ | ✓ | ✓ |
| Assembly | ✓ | ✓ | ✓ |
| Ghidra | ✓ | ✓ | ✓ |
| Disassembly | ✓ | ✓ | ✓ |
| Debugging | | ✓ | ✓ |
| Decompilation | | ✓ | ✓ |
| Control-flow analysis | | ✓ | ✓ |
| Obfuscation | | ✓ | ✓ |
| Binary diffing | | ✓ | ✓ |
| Vulnerability research | | ✓ | ✓ |
| Exploit analysis | | | ✓ |
| Automation | | ✓ | ✓ |
| Firmware reversing | | | ✓ |
| Advanced malware reversing | | | ✓ |

---

# Learning Path

A recommended progression is:

```text
Computer Architecture
        │
        ▼
Assembly
        │
        ▼
Executable Formats
        │
        ▼
Static Analysis
        │
        ▼
Decompilation
        │
        ▼
Debugging
        │
        ▼
Obfuscation
        │
        ▼
Vulnerability Research
        │
        ▼
Automation
        │
        ▼
Advanced Research
```

Do not attempt advanced vulnerability research without understanding:

```text
Registers
Memory
Stack
Calling conventions
Assembly
Executable formats
```

---

# Practical Lab Progression

## Level 1 — Beginner

Analyze a simple compiled program.

Identify:

```text
Entry point
Functions
Strings
Imports
```

---

## Level 2 — Intermediate

Analyze a stripped binary.

Identify:

```text
Functions
Control flow
Data structures
API usage
```

---

## Level 3 — Advanced

Analyze an obfuscated binary.

Identify:

```text
Unpacking
Runtime configuration
Anti-analysis
Core functionality
```

---

## Level 4 — Security Research

Analyze a vulnerable application.

Identify:

```text
Crash
Root cause
Affected function
Memory corruption
Security impact
```

---

## Level 5 — Professional

Complete an end-to-end investigation:

```text
Binary
 ↓
Architecture
 ↓
Static Analysis
 ↓
Dynamic Analysis
 ↓
Reverse Engineering
 ↓
Security Assessment
 ↓
Detection / Mitigation
 ↓
Professional Report
```

---

# Reverse Engineering and Other Knowledge Areas

This section integrates directly with the rest of the knowledge base.

### Malware Analysis

```text
Malware Analysis
       ↓
Reverse Engineering
       ↓
Code-Level Understanding
```

### Digital Forensics

```text
Forensic Artifact
       ↓
Binary Analysis
       ↓
Runtime Behavior
```

### Vulnerability Research

```text
Binary
 ↓
Reverse Engineering
 ↓
Bug
 ↓
Root Cause
 ↓
Security Impact
```

### Detection Engineering

```text
Reverse Engineering
       ↓
Behavior
       ↓
TTP
       ↓
Detection
```

### Incident Response

```text
Malware
 ↓
Reverse Engineering
 ↓
Capabilities
 ↓
Scope
 ↓
Containment
```

---

# Enterprise Reverse Engineering Workflow

```text
                 Security Event
                       │
                       ▼
                 Binary Intake
                       │
                       ▼
                 Evidence Store
                       │
                       ▼
                 Static Triage
                       │
              ┌────────┴────────┐
              ▼                 ▼
          Disassembly       Metadata
              │                 │
              └────────┬────────┘
                       ▼
                  Decompilation
                       │
                       ▼
                 Dynamic Analysis
                       │
                       ▼
                   Debugging
                       │
                       ▼
              Security Assessment
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
       Malware      Vulnerability  Detection
       Analysis       Research     Engineering
          │            │            │
          └────────────┼────────────┘
                       ▼
                     Report
```

---

# Professional Documentation Standard

Every significant reverse-engineering investigation should record:

```text
Case ID
Sample / Binary
SHA-256
Architecture
Operating System
Tool versions
Analysis environment
Entry point
Important functions
Relevant addresses
Observed behavior
Inferred behavior
Security findings
Confidence
Limitations
References
```

---

# Analyst Evidence Model

Use:

```text
Observed
Inferred
Hypothesized
Unknown
```

For example:

```text
Observed:
Function calls WinHttpConnect.

Inferred:
The function likely establishes HTTP/S communication.

Confirmed:
Runtime execution shows a connection to the observed destination.

Unknown:
Whether the destination is attacker-controlled without additional evidence.
```

---

# Tool-Assisted Analysis Principles

Tools such as Ghidra, IDA, x64dbg and GDB are extremely powerful.

However:

> **A tool output is an analytical aid, not a conclusion.**

Always understand:

```text
What the tool identified
Why it identified it
What assumptions it made
What evidence supports the interpretation
```

---

# Reverse Engineering Safety

When working with unknown or malicious binaries:

- Use isolated environments.
- Do not use production credentials.
- Do not execute malware on personal systems.
- Control network connectivity.
- Prefer simulated network services.
- Preserve snapshots.
- Keep evidence separate from working files.
- Patch analysis systems.
- Restrict host integration features.
- Never assume virtualization provides absolute isolation.

---

# Recommended References

- [Ghidra](https://ghidra-sre.org/)
- [Ghidra Documentation](https://ghidra.re/)
- [MITRE ATT&CK](https://attack.mitre.org/)
- [Microsoft PE Format](https://learn.microsoft.com/windows/win32/debug/pe-format)
- [System V ABI](https://refspecs.linuxfoundation.org/)
- [ELF Specification](https://refspecs.linuxfoundation.org/elf/)
- [Intel Software Developer Manuals](https://www.intel.com/content/www/us/en/developer/articles/technical/intel-sdm.html)
- [AMD64 Architecture Programmer's Manual](https://www.amd.com/en/support/tech-docs)
- [ARM Architecture](https://developer.arm.com/documentation/)
- [x64dbg](https://x64dbg.com/)
- [GDB](https://sourceware.org/gdb/)
- [LLVM](https://llvm.org/)
- [BinDiff](https://github.com/google/bindiff)
- [Diaphora](https://github.com/FelixBer/Diaphora)
- [angr](https://angr.io/)
- [AFL++](https://aflplus.plus/)
- [libFuzzer](https://llvm.org/docs/LibFuzzer.html)
- [NIST Cybersecurity Publications](https://csrc.nist.gov/publications)

---

# Completion Criteria

This section should ultimately enable the learner to:

- [ ] Explain CPU architecture fundamentals
- [ ] Read basic x86/x64 assembly
- [ ] Understand registers and memory
- [ ] Understand stack and heap behavior
- [ ] Explain calling conventions
- [ ] Parse PE and ELF structures
- [ ] Identify executable sections
- [ ] Analyze imports and exports
- [ ] Perform static binary analysis
- [ ] Navigate Ghidra or an equivalent tool
- [ ] Understand disassembly
- [ ] Use decompilation effectively
- [ ] Build control-flow understanding
- [ ] Trace function relationships
- [ ] Debug binaries
- [ ] Inspect registers and memory
- [ ] Analyze runtime behavior
- [ ] Understand common obfuscation
- [ ] Analyze packing
- [ ] Identify anti-debugging techniques
- [ ] Perform basic vulnerability research
- [ ] Understand patch diffing
- [ ] Automate repetitive analysis
- [ ] Produce professional reverse-engineering reports
- [ ] Translate technical findings into security recommendations

---

# Final Objective

The ultimate goal of this knowledge area is to develop the ability to move confidently between:

```text
High-Level Behavior
        ↕
Program Logic
        ↕
Functions
        ↕
Control Flow
        ↕
Assembly
        ↕
Machine Code
        ↕
CPU Architecture
```

and then connect that understanding to:

```text
Security
   │
   ├── Malware Analysis
   ├── Vulnerability Research
   ├── Incident Response
   ├── Detection Engineering
   ├── Threat Intelligence
   └── Product Security
```

A strong reverse engineer does not simply recognize assembly instructions.

They can take an unknown binary, systematically reduce uncertainty, reconstruct its important logic, validate their conclusions, identify security implications, and communicate the findings clearly.

The final progression is:

```text
Unknown Binary
      ↓
Understand Format
      ↓
Understand Architecture
      ↓
Disassemble
      ↓
Reconstruct Functions
      ↓
Understand Control Flow
      ↓
Understand Data Flow
      ↓
Validate Dynamically
      ↓
Understand Behavior
      ↓
Identify Security Implications
      ↓
Produce Evidence-Based Findings
```

That is the foundation of professional reverse engineering.
