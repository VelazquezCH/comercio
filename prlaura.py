
import mysql.connector
from datetime import datetime
import sys
import os
import tkinter as tk
from tkinter import ttk,messagebox


conn = mysql.connector.connect(
            host = "localhost",
            port = 3306,
            user = "root",
            passwd = "juanolijaz",
            database = "laura"
        )
cursor = conn.cursor()

def carga_tabla_venta():
        pass

def format_currency(value):
    try:
        return f"$ {float(value):,.2f}"  # Permite decimales con dos dígitos
    except ValueError:
        return value
    
def calcular_total():
    total_compra = 0
    #Recorrer toas las filas de Treeview
    for item in tabla_treeview.get_children():
        valores = tabla_treeview.item(item, "values")#obtener valores de la fila
        valor_grid3 = valores[4]
        valor_grid3 = float(valor_grid3.replace("$","").replace(",","").strip())
        total_compra += valor_grid3
    label_total.config(text=f"Total: ${total_compra:,.2f}")
    return total_compra


def consulta_producto(event=None):
    try:
        codigo = int(caja_ingreso_codigo.get())
    except ValueError:
         return
    cursor.execute("select ID_producto,nombre,precio from productos where codigo = %s;",(codigo,))
    producto = cursor.fetchall()
    if producto:
        id_producto = producto[0][0]
        nombre = producto[0][1]
        precio = float(producto[0][2])
        cantidad = int(caja_ingreso_cantidad.get())
        total = precio * cantidad
        tabla_treeview.insert("", tk.END, values=(id_producto, nombre, precio, cantidad,format_currency(total)))
        caja_ingreso_codigo.delete(0,tk.END)   
        caja_ingreso_cantidad.delete(0,tk.END)
        caja_ingreso_cantidad.insert(0,1)         
        calcular_total()
        
    else:
         messagebox.showerror("Error", "Producto no encontrado.") 
    
def borrar_select():
    try:
        seleccionados = tabla_treeview.selection()  # Obtiene los ítems seleccionados
        if not seleccionados:  # Verifica si hay selección
            raise ValueError("No hay elementos seleccionados")
        respuesta = messagebox.askyesno(title="Confirmación", message="¿Seguro que quieres borrar los elementos seleccionados?")
        if respuesta:  # Solo borra si el usuario presiona "Sí"
            for item in seleccionados:
                tabla_treeview.delete(item)
            calcular_total()  # Actualizar el total después de eliminar
    except ValueError:
        messagebox.showwarning(title="Aviso", message="Selecciona un elemento para borrar.")

def confirmacion_guardado():
    if tabla_treeview.get_children():
        fecha_hora = datetime.now()
        total = calcular_total()
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
        conn.commit()
        limpiar_grid()
        caja_nombre_cliente.delete(0, tk.END)

def limpiar_grid():
   if tabla_treeview.get_children(): #Verifica que haya elementos antes de borrar
    for item in tabla_treeview.get_children():
            tabla_treeview.delete(item)
    calcular_total()

if conn:
    print("Conexion con exito")
else:
    print("Error en conexion.")

#Ventana Principal
ventana_pricipal = tk.Tk()
ventana_pricipal.title("New TOMAS Kiosco")
ventana_pricipal.config(width=900, height=2000)

#Ingreso de codigo de barra
caja_ingreso_codigo = tk.Entry()
caja_ingreso_codigo.bind("<Return>", consulta_producto)
caja_ingreso_codigo.place(x=110, y=35)
caja_ingreso_codigo.config(width=20)
label_codigo = tk.Label(text="Código barra:")
label_codigo.place(x=10, y=35)


#Caja de texto para ingreso de cantidad de producto seleccionado por el codigo de barras
caja_ingreso_cantidad = tk.Entry()
caja_ingreso_cantidad.insert(0, 1)
caja_ingreso_cantidad.bind("<Return>", consulta_producto)
caja_ingreso_cantidad.place(x=110, y=60)
caja_ingreso_cantidad.config(width=10)
label_cantidad =tk.Label(text="Cantidad:")
label_cantidad.place(x=10, y=60)

#Caja de nombre_Cliente
caja_nombre_cliente = tk.Entry()
caja_nombre_cliente.place(x=110, y=10)
label_nombre = tk.Label(text="Nombre Cliente:")
label_nombre.place(x=10, y=10)


#Probar con un boton
boton_consulta = tk.Button(text="Agergar", command=consulta_producto)
boton_consulta.bind("<Return>", consulta_producto)
boton_consulta.place(x=300, y=55)

boton_quitar = tk.Button(text="Quitar", command=borrar_select)
boton_quitar.place(x=400, y=55)

boton_confirmar_venta = tk.Button(text="Confirmar", command=confirmacion_guardado)
boton_confirmar_venta.place(x=480, y=55)

#Grid
tabla_treeview = ttk.Treeview(ventana_pricipal, columns=("ID_producto","Nombre", "Precio", "Cantidad", "Total"), show="headings")
tabla_treeview.grid(row=0, column=0, columnspan=5)
tabla_treeview.pack(expand=True,padx=25, pady=85)
#grid1.place(x=10, y=50)

# Configurar encabezados
tabla_treeview.heading("ID_producto", text="ID")
tabla_treeview.heading("Nombre", text="Nombre")
tabla_treeview.heading("Precio", text="Precio")
tabla_treeview.heading("Cantidad", text="Cantidad")
tabla_treeview.heading("Total", text="Total")

label_total = tk.Label(text="Total: 0")
label_total.place(x=600, y=35)
label_total.config(font=("Arial", 14, "bold"), fg="red")



ventana_pricipal.mainloop()
conn.close()