
# Agendar Cita Controller

The **Agendar Cita Controller** is a key component of the **Dating Service** microservice responsible for handling appointment scheduling requests. It acts as an intermediary between the API and the underlying business logic for booking barber appointments.

## Purpose and Functionality

This controller is designed to receive HTTP requests for scheduling appointments from the users. It processes the incoming request data, which includes the appointment date (`fecha`) and time (`hora`), and passes this data to the **AgendarCitaService** for further processing. The controller ensures that the data is properly formatted before being handled by the service layer.

### Key Responsibilities:
- **Handle Appointment Scheduling Requests:** Accepts requests to schedule barber appointments, extracting the necessary data (date and time).
- **Intermediary Between API and Service Layer:** The controller forwards the appointment data to the **AgendarCitaService** to ensure proper business logic execution.
- **Data Validation:** Ensures that the incoming data is in the expected format, which includes date and time values for the appointment.

By separating the controller logic from the service logic, this structure ensures a clean and maintainable architecture. The controller focuses on request handling, while the service layer handles the actual business logic related to the appointment scheduling.

This organization allows for easier scaling, debugging, and testing, as each component is responsible for a specific task.

