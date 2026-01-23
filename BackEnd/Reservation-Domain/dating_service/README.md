
# Dating Service - Barber Appointment Microservice 💈

Welcome to the **Dating Service** repository! This is a microservice that provides functionality for generating barber appointments. The system allows clients to schedule their appointments with the barber, providing an easy interface for managing bookings.

## Description 🔐

The **Dating Service** is built to handle the creation and management of appointments for a barber shop. Clients can reserve time slots, and the system ensures that data is stored securely in a relational database. This microservice is part of the **Reservation Service** system and interacts with other services for comprehensive scheduling functionality.

### Key Features ⚙️
- **Appointment Generation:** Users can generate appointments for a barber.
- **Real-time Scheduling:** Clients can check available time slots and make bookings.
- **Secure Data Storage:** Uses a SQL database to store appointment information securely.

## Architecture & Design 🏗️

- **Programming Language:** Python 3.x
- **Architecture Style:** Microservices architecture, allowing for independent scaling and maintenance.
- **Design Pattern:** This service follows the **Controller-Service-Model (CSM)** design pattern, with clear separation between controller logic, service logic, and database models.

## Project Structure 📂

- **controllers:** Contains the logic for handling API requests related to appointments. 
  - `agendar_cita_controller.py`: Handles HTTP requests for scheduling appointments.
  
- **models:** Contains the data models for the service.
  - `cita_model.py`: Defines the data structure for appointments.
  - `user_model.py`: Defines the data structure for users involved in appointments.
  
- **routes:** Contains the routing logic for handling various endpoints.
  - `agendar_cita_routes.py`: Defines the API routes related to appointment scheduling.
  
- **services:** Contains the business logic for the service.
  - `agendar_cita_service.py`: Contains functions that handle the appointment creation and management.
  
- **utils:** Helper functions and utilities for the service.
  - `db.py`: Handles database connection and operations.
  
- **app.py:** The main entry point for running the service.
- **Dockerfile:** Contains instructions for building the Docker image for the service.
- **requirements.txt:** Lists the required Python dependencies for the service.

## Docker 🐳

This service is containerized using Docker for easy deployment. The Docker image is hosted on Docker Hub with the name `galo12/dating`. To deploy the service, use the following commands:

1. **Build the Docker image:**
   ```bash
   docker build -t galo12/dating .
   ```

2. **Run the Docker container:**
   ```bash
   docker run -p 5000:5000 galo12/dating
   ```

### Additional Information 📌

- **Database:** SQL Server is used for storing the appointment data.
- **Scalability:** As a microservice, it can scale independently to handle a large number of requests, ensuring high availability for the booking process.
- **Security:** Data is securely stored in the database and accessed only via the defined API.

Feel free to contribute to the repository. We welcome suggestions and improvements to make the service more efficient and useful.


