# API de Productos

Una API simple para gestionar un catálogo de productos.

## Prerrequisitos

- Python 3.8+
- pip

## Instalación

1.  Clona el repositorio:
    ```bash
    git clone <URL_DEL_REPOSITORIO>
    cd api-productos
    ```

2.  Crea y activa un entorno virtual:
    ```bash
    python -m venv .venv
    # En Windows
    .venv\Scripts\activate
    # En macOS/Linux
    source .venv/bin/activate
    ```

3.  Instala las dependencias:
    ```bash
    pip install fastapi "uvicorn[standard]" sqlalchemy
    ```

## Ejecución

Para ejecutar la aplicación, usa el siguiente comando:

```bash
uvicorn main:app --reload
```

La API estará disponible en `http://127.0.0.1:8000`.

## Endpoints de la API

La API de productos soporta las siguientes operaciones:

### Crear un Producto

- **POST** `/productos`
- **Body**:
  ```json
  {
    "nombre": "string",
    "precio": "float"
  }
  ```

### Obtener todos los Productos

- **GET** `/productos`

### Obtener un Producto

- **GET** `/productos/{producto_id}`

### Actualizar un Producto

- **PUT** `/productos/{producto_id}`
- **Body**:
  ```json
  {
    "nombre": "string",
    "precio": "float"
  }
  ```

### Eliminar un Producto

- **DELETE** `/productos/{producto_id}`

## Base de Datos

El proyecto utiliza una base de datos SQLite (`sql_app.db`) que se creará automáticamente al iniciar la aplicación.
