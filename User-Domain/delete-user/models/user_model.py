from utils.db import get_connection

class UserModel:

    @staticmethod
    def delete_user(user_id):
        conn, cursor = get_connection()
        cursor.execute("DELETE FROM users WHERE id=?", (user_id,))
        conn.commit()
