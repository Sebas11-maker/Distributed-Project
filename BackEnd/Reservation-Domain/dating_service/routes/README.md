
# Routes Folder

The **Routes Folder** is responsible for defining the URL routes and the associated HTTP methods that the application will use. It serves as a routing layer, linking the incoming requests to the appropriate controller methods that handle the actual business logic.

## Purpose and Functionality

The routes in this folder define the URL patterns that the client can use to interact with the microservice. They receive the HTTP requests, parse any incoming data, and then pass the data to the controllers, which handle the business logic. After processing, the controllers return a response to the client.

### Key Route

- **Agendar Cita Route:** The folder currently contains a route for scheduling appointments. This route listens for `POST` requests at the `/agendar-cita` endpoint. When an appointment request is received, the route calls the **agendar_cita()** function from the **Agendar Cita Controller**, which processes the appointment creation.

### Blueprint Usage

The routes in this folder are encapsulated in a **Flask Blueprint**, which is used to organize the application's routing logic in a modular and maintainable way. Blueprints allow the application to have multiple route files, which can be registered in the main application.

### Summary

By separating the routes into a dedicated folder and using blueprints, the application achieves a cleaner structure. The routes handle the incoming requests and delegate the logic to the appropriate controllers, keeping the application modular and easy to maintain.

