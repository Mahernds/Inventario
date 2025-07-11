# Inventario Tienda de Ropa Deportiva

Proyecto base para un sistema de inventario de una tienda de ropa deportiva.

## Configuración Inicial

### 1. Crear Entorno Virtual y Activar
```bash
python -m venv env
# En Windows
env\\Scripts\\activate
# En macOS/Linux
source env/bin/activate
```

### 2. Instalar Dependencias
```bash
pip install -r requirements.txt
```

### 3. Configurar Base de Datos
Inicialmente, el proyecto utiliza SQLite para desarrollo. La configuración se encuentra en `inventario_tienda/settings.py`.

Para producción, se puede cambiar a PostgreSQL modificando la configuración `DATABASES` en `settings.py`.

### 4. Aplicar Migraciones
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Crear Superusuario (para acceder al Admin)
```bash
python manage.py createsuperuser
```
Ingrese los datos solicitados (nombre de usuario, email, contraseña).

### 6. Ejecutar Servidor de Desarrollo
```bash
python manage.py runserver
```
El sitio estará disponible en `http://127.0.0.1:8000/`.
El panel de administración estará en `http://127.0.0.1:8000/admin/`.

## App Productos
La app `productos` maneja la lógica relacionada con los productos de la tienda.

- **Modelos**: `productos/models.py` define la estructura de los datos de los productos.
- **Admin**: `productos/admin.py` registra los modelos para ser gestionados a través del panel de administración de Django.
- **Vistas**: `productos/views.py` contiene la lógica para presentar los datos y manejar las interacciones del usuario.
- **URLs**: `productos/urls.py` define las rutas para la app de productos.
- **Plantillas**: Los archivos HTML se encuentran en `productos/templates/productos/`.

## Siguientes Pasos (Post-configuración inicial)
- Verificar que el modelo `Producto` y su interfaz en el admin funcionen correctamente.
- Implementar la vista para agregar productos manualmente a través de un formulario.
- Preparar el sistema para:
    - Agregar stock a los productos existentes.
    - Registrar y visualizar colores y metros de tela por producto.
    - Eventualmente, conectar a una base de datos PostgreSQL para producción.
