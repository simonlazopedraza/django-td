# OnlyFlans - Sistema Web de Repostería (Django)
**Hito 3 - Base de Datos, ORM y Formularios**

Este proyecto es una plataforma web desarrollada en Python con Django para la PYME "OnlyFlans".
## 🛠️ Tecnologías y Arquitectura
- **Backend:** Python 3.14 / Django 6.1
- **Base de Datos:** PostgreSQL (pgAdmin4)
- **Frontend:** HTML5, CSS3, Bootstrap 5
- **Seguridad:** Autenticación por Tokens CSRF, Gestión de variables de entorno (`.env`).

## 📋 Funcionalidades Implementadas (Hito 1, 2 y 3)
1. **Modelos (ORM):** 
   - `Flan`: Catálogo de productos con diferenciación de acceso (`is_private`). Uso de `UUID` en lugar de IDs auto-incrementales.
   - `ContactForm`: Almacenamiento seguro de consultas de usuarios.
2. **Vistas y Renderizado Dinámico:**
   - La página de inicio (`/`) inyecta dinámicamente flanes públicos.
   - La página de bienvenida (`/bienvenido/`) filtra e inyecta flanes VIP.
3. **Formularios (`ModelForm`):**
   - Ruta `/contacto/` operativa. Implementa ciclo POST, validación de datos en servidor (`is_valid()`) y redirección de éxito (`/exito/`).
4. **Diseño Frontend:** Responsive Mobile-First con Bootstrap 5.

## ⚙️ Instrucciones de Instalación para el Evaluador

**⚠️ AVISO IMPORTANTE SOBRE LA BASE DE DATOS:** 
Este proyecto fue escalado a estándares de la industria, por lo que no utiliza SQLite3. **Utiliza PostgreSQL**. Para correr el proyecto localmente, por favor sigue estos pasos:

1. Crea un entorno virtual y actívalo.
2. Instala las dependencias:
   `pip install -r requirements.txt`
3. Crea una base de datos en tu servidor PostgreSQL local (ej. `desafio_final_django_td`).
4. Crea un archivo llamado `.env` en la raíz del proyecto y agrega tu clave local de Postgres:
   `DB_PASSWORD=tu_clave_postgres`
5. Ejecuta las migraciones para construir las tablas:
   `python manage.py makemigrations`
   `python manage.py migrate`
6. Levanta el servidor:
   `python manage.py runserver`

## 👨‍💻 Autor
- **Desarrollador:** Simón Lazo Pedraza
- **Rol:** Full Stack Developer (En Formación)
