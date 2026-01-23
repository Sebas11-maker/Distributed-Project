from flask import request
from services.ver_citas_service import VerCitasService

def ver_citas():
    # Extraer el token del encabezado
    token = request.headers.get('Authorization')
    if not token:
        return jsonify({"success": False, "error": "Token no proporcionado"}), 401

    # El token viene como 'Bearer <token>', por lo que debemos extraer solo el token
    token = token.split(" ")[1]

    return VerCitasService.ver_citas(token)
