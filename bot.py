
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import Filters
from settings import TG_TOKEN,TG_API_URL


def sms(bot, update):
    print('Кто-то меня трогает ааа')
    bot.message.reply_text('Что вам нужно, {}!?'.format(bot.message.chat.first_name))
    #print(bot.message) #узнать ответ бота

def parrot(bot, update):
        print(bot.message.text)
        bot.message.reply_text(bot.message.text)
        # print(bot.message) #узнать ответ бота

def main():
    my_bot = Updater(TG_TOKEN,TG_API_URL, use_context=True)

    my_bot.dispatcher.add_handler(CommandHandler('start', sms))
    my_bot.dispatcher.add_handler(MessageHandler(Filters.text, parrot))

    my_bot.start_polling()
    my_bot.idle()

main()