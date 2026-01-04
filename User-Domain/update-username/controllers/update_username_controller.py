from flask import request
from services.update_username_service import UpdateUsernameService

def update_username():
    data = request.get_json()
    user_id = data.get('user_id')
    new_email = data.get('new_email')
    return UpdateUsernameService.update(user_id, new_email)
