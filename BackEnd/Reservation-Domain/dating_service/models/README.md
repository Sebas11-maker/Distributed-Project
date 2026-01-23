
# Models Folder

The **Models Folder** is responsible for defining the data models used in the **Dating Service** microservice. It contains classes that interact with the database, handling the creation, retrieval, and management of user and appointment data. The models are used by other parts of the application, such as the controllers and services, to ensure proper communication with the database.

## Purpose and Functionality

The models define the data structures and provide methods for interacting with the database, including adding, retrieving, and verifying data. These models are essential for the core functionality of the microservice, which revolves around appointment scheduling and user management.

### Key Models

- **CitaModel:** Responsible for managing appointment data in the system. It handles operations such as:
  - Finding existing appointments based on date and time.
  - Creating new appointments and storing them in the database.
  
- **UserModel:** Responsible for managing user data. It handles operations such as:
  - Finding users based on their email and password (for login purposes).
  - Creating new users and storing their details (email and password) in the database.

### Database Interaction

Both models use the `get_connection()` method from the **utils/db.py** file to establish a connection with the database. Once connected, they execute SQL queries to interact with the relevant tables (`citas` for appointments and `users` for user data).

### Summary

By separating the logic for database interactions into models, the code becomes more modular and easier to maintain. This structure adheres to the **Model-View-Controller (MVC)** design pattern, where the models are responsible for data handling and storage, while the controllers and services manage the application's business logic.

