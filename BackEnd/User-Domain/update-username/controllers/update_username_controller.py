from flask import request
from services.update_username_service import UpdateUsernameService

def update_username():
    data = request.get_json()
    old_email = data.get('oldEmail')
    new_email = data.get('newEmail')
    return UpdateUsernameService.update(old_email, new_email)

