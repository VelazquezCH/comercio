import mysql.connector
from datetime import datetime

def obtener_conexion():
    return mysql.connector.connect(
                host = "localhost",
                port = 3306,
                user = "root",
                passwd = "juanolijaz",
                database = "laura"
            )
