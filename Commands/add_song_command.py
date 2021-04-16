from telegram.ext import ConversationHandler

ADD_SONG = range(1)

def add_song_command(update, context):
    update.message.reply_text("Write the name of the song, enter /cancel to cancel the command")
    return ADD_SONG


def add_song(update, context):
    print("adding song: ", update.message.text)
    return ConversationHandler.END
    # TODO: make it work with SQLite
