from flask import Flask
from flask_cors import CORS
from routes.agendar_cita_routes import agendar_cita_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(agendar_cita_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001)
