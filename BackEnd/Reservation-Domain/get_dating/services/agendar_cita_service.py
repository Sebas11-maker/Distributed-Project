from datetime import datetime
from flask import jsonify
from models.cita_model import CitaModel
from models.user_model import UserModel

class AgendarCitaService:
    @staticmethod
    def agendar_cita(fecha, hora):
        # Obtener el email del usuario desde el token o la sesión (en producción debe estar basado en el token JWT)
        cliente_email = "cliente@dominio.com"  # Debe obtenerlo del token del cliente en producción

        # Verificar si el email del cliente existe
        user = UserModel.find_user(cliente_email)
        if not user:
            return jsonify({"success": False, "error": "El usuario no existe"}), 400

        # Validar si la fecha y hora están dentro del rango permitido
        if datetime.strptime(fecha, "%Y-%m-%d").weekday() >= 5:  # 5 y 6 son sábado y domingo
            return jsonify({"success": False, "error": "Solo se pueden agendar citas de lunes a viernes"}), 400
        if not (datetime.strptime('07:00', '%H:%M').time() <= datetime.strptime(hora, '%H:%M').time() <= datetime.strptime('19:00', '%H:%M').time()):
            return jsonify({"success": False, "error": "La hora debe ser entre las 7 AM y las 7 PM"}), 400

        # Verificar si la cita ya está agendada
        cita_existente = CitaModel.encontrar_cita(fecha, hora)
        if cita_existente:
            return jsonify({"success": False, "error": "La fecha y hora ya están ocupadas"}), 400

        # Agendar la cita
        CitaModel.crear_cita(fecha, hora, cliente_email)
        return jsonify({"success": True, "message": "Cita agendada con éxito"}), 200
