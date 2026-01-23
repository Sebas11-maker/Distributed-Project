from utils.db import get_connection

class CitaModel:
    @staticmethod
    def obtener_citas(cliente_email):
        conn, cursor = get_connection()
        cursor.execute("SELECT fecha, hora FROM citas WHERE cliente_email=?", (cliente_email,))
        citas = cursor.fetchall()
        
        # Convertir la hora a string para evitar el error de serialización de JSON
        citas_serializadas = [
            {"fecha": cita[0], "hora": cita[1].strftime("%H:%M")} for cita in citas
        ]
        return citas_serializadas
