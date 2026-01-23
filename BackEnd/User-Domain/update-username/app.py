from flask import Flask
from flask_cors import CORS
from routes.update_username_routes import update_username_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(update_username_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8003)
