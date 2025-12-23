
# DEFININDO A IMAGEM PYTHO NA SER UTILIZADA NA CONSTRUÇÃO DESSA IMAGEM
FROM python:3.13-slim

# DEFININDO O NOME DO DIRETÓRIO DENTRO DO CONTAINER
WORKDIR /SGE_DOCKER

# Evita que o Python gere arquivos .pyc
ENV PYTHONDONTWRITEBYTECODE=1
# Garante que logs sejam enviados direto para o terminal
ENV PYTHONUNBUFFERED=1

# LEVANDO TODO O DIRETÓRIO PARA DENTRO DO CONTAINER 
    # Atenção aqui; configure corretamente o .dockerignore
COPY . . 

# RODANDO UM COMANDO NO CONTAINER
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
# RUN python manage.py migrate


# ORIENTANDO QUAL PORTA ESTARÁ APTA A RECER CONEXÕES NO CONTINER
EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
