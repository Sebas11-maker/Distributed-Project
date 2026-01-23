import pyodbc

def get_connection():
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 18 for SQL Server};'
        'SERVER=54.144.243.21,1433;'
        'DATABASE=auth_db;'
        'UID=sa;'
        'PWD=Password123!;'
        'Encrypt=yes;'
        'TrustServerCertificate=yes;'
    )
    return conn, conn.cursor()
