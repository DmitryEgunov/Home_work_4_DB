import sqlalchemy


def select_requests():
    # Запросы:
    # ------------------
    print('1 - название и год выхода альбомов, вышедших в 2018 году;')
    name_release_in_2018 = """
        SELECT name, releaseyear FROM album
            WHERE releaseyear IN ('2018')
    """
    print('2 - название и продолжительность самого длительного трека;')
    name_duration_max_len = """
            SELECT name, duration FROM track
                ORDER BY duration DESC
        """
    print('3 - название треков, продолжительность которых не менее 3,5 минуты;')
    track_name_up_to_3_50 = """
            SELECT name FROM track
                WHERE duration > 3.50
        """
    print('4 - названия сборников, вышедших в период с 2018 по 2020 год включительно;')
    name_compilation_2018_2020 = """
            SELECT name FROM compilation
                WHERE releaseyear BETWEEN 2018 AND 2020
        """
    print('5 - исполнители, чье имя состоит из 1 слова;')
    artist_name_one_word = """
            SELECT name FROM artist
                WHERE name NOT LIKE '%% %%'
        """
    print('6 - название треков, которые содержат слово "мой"/"my".')
    track_name_my = """
            SELECT name FROM track
                WHERE name LIKE '%%мой%%' OR name LIKE '%%my%%'
        """
    print('q - выход')

    # Меню выбора:
    # ------------------------
    while True:
        engine = sqlalchemy.create_engine('postgresql://postgres:admin@localhost:5432/test1')
        connection = engine.connect()
        num = input('Введите номер запроса :')
        if num == '1':
            res = connection.execute(
                f"""
                {name_release_in_2018}
                """).fetchall()
            print(res)
        if num == '2':
            res = connection.execute(
                f"""
                {name_duration_max_len}
                """).fetchall()
            print(res[0])
        if num == '3':
            res = connection.execute(
                f"""
                {track_name_up_to_3_50}
                """).fetchall()
            print(res)
        if num == '4':
            res = connection.execute(
                f"""
                {name_compilation_2018_2020}
                """).fetchall()
            print(res)
        if num == '5':
            res = connection.execute(
                f"""
                {artist_name_one_word}
                """).fetchall()
            print(res)
        if num == '6':
            res = connection.execute(
                f"""
                {track_name_my}
                """).fetchall()
            print(res)
        if num == 'q':
            break


if __name__=='__main__':
    select_requests()
