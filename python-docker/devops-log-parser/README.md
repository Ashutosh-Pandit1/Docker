# DevOps Automated Nginx Log Parser

A containerized, memory-efficient Python log analytics engine designed to process high-volume server log arrays without exhausting local compute resources.

## 🚀 Architectural Capabilities
- **Lazy Evaluation Memory Pipeline:** Uses Python Generators (`yield`) to stream text files line-by-line, maintaining a flat $O(1)$ memory consumption footprint even when auditing multi-gigabyte log vectors.
- **Regex Security Triage:** Implements advanced token pattern processing to track HTTP Status Distribution and pull out malicious clients triggering security violations (`403 Forbidden` / `429 Too Many Requests`).

## 🛠️ Execution Blueprint
1. Build the engine configuration image:
   ```bash
   docker build -t devops-log-parser.

2. Execute the isolated evaluation context layer:

   docker run --rm --name log-auditor devops-log-parser
