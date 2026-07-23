# 18 - Wireless Networks

# Part 1 — Wireless Fundamentals, IEEE 802.11 Standards, Wi-Fi Architecture, Access Points, Wireless LAN Controllers, Frequency Bands, Channels, and Enterprise Wireless Design

---

# Overview

Wireless networking has become the primary method for connecting users, mobile devices, Internet of Things (IoT) devices, and enterprise systems. Unlike traditional wired Ethernet networks that rely on physical cables, wireless networks use **radio frequency (RF)** signals to transmit data through the air.

Modern enterprise Wi-Fi supports:

- Corporate offices
- Universities
- Hospitals
- Manufacturing facilities
- Retail environments
- Airports
- Hotels
- Smart buildings
- Warehouses
- Cloud-connected IoT deployments

Because wireless traffic travels through an open medium, organizations must carefully design, secure, monitor, and manage their wireless infrastructure.

---

# Learning Objectives

After completing this chapter, you will understand:

- Wireless networking fundamentals
- Radio frequency (RF) concepts
- IEEE 802.11 standards
- Wi-Fi architecture
- Access Points (APs)
- Wireless LAN Controllers (WLCs)
- Frequency bands
- Wireless channels
- SSIDs
- Basic Service Set (BSS)
- Extended Service Set (ESS)
- Wireless roaming
- Enterprise wireless architecture
- Business use cases

---

# What is a Wireless Network?

A **Wireless Network (Wi-Fi)** allows devices to communicate without physical Ethernet cables by transmitting data using radio waves.

```
Laptop

     ))))

        ))))

      Access Point

          │

       Ethernet

          │

      Core Network
```

Wireless networking combines the flexibility of mobility with the performance of modern IP networks.

---

# Why Wireless Networks Matter

Wireless technology enables organizations to:

- Improve employee mobility
- Reduce cabling costs
- Support Bring Your Own Device (BYOD)
- Enable remote collaboration
- Connect IoT devices
- Increase workplace flexibility
- Accelerate digital transformation

---

# Characteristics of Wireless Networks

Wireless communication differs from wired networking because it uses a **shared radio medium**.

Important characteristics include:

- Radio-based communication
- Shared bandwidth
- Variable signal strength
- Susceptibility to interference
- Mobility support
- Dynamic association
- Roaming capabilities

---

# Wired vs Wireless Networks

| Feature | Wired Network | Wireless Network |
|----------|---------------|------------------|
| Medium | Copper/Fiber | Radio Frequency |
| Mobility | Limited | High |
| Installation Cost | Higher | Lower |
| Reliability | Very High | Environment Dependent |
| Interference | Minimal | Higher |
| Security | Physical + Logical | Primarily Logical |

---

# Radio Frequency (RF) Fundamentals

Wireless communication relies on electromagnetic waves.

Basic concepts include:

- Frequency
- Wavelength
- Amplitude
- Signal strength
- Noise
- Interference

Understanding RF behavior is essential for designing reliable wireless networks.

---

# Frequency

Frequency measures how many wave cycles occur every second.

Measured in:

```
Hertz (Hz)

Kilohertz (kHz)

Megahertz (MHz)

Gigahertz (GHz)
```

Wi-Fi primarily operates in:

- 2.4 GHz
- 5 GHz
- 6 GHz (Wi-Fi 6E and later)

---

# Wavelength

Frequency and wavelength have an inverse relationship.

```
Higher Frequency

↓

Shorter Wavelength

↓

Higher Speed

↓

Lower Range
```

```
Lower Frequency

↓

Longer Wavelength

↓

Greater Range

↓

Lower Maximum Throughput
```

---

# Signal Strength

Signal strength is commonly measured in **dBm**.

Typical values:

| Signal | Approximate Strength |
|----------|----------------------|
| Excellent | -30 dBm |
| Very Good | -50 dBm |
| Good | -60 dBm |
| Fair | -70 dBm |
| Poor | -80 dBm |
| Unusable | Below -90 dBm |

Stronger signals generally provide higher throughput and more reliable communication.

---

# Signal-to-Noise Ratio (SNR)

Signal quality depends on both signal strength and background noise.

```
Signal

────────────

Noise

=

SNR
```

Higher SNR values result in:

- Better throughput
- Lower packet loss
- Improved stability

---

# Wireless Interference

Common interference sources include:

- Microwave ovens
- Bluetooth devices
- Cordless phones
- Neighboring Wi-Fi networks
- Wireless cameras
- Industrial equipment
- Thick concrete walls
- Metal structures

Proper channel planning minimizes interference.

---

# IEEE 802.11 Standards

The IEEE develops Wi-Fi standards under the **802.11** family.

Major standards include:

| Standard | Band | Maximum Theoretical Speed |
|-----------|------|---------------------------|
| 802.11a | 5 GHz | 54 Mbps |
| 802.11b | 2.4 GHz | 11 Mbps |
| 802.11g | 2.4 GHz | 54 Mbps |
| 802.11n (Wi-Fi 4) | 2.4 / 5 GHz | Up to 600 Mbps |
| 802.11ac (Wi-Fi 5) | 5 GHz | Multi-Gigabit |
| 802.11ax (Wi-Fi 6 / 6E) | 2.4 / 5 / 6 GHz | Higher efficiency and throughput |
| 802.11be (Wi-Fi 7) | 2.4 / 5 / 6 GHz | Extremely High Throughput (EHT) |

Actual throughput depends on channel width, client capabilities, interference, and deployment conditions.

---

# Wi-Fi Generations

To simplify naming, the Wi-Fi Alliance introduced generation-based branding.

| Wi-Fi Generation | IEEE Standard |
|------------------|---------------|
| Wi-Fi 4 | 802.11n |
| Wi-Fi 5 | 802.11ac |
| Wi-Fi 6 | 802.11ax |
| Wi-Fi 6E | 802.11ax (6 GHz support) |
| Wi-Fi 7 | 802.11be |

---

# Wi-Fi Architecture

A simplified enterprise wireless architecture:

```
Wireless Client

     ))))

Access Point

     │

Wireless LAN Controller

     │

Distribution Switch

     │

Core Network
```

Large organizations centralize wireless management through Wireless LAN Controllers (WLCs).

---

# Access Point (AP)

An **Access Point (AP)** bridges wireless clients to the wired Ethernet network.

Functions include:

- Wireless communication
- Beacon transmission
- Client association
- Authentication forwarding
- Traffic forwarding

Enterprise APs typically support dozens to hundreds of concurrent clients, depending on hardware and workload.

---

# Autonomous Access Points

Autonomous APs operate independently.

```
Client

↓

Access Point

↓

Switch

↓

Network
```

Advantages:

- Simple deployment
- Lower cost
- Suitable for small offices

Limitations:

- Individual configuration
- Limited scalability
- Manual management

---

# Controller-Based Access Points

Enterprise deployments commonly use controller-based APs.

```
Clients

↓

Multiple APs

↓

Wireless LAN Controller

↓

Network
```

Benefits include:

- Centralized management
- Centralized security policies
- Simplified firmware updates
- Faster troubleshooting
- Consistent configurations

---

# Wireless LAN Controller (WLC)

A Wireless LAN Controller manages multiple Access Points from a single platform.

Typical responsibilities:

- AP management
- RF optimization
- Client authentication
- Roaming support
- Security policy enforcement
- Firmware distribution
- Performance monitoring

---

# Access Point Discovery

Before joining a WLC, an AP must discover the controller.

Common discovery methods include:

- Static configuration
- DHCP options
- DNS
- Layer 2 discovery
- Layer 3 discovery

Once discovered, the AP establishes a secure management connection.

---

# Frequency Bands

Enterprise Wi-Fi primarily uses three frequency bands.

---

## 2.4 GHz

Advantages:

- Longer range
- Better wall penetration
- Broad compatibility

Disadvantages:

- Higher interference
- Fewer non-overlapping channels
- Lower overall capacity

---

## 5 GHz

Advantages:

- Higher throughput
- Less interference
- More available channels
- Better enterprise performance

Disadvantages:

- Reduced range compared to 2.4 GHz

---

## 6 GHz

Introduced with Wi-Fi 6E and expanded in Wi-Fi 7.

Advantages:

- Additional spectrum
- Reduced congestion
- Higher throughput
- Lower latency

Requirements:

- Compatible infrastructure
- Compatible client devices

---

# Frequency Comparison

| Feature | 2.4 GHz | 5 GHz | 6 GHz |
|----------|----------|--------|--------|
| Coverage | High | Medium | Lower |
| Throughput | Moderate | High | Very High |
| Interference | High | Lower | Lowest |
| Available Channels | Few | Many | More than previous generations (region dependent) |

---

# Wireless Channels

Each frequency band is divided into channels.

```
2.4 GHz

Channel 1

Channel 6

Channel 11
```

These channels are commonly used because they do not overlap in many regulatory domains.

---

# Channel Width

Common channel widths include:

- 20 MHz
- 40 MHz
- 80 MHz
- 160 MHz
- 320 MHz (Wi-Fi 7)

Larger channel widths provide greater throughput but increase susceptibility to interference and spectrum consumption.

---

# Channel Planning

Poor channel planning causes:

- Co-channel interference
- Adjacent-channel interference
- Reduced throughput
- Increased latency

Enterprise wireless deployments perform RF site surveys to optimize channel assignments.

---

# Service Set Identifier (SSID)

The **SSID** is the logical name of a wireless network.

Example:

```
Corporate-WiFi
```

Organizations often deploy multiple SSIDs for:

- Employees
- Guests
- IoT devices
- Voice devices

Each SSID can map to a different VLAN and security policy.

---

# Basic Service Set (BSS)

A Basic Service Set consists of:

```
Clients

↓

Single Access Point
```

Each BSS is identified by a unique **BSSID**, typically derived from the AP's MAC address.

---

# Extended Service Set (ESS)

An Extended Service Set connects multiple APs that share the same SSID.

```
AP1

↓

AP2

↓

AP3

↓

Same SSID
```

An ESS allows users to move throughout a building while maintaining network connectivity.

---

# Wireless Roaming

Roaming enables a client device to transition between Access Points without requiring the user to reconnect manually.

```
AP1

↓

Client Moves

↓

AP2

↓

Session Continues
```

Fast roaming technologies help minimize disruptions to voice and video applications.

---

# Enterprise Wireless Design

A typical enterprise deployment:

```
Internet

↓

Firewall

↓

Core Switch

↓

Wireless LAN Controller Cluster

↓

Access Switches

↓

Multiple Access Points

↓

Wireless Clients
```

Redundant controllers and properly planned AP placement improve availability and scalability.

---

# Business Impact

Well-designed wireless networks enable organizations to:

- Increase employee productivity
- Support hybrid workspaces
- Improve customer experience
- Enable mobility
- Simplify device connectivity
- Support modern collaboration tools

---

# Enterprise Best Practices

Organizations should:

- Conduct RF site surveys before deployment.
- Use controller-based APs for large environments.
- Minimize channel overlap.
- Prefer the 5 GHz and 6 GHz bands where appropriate.
- Limit the number of SSIDs to reduce management overhead.
- Plan for redundancy and controller high availability.
- Monitor wireless performance continuously.

---

# Key Takeaways

- Wireless networks use radio frequency instead of physical cables.
- IEEE 802.11 defines Wi-Fi standards.
- Access Points connect wireless devices to wired networks.
- Wireless LAN Controllers simplify enterprise management.
- 2.4 GHz, 5 GHz, and 6 GHz each have different characteristics.
- Proper channel planning is essential for performance.
- ESS and roaming enable seamless enterprise mobility.

---


