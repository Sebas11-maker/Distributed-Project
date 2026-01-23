
# Utils Folder

The **Utils Folder** is responsible for providing utility functions that are used across the application. These utilities are meant to be reusable components that simplify common tasks and make the codebase more modular and maintainable.

## Purpose and Functionality

The **db.py** file inside this folder contains the `get_connection()` function, which is responsible for establishing a connection to the database. This function is used by various parts of the application to interact with the SQL Server database.

### Key Utility

- **get_connection():** This function is used to obtain a connection to the SQL Server database. It returns both the connection object and the cursor, which are used to execute queries and retrieve results. The connection details are hardcoded in the function for now but could be refactored to be more dynamic or configurable in the future.

### Summary

By placing the database connection logic in a utility file, we ensure that the code is clean and avoids redundancy. Any part of the application that needs to interact with the database can call this utility function to establish a connection. This structure follows the **Single Responsibility Principle (SRP)**, as the utility function has one clear purpose: to manage database connections.

