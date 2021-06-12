DB_NAME = "db/musicDB.db"

SQL_CREATE_SONGS_TABLE = """ CREATE TABLE IF NOT EXISTS songs (
                                artist_name text,
                                song_name text,
                                is_private int,
                                album_name text,
                                added_to_sd int,
                                PRIMARY KEY (artist_name, song_name)
                            ); """

SQL_CREATE_ALBUMS_TABLE = """ CREATE TABLE IF NOT EXISTS albums (
                                artist_name text ,
                                album_name text,
                                is_private int,
                                added_to_sd int,
                                PRIMARY KEY (artist_name, album_name)
                            ); """

SQL_ADD_SONG = """ INSERT OR IGNORE INTO songs (song_name, artist_name, album_name, is_private, added_to_sd)
                   VALUES(?,?,?,?,?) """

SQL_ADD_ALBUM = """ INSERT OR IGNORE INTO albums (album_name, artist_name, is_private, added_to_sd)
                    VALUES(?,?,?,?) """

