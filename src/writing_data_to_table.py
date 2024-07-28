from src.classes.HhApi import HhApi


def insert_data_employers(cursor):
    """Вставляет данные о компаниях в таблицу `employers`"""
    hh_api = HhApi()
    company_data = hh_api.get_multiple_companies_info()
    insert_query = """
    INSERT INTO employers(employer_id, name, 
    site_url, employer_url, area_name, open_vacancies)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    for item in company_data:
        cursor.execute(insert_query, (item['id'], item['name'],
                                      item['site_url'], item['alternate_url'],
                                      item['area']['name'], item['open_vacancies']))


def insert_data_vacancies(cursor):
    """Вставляет данные о вакансиях в таблицу `vacancies`"""
    hh_api = HhApi()
    vacancy = hh_api.create_vacancy_from_item()
    insert_query = """
    INSERT INTO vacancies(vacancies_id, employer_id, name, area,
    salary_from, salary_to, salary_currency,
    experience, published_at, alternate_url)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    for item in vacancy:
        cursor.execute(insert_query, (item['vacancies_id'], item['employer_id'],
                                      item['name'], item['area'],
                                      item['salary_from'], item['salary_to'],
                                      item['salary_currency'], item['experience'],
                                      item['published_at'], item['alternate_url']
                                      ))
