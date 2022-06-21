import sqlalchemy
import json
import time
import random

def open_file():
    with open('musics.json', 'r', encoding='utf8') as data_file:
        data = json.loads(data_file.read().strip())
    return data

def insert_requests(table_name):
    engine = sqlalchemy.create_engine('postgresql://postgres:admin@localhost:5432/test1')
    connection = engine.connect()
    data = open_file()
    table = table_name
    i = 0
    if table in data and type(data[table]) == list:
        while i < len(data[table]):
            item = data[table][i]
            connection.execute(
                f"""
                INSERT INTO {table} (name)
                    VALUES ('{item}');
                """)
            print(f"""({i + 1}/{len(data[table])})""")
            time.sleep(0.5)
            i += 1
    if table in data and type(data[table]) == dict:
        for key, val in data[table].items():
            if type(val) == float:
                album_id = random.randrange(1, int(len(data['album']) + 1), 1)
                connection.execute(
                    f"""
                    INSERT INTO {table} (name, album_id, duration)
                        VALUES ('{key}', '{album_id}', '{val}');
                    """)
                print(f"""({i + 1}/{len(data[table])})""")
                time.sleep(0.5)
                i += 1
            if type(val) == int and len(str(val)) == 4:
                connection.execute(
                    f"""
                    INSERT INTO {table} (name, releaseyear)
                        VALUES ('{key}', '{val}');
                    """)
                print(f"""({i + 1}/{len(data[table])})""")
                time.sleep(0.5)
                i += 1
    if table == 'album_artist':
        i = 1
        while i <= len(data['album']):
            connection.execute(
                f"""
                INSERT INTO {table} (album_id, artist_id)
                    VALUES ('{i}', '{i}');
                """)
            time.sleep(0.5)
            print(f"{i}/{len(data['album'])}")
            i += 1
    if table == 'genre_artist':
        connection.execute(
            f"""
            INSERT INTO {table} (genre_id, artist_id)
                VALUES (3, 1), (4, 1), (5, 2), (1, 3), (2, 3), (4, 4), (5, 4), (6, 5), (6, 6), (3, 7), (2, 8), (1, 9);
            """)
    if table == 'compilation_track':
        i = 1
        while i <= len(data['track']):
            compilation_id = random.randrange(1, int(len(data['compilation']) + 1), 1)
            connection.execute(
                f"""
                INSERT INTO {table} (track_id, compilation_id)
                    VALUES ({i}, {compilation_id});
                """)
            print(f"{i}/{len(data['track'])}")
            time.sleep(0.5)
            i += 1
    print(f"""Запись данных в таблицу "{table}" завершена.""")


if __name__=='__main__':
    open_file()
    insert_requests('artist')
    insert_requests('genre')
    insert_requests('album')
    insert_requests('track')
    insert_requests('compilation')
    insert_requests('album_artist')
    insert_requests('genre_artist')
    insert_requests('compilation_track')


