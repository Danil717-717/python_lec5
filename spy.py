from bdb import effective
from telegram import Update
from telegram.ext import Updater, ApplicationBuilder, CommandHandler, ContextTypes

async def log(update: Update, context: CommandHandler):
    file = open('db.csv', 'a')
    file.write(f'{update.effective_user.first_name}, {update.effective_user.id}, {update.message.text}\n')
    file.close()