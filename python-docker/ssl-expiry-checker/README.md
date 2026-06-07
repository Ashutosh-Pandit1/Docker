# Network SSL/TLS Certificate Expiry Checker

An automated, containerized infrastructure utility written in Python that interrogates remote network socket interfaces to inspect and calculate TLS certificate lifecycles.

## 🚀 Architectural Capabilities
- **Low-Level Socket Interaction:** Establishes direct TCP connections (`socket`) and wraps them inside an encrypted handshake overlay (`ssl`) to query external networks efficiently.
- **Automated Infrastructure Triage:** Programmatically parses certificate payload expiration strings and implements conditional alert tracking for impending production out-of-compliance windows (<14 days).
- **Environment-Driven Flexibility:** Supports dynamic host monitoring targets at runtime using infrastructure environment parameters (`MONITOR_DOMAINS`).

## 🛠️ Execution Blueprint

1. Build the container image:
   ```bash
   docker build -t ssl-expiry-checker.

2. Run the default baseline audit context:

   docker run --rm --name ssl-auditor ssl-expiry-checker

3. Run an advanced scan targeting custom infrastructure domains:
   Pass a comma-separated list using the -e environment variable flag:

   docker run --rm -e MONITOR_DOMAINS="netflix.com,microsoft.com,3.110.30.81" --name custom-ssl-auditor ssl-expiry-checker
