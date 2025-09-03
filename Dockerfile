FROM python:3.13.0

WORKDIR /app

ADD requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

ADD import_telebot.py /app/import_telebot.py

CMD ["python", "import_telebot.py"]