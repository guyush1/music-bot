from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ConversationHandler, CallbackContext

import db.db_handler as db_handler

SONG_NAME, IS_PRIVATE, IS_PRIVATE_QUERY = range(3)

def add_song_command(update: Update, context: CallbackContext):
    update.message.reply_text("מהו השם של האומן?")
    return SONG_NAME

def get_song_name(update: Update, context: CallbackContext):
    context.user_data["artist_name"] = update.message.text
    update.message.reply_text("מה השם של השיר?")
    return IS_PRIVATE

def get_is_private(update: Update, context: CallbackContext):
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
    success = db_handler.DBHandler.add_song(context.user_data["song_name"],
                                            context.user_data["artist_name"],
                                            context.user_data["is_private"])
    if success:
        context.bot.send_message(chat_id=update.effective_chat.id, text="השיר הוכנס בהצלחה!")
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="הפעולה לא הצליחה :(")

    return ConversationHandler.END
