# 📝 Register Microservice – Academic Tutoring Management System

This directory contains the **Register microservice**, part of the Authentication Domain of the **Academic Tutoring Management System**. This microservice is developed in **Python** and is responsible for handling **user registration and account creation** in a secure and structured way.

The service follows a **layered, clean architecture** and applies common **software design patterns** to ensure scalability, maintainability, and clear separation of responsibilities.

## 🏗 Architecture Overview

The Register microservice is organized using a **layered (MVC-inspired) architecture combined with the Service Layer Pattern**. Each folder represents a distinct responsibility within the registration workflow.

Main layers:
- **Routes** – Define and expose HTTP endpoints
- **Controllers** – Handle request validation and orchestration
- **Services** – Implement business logic for user registration
- **Models** – Manage database access and persistence
- **Utils** – Provide shared utilities such as database connections

This approach keeps the codebase modular and easy to extend.

## 📁 Folder Structure

```
Register/
├── controllers/
│   └── register_controller.py   # Handles registration request flow
├── models/
│   └── user_model.py            # User data access and persistence
├── routes/
│   └── register_routes.py       # API endpoint definitions
├── services/
│   └── auth_service.py          # Registration business logic
├── utils/
│   └── db.py                    # Database connection utilities
├── app.py                       # Application entry point
├── Dockerfile                   # Docker configuration
├── requirements.txt             # Python dependencies
└── README.md                    # Register microservice documentation
```

## 🎯 Design Patterns Used

### 🧩 MVC-inspired Architecture (API version)
Even though this is a REST API without views, it follows MVC principles:
- **Model**: `models/` – Database queries and persistence
- **Controller**: `controllers/` – Request handling and coordination
- **Routes**: `routes/` – Endpoint exposure

### 🧠 Service Layer Pattern
The **services** layer encapsulates all business logic related to registration:
- Input validation
- Duplicate user checks
- User creation logic

This keeps controllers lightweight and focused on HTTP concerns.

### ✅ Single Responsibility Principle
Each layer performs a single, well-defined role:
- Routes expose endpoints
- Controllers manage flow and validation
- Services apply business rules
- Models handle persistence
- Utils provide reusable helpers

## 🔐 Registration Flow (High Level)

1. Client sends registration data to the register endpoint
2. Route forwards the request to the controller
3. Controller validates input and calls the service layer
4. Service checks for existing users and creates a new account
5. Model persists user data in the database
6. Response is returned to the client

## 🛠 Technologies Used

- **Python**
- **Flask / FastAPI**
- **REST APIs**
- **Docker**
- **Database integration** (SQL-based)

## 🚀 Purpose

The Register microservice provides the user onboarding entry point for the Academic Tutoring Management System. Its clean architecture allows independent deployment, easy maintenance, and secure account creation workflows.
