# Nginx Reverse Proxy & Layer 7 Load Balancer

A production-ready Nginx configuration demonstrating Layer 7 routing, reverse proxying, and round-robin load balancing across decoupled backend services.

## 🚀 Features
- **Reverse Proxying:** Hides backend server details from clients to enhance security.
- **Round-Robin Load Balancing:** Automatically distributes incoming traffic equally across multiple backend instances.
- **Containerized Deployment:** Fully Dockerized architecture for quick deployment and zero environment drift.

## ⚙️ Architecture
When a user hits port `81`, Nginx captures the request and forwards it to one of the available mock upstream servers running internally on ports `8081` and `8082`.

## 🛠️ How to Run
Ensure you have Docker installed on your machine.

1. Clone the repository:
   
   git clone <your-repository-url>
   cd nginx-docker/nginx-reverse-proxy

2. Build the Docker image:

   docker build -t nginx-load-balancer .

3. Run the container:

   docker run -d -p 81:81 --name nginx-cluster nginx-load-balancer
   
4. Open http://localhost in your browser and refresh to see the load balancer alternate traffic between Backend 1 and Backend 2.
