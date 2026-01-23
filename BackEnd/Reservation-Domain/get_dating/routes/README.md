
# Routes Folder

The **Routes Folder** defines the URL routes and the associated HTTP methods that allow the users to interact with the microservice. It serves as the bridge between the client and the controller layer, ensuring that incoming requests are properly routed to the correct controller functions.

## Purpose and Functionality

This folder defines the routes for both scheduling appointments (`agendar_cita_routes.py`) and viewing appointments (`ver_citas_routes.py`). These routes map the incoming HTTP requests to the appropriate controller actions for handling the logic.

### Key Routes

- **Agendar Cita Routes:** These routes handle the appointment scheduling logic.
  - `/agendar-cita` (POST): This route receives appointment scheduling requests and forwards them to the **Agendar Cita Controller** for processing.

- **Ver Citas Routes:** These routes handle the logic for retrieving and displaying appointments.
  - `/view-appointments` (GET): This route allows users to view their scheduled appointments. It forwards the request to the **Ver Citas Controller**, which retrieves and displays the appointments.

### Blueprint Usage

The routes are organized into **Flask Blueprints**, which provide a way to organize routes into modular sections. This allows for better scalability and easier management of related routes. The **Agendar Cita Blueprint** is responsible for handling appointment creation, while the **Ver Citas Blueprint** manages appointment retrieval.

### Summary

By organizing the routes into separate blueprints and files, the application is structured in a maintainable way. Each route file is focused on a specific task, such as managing appointments or viewing them, ensuring clear separation of concerns and enhancing code readability.

