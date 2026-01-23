
# Models Folder

The **Models Folder** defines the data models and database interactions for the **Dating Service** microservice. This folder is responsible for managing the user and appointment data, ensuring that data is retrieved and stored correctly in the database.

## Purpose and Functionality

The models provide a structured way to interact with the database by defining the data entities and the methods for accessing and modifying the data. In this microservice, the models focus on two main entities: **appointments** (citas) and **users**.

### Key Models

- **CitaModel:** This model is responsible for handling operations related to appointments. It includes methods for:
  - Retrieving a list of appointments for a particular user based on their email.
  
- **UserModel:** This model handles operations related to user data. It includes methods for:
  - Finding users by email (and optionally by password) for authentication.
  - Creating new users by storing their email and password in the database.

### Database Interaction

Both models use the `get_connection()` method from the **utils/db.py** file to establish a connection to the database. Once connected, they execute SQL queries to interact with the `users` and `citas` tables.

- **CitaModel**: Handles the retrieval of appointments from the `citas` table based on the user's email and formats the results to be used in the application.
- **UserModel**: Handles user authentication by checking the `users` table to find a matching email (and password, if provided). It also allows the creation of new users by inserting data into the `users` table.

### Summary

By organizing the data interaction in the models folder, we maintain a clean separation of concerns. The models focus on how data is stored and retrieved, while other components, such as the controllers and services, handle the application logic.

