
# Services Folder

The **Services Folder** contains the business logic for the **Dating Service** microservice. It handles all the core functionality related to the scheduling and retrieval of barber appointments. The services interact with the models to retrieve or store data and implement the rules for appointment management.

## Purpose and Functionality

This folder contains two primary services: **AgendarCitaService** for scheduling appointments, and **VerCitasService** for retrieving and viewing appointments.

### Key Services

- **AgendarCitaService:** This service handles the logic for scheduling a new appointment. It verifies the availability of the client and the desired appointment time, ensuring that:
  - The client exists in the database.
  - The requested date and time fall within the allowed range (Monday to Friday, 7 AM to 7 PM).
  - The selected time slot is available.
  After validating these conditions, the service schedules the appointment in the database.

- **VerCitasService:** This service retrieves and displays the appointments for a specific user. It takes the authorization token, decodes it, extracts the client's email, and fetches their appointments from the database. The service ensures that the token is valid before proceeding with the request.

### Summary

By separating the business logic into distinct services, the application follows the **Service Layer** design pattern. This structure promotes maintainability and scalability by ensuring that each service is responsible for a specific set of tasks. The services layer communicates with the models for data handling and returns the results to the controllers, which then send the response to the client.

