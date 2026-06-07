import socket
import ssl
import datetime
import os
import sys

def check_ssl_expiry(domain_name, target_port=443):
    # Establish a default SSL context configuration to trust official Certificate Authorities
    context = ssl.create_default_context()
    
    try:
        print(f"📡 Querying network interface for: {domain_name}:{target_port}")
        
        # Open a standard TCP socket connection with a strict 5-second timeout
        with socket.create_connection((domain_name, target_port), timeout=5) as sock:
            # Wrap the raw TCP socket inside an encrypted SSL/TLS handshake
            with context.wrap_socket(sock, server_hostname=domain_name) as ssock:
                # Fetch the peer certificate payload as a structured Python dictionary
                cert_data = ssock.getpeercert()
                
                # Extract the expiration date string (e.g., 'Jun 07 23:59:59 2027 GMT')
                expiry_str = cert_data['notAfter']
                
                # Parse the time string format into a native Python datetime object
                expiry_date = datetime.datetime.strptime(expiry_str, r'%b %d %H:%M:%S %Y %Z')
                
                # Compute the difference against the current UTC timestamp
                time_remaining = expiry_date - datetime.datetime.utcnow()
                days_left = time_remaining.days
                
                print(f"   📅 Expiration Deadline: {expiry_date.strftime('%Y-%m-%d')}")
                print(f"   ⏳ Time Remaining: {days_left} Days")
                
                # Flag a warning state if the certificate expires within an actionable two-week window
                if days_left < 14:
                    print("   🚨 CRITICAL WARNING: Immediate renewal required to prevent service disruption!")
                else:
                    print("   ✅ Certificate health check passed successfully.")
                print("-" * 50)
                
    except Exception as network_error:
        print(f"❌ Network Security Audit Failed for {domain_name}: {network_error}")
        print("-" * 50)

if __name__ == "__main__":
    # Fetch a comma-separated list of domains from environment variables, or use default fallbacks
    domain_env = os.environ.get("MONITOR_DOMAINS", "google.com,github.com,aws.amazon.com")
    target_domains = domain_env.split(",")
    
    print(f"=== Starting Network TLS Infrastructure Audit Engine ===\n")
    for domain in target_domains:
        clean_domain = domain.strip()
        if clean_domain:
            check_ssl_expiry(clean_domain)
