from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ConversationHandler, CallbackContext

import db.db_handler as db_handler

ALBUM_NAME, IS_PRIVATE, IS_PRIVATE_QUERY = range(3)


def add_album_command(update: Update, context: CallbackContext):
    update.message.reply_text("What is the name of the artist?")
    return ALBUM_NAME


def get_album_name(update: Update, context: CallbackContext):
    context.user_data["artist_name"] = update.message.text
    update.message.reply_text("What is the album's name?")
    return IS_PRIVATE


def is_private(update: Update, context: CallbackContext):
    context.user_data["album_name"] = update.message.text
    keyboard = [
                    [
                        InlineKeyboardButton("yes", callback_data=int(True)),
                        InlineKeyboardButton("no", callback_data=int(False))
                    ],
                ]
    is_private_question = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("Do you want the album to be private? (will be placed in the private folder)", reply_markup=is_private_question)
    return IS_PRIVATE_QUERY


def get_is_private_query(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    context.user_data["is_private"] = query.data

    # Add the album to the album db
    db_handler.DBHandler().add_album(context.user_data["album_name"],
                                     context.user_data["artist_name"],
                                     context.user_data["is_private"])

    return ConversationHandler.END
