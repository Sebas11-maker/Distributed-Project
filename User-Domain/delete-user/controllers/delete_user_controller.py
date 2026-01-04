from flask import request
from services.delete_user_service import DeleteUserService

def delete_user():
    data = request.get_json()
    user_id = data.get('user_id')
    return DeleteUserService.delete(user_id)
