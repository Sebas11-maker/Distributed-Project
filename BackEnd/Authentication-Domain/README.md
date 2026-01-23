# 🔐 Authentication Domain – Academic Tutoring Management System

This directory contains the **Authentication Domain** of the **Academic Tutoring Management System**, a platform designed to manage **academic tutoring appointments (citas académicas)** in an organized, secure, and scalable way.

All services in this domain are developed in **Python** and follow a **microservices architecture**, where each service has a clear responsibility and can be deployed independently. The Authentication Domain ensures that only authorized users (students, tutors, and administrators) can access the platform and its protected resources.

## 🧩 Domain Purpose

The Authentication Domain provides the core identity and security layer of the system. Its responsibilities include:
- User onboarding (registration)
- Secure login and session handling
- Access control for protected endpoints
- Anti-bot protections (captcha validation)
- Token issuance and validation (e.g., JWT)

By isolating authentication into its own domain, the overall system becomes more modular and easier to scale, maintain, and secure.

## 🧱 Microservices Included

### 🔑 Login Microservice
Handles user authentication and access control entry into the platform.

Typical responsibilities:
- Validate credentials (email/username + password)
- Authenticate users against the database
- Generate access tokens (JWT) for stateless authentication
- Return standardized responses for frontend clients

This service is the gateway for students and tutors to sign in and manage tutoring appointments.

### 📝 Register Microservice
Handles user creation and onboarding flows.

Typical responsibilities:
- Validate required user data (email, password, role)
- Prevent duplicate accounts
- Persist user records securely in the database
- Apply security rules (recommended: password hashing, strength validation)

This service enables new users to create accounts so they can request or manage tutoring sessions.

### 🧩 Captcha Microservice
Provides anti-bot protection to reduce automated abuse (fake registrations, brute force login attempts).

Typical responsibilities:
- Validate captcha tokens submitted by the frontend
- Reject requests that fail validation
- Provide a reusable security layer for both login and registration workflows

This microservice is especially useful when the system is exposed publicly and needs additional security controls.

## 🏗 Architecture & Design Approach

The Authentication Domain is built using a **layered architecture** inside each microservice, commonly using:
- **Routes / Controllers** for HTTP request handling
- **Services** for business logic
- **Models** for data access
- **Utils** for shared helpers (DB connection, tokens, hashing, validation)

This approach aligns with:
- **Service Layer Pattern** (business logic in services)
- **MVC-inspired separation** (models/controllers/routes)
- **Single Responsibility Principle** (each microservice does one main job)

## 🛠 Technologies Used

- **Python** – Core language across all microservices
- **Flask / FastAPI** – For building REST APIs
- **JWT (recommended)** – Token-based authentication and authorization
- **Docker** – Containerization for consistent deployment
- **Database Integration** – Depends on system setup (e.g., SQL Server or other DB engines)

## 📁 Folder Structure

```
Authentication-Domain/
├── captcha-microservice/   # Captcha validation service (anti-bot)
├── Login/                  # Login/authentication service
├── Register/               # Registration/onboarding service
└── README.md               # Authentication domain documentation
```

## 🔐 Security Best Practices (Recommended)

To make authentication production-ready, it is recommended to:
- Hash passwords (bcrypt/argon2/werkzeug)
- Store secrets in environment variables (not hardcoded)
- Enforce strong password policies
- Apply rate limiting and logging
- Use HTTPS in production deployments
- Validate JWT tokens on protected routes
- Use captcha on sensitive endpoints (login/register)

## 🎯 Why This Domain Matters

The Authentication Domain is the foundation that enables safe management of academic tutoring appointments. Without a strong and isolated authentication layer:
- Unauthorized users could access private schedules
- Student and tutor data could be exposed
- The appointment system could be abused by bots

With this domain, the Academic Tutoring Management System can confidently provide secure access to tutoring resources and scheduling features.
