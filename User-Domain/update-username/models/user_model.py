from utils.db import get_connection

class UserModel:

    @staticmethod
    def update_email_by_email(old_email, new_email):
        conn, cursor = get_connection()
        cursor.execute(
            "UPDATE users SET email=? WHERE email=?",
            (new_email, old_email)
        )
        rows = cursor.rowcount
        conn.commit()
        conn.close()
        return rows

