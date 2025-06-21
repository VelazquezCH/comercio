from MySQLconexion import obtener_conexion
from datetime import datetime
import tkinter as tk
from tkinter import ttk,messagebox



# def guardar_venta(treeview, nombre_cliente, label_total):
#     conn = obtener_conexion()
#     cursor = conn.cursor()
#     # lógica de inserción
#     conn.commit()
#     conn.close()


def confirmacion_guardado(tabla_treeview, caja_nombre_cliente, label_total):
    conn = obtener_conexion()
    cursor = conn.cursor()
    if tabla_treeview.get_children():
        fecha_hora = datetime.now()
        total = calcular_total(tabla_treeview, label_total)
        nombre = caja_nombre_cliente.get()
        cursor.execute("INSERT INTO ventas (nombre, fecha, total) VALUES( %s, %s, %s)",(nombre, fecha_hora,total))
        cursor.execute("SELECT LAST_INSERT_ID();")
        id_venta = cursor.fetchone()[0]

        #Recorrer el grid para tener los valores/productos
        for row in tabla_treeview.get_children():
            values = tabla_treeview.item(row, "values") #Obtener los valores de la fila
            id_producto = values[0]
            precio = values[2]
            cantidad = values[3]

            #insertar cada producto en la tabla venta_producto
            cursor.execute("INSERT INTO venta_producto (ID_venta, ID_producto, cantidad, precio) VALUES (%s, %s, %s, %s)",(id_venta, id_producto, cantidad, precio))
            reducir_stock(cantidad, id_producto)
        conn.commit()
        limpiar_grid(tabla_treeview, label_total)
        caja_nombre_cliente.delete(0, tk.END)

def reducir_stock(cantidad, id):
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute("UPDATE stock SET stock = stock - %s where ID_producto = %s;",(cantidad, id))



def limpiar_grid(tabla_treeview, label_total):
    for item in tabla_treeview.get_children():
        tabla_treeview.delete(item)
    label_total.config(text="Total: $0.00")    

def format_currency(value):
    try:
        return f"$ {float(value):,.2f}"  # Permite decimales con dos dígitos
    except ValueError:
        return value
    


def calcular_total(tabla_treeview, label_total):
    total_compra = 0
    for item in tabla_treeview.get_children():
        valores = tabla_treeview.item(item, "values")
        valor_grid3 = valores[4]
        valor_grid3 = float(valor_grid3.replace("$", "").replace(",", "").strip())
        total_compra += valor_grid3
    label_total.config(text=f"Total: ${total_compra:,.2f}")
    return total_compra

