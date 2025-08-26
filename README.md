# Event Management System – Django REST API with Docker & AWS

## 📌 Overview
This project is a **cloud-native event management system** built with **Django REST Framework** and containerized with **Docker**.  
It was designed to demonstrate a microservices-based architecture, and deployed on **AWS ECS (Fargate)** with **Amazon RDS (PostgreSQL)**.  

The system provides REST APIs to create, list, and retrieve events, with a PostgreSQL backend.

---

## 🚀 Features
- `GET /api/events/` → Retrieve list of all events  
- `GET /api/events/{id}` → Get details of a specific event  
- `POST /api/events/` → Create a new event  
- Django Admin interface for event management  
- Dockerized service with PostgreSQL support  
- Deployment-ready for AWS (ECR, ECS, RDS)

---

## 🛠️ Tech Stack
- **Backend:** Django REST Framework (Python 3.10)  
- **Database:** PostgreSQL (local & AWS RDS)  
- **Containerization:** Docker  
- **Cloud Services:** AWS ECR, ECS (Fargate), RDS  

---

## 📂 Project Structure
```
event-management-system/
│── eventapp/         # Django application
│── Dockerfile        # Docker build config
│── requirements.txt  # Dependencies
│── manage.py
│── .env.example      # Environment variables template
```

---

## ⚙️ Setup & Run Locally
```bash
# Clone repository
git clone https://github.com/santiagoteor/event-management-system.git
cd event-management-system

# Create virtual environment & install dependencies
python -m venv venv
source venv/bin/activate   # on Windows: venv\Scripts\activate
pip install -r requirements.txt

# Run migrations & start server
python manage.py migrate
python manage.py runserver
```

Access API at: [http://localhost:8000/api/events/](http://localhost:8000/api/events/)

---

## 🐳 Run with Docker
```bash
docker build -t event-service .
docker run -p 8000:8000 --env-file .env event-service
```

---

## ☁️ AWS Deployment (Summary)
1. Build and tag Docker image  
   ```bash
   docker build -t event-service .
   docker tag event-service:latest <ECR_REPO_URI>:latest
   ```
2. Push to AWS ECR  
   ```bash
   docker push <ECR_REPO_URI>:latest
   ```
3. Configure AWS RDS PostgreSQL instance.  
4. Create ECS cluster and Fargate task definition linked to ECR image.  
5. Deploy and access via ECS Service URL / Load Balancer.

---

## 📫 Author
**Santiago Tejada Orozco**  
- [LinkedIn](https://www.linkedin.com/in/santiago-tejada-orozco)  
- santiago.tejada.orozco@gmail.com
