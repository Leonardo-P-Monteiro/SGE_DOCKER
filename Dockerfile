
# DEFININDO A IMAGEM PYTHO NA SER UTILIZADA NA CONSTRUÇÃO DESSA IMAGEM
FROM python:3.13-slim

# DEFININDO O NOME DO DIRETÓRIO DENTRO DO CONTAINER
WORKDIR /SGE_DOCKER

# Evita que o Python gere arquivos .pyc
ENV PYTHONDONTWRITEBYTECODE=1
# Garante que logs sejam enviados direto para o terminal
ENV PYTHONUNBUFFERED=1

# Instala dependências do sistema (necessário para compilar pacotes como psycopg2)
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# LEVANDO TODO O DIRETÓRIO PARA DENTRO DO CONTAINER 
    # Atenção aqui; configure corretamente o .dockerignore
COPY . . 

# RODANDO UM COMANDO NO CONTAINER
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
# RUN python manage.py migrate
# Dá permissão de execução ao script (CRÍTICO para evitar "permission denied")
RUN chmod +x /entrypoint.sh

# ORIENTANDO QUAL PORTA ESTARÁ APTA A RECER CONEXÕES NO CONTINER
EXPOSE 8000

# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# Define o script que gerencia o boot da aplicação
ENTRYPOINT ["/entrypoint.sh"]
