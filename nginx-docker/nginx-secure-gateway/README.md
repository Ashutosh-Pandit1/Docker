# Nginx Secure API Gateway & Rate Limiter

A production-hardened Nginx Gateway implementation focused on web security, traffic shaping, and custom exception handling.

## 🚀 Features
- **IP-Based Rate Limiting:** Mitigates DDoS and brute-force attacks by restricting clients to 2 requests per second using memory tracking zones.
- **Attack Surface Reduction:** Strict location blocks that deny access to exposed environment configuration files (`.env`, `.git`).
- **Custom Graceful Degradation:** Custom styled HTML error handlers for `429 Too Many Requests` and `403 Forbidden` statuses.

## 🛠️ How to Run

1. Navigate to the gateway directory:
   ```bash
   cd nginx-docker/nginx-secure-gateway

2. Build the Docker image:

docker build -t nginx-secure-gateway .

3. Run the container:

docker run -d -p 82:82 --name security-gateway nginx-secure-gateway

4. Verification: - Access the API at http://localhost:82/api/

-> Spam refresh to trigger the 429 rate limit page.

-> Navigate to http://localhost:82/.env to trigger the 403 block.
