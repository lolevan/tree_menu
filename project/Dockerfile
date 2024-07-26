# Используем официальный образ Python в качестве базового
FROM python:3.12

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Устанавливаем зависимости для PostgreSQL
RUN apt-get update && apt-get install -y postgresql-client

# Копируем файл зависимостей в контейнер
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем содержимое текущей директории в контейнер
COPY . .

# Добавляем скрипт ожидания
COPY wait-for-postgres.sh /wait-for-postgres.sh
RUN chmod +x /wait-for-postgres.sh

# Открываем порт 8000 для доступа к приложению
EXPOSE 8000

# Запускаем сервер разработки Django после проверки готовности базы данных
CMD ["/wait-for-postgres.sh", "db", "python manage.py runserver 0.0.0.0:8000"]
