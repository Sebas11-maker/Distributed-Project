
# Get Dating Service - Barber Appointment Retrieval Microservice 💈

Welcome to the **Get Dating Service** repository! This microservice is designed to retrieve barber appointments and display them in a table format. It allows users to view scheduled appointments, providing an organized and easy-to-read interface for managing their bookings.

## Description 🔐

The **Get Dating Service** is built to handle the retrieval of scheduled appointments. It queries the database for existing appointments and returns them in a structured format, making it easier for clients and barbers to view upcoming bookings. This microservice is part of the **Reservation Service** system and interacts with other services for complete appointment management.

### Key Features ⚙️
- **Retrieve Appointments:** Fetches and displays appointments in a table format.
- **Data Access:** Interacts with the database to retrieve appointment information.
- **Organized Output:** Presents the retrieved appointment data in an easy-to-read and structured table.

## Architecture & Design 🏗️

- **Programming Language:** Python 3.x
- **Architecture Style:** Microservices architecture, allowing independent scaling and maintenance.
- **Design Pattern:** This service follows the **Controller-Service-Model (CSM)** design pattern, separating concerns between routing, business logic, and data models.

## Project Structure 📂

- **controllers:** Contains the logic for handling HTTP requests related to viewing appointments.
  - `agendar_cita_controller.py`: Handles appointment scheduling logic (also part of the larger system).
  - `ver_citas_controller.py`: Handles the logic for retrieving and displaying appointments.

- **models:** Contains the data models for the service.
  - `cita_model.py`: Defines the data structure for appointments.
  - `user_model.py`: Defines the data structure for users related to appointments.

- **routes:** Contains the routing logic for handling various endpoints.
  - `agendar_cita_routes.py`: Defines routes for scheduling appointments.
  - `ver_citas_routes.py`: Defines routes for viewing appointments.

- **services:** Contains the business logic for the service.
  - `agendar_cita_service.py`: Handles appointment creation logic (part of the larger system).
  - `ver_citas_service.py`: Contains the logic for retrieving appointment data and presenting it.

- **utils:** Helper functions and utilities for the service.
  - `db.py`: Manages database connection and queries.

- **app.py:** The main entry point for running the service.
- **Dockerfile:** Contains instructions for building the Docker image for the service.
- **requirements.txt:** Lists the required Python dependencies for the service.

## Docker 🐳

This service is containerized using Docker for easy deployment. The Docker image is hosted on Docker Hub with the name `galo12/get-dating`. To deploy the service, use the following commands:

1. **Build the Docker image:**
   ```bash
   docker build -t galo12/get-dating . 
   ```

2. **Run the Docker container:**
   ```bash
   docker run -p 5000:5000 galo12/get-dating
   ```

### Additional Information 📌

- **Database:** SQL Server is used for storing the appointment data.
- **Scalability:** As a microservice, it can scale independently to handle multiple requests, ensuring high availability for appointment viewing.
- **Security:** Data is securely stored and accessed only via the defined API.

Feel free to contribute to the repository. We welcome suggestions and improvements to make the service more efficient and useful.

### Note:
For more information on how this service interacts with other parts of the Reservation Service, please check the relevant documentation.
