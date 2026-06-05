#!/bin/bash
# Script de configuración automatizada para el despliegue del backend en Ubuntu

set -e

echo "=== 1. Actualizando paquetes del sistema ==="
sudo apt update && sudo apt upgrade -y

echo "=== 2. Instalando dependencias del sistema ==="
sudo apt install -y python3-pip python3-venv python3-dev libpq-dev postgresql postgresql-contrib nginx git curl

echo "=== 3. Configurando Base de Datos PostgreSQL ==="
# Cambiar contraseña del usuario postgres en la base de datos
sudo -u postgres psql -c "ALTER USER postgres PASSWORD '1726899113';"
# Crear la base de datos si no existe
sudo -u postgres psql -c "CREATE DATABASE maritimo_db;" || echo "La base de datos maritimo_db ya existe o fue omitida."

echo "=== 4. Preparando el Directorio de la Aplicación ==="
sudo mkdir -p /opt/maritimo_backend
sudo chown -R $USER:www-data /opt/maritimo_backend

echo "=== 5. Clonando el Repositorio ==="
# Si el directorio ya tiene archivos, hacer pull, de lo contrario clonar
if [ -d "/opt/maritimo_backend/.git" ]; then
    cd /opt/maritimo_backend
    git pull origin main
else
    git clone https://github.com/andreeesz17/maritimo_backend.git /opt/maritimo_backend
fi

cd /opt/maritimo_backend

echo "=== 6. Configurando Entorno Virtual Python ==="
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

echo "=== 7. Configurando Archivo .env ==="
if [ ! -f ".env" ]; then
    cat <<EOT >> .env
SECRET_KEY=$(python3 -c 'import secrets; print(secrets.token_hex(24))')
DEBUG=False
ALLOWED_HOSTS=zambrano-puertos.uaeftt-ute.site,159.89.92.242,localhost,127.0.0.1
DB_NAME=maritimo_db
DB_USER=postgres
DB_PASSWORD=1726899113
DB_HOST=localhost
DB_PORT=5432
CORS_ALLOW_ALL_ORIGINS=True
EOT
    echo "Archivo .env creado."
else
    echo "Archivo .env ya existe. Omitiendo creación."
fi

echo "=== 8. Ejecutando Migraciones y Recopilando Estáticos ==="
source .venv/bin/activate
python manage.py makemigrations --noinput
python manage.py migrate --noinput
python manage.py collectstatic --noinput

echo "=== 9. Configurando Permisos ==="
sudo usermod -aG www-data root
sudo chmod -R 755 /opt/maritimo_backend/staticfiles || echo "No static files yet"
sudo chmod -R 755 /opt/maritimo_backend

echo "=== 10. Copiando Configuraciones de Servicios ==="
# Gunicorn Service
sudo cp /opt/maritimo_backend/deploy/gunicorn.service /etc/systemd/system/gunicorn-maritimo.service
# Nginx Conf
sudo cp /opt/maritimo_backend/deploy/nginx.conf /etc/nginx/sites-available/maritimo
sudo ln -sf /etc/nginx/sites-available/maritimo /etc/nginx/sites-enabled/

# Crear logs para gunicorn
sudo touch /var/log/gunicorn-maritimo-access.log
sudo touch /var/log/gunicorn-maritimo-error.log
sudo chown root:www-data /var/log/gunicorn-maritimo-*.log
sudo chmod 660 /var/log/gunicorn-maritimo-*.log

echo "=== 11. Habilitando e Iniciando Servicios ==="
# Recargar systemd
sudo systemctl daemon-reload

# Habilitar e iniciar Gunicorn
sudo systemctl start gunicorn-maritimo
sudo systemctl enable gunicorn-maritimo

# Verificar Nginx y reiniciar
sudo nginx -t
sudo systemctl restart nginx

echo "============================================="
echo "¡Despliegue completado de manera exitosa!"
echo "API disponible en: http://159.89.92.242/api/"
echo "============================================="
