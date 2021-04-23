DB_NAME = "db/musicDB.db"

SQL_CREATE_SONGS_TABLE = """ CREATE TABLE IF NOT EXISTS songs (
                                song_name text PRIMARY KEY,
                                is_private int,
                                album_name text,
                                added_to_sd int
                            ); """

SQL_CREATE_ALBUMS_TABLE = """ CREATE TABLE IF NOT EXISTS albums (
                                album_name text PRIMARY KEY,
                                is_private int,
                                added_to_sd int
                            ); """

SQL_ADD_SONG = """ INSERT INTO songs (song_name, album_name, is_private, added_to_sd)
                   VALUES(?,?,?,?) """

SQL_ADD_ALBUM = """ INSERT INTO albums (album_name, is_private, added_to_sd)
                    VALUES(?,?,?) """

