# 🧠 Backend – Academic Tutoring Management System

This directory contains the **Backend** of the **Academic Tutoring Management System**, a platform created to manage **academic tutoring appointments (citas académicas)** using a **microservices architecture**.

All backend services are developed in **Python**, containerized with **Docker**, and organized by domains to keep the system modular, scalable, and easy to maintain.

## 🚀 Project Overview

The backend is responsible for:
- Authenticating users securely (students, tutors, administrators)
- Managing user-related operations (profile updates, password changes, account deletion)
- Handling tutoring appointment reservations (creating and retrieving scheduled sessions)

Instead of building a single monolithic API, the backend is separated into **domains** made up of multiple microservices. This design improves:
- Scalability (services scale independently)
- Fault isolation (one service failure doesn’t crash the entire system)
- Maintainability (each service has a single responsibility)
- Deployment flexibility (services can be deployed on different servers/instances)

## 🧩 Domain-Based Microservices

### 🔐 Authentication-Domain
Contains all services related to authentication and access control, such as:
- Login
- Register
- Captcha microservice (anti-bot protection)

This domain is responsible for issuing and validating authentication tokens and protecting system resources.

### 📅 Reservation-Domain
Contains services responsible for appointment scheduling and retrieval, such as:
- Creating tutoring reservations (date/time validation, availability checks)
- Retrieving scheduled appointments for students or tutors

This is the domain that powers the “citas académicas” workflow.

### 👤 User-Domain
Contains services for user account management and supporting features, such as:
- Change password
- Delete user
- Update username
- Date/time service (utility for consistent time handling)

This domain ensures users can manage their profiles securely and keeps user-related operations independent of authentication and reservation logic.

## 🏗 Architecture & Design Principles

The backend follows these core principles:

### ✅ Microservices Architecture
Each service:
- Has a single responsibility
- Exposes REST API endpoints
- Can be deployed and scaled independently
- Uses its own internal layered structure (routes/controllers/services/models)

### 🧠 Layered Architecture Inside Services
Most services follow:
- **Routes** (endpoints)
- **Controllers** (request orchestration)
- **Services** (business logic)
- **Models** (database queries/persistence)
- **Utils/Config** (helpers, DB connections, environment configuration)

This promotes clean code and easier testing.

### 🔐 Security-Oriented Design
Recommended practices across services:
- JWT tokens for stateless authentication
- Password hashing
- Environment variables for secrets
- Captcha validation for sensitive endpoints

## 🛠 Technologies Used

- **Python**
- **Flask / FastAPI**
- **Docker**
- **REST APIs**
- **Database integration** (SQL-based or other, depending on configuration)

## 📁 Folder Structure

```
BackEnd/
├── Authentication-Domain/   # Login, Register, Captcha services
├── Reservation-Domain/      # Appointment scheduling and retrieval services
├── User-Domain/             # User management services (profile/security)
└── README.md                # Backend documentation
```

## 🎯 Purpose

The backend provides the complete server-side foundation for the Academic Tutoring Management System. With its domain-driven microservices approach, the system is designed to handle growth in users and appointments while remaining maintainable and secure.
