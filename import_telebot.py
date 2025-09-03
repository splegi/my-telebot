import telebot
from telebot import types
import random
import schedule
import time
import threading
from datetime import datetime

# Prometheus
from prometheus_client import start_http_server, Counter

bot = telebot.TeleBot('YOUR_BOT_TOKEN_HERE')

# Счётчик отправленных сообщений
messages_sent = Counter('messages_sent_total', 'Total number of messages sent by bot')

compliments = [
    "у тебя безумно красивые глазки, такие кукольные зеленые!",
    "улыбнись!!!",
    "а я тебя очень сильно люблю!!!"
    # ... твой список
]

chat_id = None

def send_message_hour():
    global chat_id
    if chat_id is not None:
        current_hour = datetime.now().hour
        if 7 <= current_hour < 23:
            compliment = random.choice(compliments)
            bot.send_message(chat_id, compliment)
            messages_sent.inc()  # увеличиваем счётчик

schedule.every().hour.do(send_message_hour)

def schedule_checker():
    while True:
        schedule.run_pending()
        time.sleep(1)

@bot.message_handler(commands=['start'])
def main(message):
    global chat_id
    chat_id = message.chat.id

    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("любишь меня??", callback_data="love"))
    markup.add(types.InlineKeyboardButton("Хочешь получать комплименты?", callback_data="comp"))
    bot.reply_to(message, 'Привет! Бот будет отправлять комплименты!💗', reply_markup=markup)
    messages_sent.inc()  # учитываем приветственное сообщение

@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == "love":
        bot.send_message(callback.message.chat.id, "А я очень очень люблю тебя!")
        messages_sent.inc()
    elif callback.data == "comp":
        random_compliments = random.choice(compliments)
        bot.send_message(callback.message.chat.id, random_compliments)
        messages_sent.inc()

# Запуск Prometheus метрик на порту 8000
start_http_server(8000)

# Запуск планировщика
threading.Thread(target=schedule_checker).start()

# Поллинг бота
bot.polling(none_stop=True)
