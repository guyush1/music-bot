from os import stat
import db.db_queries as db_queries
import sqlite3

class DBHandler():
    """
    Class responsible handling database related operations.
    This class is defined as a singleton to maintain one instance of db handling.
    """

    def __init__(self):
        """
        function creates the required db file and tables if needed.
        """
        print("DB initializing\n")

        # Create the tables if they don't exist
        self.create_table_if_needed()

    def create_table_if_needed(self):
        """
        Creates a new sql table from a sql_query if it doesnt exist

        :param con: Our connection to the db
        :param sql_query: the query to creating the sqlLite table
        """
        try:
            with sqlite3.connect(db_queries.DB_NAME) as db_con:
                c = db_con.cursor()
                c.execute(db_queries.SQL_CREATE_SONGS_TABLE)
                c.execute(db_queries.SQL_CREATE_ALBUMS_TABLE)
        except sqlite3.Error as err:
            print(err)
            # Exit, the bot can't start.
            exit(1)

    @staticmethod
    def add_song(song_name: str, artist_name: str, song_album_name: str, is_private: bool):
        """
        Adds a song to the db.

        :param db_con: The connection to the db
        :param song_name: The name of the song we are adding
        :param song_album_name: The name of the album the song is related to, None if it is a single
        :param is_private: indicated whether the song is public or private
        """
        try:
            with sqlite3.connect(db_queries.DB_NAME) as db_con:
                c = db_con.cursor()
                c.execute(db_queries.SQL_ADD_SONG,
                        # Parameters as a tuple
                        (song_name, artist_name, song_album_name, int(is_private), int(False)))
        except sqlite3.Error as err:
            print(err)
            return False
        return True

    @staticmethod
    def add_album(album_name: str, artist_name: str, is_private: bool):
        """
        Adds an album to the db.

        :param db_con: The connection to the db
        :param album_name: The name of the album we are adding
        :param is_private:  indicated whether the song is public or private
        """
        try:
            with sqlite3.connect(db_queries.DB_NAME) as db_con:
                c = db_con.cursor()
                c.execute(db_queries.SQL_ADD_ALBUM,
                        # Parameters as a tuple
                        (album_name, artist_name, int(is_private), int(False)))
        except sqlite3.Error as err:
            print(err)
            return False
        return True
