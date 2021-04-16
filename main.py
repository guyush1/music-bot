from telegram.ext import *

from API_KEY import API_KEY
import Commands.add_song_command as song_command 
import Commands.add_album_command as album_command
import Commands.basic_commands as basic_commands

print("Bot initializing")

def main():
    updater = Updater(API_KEY, use_context=True)
    dp = updater.dispatcher

    # Add the basic commands
    dp.add_handler(CommandHandler("start", basic_commands.start_command))
    dp.add_handler(CommandHandler("help", basic_commands.help_command))

    # Add error handling
    dp.add_error_handler(basic_commands.error)

    # Add the conversation commands (addsong and addalbum)
    dp.add_handler(ConversationHandler(
        entry_points=[CommandHandler("addsong", song_command.add_song_command)],
        states={song_command.ADD_SONG: [MessageHandler((Filters.text &  ~ Filters.command), song_command.add_song)]},
        fallbacks=[CommandHandler("cancel", basic_commands.cancel_command)]))
    
    dp.add_handler(ConversationHandler(
        entry_points=[CommandHandler("addalbum", album_command.add_album_command)],
        states={album_command.ADD_ALBUM: [MessageHandler((Filters.text &  ~ Filters.command), album_command.add_album)]},
        fallbacks=[CommandHandler("cancel", basic_commands.cancel_command)]))

    # Poll and block
    updater.start_polling(0.5)
    updater.idle()

if __name__ == "__main__":
    main()