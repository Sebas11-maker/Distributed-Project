
# Controllers Folder

The **Controllers Folder** is responsible for handling the incoming HTTP requests and routing them to the appropriate services for processing. It serves as the intermediary between the HTTP requests and the business logic layer of the microservice.

## Purpose and Functionality

This folder contains the controllers for handling appointment scheduling (`agendar_cita_controller.py`) and appointment viewing (`ver_citas_controller.py`). These controllers receive the incoming requests, extract the relevant data (such as the date, time, and token), and then call the corresponding service layer to process the data and return a response.

### Key Controllers

- **Agendar Cita Controller:** This controller handles appointment scheduling requests. It receives the appointment date and time via a `POST` request, and then it forwards the data to the **AgendarCitaService** for processing.

- **Ver Citas Controller:** This controller handles requests to retrieve appointments. It checks for a valid authorization token in the request header and then forwards the token to the **VerCitasService**, which retrieves the user's appointments.

### Summary

The controller layer is essential for managing HTTP requests in a clean and organized way. By separating the routing logic from the service and model layers, we follow the **Controller-Service-Model (CSM)** design pattern, which promotes maintainability and scalability. The controllers focus on managing HTTP-specific tasks, such as request validation and response formatting, while delegating business logic to the service layer.

