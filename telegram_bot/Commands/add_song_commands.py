from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ConversationHandler, CallbackContext

import db.db_handler as db_handler

IS_ALBUM, IS_ALBUM_QUERY, ALBUM_NAME, SONG_NAME, IS_PRIVATE_QUERY = range(5)


def add_song_command(update: Update, context: CallbackContext):
    update.message.reply_text("מהו השם של האומן?")
    return IS_ALBUM


def get_is_album(update: Update, context: CallbackContext):
    context.user_data["artist_name"] = update.message.text
    keyboard = [
                    [
                        InlineKeyboardButton("כן", callback_data="yes"),
                        InlineKeyboardButton("לא", callback_data="no")
                    ],
                ]
    is_album_question = InlineKeyboardMarkup(keyboard)

    update.message.reply_text("האם השיר הוא חלק מהאלבום?", reply_markup=is_album_question)
    return IS_ALBUM_QUERY


def get_is_album_query(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    if (query.data == "yes"):
        query.message.reply_text("מה השם של האלבום?")
        return ALBUM_NAME
    else:
        context.user_data["album_name"] = ""
        query.message.reply_text("מה השם של השיר?")
        return SONG_NAME


def get_album_name(update: Update, context: CallbackContext):
    context.user_data["album_name"] = update.message.text
    update.message.reply_text("מה השם של השיר?")
    return SONG_NAME


def get_song_name(update: Update, context: CallbackContext):
    context.user_data["song_name"] = update.message.text
    keyboard = [
                    [
                        InlineKeyboardButton("כן", callback_data=int(True)),
                        InlineKeyboardButton("לא", callback_data=int(False))
                    ],
                ]
    is_private_question = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("האם אתה רוצה שהשיר יהיה פרטי? (ימוקם בתקייה נפרדת)", reply_markup=is_private_question)
    return IS_PRIVATE_QUERY


def get_is_private_query(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    context.user_data["is_private"] = query.data

    # Add the song to the song db
    db_handler.DBHandler.add_song(context.user_data["song_name"],
                                  context.user_data["artist_name"],
                                  context.user_data["album_name"],
                                  context.user_data["is_private"])

    return ConversationHandler.END
