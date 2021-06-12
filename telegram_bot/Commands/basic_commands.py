from telegram import Update
from telegram.ext import CallbackContext, ConversationHandler

import logging

def start_command(update: Update, context: CallbackContext):
    update.message.reply_text("ברוכים הבאים לבוט המוזיקה, השתמשו בפקודה /help למידע נוסף")

def help_command(update: Update, context: CallbackContext):
    update.message.reply_text("הוסף שיר/אלבום בעזרת הפקודות /addsong או /addalbum")

def cancel_command(update: Update, context: CallbackContext):
    update.message.reply_text("הפקודה בוטלה")
    return ConversationHandler.END

def error(update: Update, context: CallbackContext):
    logging.error("error is : {}".format(context.error))