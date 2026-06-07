from fastapi import FastAPI
import psutil
import platform
from datetime import datetime

app = FastAPI(title="System Monitor API Core", version="1.0.0")

@app.get("/")
def health_check():
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat()
    }

@app.get("/metrics")
def get_system_metrics():
    # Extract structural kernel hardware parameters
    cpu_util = psutil.cpu_percent(interval=1)
    vmem = psutil.virtual_memory()
    
    return {
        "operating_system": platform.system(),
        "kernel_release": platform.release(),
        "cpu": {
            "utilization_percentage": cpu_util,
            "logical_cores": psutil.cpu_count(logical=True)
        },
        "memory": {
            "total_gb": round(vmem.total / (1024 ** 3), 2),
            "used_gb": round(vmem.used / (1024 ** 3), 2),
            "available_gb": round(vmem.available / (1024 ** 3), 2),
            "utilization_percentage": vmem.percent
        }
    }
