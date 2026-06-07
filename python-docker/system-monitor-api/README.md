# Python System Monitor REST API

A production-ready infrastructure automation utility built with Python and FastAPI that programmatically extracts and exposes lower-level host system performance metrics as structured JSON telemetry data.

## 🚀 Architectural Use Case
In enterprise environments, monitoring daemons (such as Datadog agents or Prometheus Node Exporters) must query physical or virtual machines for resource footprints. This microservice demonstrates how to abstract OS-level kernel metrics and wrap them in low-latency, highly accessible REST API endpoints.

## ⚙️ Core Technical Capabilities
- **FastAPI Core Engine:** Implements high-performance, asynchronous endpoints that process queries with minimal framework overhead.
- **Dynamic Telemetry Extractor:** Leverages the native `psutil` system utilities library to sample active CPU clock loads and hardware memory mapping boundaries.
- **Containerized Architecture:** Fully containerized via an optimized Docker footprint, ensuring seamless deployment reproducibility across AWS EC2 instances or container environments without local interpreter dependencies.

---

## 📂 Repository Layout
```text
1-system-monitor-api/
├── app/
│   ├── __init__.py      # Package initialization hook
│   └── main.py          # Framework application logic & routing definitions
├── requirements.txt     # Python production package manifest
├── Dockerfile           # Optimized single-layer container build blueprint
└── README.md            # System configuration documentation
