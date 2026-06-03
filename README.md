# UNIVERSIDAD UTE

<p align="center">
  <img src="https://www.ute.edu.ec/wp-content/uploads/2020/06/cropped-logo-ute-horizontal-1.png" alt="Logo Universidad UTE" width="300"/>
</p>

## ESCUELA DE TECNOLOGÍAS
### CARRERA DE DESARROLLO DE SOFTWARE


---

* **Proyecto:** Backend REST API — Control de Puerto Marítimo
* **Materia:** Programación IV
* **Estudiante:** Andrés Zambrano
* **Docente:** Ing. Francisco Higuera
* **Fecha:** Junio 2026

---

## 🚀 Descripción del Proyecto

Este proyecto es una API REST completa y robusta construida con **Django** y **Django REST Framework (DRF)** conectada a **PostgreSQL** para la gestión y control de operaciones de un puerto marítimo. 

El backend expone 6 entidades relacionadas con todo el ciclo CRUD, implementa **Autenticación por Tokens JWT**, y cuenta con un flujo de **CI/CD automatizado** en GitHub Actions desplegado en un Droplet de **DigitalOcean**.

---

## 🛠️ Requisitos de Instalación (Local)

Sigue estos pasos para instalar y ejecutar el proyecto en tu máquina local:

### 1. Clonar el repositorio
```bash
git clone https://github.com/andreeesz17/maritimo_backend.git
cd maritimo_backend
```

### 2. Configurar el entorno virtual
```powershell
# Crear el entorno virtual
python -m venv .venv

# Activar el entorno virtual
# En Windows (PowerShell):
.venv\Scripts\Activate.ps1
# En Linux/macOS:
source .venv/bin/activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Configurar variables de entorno (`.env`)
Crea un archivo `.env` en la raíz del proyecto basándote en el archivo `.env.example`:
```ini
SECRET_KEY=django-insecure-cambiar-en-produccion-1234567890abcdef
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

DB_NAME=maritimo_db
DB_USER=postgres
DB_PASSWORD=tu_contraseña_de_postgres
DB_HOST=localhost
DB_PORT=5432

CORS_ALLOW_ALL_ORIGINS=True
```

### 5. Ejecutar migraciones y arrancar el servidor
```bash
# Crear base de datos maritimo_db en tu PostgreSQL local antes de continuar.
python manage.py migrate
python manage.py runserver
```
El servidor estará corriendo en: `http://127.0.0.1:8000/`

### 6. Crear un Superusuario (para pruebas)
```bash
python manage.py createsuperuser
```
Ingresa tu usuario, email y contraseña para poder autenticarte en los endpoints protegidos.

---

## 🔐 Autenticación JWT

El proyecto utiliza **JSON Web Tokens (JWT)** para la seguridad de la API.
* **Acceso Público (Lectura):** Cualquier usuario puede listar y ver los detalles (`GET`) de los puertos, muelles, buques, capitanes, atraques e inspecciones.
* **Acceso Protegido (Escritura):** Solo los usuarios autenticados con rol de administrador/personal (`is_staff = True`) pueden realizar operaciones de creación (`POST`), edición (`PUT`/`PATCH`) y eliminación (`DELETE`).

### Flujo de obtención de Token:
Envía una petición a `/api/auth/login/` con las credenciales del usuario:
```json
{
  "username": "admin",
  "password": "adminpassword123"
}
```
Recibirás un Token de acceso (`access`) y de refresco (`refresh`). En cada petición protegida, añade la siguiente cabecera HTTP:
```http
Authorization: Bearer <tu_token_de_acceso>
```

---

## 📌 Listado de Endpoints y Estructura API

| Recurso | Endpoint | Métodos Permitidos | Descripción |
| :--- | :--- | :---: | :--- |
| **Salud** | `/api/health/` | `GET` | Comprobar estado de la API. |
| **Auth** | `/api/auth/register/` | `POST` | Registrar un nuevo usuario normal. |
| **Auth** | `/api/auth/login/` | `POST` | Obtener Tokens JWT (Login). |
| **Auth** | `/api/auth/token/refresh/` | `POST` | Refrescar token de acceso caducado. |
| **Auth** | `/api/auth/logout/` | `POST` | Cerrar sesión y invalidar token. |
| **Usuarios** | `/api/users/profile/` | `GET`, `PATCH` | Ver o actualizar perfil de usuario logueado. |
| **Puertos** | `/api/puertos/` | `GET`, `POST` | Listar y crear puertos marítimos. |
| **Puertos** | `/api/puertos/{id}/` | `GET`, `PATCH`, `DELETE` | Operaciones en puertos por ID. |
| **Muelles** | `/api/muelles/` | `GET`, `POST` | Listar y crear muelles. |
| **Buques** | `/api/buques/` | `GET`, `POST` | Listar y crear buques. |
| **Capitanes** | `/api/capitanes/` | `GET`, `POST` | Listar y registrar capitanes. |
| **Atraques** | `/api/atraques/` | `GET`, `POST` | Listar y registrar ingresos de buques. |
| **Inspecciones**| `/api/inspecciones/` | `GET`, `POST` | Listar y registrar inspecciones. |

---

## 🛡️ Reglas de Negocio Implementadas

1. **Capacidad de muelle:** La capacidad de atraque del muelle no puede ser negativa.
2. **Capacidad del buque:** La capacidad de carga del buque debe ser estrictamente mayor que cero.
3. **Matrícula única:** La matrícula del buque debe ser única en el sistema.
4. **Licencia de navegación:** La licencia del capitán debe ser única.
5. **Consistencia de Fechas:** En los atraques, la fecha de salida no puede ser anterior a la fecha de ingreso.
6. **Muelle activo:** No se permite programar un atraque en un muelle inactivo.
7. **Puerto activo:** No se permite programar un atraque en un muelle cuyo puerto esté inactivo.
8. **Existencia de atraque:** La inspección solo se puede registrar si el atraque correspondiente ya existe.
9. **Resultado de Inspección:** El resultado de la inspección solo puede tomar los valores: `Aprobado`, `Rechazado` o `Pendiente`.

---

## 📬 Pruebas con Postman

En la raíz del proyecto se incluyen los siguientes archivos para importar en Postman de forma directa:
1. **Colección:** `maritimo_api.postman_collection.json`
2. **Entorno:** `maritimo_api.postman_environment.json`

### Ventajas de esta Colección:
* **Autoguardado de Token:** Al hacer Login, los scripts de prueba de Postman extraen el token JWT y lo configuran automáticamente en las variables del entorno para todas las peticiones posteriores.
* **Encadenamiento CRUD:** Al crear un puerto, muelle o buque, su ID se almacena dinámicamente, lo que permite ejecutar de forma secuencial las peticiones de detalle, edición y eliminación sin modificar parámetros manualmente.
