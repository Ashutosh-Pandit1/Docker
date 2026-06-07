# Nginx Path-Based Microservice Router

An API routing gateway configuration mapping incoming uniform resource identifiers (URIs) to decoupled backend internal service layers.

## 🚀 Features
- **Context Path Routing:** Evaluates structural request subpaths (`/search`, `/payment`) to dynamically determine destinations.
- **Decoupled Architecture Mocking:** Simulates internal backend processing zones isolated from public visibility.
- **Edge Header Mutation:** Automatically enforces clean JSON data streaming boundaries directly at the edge layer.

## 🛠️ How to Run
1. Build the image: `docker build -t nginx-path-router .`
2. Run on port 84: `docker run -d -p 84:84 --name router-demo nginx-path-router`
3. **Verification:**
   - Go to `http://localhost:84/` for the main gateway statement.
   - Go to `http://localhost:84/search` to hit the search microservice.
   - Go to `http://localhost:84/payment` to hit the secure payment endpoint.
