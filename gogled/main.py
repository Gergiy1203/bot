import time
from docutils.parsers.rst.directives import percentage
from gevent.testing.travis import commands
from numpy.ma.core import max_val
from telebot import telebot
from logger import logger
import apihelper
from torch.fx.passes.infra.pass_manager import pass_result_wrapper
from tornado.httpserver import HTTPRequest
from telebot import util
import numpy as np
import multiprocessing
import statistics as st
from telebot import types
from django.contrib import admin
from django.urls import path, include
import docker
import bot
import django
import db
import unittest
import cython
import ty
import py
import api
import my_module
from telebot import apihelper










ALLOWED_USERS = ['your_telegram_account', 'someone_else']
OBJECT_OF_CHECKING = 'https://polygon-mainnet.chainstacklabs.com'
# Порог для подсвечивания критического отставания
THRESHOLD = 5

LOG_FILE = '../logs.csv'
# Адрес ноды, состояние которой я отслеживаю (публичная нода в данном случае)
OBJECT_OF_CHECKING = 'https://polygon-mainnet.chainstacklabs.com'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bot',
]


token = '6579699195:AAHH6s4_pJWipA4Ac2et6zda8tKQDyuLgdw'
url = f'https://core.telegram.org/bots/api'
chat_id = 5776717042




bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start', 'help'])
def start_welcome(message):
    bot.reply_to(message, "Привет! Я бот для управления чатом. Напиши /help, чтобы узнать, что я умею.")


@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message,
                 "/id юзера видите его для просмотра \n/вывод всех команнды что я магу /error если я поламался на пишите моему папе об ошипке и прикрипете скрин тг для связи с нем @Bnder666/stats - показать пользователя\n/selfstat - показать онлен пользователя")


def index(request):
    if request.method == "POST":
        update = telebot.types.Update.de_json(request.body.decode('utf-8'))

        bot.process_new_updates([update])


@bot.message_handler(commands=['teams'])
def teams_name(message):
    bot.reply_to(message, "вывод всех команнды что я магу")


@bot.message_handler(commands=['error'])
def error_name(message):
    bot.reply_to(message,
                 "если я поламался на пишите моему папе об ошипке и прикрипете скрин тг для связи с нем @Bnder666")







@bot.message_handler(commands=['id'])
def id_name(message):
    bot.reply_to(message, "видите id пользователя для просмотра его id его сахранен")












@bot.message_handler(commands=['kick'])
def kick_user(message):
    if message.reply_to_message:

        chat_id = message.chat.id
        user_id = message.reply_to_message.from_user.id
        user_status = bot.get_chat_member(chat_id, user_id).status
        if user_status == 'administrator' or user_status == 'creator':
            bot.reply_to(message, "Невозможно кикнуть администратора.")
        else:
            bot.kick_chat_member(chat_id, user_id)
            bot.reply_to(message, f"Пользователь {message.reply_to_message.from_user.username} был кикнут.")
    else:
        bot.reply_to(message,
                     "Эта команда должна быть использована в ответ на сообщение пользователя, которого вы хотите кикнуть.")


@bot.message_handler(commands=['online user'])
def online_user(message):
    if message.reply_to_message:

        chat_id = message.chat.id

        user_id = message.reply_to_message.from_user.id

        user_status = bot.get_chat_member(chat_id, user_id).status

        if user_status == 'administrator' or user_status == 'creator':
            bot.reply_to(message, "Невозможно отслидить пользователя.")
        else:
            duration = 60

            args = message.text.split()[1:]
            if args:

                try:
                    duration = int(args[0])
                except ValueError:
                    bot.reply_to(message, "Неправильный формат времени.")
                    return
                if duration < 1:
                    bot.reply_to(message, "Время должно быть положительным числом.")
                    return
                if duration > 1440:
                    bot.reply_to(message, "Максимальное время - 1 день.")
                    return
                bot.restrict_chat_member(chat_id, user_id, until_date=time.time() + duration * 60)
                bot.reply_to(message,
                             f"Пользователь {message.reply_to_message.from_user.username} замучен на {duration} минут.")
    else:
        bot.reply_to(message,
                     "Эта команда должна быть использована в ответ на сообщение пользователя, которого вы хотите замутить.")

    def check_service():
        # заранее подготовленный список референсных нод
        # для любой сети его можно найти на сайте https://chainlist.org/
        list_of_public_nodes = [
            'https://polygon.llamarpc.com',
            'https://polygon.rpc.blxrbdn.com',
            'https://polygon.blockpi.network/v1/rpc/public',
            'https://polygon-mainnet.public.blastapi.io',
            'https://rpc-mainnet.matic.quiknode.pro',
            'https://polygon-bor.publicnode.com',
            'https://poly-rpc.gateway.pokt.network',
            'https://rpc.ankr.com/polygon',
            'https://polygon-rpc.com'
        ]


def send_pics(update, context, ):
    with multiprocessing.Pool(processes=len(list_of_public_nodes)) as pool:
        results = pool.map(get_last_block_once, list_of_public_nodes)
        last_blocks = [b for b in results if b is not None and isinstance(b, int)]

        med_val = int(np.median(last_blocks))
        max_val = int(np.max(last_blocks))

        med_support = np.sum([1 for x in last_blocks if x == med_val])
        max_support = np.sum([1 for x in last_blocks if x == max_val])

        return max_val, max_support, med_val, med_support


@bot.message_handler(commands=['unmute'])
def unmute_user(message):
    if message.reply_to_message:
        chat_id = message.chai.id
        user_id = message.reply_to_message.from_user.id
        bot.restrict_chat_member(chat_id, user_id, can_send_messages=True, can_send_media_messages=True,
                                 can_send_other_messages=True, can_add_web_page_previews=True)
        bot.reply_to(message, f"Пользователь {message.reply_to_message.from_user.username} размучен.")
    else:
        bot.reply_to(message,
                     "Эта команда должна быть использована в ответ на сообщение пользователя, которого вы хотите размутить.")


@bot.message_handler(commands=['selfstat'])
def user_stats(message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    username = message.from_user.username
    if stats:
        bot.reply_to(message, "Статиска пуста.")
    else:
        if user_id not in stats[chat_id]['users']:
            bot.replt_to(message, "Вы еще не отправляли сообщений в этом чате.")
        else:
            user_messages = stats[chat_id]['users'][user_id]['messages']
            total_messages = stats[chat_id]['total_messaes']
            percentage = round(user_messages / total_messages * 100, 2)
            bot.reply_to(message,
                         f"Статистика для пользователя @{username}:\nВсего сообщений: {user_messages}\nПроцент от общего количества сообщений: {percentage}%")


bad_words = ['анкета', 'ссылка', 'уникальное предложение']


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)


@bot.message_handler()
def function_name(message):
    bot.reply_to(message, "This is a message handler")


@bot.message_handler(func=lambda message: message.document.mime_type == 'text/plan', content_types=['document'])
def handle_text_doc(message):
    pass


def test_message(message):
    return message.document.mime_type == 'text/plan'


@bot.message_handler(func=test_message, content_types=['document'])
def handler_text_doc(message):
    pass


@bot.message_handler(commads=['hello'])
@bot.message_handler(func=lambda msg: msg.text.encode("utf-8") == SOME_FANCY_EMOJI)
def send_something(message):
    pass


@bot.callback_query_handler(func=lambda call: True)
def test_callback(call):  # <- passes a CallbackQuery type object to your function
    logger.info(call)


@bot.inline_handler(lambda query: query.query == 'text')
def query_text(inline_query):
    @bot.inline_handler(lambda query: query.query == 'text')
    def query_text(inline_query):
        try:
            r = types.InliQueryResultArticle('1', 'Result', types.InputTextMessageContent('Result message.'))
            r2 = types.InliQueryResultArticle('2', 'Result2', types.InputTextMessageContent('Result message2'))
            bot.answer_inline_query(inline_query_id, [r, r2])
        except Exception as e:
            print(e)


apihelper.ENABLE_MIDDWEWAER = True


# @bot.middleware_handler(update_types=['message'])
def modify_message(bot_instance, message):
    # modifying the message before it reaches any other handler
    message.another_text = message.text + ':changer'


@bot.message_handler(commands=['start'])
def start(message):
    assert message.another_text == message.text + ':changer'


bot.polling()


class Middleware(BaseException):
    def __init__(self):
        self.update_types = ['message']

    def pre_process(self, message, data):
        data['foo'] = 'Hello'  # just for example
        # we edited the data. now, this data is passed to handler.
        #  return SkipHandler() -> this will skip handler
        # return CancelUpdate() -> this will cancel update

    def post_process(self, message, data, exception=None):
        print(data['foo'])
        if exception:  # check for exception
            print(exception)
