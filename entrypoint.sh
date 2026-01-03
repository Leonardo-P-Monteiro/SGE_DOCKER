#!/bin/sh

# O script para execução imediatamente se algum comando falhar
set -e

echo "--> Rodando migrações do banco de dados..."
python manage.py migrate

echo "--> Verificando/Criando superusuário..."
# Executa o seu script personalizado
python create_superuser.py

echo "--> Coletando arquivos estáticos..."
# Necessário para o WhiteNoise servir o CSS/JS corretamente
python manage.py collectstatic --noinput

echo "--> Iniciando o servidor Gunicorn..."
# O Render injeta a variável $PORT automaticamente
exec gunicorn app.wsgi:application --bind 0.0.0.0:$PORT