import os
from telegram.ext import Updater, CommandHandler


def startBot(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")


TOKEN = <token>
PORT = int(os.environ.get('PORT', '8443'))
updater = Updater(TOKEN)
dispatcher = updater.dispatcher
start_handler = CommandHandler('start', startBot)
dispatcher.add_handler(start_handler)

updater.start_webhook(listen="0.0.0.0",
                      port=PORT,
                      url_path=TOKEN)
updater.bot.set_webhook("https://<app>.herokuapp.com/" + TOKEN)
updater.idle()
