# Laura - Sistema de Gestión para Kiosco

Laura es una aplicación de escritorio desarrollada en Python con Tkinter y MySQL para gestionar ventas, productos y stock de un kiosco. Incluye funciones como lectura de códigos de barra, actualización automática de inventario, cálculo total y almacenamiento de transacciones.

## Características

- Registro de ventas con fecha y total.
- Control de stock automático al vender o reponer.
- Interfaz gráfica intuitiva con Tkinter.
- Generación de tickets o reportes (próximamente con FPDF).
- Modularización del código para facilidad de mantenimiento.

##  Requisitos

- Python 3.x
- MySQL Server
- Librerías:
  - `mysql-connector-python`
  - `tkinter` (incluido en la mayoría de distribuciones Python)

##  Instalación

1. Cloná el repositorio:
   """bash
   git clone https://github.com/VelazquezCH/comercio.git
   cd comercio"""


## Configurá la base de datos MySQL:
- Crear la base de datos laura
- Crear las tablas necesarias (productos, stock, ventas, venta_producto)
- Cargar datos de prueba si es necesario
    use laura;

    create table ventas( 
        ID_venta int auto_increment primary key,
        nombre varchar(100),
        fecha datetime,
        total float);
        
    create table stock(
        ID_producto int,
        stock int,
        foreign key (ID_producto) references productos(ID_producto));    
        
    create table movimineto_stock(
        ID_producto int,
        fecha datetime,
        cantidad int,
        foreign key (ID_producto) references productos(ID_producto));
        
    create table venta_producto(
        ID_venta int,
        ID_producto int,
        cantidad int,
        precio float,
        foreign key(ID_venta) references ventas(ID_venta),
        foreign key (ID_producto) references productos(ID_producto));

    create table productos( 
        ID_producto int auto_increment primary key,
        codigo int,
        nombre varchar (100),
        precio float);


## Comandos git

git add<file>
git commit -m "..."(Algo breve)
git push origin main

## ¿Qué hace cada parte?🧠

- yscrollcommand=scroll_y.set → conecta el scroll vertical
- xscrollcommand=scroll_x.set → conecta el scroll horizontal
- scroll_y.config(command=tabla.yview) → activa el movimiento
- pack(side=RIGHT) y pack(side=BOTTOM) → colocan los scrolls al costado y abajo







🗓️ 1. DateEntry de tkcalendar
Este es el más usado en Tkinter. Permite seleccionar fechas desde un calendario desplegable.
🔧 Instalación:
pip install tkcalendar


🧪 Ejemplo básico:
from tkinter import Tk
from tkcalendar import DateEntry

root = Tk()
fecha_inicio = DateEntry(root, width=12, background='darkblue',
                         foreground='white', borderwidth=2, year=2025)
fecha_inicio.pack(padx=10, pady=10)

root.mainloop()


Podés acceder al valor con fecha_inicio.get().
## ¿que es un Frame?

    Un Frame es una caja contenedora dentro de una ventana. Sirve
para organizar widgets en grupos separados.
    Podes tener varios Frames en una misma ventana y cada uno puede tener 
su prodio sistema LAYOUT.
    LAYOUTS  es una forma de organizar y posicionar los widgets.

## ¿Por qué no se puede mezclar pack() y grid()?

    Tkinter no permite usar pack() y gridd() en el mismo contenedor.
## ¿Cómo se soluciona?

    Usando Frame como separador. Usando 
    -un Frame dende usas pack()
    -otro Frame donde usas grid() 


## ✍️ Autor 
Cristian Velázquez  
Entusiasta de Python y creador de soluciones prácticas para el mundo real.

 Consulta: productos vendidos entre dos fechas
SELECT 
    p.nombre AS nombre_producto,
    SUM(vp.cantidad) AS total_vendido
FROM 
    venta_producto vp
JOIN 
    ventas v ON vp.ID_venta = v.ID_venta
JOIN 
    productos p ON vp.ID_producto = p.ID_producto
WHERE 
    v.fecha BETWEEN '2025-01-01' AND '2025-08-30'
GROUP BY 
    vp.ID_producto, p.nombre;

















SELECT 
    p.nombre_producto,
    SUM(v.cantidad_vendida) AS total_vendido
FROM 
    ventas v
JOIN 
    productos p ON v.producto_id = p.id
WHERE 
    v.fecha_venta BETWEEN '2025-08-01' AND '2025-08-10'
GROUP BY 
    p.nombre_producto;





SELECT 
    producto_id,
    SUM(cantidad_vendida) AS total_vendido
FROM 
    ventas
WHERE 
    fecha_venta BETWEEN '2025-08-01' AND '2025-08-10'
GROUP BY 
    producto_id;












