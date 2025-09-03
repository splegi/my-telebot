import telebot
from telebot import types
import random
import schedule
import time
import threading
from datetime import datetime
from prometheus_client import start_http_server, Counter

bot = telebot.TeleBot('8020636906:AAG0SPFAfhvQ4Tj1ZpOYzdLhogyraAI-UXU')
# Метрика: количество отправленных комплиментов
compliments_sent = Counter('compliments_sent_total', 'Total compliments sent')

# Запуск HTTP сервера Prometheus на порту 8000
start_http_server(8000)
# Завершенный список комплиментов
compliments = [
    "у тебя безумно красивые глазки, такие кукольные зеленые!",
    "у тебя безумно восхитительная улыбка!!!!",
    "у тебя очень красивый маленький носик, аккуратненький такой!",
    "у тебя прекрасные маленькие щечки!",
    "у тебя прекрасные волосики, словно шерстка котика!!",
    "у тебя прекрасный маленький подбородочек!",
    "у тебя прекрасные бровки и реснички!",
    "у тебя безумно красивая и милая форма лица!",
    "улыбнись!!!",
    "а я тебя очень сильно люблю!!!",
    "у тебя безумно красивая тоненькая, хрупкая шея!",
    "у тебя такие маленькие узкие плечики, прекрасные!!!",
    "у тебя очень красивая маленькая спинка, хочу ее мять много!",
    "у тебя невероятно милые и красивые лапки, они такие маленькие и тоненькие няняня!",
    "у тебя безумно восхитительная грудь! идеального размера, формы и вкуса!",
    "у тебя восхитительный стройненький животик! он безумно вкусный и красивый.. хочу много целовать его!",
    "у тебя очень очень красивая маленькая талия!!!! я так люблю ее мять и смущать тебя этим мур!",
    "у тебя такие прекрасные и восхитительные бедра! Переход и изгиб от них к животику просто восхитителен!",
    "твоя попка просто превосходна! такая идеальная форма, размер, обожаю!!!",
    "у тебя безумно восхитительные дырочки, я так люблю их целовать, лизать и трахать мур! в них так тепло и хорошо..",
    "я так люблю твои маленькие красивые ножки!! они пиздец какие прекрасные, хочу их расцеловать, покусать и облизать..",
    "твои стопы прекрасные, такие маленькие у тебя ножки!",
    "у тебя такая прекрасная фигура!",
    "ты очень вкусная девочка!",
    "мой сладкий котенок!",
    "моя маленькая принцесса!!!",
    "улыбнись!!!!!"
]

# Глобальная переменная для хранения chat_id
chat_id = None

def send_message_hour():
    global chat_id
    if chat_id is not None:
        current_hour = datetime.now().hour
        if 7 <= current_hour < 23:
            compliment = random.choice(compliments)
            bot.send_message(chat_id, compliment)
            compliments_sent.inc()

# Планирование отправки сообщений
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
    markup.add(types.InlineKeyboardButton("Хочешь посмотреть на котиков?", url='https://ya.ru/images/search?text=милые%20котята'))
    markup.add(types.InlineKeyboardButton("У тебя плохое настроение? Посмотри на тюленчиков!", url='https://yandex.ru/images/search?from=tabbar&img_url=https%3A%2F%2Fpushinka.top%2Fuploads%2Fposts%2F2023-08%2F1693322844_pushinka-top-p-morskoi-kotik-kartinki-instagram-29.jpg&lr=21776&pos=9&rpt=simage&text=тюленчик'))
    markup.add(types.InlineKeyboardButton("Хочешь получать рассылку комплиментов??", callback_data="comp"))
    bot.reply_to(message, 'Привет моя любимая девочка! Это подарок тебе на годик! Бот будет отправлять тебе случайные, написанные лично мной комплименты!💗💗💗', reply_markup=markup)

@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == "love":
        bot.send_message(callback.message.chat.id, "А я очень очень люблю тебя сонечка!")
    elif callback.data == "comp":
        random_compliments = random.choice(compliments)
        bot.send_message(callback.message.chat.id, random_compliments)
        compliments_sent.inc()

# Запуск потока для планировщика
threading.Thread(target=schedule_checker).start()

# Поллинг для бота
bot.polling(none_stop=True)
