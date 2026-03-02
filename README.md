#  Generador de Contraseñas — Django + Docker

Aplicación web desarrollada con Django que permite generar contraseñas seguras automáticamente. El proyecto está configurado con Docker para facilitar su ejecución en cualquier entorno.

## Características
- Generación automática de contraseñas seguras
- Interfaz web sencilla e interactiva
- Arquitectura basada en Django
- Contenedorizado con Docker
- Código organizado por apps
- Generación dinámica sin recargar la página

## Tecnologías utilizadas
- Python
- Django
- Docker
- HTML
- CSS
- JavaScript
- SQLite (base de datos por defecto)

## Estructura del proyecto
PASSWORDS/
│
├── config/              # Configuración principal del proyecto Django
├── generator/           # App principal del sistema
│   ├── templates/
│   ├── static/
│   ├── views.py
│   └── models.py
│
├── Dockerfile           # Configuración del contenedor
├── docker-compose.yml   # Orquestación de servicios
├── manage.py
└── db.sqlite3

## Ejecución del proyecto

### Con Docker (recomendado)
docker compose up --build

Abrir en navegador:
http://127.0.0.1:8001

### Sin Docker (modo local)
Instalar dependencias:
pip install -r requirements.txt

Aplicar migraciones:
python manage.py migrate

Ejecutar servidor:
python manage.py runserver

Abrir:
http://127.0.0.1:8000

## Panel Administrador
Crear usuario admin:
python manage.py createsuperuser

Ingresar en:
http://127.0.0.1:8000/admin

## Variables de entorno
Crear archivo `.env` si el proyecto requiere configuración sensible.

Ejemplo:
SECRET_KEY=clave_secreta
DEBUG=True

## Autor
Carolina Alvarez

## Estado del proyecto
En desarrollo

## Licencia
Proyecto de uso educativo.