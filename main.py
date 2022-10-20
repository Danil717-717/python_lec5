from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_command import*

app = ApplicationBuilder().token("5614398079:AAHG5xeB3Tza3l1P0Y7vOVDPIKpK1huPglo").build()

app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("sum", sum_command))

print("Server start")
app.run_polling()