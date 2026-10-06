# Chapter 20 – Real-World Case Studies

# Overview

Real-world case studies help bridge the gap between theory and practice by demonstrating how container technologies are used in production environments. They also highlight common architectural decisions, operational challenges, and security lessons learned.

This chapter presents realistic scenarios inspired by common industry patterns. The focus is on understanding engineering decisions, troubleshooting approaches, incident response, and best practices—not on exploiting systems.

These case studies are relevant for:

- DevOps Engineers
- DevSecOps Engineers
- Cloud Engineers
- Platform Engineers
- Security Engineers
- Site Reliability Engineers (SRE)
- SOC Analysts
- Software Engineers

---

# Learning Objectives

After completing this chapter, you should be able to:

- Analyze container architectures
- Identify operational risks
- Understand production deployments
- Improve troubleshooting skills
- Apply container security best practices
- Understand incident response workflows
- Make informed architectural decisions

---

# Case Study 1 – E-Commerce Platform Migration

## Background

A retail company migrated its monolithic web application to Docker.

Original architecture:

```
Web Server

↓

Application

↓

Database
```

New architecture:

```
Load Balancer

↓

Frontend Containers

↓

API Containers

↓

Database

↓

Redis
```

---

## Challenges

- Environment inconsistency
- Long deployment times
- Difficult scaling
- Configuration drift

---

## Solution

The organization implemented:

- Docker images
- Docker Compose for development
- CI/CD automation
- Versioned image releases
- Centralized logging
- Health checks

---

## Results

Benefits included:

- Faster deployments
- Consistent environments
- Improved scalability
- Easier rollback
- Simplified maintenance

---

## Lessons Learned

- Standardize image creation.
- Use immutable deployments.
- Automate builds and deployments.
- Monitor application health continuously.

---

# Case Study 2 – Image Size Optimization

## Problem

A production image exceeded **2 GB**.

Deployment became slow.

---

## Investigation

Analysis showed:

```
Ubuntu

+

Development Tools

+

Unused Packages

+

Temporary Files

↓

Large Image
```

---

## Improvements

The engineering team:

- Switched to a smaller base image where appropriate.
- Used multi-stage builds.
- Removed unnecessary packages.
- Deleted build artifacts.

---

## Results

```
2 GB

↓

320 MB
```

Benefits:

- Faster downloads
- Lower storage costs
- Smaller attack surface

---

## Lessons Learned

Optimize images before production deployment.

---

# Case Study 3 – Database Data Loss

## Problem

A database container was removed accidentally.

Application data disappeared.

---

## Root Cause

The database stored information only inside the container's writable layer.

```
Container

↓

Delete Container

↓

Data Lost
```

---

## Resolution

The database was reconfigured to use:

```
Docker Volume

↓

Persistent Storage
```

---

## Lessons Learned

Never store important application data exclusively in a container's writable layer.

Use persistent storage for databases and other stateful workloads.

---

# Case Study 4 – Misconfigured Secrets

## Problem

A developer embedded cloud credentials inside a Dockerfile.

```
Dockerfile

↓

API Key

↓

Container Image
```

The image was later shared internally.

---

## Response

The organization:

- Rotated the exposed credentials.
- Rebuilt the image.
- Removed secrets from source code.
- Implemented secure secret management.

---

## Lessons Learned

Never embed secrets in:

- Dockerfiles
- Images
- Source code
- Version control

---

# Case Study 5 – Production Outage

## Problem

Users reported intermittent failures.

---

## Investigation

Monitoring showed:

```
CPU

↓

95%

↓

Memory

↓

100%

↓

Container Restart
```

Logs identified a memory leak in the application.

---

## Resolution

Developers:

- Fixed the memory leak.
- Rebuilt the image.
- Redeployed the application.
- Added monitoring alerts.

---

## Lessons Learned

Monitoring should include:

- CPU
- Memory
- Restarts
- Error rates
- Response time

---

# Case Study 6 – Container Vulnerability

## Problem

Routine image scanning identified several Critical CVEs in a production image.

---

## Investigation

The vulnerabilities originated from an outdated base image.

---

## Response

```
Update Base Image

↓

Rebuild Image

↓

Security Scan

↓

Deploy
```

---

## Results

The updated image contained significantly fewer known vulnerabilities.

---

## Lessons Learned

- Keep base images updated.
- Scan images continuously.
- Rebuild images regularly.

---

# Case Study 7 – Unauthorized Container Deployment

## Problem

Operations discovered an unexpected container running in production.

---

## Investigation

Evidence reviewed:

- Registry activity
- Deployment logs
- Docker events
- Cloud audit logs

The investigation determined the deployment resulted from a misconfigured automation process rather than malicious activity.

---

## Resolution

The automation configuration was corrected and deployment approval controls were strengthened.

---

## Lessons Learned

- Review deployment automation regularly.
- Monitor deployment events.
- Maintain audit logs.
- Implement change management.

---

# Case Study 8 – Log Retention Issue

## Problem

A production incident occurred several weeks earlier.

During investigation:

```
Container Deleted

↓

Logs Deleted
```

Important historical evidence was unavailable.

---

## Resolution

The organization implemented centralized logging with defined retention policies.

---

## Lessons Learned

Logs should be:

- Centralized
- Searchable
- Protected
- Retained according to business and compliance requirements

---

# Case Study 9 – Registry Downtime

## Problem

The container registry became temporarily unavailable.

---

## Impact

Existing containers continued running.

However:

- New deployments were delayed.
- Autoscaling requiring new image pulls was affected.
- Recovery of new nodes became slower.

---

## Resolution

The organization implemented:

- Registry redundancy
- Image caching where appropriate
- Improved monitoring
- Disaster recovery procedures

---

## Lessons Learned

Treat the container registry as critical infrastructure.

---

# Case Study 10 – Production Readiness Review

## Scenario

Before deployment, the engineering team performed a production readiness assessment.

Checklist:

```
Image Scanned

↓

Version Tagged

↓

Secrets Secured

↓

Health Checks

↓

Monitoring

↓

Logging

↓

Resource Limits

↓

Backup Strategy

↓

Approved
```

---

## Outcome

Potential deployment issues were identified and corrected before production release.

---

## Lessons Learned

Production readiness reviews reduce operational risk and improve deployment quality.

---

# Common Themes Across Case Studies

```
Automation

↓

Security

↓

Monitoring

↓

Logging

↓

Testing

↓

Continuous Improvement
```

Successful organizations consistently apply these principles throughout the container lifecycle.

---

# Engineering Takeaways

## Design

- Build small images.
- Separate application responsibilities.
- Use immutable infrastructure.

---

## Security

- Scan images.
- Protect secrets.
- Apply least privilege.
- Use trusted base images.

---

## Operations

- Monitor continuously.
- Centralize logging.
- Define resource limits.
- Automate deployments.

---

## Reliability

- Use health checks.
- Implement backups.
- Validate production readiness.
- Document recovery procedures.

---

# Reflection Questions

1. Which case study most closely resembles a challenge you might encounter in production?
2. What preventive controls could have reduced the impact?
3. Which monitoring metrics would have detected the issue earlier?
4. How would immutable infrastructure improve recovery?
5. Which security controls should be added to your own container projects?

---

# Production Success Checklist

| Area | Recommendation |
|------|----------------|
| Images | Keep small and updated |
| Security | Scan continuously |
| Secrets | Never hardcode |
| Storage | Use persistent volumes |
| Monitoring | Enable metrics and alerts |
| Logging | Centralize logs |
| Networking | Expose only required ports |
| Deployment | Automate with CI/CD |
| Recovery | Test backup and restore |
| Operations | Continuously review and improve |

---

# Summary

Real-world container operations require much more than simply running Docker commands.

Successful organizations consistently combine:

```
Good Design

↓

Automation

↓

Security

↓

Monitoring

↓

Incident Response

↓

Continuous Improvement
```

These practices lead to resilient, scalable, and maintainable container platforms.

---

# Chapter 20 – Container Troubleshooting Playbook

# Overview

Even well-designed containerized applications experience issues in production. Effective troubleshooting requires a **structured, repeatable methodology** rather than guessing or making random configuration changes.

This playbook provides a systematic approach to diagnosing and resolving common Docker and container-related problems encountered in development and production environments.

It is intended for:

- DevOps Engineers
- DevSecOps Engineers
- Platform Engineers
- Cloud Engineers
- Site Reliability Engineers (SRE)
- Security Engineers
- Software Engineers

---

# Troubleshooting Philosophy

Avoid this approach:

```
Problem

↓

Guess

↓

Random Changes

↓

More Problems
```

Instead, follow a structured workflow:

```
Observe

↓

Collect Evidence

↓

Analyze

↓

Identify Root Cause

↓

Implement Fix

↓

Validate

↓

Document
```

The objective is to solve the **root cause**, not just the visible symptoms.

---

# Universal Troubleshooting Workflow

```
Problem Reported

↓

Verify Problem

↓

Collect Logs

↓

Inspect Container

↓

Review Configuration

↓

Analyze Metrics

↓

Identify Root Cause

↓

Apply Fix

↓

Verify Resolution

↓

Document Findings
```

---

# Scenario 1 – Container Will Not Start

## Symptoms

- Container exits immediately.
- Restart loop.
- Application unavailable.

---

## Investigation

Check all containers:

```bash
docker ps -a
```

View logs:

```bash
docker logs container_name
```

Inspect configuration:

```bash
docker inspect container_name
```

---

## Common Causes

- Incorrect command
- Missing dependencies
- Missing environment variables
- Configuration errors
- Permission problems
- Application crash

---

## Resolution

Fix the root cause.

Rebuild the image if necessary.

Deploy a new container.

---

# Scenario 2 – Container Continuously Restarts

## Investigation

```
Restart

↓

Logs

↓

Exit Code

↓

Health Check

↓

Resources

↓

Application
```

Useful commands:

```bash
docker logs

docker inspect

docker events

docker stats
```

---

## Possible Causes

- Memory exhaustion
- Failed health checks
- Application exceptions
- Database unavailable
- Invalid configuration

---

# Scenario 3 – Application Is Slow

## Investigation

Check:

```bash
docker stats
```

Review:

- CPU
- Memory
- Network
- Storage
- Application logs

---

## Possible Causes

- Resource limits
- High traffic
- Slow database
- Memory leak
- Inefficient queries

---

# Scenario 4 – Database Connection Failure

## Investigation Workflow

```
Application

↓

Database Running?

↓

Network

↓

DNS

↓

Credentials

↓

Firewall
```

Useful commands:

```bash
docker ps

docker network ls

docker network inspect
```

---

## Resolution

Verify:

- Database status
- Container networking
- Environment variables
- Connection string

---

# Scenario 5 – Container Cannot Access Internet

## Check

- Network configuration
- DNS
- Firewall
- Proxy configuration
- Host connectivity

Inspect:

```bash
docker inspect container_name
```

---

# Scenario 6 – Port Already in Use

Error:

```
Bind for 0.0.0.0:8080 failed
```

---

## Investigation

Determine which service is using the port.

On Linux:

```bash
ss -tulnp
```

or

```bash
netstat -tulnp
```

---

## Resolution

- Stop the conflicting service.
- Choose another host port.
- Reconfigure the application.

---

# Scenario 7 – Volume Data Missing

## Investigation

Inspect:

```bash
docker volume ls

docker volume inspect volume_name
```

Verify:

- Correct volume
- Mount point
- Container configuration

---

## Common Causes

- Wrong volume
- Container recreation
- Incorrect mount
- Data stored in writable layer

---

# Scenario 8 – High Disk Usage

Check:

```bash
docker system df
```

---

Remove unused resources:

```bash
docker system prune
```

Review before deleting resources in production.

---

# Scenario 9 – Container Networking Problems

Verify:

```bash
docker network ls

docker network inspect network_name
```

---

Common Issues

- Wrong network
- DNS problems
- Firewall rules
- Incorrect hostname

---

# Scenario 10 – Image Build Failure

Review:

```
Dockerfile

↓

Build Logs

↓

Dependencies

↓

COPY Paths
```

Build with detailed output:

```bash
docker build .
```

Read the reported errors carefully to identify the failing instruction.

---

# Common Docker Commands

## Containers

```bash
docker ps

docker ps -a

docker stop

docker start

docker restart

docker rm
```

---

## Images

```bash
docker images

docker build

docker pull

docker push

docker rmi
```

---

## Logs

```bash
docker logs

docker logs -f
```

---

## Monitoring

```bash
docker stats

docker top

docker events
```

---

## Inspection

```bash
docker inspect
```

---

## Networks

```bash
docker network ls

docker network inspect
```

---

## Volumes

```bash
docker volume ls

docker volume inspect
```

---

## Cleanup

```bash
docker system df

docker system prune
```

---

# Root Cause Analysis Checklist

When troubleshooting, ask:

- What changed recently?
- When did the issue begin?
- Is the issue reproducible?
- Which services are affected?
- Are logs available?
- Are metrics available?
- Were recent deployments made?
- Were configuration changes introduced?

Avoid assuming the first observed symptom is the root cause.

---

# Troubleshooting Decision Tree

```
Application Fails

↓

Container Running?

↓

No

↓

Check Logs

↓

Check Configuration

↓

Restart?

↓

Investigate Exit Code

↓

Fix

↓

Redeploy

↓

Validate
```

If the container is running:

```
Running

↓

Health Check

↓

Logs

↓

Resources

↓

Networking

↓

Dependencies

↓

Root Cause
```

---

# Best Practices

- Reproduce the issue in a safe environment when possible.
- Gather evidence before making changes.
- Review logs and metrics together.
- Investigate recent deployments.
- Make one change at a time.
- Validate every fix.
- Document findings and preventive actions.

---

# Troubleshooting Checklist

| Item | Verify |
|------|--------|
| Container Running | ✓ |
| Logs Reviewed | ✓ |
| Image Valid | ✓ |
| Environment Variables | ✓ |
| Network Connectivity | ✓ |
| Storage Mounted | ✓ |
| Resource Limits | ✓ |
| Health Checks | ✓ |
| Recent Changes | ✓ |
| Monitoring Data | ✓ |

---

# Key Takeaways

Successful troubleshooting follows this pattern:

```
Observe

↓

Measure

↓

Analyze

↓

Fix

↓

Validate

↓

Document
```

A structured process reduces downtime, avoids unnecessary changes, and improves long-term operational reliability.

---

