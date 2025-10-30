import asyncio
import os
from pyrogram.raw.types import dialog
import telebot
import test   # noqa: F401
from pyrogram import Client







api_id = "20368885"
api_hash = "1d499a8be7aad4553d3c2395829292c6"
token = "8225602323:AAFF0R9Pju3jRaEuWC4n_jyj18VWdb-veZU"

model = ""







with Client(name="my_account", api_hash=api_hash, api_id=api_id) as app:
    app.send_message("me", "Это я бот")




#client = Mistral(api_key=api_key)



#chat_response = client.chat.complete(
    #model= model,
    #messages = [
        #{
            #"role": "user",
            #"content":"What is the best French cheese?"
            #},
        #   ]
#)







 # app.send_location("me", latitude, longitude)


# await app.send_cached_media("me", file_id)














@app.on_callback_query()
async def callback_query_handler(client, query):
    await query.answer("Callback query received!", show_alert=True)


async def main():
    async with app:
        bot_results = await app.get_dialogs()
        await app.send_inline_bot_result(
            "me", bot_results.query_id, bot_results.results[0].id
        )


@app.on_raw_update()
async def raw(client, update, users, chats):
    print(update)


with app:
    app.send_message("me", "hi!")


async def main():
    await app.start()
    await app.stop()




async def main():
    async with app:
        print(await app.get_me())




















bot = telebot.TeleBot(token)


@bot.message_handler(commands=["start", "help"])
def start_welcome(message):
    bot.reply_to(
        message,
        "Привет! Я бот для управления чатом. Напиши /help, чтобы узнать, что я умею.",
    )


@bot.message_handler(commands=["help"])
def help(message):
    bot.reply_to(message, "тут буду каманды")


def index(request):
    if request.method == "POST":
        update = telebot.types.Update.de_json(request.body.decode("utf-8"))

        bot.process_new_updates([update])


@bot.message_handler(commands=["teams"])
def teams_name(message):
    bot.reply_to(message, "вывод всех команнды что я магу")


@bot.message_handler(commands=["error"])
def error_name(message):
    bot.reply_to(
        message,
        "если я поламался на пишите моему папе об ошипке и прикрипете скрин тг для связи с нем @Bnder666",
    )


@bot.message_handler(commands=["subscription"])
def subscription_name(message):
    bot.reply_to(message, "subscrription подписан на канал от песался от канала ")


@bot.message_handler(commands=["ban"])
def ban_user(message):
    if message.reply_to_message:
        chat_id = message.chat.id
        user_id = message.reply_to_member.from_user.id
        user_status = bot.get_chat_member(chat_id, user_id).status
        if user_status == "administratator" or user_status == "creator":
            bot.reply_to(message, "ban пользоватяля")
    else:
        bot.ban_chat_member(chat_id, user_id)
        bot.reply_to(
            message,
            f"Пользователь {message.reply_to_message.from_user.username} был забанен.",
        )


@bot.message_handler(commands=["online bot"])
def online_bot(message):
    if message.reply_to_message:
        chat_id = message.id

        uers_id = message.reply_to_message.from_user.id

        user_status = bot.get_chat_member(chat_id, user_id).status

        if user_status == "administrator" or user_status == "creator":
            bot.reply_to(message, "Невозможно отслидить бота.")
    else:
        duration = 60

    args = message.text.split()[1:]
    if args:
        try:
            duration = int(args[0])
        except ValueError:
            bot.reply_to(message, "Неправильное время ")


def send_pics(update, context):
    with multiprocessing.Pool:
        results = pool.map(get_last_block_once, list_of_public_nodes)
    last_blocks = [b for b in results if b is not None and isinstance(b, int)]

    med_val = int(np.median(last_blocks))
    max_val = int(np.max(last_blocks))

    med_support = np.sum([1 for x in last_blocks if x == med_val])
    max_support = np.sum([1 for x in last_blocks if x == max_val])

    return max_val, max_support, med_val, med_support


@bot.message_handler(commands=["unmute"])
def unmute_user(message):
    if message.reply_to_message:
        chat_id = message.chai.id
        user_id = message.reply_to_message.from_user.id
        bot.restrict_chat_member(
            chat_id,
            user_id,
            can_send_messages=True,
            can_send_media_messages=True,
            can_send_other_messages=True,
            can_add_web_page_previews=True,
        )
        bot.reply_to(
            message,
            f"Пользователь {message.reply_to_message.from_user.username} размучен.",
        )
    else:
        bot.reply_to(
            message,
            "Эта команда должна быть использована в ответ на сообщение пользователя, которого вы хотите размутить.",
        )


@bot.message_handler(["channel"])
def user_status(message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    username = message.from_user.username
    if stats:
        bot.reply_to(message, "Статистика пуста.")
    else:
        if user_id not in stats[chat_id]["users"]:
            bot.replt_to(message, "Вы еще не отправляли сообщений.")
        else:
            user_messages = stats[chat_id]["users"][user_id]["messages"]
            total_messages = stats[chat_id]["total_messaes"]
            percentage = round(user_messages / total_messages * 100, 2)
            bot.reply_to(
                message,
                f"Статистика для пользователя @{username}:\nВсего сообщений: {user_messages}\nПроцент от общего количества сообщений: {percentage}%",
            )


bad_words = ["анкета", "ссылка", "уникальное предложение"]


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)


@bot.message_handler()
def function_name(message):
    bot.reply_to(message, "This is a message handler")


@bot.message_handler(
    func=lambda message: message.document.mime_type == "text/plan",
    content_types=["document"],
)
def handle_text_doc(message):
    pass


def test_message(message):
    return message.document.mime_type == "text/plan"


@bot.message_handler(func=test_message, content_types=["document"])
def handler_text_doc(message):
    pass


@bot.message_handler(commands=["hello"])
@bot.message_handler(func=lambda msg: msg.text.encode("utf-8") == SOME_FANCY_EMOJI)
def send_something(message):
    pass


@bot.inline_handler(lambda query: query.query == "text")
def query_text(inline_query):
    @bot.inline_handler(lambda query: query.query == "text")
    def query_text(inline_query):
        try:
            r = types.InliQueryResultArticle(
                "1", "Result", types.InputTextMessageContent("Result message.")
            )
            r2 = types.InliQueryResultArticle(
                "2", "Result2", types.InputTextMessageContent("Result message2")
            )
            bot.answer_inline_query(inline_query_id, [r, r2])
        except Exception as e:
            print(e)


def modify_message(bot_instance, message):
    message.anther_text = message.text + ":changer"


@bot.message_handler(commands=["start"])
def start(message):
    assert message.another_text == message.text + ":changer"


bot.polling()


class Middleeware(BaseException):
    def __init__(self):
        self.update_types = ["message"]


async def main():
    async with Client("my_account", api_id, api_hash) as app:
        await app.send_message("me", "Greetings from **Pyrogram**!")


asyncio.run(main())
