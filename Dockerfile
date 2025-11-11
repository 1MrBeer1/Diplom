# Базовый образ
FROM python:3.11-slim

# Установим зависимости
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Рабочая директория
WORKDIR /code

# Копируем зависимости
COPY requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Копируем проект
COPY . /code/

# Копируем скрипт wait-for-it.sh
COPY wait-for-it.sh /wait-for-it.sh
RUN chmod +x /wait-for-it.sh

# Пробрасываем порт для Django
EXPOSE 8000
