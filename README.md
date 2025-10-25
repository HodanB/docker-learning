# 🐳 Docker Learning Journey

This repository documents my Docker learning path — from building and managing single-container apps to handling multi-container environments using Redis, MySQL, and Nginx.

---

## 🧠 Topics Covered
- Building Docker images and containers  
- Using Docker Compose for multi-container setups  
- Pushing and pulling images from AWS ECR  
- Docker networking, volumes, and environment variables  
- Container orchestration (Kubernetes introduction)

---

## 💡 Projects

### 1️⃣ Hello Flask — Flask + MySQL
A simple Flask web app connected to a MySQL database using Docker Compose.

**Key Concepts:**
- Multi-container setup (Flask app + MySQL)
- Persistent MySQL data using Docker volumes
- Multi-stage Docker builds for smaller images

**Run it:**
cd Hello_Flask
sudo docker compose up -d --build 
Visit: http://localhost:5002

---

### 2️⃣ Hello Flask — Flask + MySQL
A Flask + Redis counter app with Nginx load balancing and persistent Redis data.

**Key Concepts:**
- Using Redis for in-memory data store
- Environment variables for flexible configuration
- Docker volumes for persistence
- Nginx reverse proxy and load balancing
- Scaling Flask services with Compose

**Run it:**
cd Flask_Challenge
sudo docker compose up -d --build
Visit: http://localhost:5000
Visit: http://localhost:5000/count

---

## 📦 AWS ECR Integration
Built and pushed custom Docker images to Amazon ECR.
Pulled images to run containers in local and remote environments.

---

👩‍💻 Author
Hodan B.