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

## ✍️ Autor
Cristian Velázquez  
Amante del backend, entusiasta de Python y creador de soluciones prácticas para el mundo real.










