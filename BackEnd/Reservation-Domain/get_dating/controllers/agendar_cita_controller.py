from flask import request
from services.agendar_cita_service import AgendarCitaService

def agendar_cita():
    data = request.get_json()
    fecha = data.get('fecha')
    hora = data.get('hora')
    return AgendarCitaService.agendar_cita(fecha, hora)
