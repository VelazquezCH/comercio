import mysql.connector
from datetime import datetime


conn = mysql.connector.connect(
            host = "localhost",
            port = 3306,
            user = "root",
            passwd = "juanolijaz",
            database = "laura"
        )
cursor = conn.cursor()

# cursor.execute("SELECT LAST_INSERT_ID();")
# #id_venta = cursor.fetchall()---> devuelve [(0,)]
# id_venta = cursor.fetchone()
# print(id_venta[0])

#Consulta de productos 
# codigo = 101011
# cursor.execute("select nombre from productos where codigo = %s;",(codigo,))
# print(cursor.fetchone())

#Consulta estructura da una tabla
cursor.execute("desc stock;")
print(cursor.fetchall())

fecha_actual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
cursor.execute("""
            INSERT INTO movimiento_stock (ID_producto, cantidad, fecha)
            VALUES (%s, %s, %s)
        """, (1, 1, fecha_actual))
conn.commit()
conn.close()