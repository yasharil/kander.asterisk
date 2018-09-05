import os
from telegram.ext import Updater, CommandHandler

TOKEN = '674274976:AAFpC8eZMhx9KwFGE0i8gfRkEFMbpcyPVjE'
PORT = int(os.environ.get('PORT', '8443'))
updater = Updater(TOKEN)
# add handlers
updater.start_webhook(listen="0.0.0.0",
                      port=PORT,
                      url_path=TOKEN)
updater.bot.set_webhook("https://quiet-stream-94228.herokuapp.com/" + TOKEN)
updater.idle()
