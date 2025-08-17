

```markdown
# 💼 Laura - Sistema de Gestión para Kiosco

Laura es una aplicación de escritorio desarrollada en Python con Tkinter y MySQL para gestionar ventas, productos y stock de un kiosco. Incluye lectura de códigos de barra, actualización automática de inventario, cálculo total y almacenamiento de transacciones.

---

## 🚀 Características

- Registro de ventas con fecha y total.
- Control automático de stock.
- Interfaz gráfica con Tkinter.
- Generación de tickets (próximamente con FPDF).
- Código modular para mantenimiento.

---

## 🧰 Requisitos

- Python 3.x
- MySQL Server
- Librerías:
  - `mysql-connector-python`
  - `tkcalendar`
  - `tkinter` (incluido en Python)

---

## 🛠️ Instalación

```bash
git clone https://github.com/VelazquezCH/comercio.git
cd comercio
```

---

## 🗄️ Configuración de la base de datos

```sql
CREATE DATABASE laura;
USE laura;

CREATE TABLE productos (
  ID_producto INT AUTO_INCREMENT PRIMARY KEY,
  codigo INT,
  nombre VARCHAR(100),
  precio FLOAT
);

CREATE TABLE ventas (
  ID_venta INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(100),
  fecha DATETIME,
  total FLOAT
);

CREATE TABLE stock (
  ID_producto INT,
  stock INT,
  FOREIGN KEY (ID_producto) REFERENCES productos(ID_producto)
);

CREATE TABLE movimiento_stock (
  ID_producto INT,
  fecha DATETIME,
  cantidad INT,
  FOREIGN KEY (ID_producto) REFERENCES productos(ID_producto)
);

CREATE TABLE venta_producto (
  ID_venta INT,
  ID_producto INT,
  cantidad INT,
  precio FLOAT,
  FOREIGN KEY (ID_venta) REFERENCES ventas(ID_venta),
  FOREIGN KEY (ID_producto) REFERENCES productos(ID_producto)
);
```

---

## 👤 Autor

**Cristian Velázquez**  
Entusiasta de Python y creador de soluciones prácticas para el mundo real.

---

## 🧠 Apuntes técnicos (útiles para desarrolladores)

### Tkinter: Scroll y Layouts

| Comando | Descripción |
|--------|-------------|
| `yscrollcommand=scroll_y.set` | Conecta el scroll vertical |
| `xscrollcommand=scroll_x.set` | Conecta el scroll horizontal |
| `scroll_y.config(command=tabla.yview)` | Activa el movimiento |
| `pack(side=RIGHT)` | Coloca el scroll a la derecha |
| `pack(side=BOTTOM)` | Coloca el scroll abajo |

### ¿Qué es un Frame?

Un `Frame` es un contenedor que organiza widgets. Podés usar `pack()` en un Frame y `grid()` en otro para evitar conflictos.

---

### 📅 Tkcalendar: DateEntry

```bash
pip install tkcalendar
```

```python
from tkinter import Tk
from tkcalendar import DateEntry

root = Tk()
fecha_inicio = DateEntry(root, year=2025)
fecha_inicio.pack()
root.mainloop()
```

---

## 🧪 Consultas SQL útiles

```sql
SELECT p.nombre AS nombre_producto, SUM(vp.cantidad) AS total_vendido
FROM venta_producto vp
JOIN ventas v ON vp.ID_venta = v.ID_venta
JOIN productos p ON vp.ID_producto = p.ID_producto
WHERE v.fecha BETWEEN '2025-01-01' AND '2025-08-30'
GROUP BY vp.ID_producto, p.nombre;
```

---

## 🧬 Comandos Git recomendados

```bash
# Guardar cambios
git add archivo
git commit -m "Mensaje breve"
git push origin desarrolloCristian

# Fusionar al main
git checkout main
git merge desarrolloCristian
git push origin main

# Guardar temporalmente
git stash
git checkout main
git stash pop

# Descartar cambios (⚠️ cuidado)
git restore README.md notas.txt
git checkout main

#traer un archivo del main

git checkout main -- .gitignore
```

---







