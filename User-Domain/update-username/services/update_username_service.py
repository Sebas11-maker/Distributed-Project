from flask import jsonify
from models.user_model import UserModel

class UpdateUsernameService:
    @staticmethod
    def update(old_email, new_email):
        if not old_email or not new_email:
            return jsonify({'error': 'Datos incompletos'}), 400

        if UserModel.email_exists(new_email):
            return jsonify({'error': 'Email ya existe'}), 409

        updated = UserModel.update_email_by_email(old_email, new_email)

        if updated == 0:
            return jsonify({'error': 'Usuario no encontrado'}), 404

        return jsonify({'message': 'Usuario actualizado'}), 200
