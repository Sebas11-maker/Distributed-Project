import jwt
from flask import jsonify
from models.cita_model import CitaModel
from models.user_model import UserModel

SECRET_KEY = "supersecretkey"  # Usa tu clave secreta aquí

class VerCitasService:
    @staticmethod
    def ver_citas(token):
        try:
            decoded = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            cliente_email = decoded.get('email')  # Extraer el email del usuario desde el token
        except jwt.ExpiredSignatureError:
            return jsonify({"success": False, "error": "Token expirado"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"success": False, "error": "Token inválido"}), 401

        # Obtener las citas del usuario
        citas = CitaModel.obtener_citas(cliente_email)
        return jsonify({"success": True, "appointments": citas}), 200
