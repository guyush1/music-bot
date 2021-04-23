import db.db_queries as db_queries
import sqlite3
from typing import Union


def initialize_db():
    """
    function creates the required db file and tables if needed.
    """
    print("DB initializing\n")

    # Create a global variable for accessing the db
    global db_con

    # Create the db file
    db_con = sqlite3.connect(db_queries.DB_NAME)

    # Create the tables if they don't exist
    create_table_if_needed(db_queries.SQL_CREATE_SONGS_TABLE)
    create_table_if_needed(db_queries.SQL_CREATE_ALBUMS_TABLE)


def create_table_if_needed(sql_query):
    """
    Creates a new sql table from a sql_query if it doesnt exist

    :param con: Our connection to the db
    :param sql_query: the query to creating the sqlLite table
    """
    try:
        c = db_con.cursor()
        c.execute(sql_query)
    except sqlite3.Error as err:
        print(err)


def get_song_name(song_name: str, song_album_name: Union[str, None], is_private: bool):
    """
    Adds a song to the db.

    :param db_con: The connection to the db
    :param song_name: The name of the song we are adding
    :param song_album_name: The name of the album the song is related to, None if it is a single
    :param is_private: indicated whether the song is public or private
    """
    try:
        c = db_con.cursor()
        c.execute(db_queries.SQL_ADD_SONG,
                  # Parameters as a tuple
                  (song_name, "" if not song_album_name else song_album_name, int(is_private), int(False)))
        db_con.commit()
    except sqlite3.Error as err:
        print(err)


def add_album(album_name: str, is_private: bool):
    """
    Adds an album to the db.

    :param db_con: The connection to the db
    :param album_name: The name of the album we are adding
    :param is_private:  indicated whether the song is public or private
    """
    try:
        c = db_con.cursor()
        c.execute(db_queries.SQL_ADD_ALBUM,
                  # Parameters as a tuple
                  (album_name, int(is_private), int(False)))
        db_con.commit()
    except sqlite3.Error as err:
        print(err)
