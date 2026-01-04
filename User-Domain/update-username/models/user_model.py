from utils.db import get_connection

class UserModel:

    @staticmethod
    def email_exists(email):
        conn, cursor = get_connection()
        cursor.execute("SELECT id FROM users WHERE email=?", (email,))
        return cursor.fetchone()

    @staticmethod
    def update_email(user_id, email):
        conn, cursor = get_connection()
        cursor.execute(
            "UPDATE users SET email=? WHERE id=?",
            (email, user_id)
        )
        conn.commit()
