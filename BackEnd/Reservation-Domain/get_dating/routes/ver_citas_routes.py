from flask import Blueprint
from controllers.ver_citas_controller import ver_citas  # Controlador para manejar la lógica

ver_citas_bp = Blueprint('ver_citas_bp', __name__)

# Ruta para ver las citas del usuario
@ver_citas_bp.route('/view-appointments', methods=['GET'])
def view_appointments():
    return ver_citas()  # Llama al controlador para ver las citas
