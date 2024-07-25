## Курсовой проект по теме «API, библиотека requests, SQL»

[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![SQL](https://img.shields.io/badge/-SQL-464646?style=flat-square&logo=SQL)](https://www.w3schools.com/sql/)
[![Requests](https://img.shields.io/badge/-Requests-464646?style=flat-square&logo=Requests)](https://pypi.org/project/requests/)

### Технологии:

- Python 3.10.12
- psycopg2-binary==2.9.9
- requests 2.32.3

### Задание

В рамках проекта было необходимо получить данные о компаниях и вакансиях с сайта `https://hh.ru/`,
спроектировать таблицы в БД PostgreSQL и загрузить полученные данные в созданные таблицы.

### Критерии выполнения курсовой работы:

- Проект выложен на GitHub.
- Оформлен файл README.md с информацией, о чем проект, как его запустить и как с ним работать.
- Есть Python-модуль для создания и заполнения данными таблиц БД.

### Инструкция для развертывания проекта:

#### Клонирование проекта:

```bash
git clone git@github.com:AlinaKhomkolova/company_data_hh.git
```

#### Создать виртуальное окружение:

```bash
python3 -m venv venv
```

#### Активировать виртуальное окружение:

Для Linux

```bash
source venv/bin/activate
```

Для Windows

```bash
venv\Scripts\activate.bat
```

#### Установить зависимости:

```bash
pip install -r requirements.txt
```

#### Открыть проект в PyCharm.

### Запуск программы

- Запустите файл main.py.

```bash
python3 main.py
```

Автор проекта Хомколова Алина