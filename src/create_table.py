import psycopg2

from src.config import config
from src.settings import CREATE_TABLES
from src.writing_data_to_table import insert_data_employers, insert_data_vacancies


def apply_table_schema(cursor):
    """Применяет схему таблиц к базе данных"""
    # Читаем содержимое файла create_tables.sql
    with open(CREATE_TABLES, 'r') as file:
        sql_query = file.read()
    # выполнить SQL-запрос из файла
    cursor.execute(sql_query)
    print('Таблицы созданы')


def connect_and_create_table():
    """
    Устанавливает соединение с базой данных, создает таблицы и вставляет данные.

    Эта функция выполняет следующие действия:
    1. Устанавливает соединение с базой данных с использованием параметров, полученных из функции `config`.
    2. Выполняет SQL-запросы для создания таблиц и вставки данных в них.
    3. Фиксирует изменения в базе данных и закрывает соединение.
    """
    conn = None
    try:
        # Получаем параметры соединения
        params = config()
        # Устанавливаем соединение с базой данных
        conn = psycopg2.connect(**params)
        print('Успешный коннект')
        # Выполняем SQL-запросы
        try:
            with conn.cursor() as cursor:
                # Создание таблицы
                apply_table_schema(cursor)
                print('Таблицы успешно созданы')
                insert_data_employers(cursor)
                print('Данные о компании успешно записаны')
                insert_data_vacancies(cursor)
                print('Данные о вакансиях успешно записаны')
                conn.commit()  # Фиксируем изменения в базе данных
        except Exception as ex:
            print('Ошибка выполнения SQL-запросов')
            print(ex)
    except Exception as ex:
        print('Нет соединения')
        print(ex)
    finally:
        if conn is not None:
            conn.close()
            print('Соединение закрыто')
