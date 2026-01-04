from flask import request
from services.change_password_service import ChangePasswordService

def change_password():
    data = request.get_json()
    user_id = data.get('user_id')
    new_password = data.get('new_password')
    return ChangePasswordService.change(user_id, new_password)
