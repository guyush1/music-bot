from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ConversationHandler, CallbackContext

import db.db_handler as db_handler

ALBUM_NAME, IS_PRIVATE, IS_PRIVATE_QUERY = range(3)


def add_album_command(update: Update, context: CallbackContext):
    update.message.reply_text("מהו השם של האומן?")
    return ALBUM_NAME


def get_album_name(update: Update, context: CallbackContext):
    context.user_data["artist_name"] = update.message.text
    update.message.reply_text("מהו השם של האלבום?")
    return IS_PRIVATE


def get_is_private(update: Update, context: CallbackContext):
    context.user_data["album_name"] = update.message.text
    keyboard = [
                    [
                        InlineKeyboardButton("כן", callback_data=int(True)),
                        InlineKeyboardButton("לא", callback_data=int(False))
                    ],
                ]
    is_private_question = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("האם אתה רוצה שהאלבום יהיה פרטי (ימוקם בתקייה נפרדת)", reply_markup=is_private_question)
    return IS_PRIVATE_QUERY


def get_is_private_query(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    context.user_data["is_private"] = query.data

    # Add the album to the album db
    success = db_handler.DBHandler.add_album(context.user_data["album_name"],
                                             context.user_data["artist_name"],
                                             context.user_data["is_private"])
    if success:
        context.bot.send_message(chat_id=update.effective_chat.id, text="האלבום הוכנס בהצלחה!")
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="הפעולה לא הצליחה :(")

    return ConversationHandler.END
