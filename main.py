from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def hello (update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello  {update.effective_user.first_name}')


app = ApplicationBuilder().token("5614398079:AAHG5xeB3Tza3l1P0Y7vOVDPIKpK1huPglo").build()

app.add_handler(CommandHandler("hello", hello))
print("Server start")
app.run_polling()