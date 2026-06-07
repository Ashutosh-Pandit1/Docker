# Nginx Static Content Server & Browser Caching

An enterprise-grade Nginx configuration optimized for serving high-performance static web assets with aggressive client-side caching policies.

## 🚀 Features
- **Kernel-Level Streaming:** Leverages `sendfile` to stream files directly from disk storage bypassing user-space overhead.
- **Cache-Control Headers:** Configured to push a 7-day expiration policy onto client browsers for image and style assets.
- **Custom Header Injection:** Appends an `X-Cache-Status` response header verifying that Nginx handled the asset optimization directly.

## 🛠️ How to Run
1. Build the image: `docker build -t nginx-static-cache .`
2. Run on port 83: `docker run -d -p 83:83 --name cache-demo nginx-static-cache`
3. Open `http://localhost:83` in your browser. Open Developer Tools (F12) -> Network Tab, click on `style.css`, and view the response headers to see the caching parameters active!
