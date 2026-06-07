import re
import sys
import os

# Regular Expression pattern to isolate Client IP, URL Path, and HTTP Status Codes
LOG_REGEX = r'(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*?"\w+ (?P<path>.*?) HTTP/.*?" (?P<status>\d{3})'

def stream_log_file(file_path):
    """
    High-Performance Memory Generator.
    Bypasses reading whole gigabyte log arrays into application memory,
    lazily streaming lines one-by-one from disk storage.
    """
    with open(file_path, "r") as file:
        for line in file:
            yield line

def analyze_infrastructure_logs(log_path):
    print(f"=== Initializing Production Log Audit Engine ===")
    print(f"Targeting: {log_path}\n")
    
    if not os.path.exists(log_path):
        print(f"❌ Critical Error: Target log vector layout '{log_path}' not found.")
        sys.exit(1)

    threat_ips = set()
    status_counts = {}
    total_lines = 0

    # Execute the streaming loop over our line generator
    for raw_line in stream_log_file(log_path):
        total_lines += 1
        match = re.search(LOG_REGEX, raw_line)
        
        if match:
            ip = match.group("ip")
            status = match.group("status")
            
            # Count the frequency of each HTTP Status Code
            status_counts[status] = status_counts.get(status, 0) + 1
            
            # Isolate malicious traffic variants targeting secure assets
            if status in ["403", "429"]:
                threat_ips.add(ip)

    # Output report metadata compilation
    print("[📊 INFRASTRUCTURE ANALYSIS METRICS SUMMARY]")
    print(f" -> Total Log Lines Audited: {total_lines}")
    
    print("\n[🔹 HTTP HTTP STATUS DISTRIBUTION MATRIX]")
    for status, count in status_counts.items():
        print(f"    HTTP Status {status}: {count} requests")
        
    print("\n[🚨 IDENTIFIED THREATS & SUSPICIOUS ACTORS]")
    if threat_ips:
        for ip in threat_ips:
            print(f"    ⚠️ Blocked Host Source Entity: {ip}")
    else:
        print("    ✅ No security threshold violations isolated.")

if __name__ == "__main__":
    # Pull the log filename from environment variables or default to standard fallback
    target_log = os.environ.get("TARGET_LOG_FILE", "dummy_access.log")
    analyze_infrastructure_logs(target_log)
