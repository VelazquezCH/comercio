from tkinter import Tk, Frame, Scrollbar, VERTICAL, HORIZONTAL, RIGHT, BOTTOM, Y, X
from tkinter import ttk, messagebox
import tkinter as tk
from validar import pasar_int
from MySQLconexion import obtener_conexion
from datetime import datetime







#___________________________Ventana de agregado de stock____________________________________

def ventana_agregar_stock_varios():
    def consulta_producto(): #event=None

        #---------------------Conexion a la base de datos
        #----reemplazo el codigo por MySQLconecion.py
        # conn = mysql.connector.connect(
        #     host = "localhost",
        #     port = 3306,
        #     user = "root",
        #     passwd = "juanolijaz",
        #     database = "laura"
        #     )
        conn = obtener_conexion()
        cursor = conn.cursor()
        #Llamo ala funcion para validar el ingreso
        codigo = pasar_int(entry_codigo.get())
        #Consulto nombre y id para agregar a la tabla
        cursor.execute("select ID_producto,nombre from productos where codigo = %s;",(codigo,))
        producto = cursor.fetchall()
        if producto:#si no esta vacio continua el codigo
            id_producto = producto[0][0]
            nombre = producto[0][1]
            cantidad = pasar_int(entry_cantidad.get(), "Cantidad incorrecto")
            if cantidad:#En validacion, si es incorrecto devuelve None
                tabla.insert("", tk.END, values=(id_producto, nombre, cantidad))
                entry_codigo.delete(0,tk.END)   
                entry_cantidad.delete(0,tk.END)
                entry_cantidad.insert(0,0)
        else:
            messagebox.showerror("Error", "Producto no encontrado.") 
        cursor.close()
        conn.close()

    def borrar_select():
        try:
            seleccionados = tabla.selection()  # Obtiene los ítems seleccionados
            if not seleccionados:  # Verifica si hay selección
                raise ValueError("No hay elementos seleccionados")
            respuesta = messagebox.askyesno(title="Confirmación", message="¿Seguro que quieres borrar los elementos seleccionados?")
            if respuesta:  # Solo borra si el usuario presiona "Sí"
                for item in seleccionados:
                    tabla.delete(item)
        except ValueError:
            messagebox.showwarning(title="Aviso", message="Selecciona un elemento para borrar.")



    def actualizar_stock():
        conn = obtener_conexion()
        cursor = conn.cursor()
        if tabla.get_children():
            fecha_hora = datetime.now()
            for row in tabla.get_children():
                values = tabla.item(row, "values") #Obtener los valores de la fila
                id_producto = values[0]
                cantidad = values[2]
                cursor.execute("INSERT INTO movimiento_stock(ID_producto,fecha, cantidad) VALUES (%s,%s,%s)",(id_producto, fecha_hora, cantidad))
                cursor.execute("UPDATE stock SET stock = stock + %s WHERE ID_producto = %s",(cantidad, id_producto))
                conn.commit()
        messagebox.showinfo("Exitoso", message="Se guardaron los cambios con exito")
        cursor.close()
        conn.close()
        

    root = tk.Tk()
    root.title("Agregar Stock de Varios Productos")
    root.geometry("400x300")
    root.resizable(False, False)

    # ───────────── Frame Título ─────────────
    frame_titulo = tk.Frame(root)
    frame_titulo.pack(pady=10)

    label_titulo = tk.Label(frame_titulo, text="Agregar Stock", font=("Arial", 16, "bold"))
    label_titulo.pack()

    # ───────────── Frame Formulario ─────────────
    frame_formulario = tk.Frame(root)
    frame_formulario.pack(padx=20, pady=10)

    # Usamos grid dentro del frame_formulario
    label_codigo = tk.Label(frame_formulario, text="Código del producto:")
    label_codigo.grid(row=0, column=0, sticky="e", pady=5)

    entry_codigo = tk.Entry(frame_formulario)
    entry_codigo.grid(row=0, column=1, pady=5)

    label_cantidad = tk.Label(frame_formulario, text="Cantidad a agregar:")
    label_cantidad.grid(row=1, column=0, sticky="e", pady=5)

    entry_cantidad = tk.Entry(frame_formulario)
    entry_cantidad.grid(row=1, column=1, pady=5)
    entry_cantidad.insert(0,0)

    # ───────────── Frame Botones ─────────────
    frame_botones = tk.Frame(root)
    frame_botones.pack(pady=20)

    boton_aceptar = tk.Button(frame_botones, text="Aceptar", width=10, command=consulta_producto)#lambda: print("Aceptar")
    boton_aceptar.pack(side="left", padx=10)

    boton_cancelar = tk.Button(frame_botones, text="Cancelar", width=10, command=root.destroy)
    boton_cancelar.pack(side="left", padx=10)

    boton_quitar = tk.Button(frame_botones, text="Quitar", width=10, command=borrar_select)
    boton_quitar.pack(side="left", padx=10)

    boton_guardar_db = tk.Button(frame_botones, text="Guardar lista/stock", command=actualizar_stock)
    boton_guardar_db.pack(side="left", padx=10)

    #------------Frame tabla ---------------

    frame_tabla = tk.Frame(root)
    frame_tabla.pack(padx=20, pady=10, fill="both", expand=True)

    #------------Scrollbars -----------------
    
    scroll_y = Scrollbar(frame_tabla, orient=VERTICAL)
    scroll_x = Scrollbar(frame_tabla, orient=HORIZONTAL)

    #-----------Tabla Treeview -----------

    tabla = ttk.Treeview(frame_tabla, columns=("codigo","nombre", "cantidad"), show="headings", yscrollcommand= scroll_y.set, xscrollcommand=scroll_x.set)
    tabla.heading("codigo", text="Código")
    tabla.heading("nombre", text="Nombre Producto")
    tabla.heading("cantidad", text="Cantidad")
    tabla.column("codigo", width=120)
    tabla.column("nombre", width=150)
    tabla.column("cantidad", width=100)

    #------------- Ubicar tabla y scrolls --------------

    tabla.pack(side="left", fill="both", expand=True)
    scroll_y.pack(side=RIGHT, fill=Y)
    scroll_x.pack(side=BOTTOM, fill=X)

    #-------------- Vincular scrolls ---------------

    scroll_y.config(command=tabla.yview)
    scroll_x.config(command=tabla.xview)

    root.mainloop()
    




#ventana_agregar_stock_varios()