import pyodbc

def get_connection():
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 18 for SQL Server};'
        'SERVER=98.89.162.195,1433;'
        'DATABASE=auth_db;'
        'UID=sa;'
        'PWD=Password123!;'
        'Encrypt=no;'
        'TrustServerCertificate=yes;'
    )
    return conn, conn.cursor()