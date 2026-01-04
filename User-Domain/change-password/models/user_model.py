from utils.db import get_connection

class UserModel:

    @staticmethod
    def update_password(user_id, password):
        conn, cursor = get_connection()
        cursor.execute(
            "UPDATE users SET password=? WHERE id=?",
            (password, user_id)
        )
        conn.commit()
