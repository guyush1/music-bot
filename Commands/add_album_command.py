from telegram.ext import ConversationHandler

ADD_ALBUM = range(1)

def add_album_command(update, context):
    update.message.reply_text("Write the name of the album")
    return ADD_ALBUM


def add_album(update, context):
    print("adding album: ", update.message.text)
    return ConversationHandler.END
    # TODO: make it work with SQLite
