from utils.db import get_connection

class CitaModel:
    @staticmethod
    def encontrar_cita(fecha, hora):
        conn, cursor = get_connection()
        cursor.execute("SELECT id FROM citas WHERE fecha=? AND hora=?", (fecha, hora))
        return cursor.fetchone()

    @staticmethod
    def crear_cita(fecha, hora, cliente_email):
        conn, cursor = get_connection()
        cursor.execute("INSERT INTO citas (fecha, hora, cliente_email) VALUES (?, ?, ?)", (fecha, hora, cliente_email))
        conn.commit()
