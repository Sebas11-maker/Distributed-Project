from flask import jsonify
from models.user_model import UserModel

class UpdateUsernameService:
    @staticmethod
    def update(user_id, new_email):
        if UserModel.email_exists(new_email):
            return jsonify({'error': 'Email ya existe'}), 409

        UserModel.update_email(user_id, new_email)
        return jsonify({'message': 'Usuario actualizado'}), 200
