import pyodbc

def get_connection():
    conn_str = (
        "DRIVER={ODBC Driver 18 for SQL Server};"
        "SERVER=98.89.162.195,1433;"
        "DATABASE=auth_db;"
        "UID=sa;"
        "PWD=Password123!;"
        "Encrypt=yes;"
        "TrustServerCertificate=yes;"
        "Connection Timeout=30;"
        "Login Timeout=30;"
    )
    conn = pyodbc.connect(conn_str, timeout=30)
    return conn, conn.cursor()
