from flask import Blueprint
from controllers.update_username_controller import update_username

update_username_bp = Blueprint('update_username_bp', __name__)

@update_username_bp.route('/update-username', methods=['PUT'])
def update():
    return update_username()
