#!/bin/env python3

import logging

from telegram.ext import *
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update

import db.db_handler as db_handler

from telegram_bot.API_KEY import API_KEY
import telegram_bot.Commands.add_song_commands as song_command
import telegram_bot.Commands.add_album_commands as album_command
import telegram_bot.Commands.basic_commands as basic_commands


def init_bot(updater: Updater):
    bot_dispatcher = updater.dispatcher

    # Add the basic commands
    bot_dispatcher.add_handler(CommandHandler("start", basic_commands.start_command))
    bot_dispatcher.add_handler(CommandHandler("help", basic_commands.help_command))

    # Add error handling
    bot_dispatcher.add_error_handler(basic_commands.error)
    
    # Add the conversation commands (addsong and addalbum)
    bot_dispatcher.add_handler(ConversationHandler(
        entry_points=[CommandHandler("addsong", song_command.add_song_command)],
        states={
                song_command.SONG_NAME:                 [MessageHandler((Filters.text &  ~ Filters.command), song_command.get_song_name)],
                song_command.IS_PRIVATE:                [MessageHandler((Filters.text &  ~ Filters.command), song_command.get_is_private)],
                song_command.IS_PRIVATE_QUERY:          [CallbackQueryHandler(song_command.get_is_private_query)],
            },
        fallbacks=[CommandHandler("cancel", basic_commands.cancel_command)]))
    
    bot_dispatcher.add_handler(ConversationHandler(
        entry_points=[CommandHandler("addalbum", album_command.add_album_command)],
        states={
                album_command.ALBUM_NAME:                       [MessageHandler((Filters.text &  ~ Filters.command), album_command.get_album_name)],
                album_command.IS_PRIVATE:                       [MessageHandler((Filters.text &  ~ Filters.command), album_command.get_is_private)],
                album_command.IS_PRIVATE_QUERY:                 [CallbackQueryHandler(album_command.get_is_private_query)],
            },
        fallbacks=[CommandHandler("cancel", basic_commands.cancel_command)]))

    # Poll and block
    updater.start_polling(0.5)
    updater.idle()


def main():
    logging.getLogger().setLevel(logging.ERROR)
    print("Bot initializing!\n")

    # Initalize the db using the one time used "init"
    db_handler.DBHandler()

    updater = Updater(API_KEY, use_context=True)
    init_bot(updater)


if __name__ == "__main__":
    main()
