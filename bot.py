from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CommandHandler

telegram_bot_token = "5635002243:AAGvx_tNLzicrf6m_fEER247mHXou4zy0GE"

updater = Updater(token=telegram_bot_token, use_context=True)
dispatcher = updater.dispatcher

# set up the introductory statement for the bot when the /start command is invoked
def start(update, context):
    chat_id = update.effective_chat.id
    context.bot.send_message(chat_id=chat_id, text="Hello, it's time to win or lose some money, using TON")

def echo(bot, update):
    update.message.reply_text(update.message.text)

# run the start function when the user invokes the /start command 
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(Filters.text, echo)


updater.start_polling()
