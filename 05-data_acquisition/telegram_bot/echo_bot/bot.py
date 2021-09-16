import logging
from flask import Flask, request
from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, Dispatcher

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

TOKEN = "1990780446:AAF9U12r7AfYUlELiz-JDO7QwR_txdfc0sA"

app = Flask(__name__)

@app.route('/')

def index():
	return "Hello!"

@app.route(f'/{TOKEN}', methods=['GET', 'POST'])
def webhook():
    update = Update.de_json(request.get_json(), bot)
    dp.process_update(update)
    return "ok"

logger = logging.getLogger(__name__)

def start(update: Update, context: CallbackContext):
    user = update.effective_user
    reply = "Hi {}\n\nType /help to see the features.".format(user.first_name)
    update.message.reply_text(reply)

def _help(update: Update, context: CallbackContext):
    update.message.reply_text("Sorry, I can't!")
    update.message.reply_text('JK\nThis is an Echo Bot!\n It echoes all your messages and stickers. \nGive it a try. \nTry sending a message or a sticker!')

def echo_text(update: Update, context: CallbackContext):
	print(update.message.text)
	update.message.reply_text(update.message.text)

def echo_sticker(update: Update, context: CallbackContext):
    update.message.reply_sticker(update.message.sticker)

if __name__ == '__main__':

    bot = Bot(TOKEN)
    bot.set_webhook(url="https://55dc-122-177-110-204.ngrok.io/{}".format(TOKEN))

    dp = Dispatcher(bot, None)
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", _help))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo_text))
    dp.add_handler(MessageHandler(Filters.sticker & ~Filters.command, echo_sticker))
    app.run(port=8443)