# 🔐 Login Microservice – Academic Tutoring Management System

This directory contains the **Login microservice**, part of the Authentication Domain of the **Academic Tutoring Management System**. This microservice is fully developed in **Python** and is responsible for authenticating users and granting secure access to the platform.

It follows a **layered architecture** and applies well-known **software design patterns** to ensure clean separation of concerns, scalability, and maintainability.

## 🏗 Architecture Overview

The Login microservice is structured using a **layered (MVC-inspired) architecture combined with the Service Layer Pattern**. Each folder has a specific responsibility and communicates with other layers in a controlled way.

Main layers:
- **Routes** – Define HTTP endpoints
- **Controllers** – Handle request flow and validation
- **Services** – Contain business logic
- **Models** – Manage data access and persistence
- **Utils** – Provide shared utilities (database, helpers)

This structure keeps the codebase clean, modular, and easy to extend.

## 📁 Folder Structure

```
Login/
├── controllers/
│   └── login_controller.py   # Handles login request flow
├── models/
│   └── user_model.py         # User data access and queries
├── routes/
│   └── login_routes.py       # API endpoint definitions
├── services/
│   └── auth_service.py       # Authentication business logic
├── utils/
│   └── db.py                 # Database connection utilities
├── app.py                    # Application entry point
├── Dockerfile                # Docker configuration
├── requirements.txt          # Python dependencies
└── README.md                 # Login microservice documentation
```

## 🎯 Design Patterns Used

### 🧩 MVC-inspired Architecture (API version)
Although this microservice does not include views, it follows MVC principles:
- **Model**: `models/` – Database access logic
- **Controller**: `controllers/` – Request orchestration
- **Routes**: `routes/` – HTTP endpoint exposure

### 🧠 Service Layer Pattern
The **services** layer contains all authentication logic:
- Credential validation
- Password verification
- Token generation (JWT, if implemented)

This keeps controllers thin and focused on HTTP responsibilities.

### ✅ Single Responsibility Principle
Each layer performs one clear task:
- Routes expose endpoints
- Controllers manage request flow
- Services implement business rules
- Models handle persistence
- Utils provide shared helpers

## 🔐 Authentication Flow (High Level)

1. Client sends login credentials to the login endpoint
2. Route forwards the request to the controller
3. Controller validates input and calls the service layer
4. Service authenticates the user using the model
5. Response (success or error) is returned to the client

## 🛠 Technologies Used

- **Python**
- **Flask / FastAPI**
- **REST APIs**
- **Docker**
- **Database integration** (SQL-based)

## 🚀 Purpose

The Login microservice acts as the secure entry point for students and tutors in the Academic Tutoring Management System. Its clean architecture allows independent deployment, easy maintenance, and secure authentication workflows.
