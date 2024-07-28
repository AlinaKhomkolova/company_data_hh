from configparser import ConfigParser
from datetime import datetime

from src.settings import DATABASE_INI


def config(filename=DATABASE_INI, section='postgresql') -> dict:
    """Подключение к базе данных"""
    # Создание Parser
    parser = ConfigParser()
    # Чтение database файла
    parser.read(filename)
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception(
            'Раздел {0} не найден в {1} файле'.format(section, filename)
        )
    return db


def formatting_date(published_at) -> str:
    """Форматирует дату публикации вакансии."""
    date = datetime.strptime(published_at, '%Y-%m-%dT%H:%M:%S%z')
    return f'{date:%d.%m.%Y}'
