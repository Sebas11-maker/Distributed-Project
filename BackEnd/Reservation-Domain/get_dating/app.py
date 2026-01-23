from flask import Flask
from flask_cors import CORS
from routes.agendar_cita_routes import agendar_cita_bp  # Rutas para agendar citas
from routes.ver_citas_routes import ver_citas_bp  # Nueva ruta para ver citas

app = Flask(__name__)
CORS(app)

# Registrar el blueprint para las rutas de agendar citas
app.register_blueprint(agendar_cita_bp)

# Registrar el blueprint para las rutas de ver citas
app.register_blueprint(ver_citas_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8002)
