from telegram import Update
from telegram.ext import CallbackContext, ConversationHandler

import logging


def start_command(update: Update, context: CallbackContext):
    update.message.reply_text("Welcome to my music bot, use the help command for more info :)")


def help_command(update: Update, context: CallbackContext):
    update.message.reply_text("Add a song/album using the /addsong or /addalbum command")


def cancel_command(update: Update, context: CallbackContext):
    update.message.reply_text("Command canceled")
    return ConversationHandler.END


def error(update: Update, context: CallbackContext):
    logging.error("error is : {}".format(context.error))