from flask import jsonify
from models.user_model import UserModel

class DeleteUserService:
    @staticmethod
    def delete(user_id):
        UserModel.delete_user(user_id)
        return jsonify({'message': 'Usuario eliminado'}), 200
