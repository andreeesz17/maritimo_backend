# Documentación de la API - Control de Puerto Marítimo

Este documento describe detalladamente los endpoints disponibles en el backend de Control de Puerto Marítimo, las reglas de negocio implementadas y ejemplos de cargas útiles (JSON payloads).

---

## Configuración General

* **Autenticación:** Por defecto se utiliza `SessionAuthentication` con permisos de lectura para todos (`AllowAny` en modo de prueba académica). Las operaciones de escritura (`POST`, `PUT`, `PATCH`, `DELETE`) están limitadas a usuarios del staff mediante permisos configurados en la aplicación (`IsStaffOrReadOnly`).
* **Paginación:** Configurada globalmente con `StandardPagination`. Cada listado devuelve un máximo de 10 elementos por página de manera predeterminada.
  * Parámetro de página: `?page=1`
  * Parámetro de tamaño: `?page_size=20` (máximo 100)
* **Búsqueda y Ordenamiento:** Filtros avanzados por campos de estado, fechas, nombres, etc. y ordenamientos configurados por defecto mediante `django-filter` y clases ViewSets de Django REST Framework.

---

## Endpoints del Sistema

### 1. Health Check
* **Endpoint:** `GET /api/health/`
* **Descripción:** Endpoint para verificar la salud del servicio backend.
* **Respuesta de Éxito (200 OK):**
```json
{
  "service": "maritimo-api",
  "status": "ok",
  "version": "1.0"
}
```

---

### 2. Puertos (`/api/puertos/`)

#### Listar Puertos
* **Endpoint:** `GET /api/puertos/`
* **Parámetros de Filtro/Búsqueda opcionales:**
  * `?estado=activo` o `?estado=inactivo`
  * `?ciudad=Valparaiso`
  * `?search=NombrePuerto` (busca en `nombre` y `ciudad`)
  * `?ordering=capacidad_maxima_buques` o `?ordering=-nombre`
* **Respuesta de Éxito (200 OK):**
```json
{
  "count": 1,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "nombre": "Puerto de Valparaíso",
      "ciudad": "Valparaíso",
      "capacidad_maxima_buques": 50,
      "estado": "activo"
    }
  ]
}
```

#### Crear Puerto
* **Endpoint:** `POST /api/puertos/`
* **Payload JSON:**
```json
{
  "nombre": "Puerto de San Antonio",
  "ciudad": "San Antonio",
  "capacidad_maxima_buques": 80,
  "estado": "activo"
}
```
* **Regla de Negocio:** La capacidad máxima de buques no puede ser negativa.

#### Obtener Puerto por ID
* **Endpoint:** `GET /api/puertos/{id}/`
* **Respuesta (200 OK):**
```json
{
  "id": 2,
  "nombre": "Puerto de San Antonio",
  "ciudad": "San Antonio",
  "capacidad_maxima_buques": 80,
  "estado": "activo"
}
```

#### Actualizar Puerto
* **Endpoint:** `PUT /api/puertos/{id}/` o `PATCH /api/puertos/{id}/`
* **Payload JSON (PATCH):**
```json
{
  "capacidad_maxima_buques": 85
}
```

#### Eliminar Puerto
* **Endpoint:** `DELETE /api/puertos/{id}/`
* **Nota:** Utiliza protección `models.PROTECT`. No se puede eliminar un puerto si tiene muelles asociados.

---

### 3. Muelles (`/api/muelles/`)

#### Listar Muelles
* **Endpoint:** `GET /api/muelles/`
* **Filtros opcionales:** `?estado=activo`, `?puerto=1`, `?search=MuelleCodigo`
* **Respuesta de Éxito (200 OK):**
```json
{
  "count": 1,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "puerto": {
        "id": 1,
        "nombre": "Puerto de Valparaíso",
        "ciudad": "Valparaíso",
        "capacidad_maxima_buques": 50,
        "estado": "activo"
      },
      "codigo": "MLL-A1",
      "capacidad_atraque": 5,
      "estado": "activo"
    }
  ]
}
```

#### Crear Muelle
* **Endpoint:** `POST /api/muelles/`
* **Payload JSON:**
```json
{
  "puerto_id": 1,
  "codigo": "MLL-A1",
  "capacidad_atraque": 5,
  "estado": "activo"
}
```
* **Reglas de Negocio:**
  * La capacidad de atraque del muelle no puede ser negativa.
  * No se permite asociar un muelle a un puerto inactivo.

---

### 4. Buques (`/api/buques/`)

#### Listar Buques
* **Endpoint:** `GET /api/buques/`
* **Filtros opcionales:** `?tipo_buque=Carguero`, `?pais_origen=Chile`, `?search=MatriculaOBuque`
* **Respuesta de Éxito (200 OK):**
```json
{
  "count": 1,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "nombre": "Estrella del Sur",
      "matricula": "MS-9876-X",
      "tipo_buque": "Carguero",
      "capacidad_carga": "12500.50",
      "pais_origen": "Chile"
    }
  ]
}
```

#### Crear Buque
* **Endpoint:** `POST /api/buques/`
* **Payload JSON:**
```json
{
  "nombre": "Estrella del Sur",
  "matricula": "MS-9876-X",
  "tipo_buque": "Carguero",
  "capacidad_carga": 12500.50,
  "pais_origen": "Chile"
}
```
* **Reglas de Negocio:**
  * La capacidad de carga del buque debe ser estrictamente mayor a 0.
  * La matrícula del buque debe ser única en el sistema.

---

### 5. Capitanes (`/api/capitanes/`)

#### Listar Capitanes
* **Endpoint:** `GET /api/capitanes/`
* **Respuesta de Éxito (200 OK):**
```json
{
  "count": 1,
  "results": [
    {
      "id": 1,
      "nombres": "Roberto",
      "apellidos": "Gómez",
      "licencia_navegacion": "LIC-998822-CH",
      "nacionalidad": "Chile"
    }
  ]
}
```

#### Crear Capitán
* **Endpoint:** `POST /api/capitanes/`
* **Payload JSON:**
```json
{
  "nombres": "Roberto",
  "apellidos": "Gómez",
  "licencia_navegacion": "LIC-998822-CH",
  "nacionalidad": "Chile"
}
```
* **Reglas de Negocio:**
  * La licencia de navegación del capitán debe ser única.

---

### 6. Atraques (`/api/atraques/`)

#### Listar Atraques
* **Endpoint:** `GET /api/atraques/`
* **Filtros opcionales:** `?estado=programado`, `?muelle=1`, `?buque=1`, `?capitan=1`
* **Respuesta de Éxito (200 OK):**
```json
{
  "count": 1,
  "results": [
    {
      "id": 1,
      "buque": {
        "id": 1,
        "nombre": "Estrella del Sur",
        "matricula": "MS-9876-X"
      },
      "muelle": {
        "id": 1,
        "codigo": "MLL-A1",
        "puerto": {
          "id": 1,
          "nombre": "Puerto de Valparaíso"
        }
      },
      "capitan": {
        "id": 1,
        "nombres": "Roberto",
        "apellidos": "Gómez"
      },
      "fecha_ingreso": "2026-06-03T10:00:00-05:00",
      "fecha_salida": "2026-06-04T18:00:00-05:00",
      "estado": "programado"
    }
  ]
}
```

#### Crear Atraque
* **Endpoint:** `POST /api/atraques/`
* **Payload JSON:**
```json
{
  "buque_id": 1,
  "muelle_id": 1,
  "capitan_id": 1,
  "fecha_ingreso": "2026-06-03T10:00:00-05:00",
  "fecha_salida": "2026-06-04T18:00:00-05:00",
  "estado": "programado"
}
```
* **Reglas de Negocio:**
  * No permitir atraque en un muelle inactivo.
  * No permitir atraque en un puerto inactivo.
  * La fecha de salida no puede ser menor a la fecha de ingreso.

---

### 7. Inspecciones (`/api/inspecciones/`)

#### Listar Inspecciones
* **Endpoint:** `GET /api/inspecciones/`
* **Filtros opcionales:** `?resultado=Aprobado`, `?atraque=1`
* **Respuesta de Éxito (200 OK):**
```json
{
  "count": 1,
  "results": [
    {
      "id": 1,
      "atraque": {
        "id": 1,
        "buque": {"nombre": "Estrella del Sur"},
        "muelle": {"codigo": "MLL-A1"}
      },
      "fecha_inspeccion": "2026-06-03T12:00:00-05:00",
      "resultado": "Aprobado",
      "observaciones": "El buque cumple con todas las normas de seguridad del puerto marítimo."
    }
  ]
}
```

#### Crear Inspección
* **Endpoint:** `POST /api/inspecciones/`
* **Payload JSON:**
```json
{
  "atraque_id": 1,
  "fecha_inspeccion": "2026-06-03T12:00:00-05:00",
  "resultado": "Aprobado",
  "observaciones": "El buque cumple con todas las normas de seguridad del puerto marítimo."
}
```
* **Reglas de Negocio:**
  * La inspección solo se puede registrar si el atraque existe.
  * El resultado de la inspección solo puede ser: `Aprobado`, `Rechazado`, o `Pendiente`.
