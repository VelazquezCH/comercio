from tkinter import ttk, messagebox
import tkinter as tk
    
    
def pasar_int(a, mensaje="Código incorrecto"):
    try:
        numero = int(a)
        if numero < 0:
            messagebox.showerror("Número incorrecto", mensaje)
            return None
        return numero
    except ValueError:
        messagebox.showerror("Valor inválido", mensaje)
        return None



