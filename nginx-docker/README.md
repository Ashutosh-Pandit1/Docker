# Nginx Infrastructure Patterns & Traffic Management Core

A collection of production-grade Nginx architectures demonstrating advanced Layer 7 traffic routing, web security hardening, high-availability optimization, and edge routing logic. 

Every architectural module is fully decoupled, containerized utilizing Docker, and optimized for seamless deployment across cloud architectures (such as AWS EC2).

---

## 🗺️ Architectural Portfolio Index

| Project Folder | Core Use Case | Primary Production Benefit | Active Port |
| :--- | :--- | :--- | :--- |
| [🔗 nginx-reverse-proxy](./nginx-reverse-proxy) | Layer 7 Load Balancing | High Availability & Traffic Distribution | `81` |
| [🔗 nginx-secure-gateway](./nginx-secure-gateway) | Security Gateway | DDoS Mitigation & Access Controls (429/403) | `82` |
| [🔗 nginx-static-cache](./nginx-static-cache) | Content Acceleration | Kernel-level Streaming (`sendfile`) & 7d Browser Caching | `83` |
| [🔗 nginx-custom-routing](./nginx-custom-routing) | Microservice Router | Context Path-Based API Routing (`/search`, `/payment`) | `84` |

---

## 🛠️ Global Prerequisites & Infrastructure Engine

To spin up any standalone ecosystem block, ensure your runtime host environment has the Docker engine active:

```bash
# Verify your local daemon status
docker --version
