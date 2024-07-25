from src.classes.DBManager import DBManager
from src.create_table import connect_and_create_table


def main():
    db = DBManager()
    connect_and_create_table()
    # Словарь с методами для вызова в зависимости от выбора пользователя
    dict_for_user_input = {
        1: db.get_companies_and_vacancies_count,
        2: db.get_all_vacancies,
        3: db.get_avg_salary,
        4: db.get_vacancies_with_higher_salary,
        5: lambda: db.get_vacancies_with_keyword(input("Введите ключевое слово: "))
    }
    print(f"Выбери фильтрацию которая тебя интересует:\n"
          f"1: Получает список всех компаний и количество вакансий у каждой компании.\n"
          f"2: Получает список всех вакансий с указанием названия компании,"
          f"названия вакансии и зарплаты и ссылки на вакансию.\n"
          f"3: Получает среднюю зарплату по вакансиям.\n"
          f"4: Получает список всех вакансий,"
          f"у которых зарплата выше средней по всем вакансиям.\n"
          f"5: Получает список всех вакансий,"
          f"в названии которых содержатся переданные в метод слова,"
          f"например python.\n")

    user_input = int(input('->'))

    # Получение метода по выбору пользователя и выполнение
    if user_input in dict_for_user_input:
        method = dict_for_user_input[user_input]
        result = method()
        return result
    else:
        print("Некорректный ввод. Пожалуйста, выберите номер от 1 до 5.")


if __name__ == '__main__':
    main()
