from flask import Blueprint
from controllers.agendar_cita_controller import agendar_cita

agendar_cita_bp = Blueprint('agendar_cita_bp', __name__)

@agendar_cita_bp.route('/agendar-cita', methods=['POST'])
def agendar():
    return agendar_cita()
