import asyncio
from pyrogram import Client

api_id = "20368885"
api_hash = "1d499a8be7aad4553d3c2395829292c6"
bot = "8225602323:AAFF0R9Pju3jRaEuWC4n_jyj18VWdb-veZU"


bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start', 'help'])
def start_welcome(message):
    bot.reply_to(message, "Привет! Я бот для управления чатом. Напиши /help, чтобы узнать, что я умею.")




@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message, "")



def index(request):
    if request.method == "POST":
        update = telebot.types.Update.de_json(request.body.decode('utf-8'))


        bot.process_new_updates([update])


@bot.message_handler(commands=['teams'])
def teams_name(message):
    bot.reply_to(message, "вывод всех команнды что я магу")


@bot.message_handler(commands=['error'])
def error_name(message):
    bot.reply_to(message, "если я поламался на пишите моему папе об ошипке и прикрипете скрин тг для связи с нем @Bnder666")



@bot.message_handler(commands=['subscription'])
def subscription_name(message):
    bot.reply_to(message, "subscrription подписан на канал от песался от канала ")



@bot.message_handler(commands=['ban'])
def ban_user(message):
    if message.reply_to_message:

        chat_id = message.chat.id
        user_id = message.reply_to_member.from_user.id
        user_status = bot.get_chat_member(chat_id, user_id).status
        if user_status == 'administratator' or user_status == 'creator':
            bot.reply_to(message, "ban пользоватяля")
       else:
           bot.ban_chat_member(chat_id, user_id)
           bot.reply_to(message, f"Пользователь {message.reply_to_message.from_user.username} был забанен.")
      else:
          bot.reply_to(message, "Это команада должна быть использована в ответ на сообщение пользователя которого был за банен.")


@bot.message_handler(commands=['online bot'])
def online_bot(message):
    if message.reply_to_message:


        chat_id = message.id


        uers_id = message.reply_to_message.from_user.id


        user_status = bot.get_chat_member(chat_id, user_id).status


        if user_status == 'administrator' or user_status == 'creator':
            bot.reply_to(message, "Невозможно отслидить бота.")
       else:
           duration = 60


         args = message.text.split()[1:]
         if args:

             try:
                 duration = int(args[0])
           except ValuError:
                bot.reply_to(message, "")
                return
            if duration < 1:
                bot.reply_to(message, "Время должно быть положительным числом.")
                    return
                if duration > 1440:
                    bot.reply_to(message, "Максимальное время - 1 день.")
                    return
                bot.restrict_chat_member(chat_id, user_id, until_date=time.time() + duration * 60)
                bot.reply_to(message,f"Пользователь {message.reply_to_message.from_user.username} замучен на {duration} минут.")
    else:
        bot.reply_to(message,"Эта команда должна быть использована в ответ на сообщение пользователя, которого вы хотите замутить.")



def send_pics(update, context):
    with multiprocessing.Pool
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
        bot.restrict_chat_member(chat_id, user_id, can_send_messages=True, can_send_media_messages=True, can_send_other_messages=True, can_add_web_page_previews=True)
        bot.reply_to(message, f"Пользователь {message.reply_to_message.from_user.username} размучен.")
    else:
        bot.reply_to(message,"Эта команда должна быть использована в ответ на сообщение пользователя, которого вы хотите размутить.")



@bot.message_handler(['channel'])
def user_status(message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    username = message.from_user.username
    if stats:
        bot.reply_to(message, "Статистика пуста.")
    else:
        is user_id not in stats[chat_id]['users']:



          




    







async def main():
    async with Client("my_account", api_id, api_hash) as app:
        await app.send_message("me", "Greetings from **Pyrogram**!")

        

asyncio.run(main())
