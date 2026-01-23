# 👤 User Domain – Academic Tutoring Management System

This directory contains the **User Domain** of the **Academic Tutoring Management System**, responsible for managing user-related operations beyond authentication.

All microservices in this domain are developed in **Python** and follow a **microservices architecture** with a **layered design**, ensuring modularity, scalability, and maintainability.

The User Domain focuses on user account management, profile updates, and supporting services that enhance the tutoring experience.

## 🧩 Domain Purpose

The User Domain handles operations related to:
- User profile management
- Account updates and maintenance
- Security-related user actions
- User-specific data retrieval

This domain works closely with the Authentication and Reservation domains to provide a complete and secure user lifecycle.

## 🧱 Microservices Included

### 🔒 change-password
Manages secure password update operations.

Main responsibilities:
- Validate user identity and authorization
- Apply password update logic
- Enforce password rules and security best practices
- Persist updated credentials securely

### 🗑 delete-user
Handles user account removal requests.

Main responsibilities:
- Validate permissions to delete an account
- Remove or deactivate user records
- Ensure data consistency with related domains
- Support compliance and user data control

### 🕒 date-time-service
Provides date and time related functionality.

Main responsibilities:
- Return current system date and time
- Provide standardized time responses for the platform
- Support synchronization across services (appointments, logs, etc.)

### ✏️ update-username
Manages username update operations.

Main responsibilities:
- Validate new username data
- Prevent duplicates or invalid usernames
- Update user profile information
- Return confirmation responses to the frontend

## 🏗 Architecture & Design Approach

Each microservice in the User Domain follows a **layered architecture**, typically including:
- **Routes / Controllers** for request handling
- **Services** for business logic
- **Models** for data access
- **Utils / Config** for shared helpers

This approach aligns with:
- **Service Layer Pattern**
- **MVC-inspired architecture**
- **Single Responsibility Principle**

## 🛠 Technologies Used

- **Python**
- **Flask / FastAPI**
- **REST APIs**
- **Docker**
- **Database integration** (SQL or NoSQL depending on system configuration)

## 📁 Folder Structure

```
User-Domain/
├── change-password/     # Password update microservice
├── date-time-service/   # Date and time utility service
├── delete-user/         # User account deletion service
├── update-username/     # Username update service
└── README.md            # User domain documentation
```

## 🎯 Why This Domain Matters

The User Domain ensures that users can safely manage their accounts and personal data within the Academic Tutoring Management System.

By separating user management into independent microservices, the system remains flexible, secure, and ready for future enhancements such as profile extensions, preferences, and notifications.
