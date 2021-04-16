from telegram.ext import *


def start_command(update, context):
    update.message.reply_text("Welcome to my music bot, use the help command for more info :)")


def help_command(update, context):
    update.message.reply_text("Add a song/album using the /addsong or /addalbum command")


def cancel_command(update, context):
    update.message.reply_text("Command canceled")
    return ConversationHandler.END


def error(update, context):
    print("Update ", update, "caused error")