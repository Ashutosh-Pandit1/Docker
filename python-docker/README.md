# Python Automation Engines & Systems Utilities Core

A collection of production-grade Python workloads demonstrating object-oriented development, performance-tuned system utilities, asynchronous API layers, and memory-safe stream processing patterns.

Every application is engineered using minimal single-stage deployment boundaries (`python:3.12-slim`), isolating runtime dependencies and eliminating local host environmental drift.

---

## 🗺️ Python Architectural Portfolio Index

| Project Folder | Core DevOps Use Case | Primary Engineering Competency | Base Strategy |
| :--- | :--- | :--- | :--- |
| [🔗 system-monitor-api](./system-monitor-api) | Live Host Telemetry Extraction | Asynchronous API Design & Low-level Host Queries | FastAPI / `psutil` Core |
| [🔗 devops-log-parser](./devops-log-parser) | Security Audit File Analysis | $O(1)$ Memory Consumption Streaming Pipelines | Python Lazy Generators |
| [🔗 ssl-expiry-checker](./ssl-expiry-checker) | Network Triage & Outage Prevention | Low-level Encrypted Socket Hands-shaking Lifecycle | Native `socket` / `ssl` Context |
| [🔗 db-migration-worker](./db-migration-worker) | Database Operations Automation | Transaction Commits & Database State Integrity Controls | SQLite Parameterized Engines |

---

## ⚙️ Core Engineering Design Patterns Demonstrated

### 1. Defensive Single-Stage Compilation Hardening
To support compiled dependencies like `psutil` without shifting away from single-stage configurations, the environment securely isolates necessary build headers via targeted package management loops:
```dockerfile
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc python3-dev && \
    rm -rf /var/lib/apt/lists/*
