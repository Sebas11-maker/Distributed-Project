
# Services Folder

The **Services Folder** contains the core business logic for the **Dating Service** microservice. The services are responsible for processing the data received from the API and executing the necessary actions related to appointments, such as scheduling an appointment, checking for existing bookings, and verifying the user. 

## Purpose and Functionality

This folder contains the **AgendarCitaService** class, which implements the logic for booking an appointment. The service ensures that the request is valid, verifies that the user exists, checks if the requested time slot is available, and creates the appointment if all conditions are met. 

### Key Service

- **AgendarCitaService:** This service is responsible for handling appointment scheduling. It performs the following tasks:
  - **Token Validation:** It validates the JWT token provided by the client to ensure the user is authenticated.
  - **User Verification:** It verifies that the user exists in the database before proceeding with scheduling.
  - **Date and Time Validation:** Ensures the appointment is scheduled on a valid day and within the allowed time range (Monday to Friday, 7 AM to 7 PM).
  - **Appointment Creation:** Checks if the selected date and time are already booked and creates the appointment if available.

The service interacts with both the **UserModel** and **CitaModel** to retrieve and store user and appointment data.

### Summary

By separating the business logic into the services folder, we follow the **Service Layer** design pattern. This makes the application easier to maintain, test, and scale. The service layer handles complex logic and leaves the controller and route layers to handle incoming requests and responses, ensuring a clean separation of concerns.

