from flask import jsonify
from models.user_model import UserModel

class ChangePasswordService:
    @staticmethod
    def change(user_id, new_password):
        UserModel.update_password(user_id, new_password)
        return jsonify({'message': 'Contraseña actualizada'}), 200
