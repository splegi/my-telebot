FROM python:3.13.0

WORKDIR /app

# Копируем зависимости
ADD requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Копируем код бота
ADD import_telebot.py /app/import_telebot.py

# Проброс порта для Prometheus
EXPOSE 8000

# Запуск бота
CMD ["python", "import_telebot.py"]
