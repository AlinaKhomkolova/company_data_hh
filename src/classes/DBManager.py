import psycopg2

from src.config import config


class DBManager:

    def __init__(self):
        self.params = config()

    def _connect(self):
        """Устанавливает соединение с базой данных"""
        return psycopg2.connect(**self.params)

    def _execute_query(self, query: str, params: None):
        """Выполняет запрос и возвращает результаты"""
        try:
            with self._connect() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(query, params)
                    return cursor.fetchall()
        except psycopg2.Error as e:
            print("Ошибка при выполнении запроса:", e)
            return []

    def get_companies_and_vacancies_count(self):
        """Получает список всех компаний и количество вакансий у каждой компании"""
        query = """
        SELECT e.name AS employer_name,
               COUNT(v.vacancies_id) AS vacancy_count
        FROM employers e
        LEFT JOIN vacancies v ON e.employer_id = v.employer_id
        GROUP BY e.name;
        """
        results = self._execute_query(query, params=self._connect())
        # Возвращаем список словарей с результатами
        for row in results:
            print({'employer_name': row[0], 'vacancy_count': row[1]})

    def get_all_vacancies(self):
        """
        Получает список всех вакансий с указанием названия компании,
        названия вакансии и зарплаты и ссылки на вакансию
        """
        query = """
                SELECT e.name AS employer_name,
                v.name AS vacancy_name,
                v.salary_from,
                v.salary_to,
                v.alternate_url
                FROM vacancies v
                JOIN employers e ON e.employer_id = v.employer_id;
                """
        results = self._execute_query(query, params=self._connect())
        # Возвращаем список словарей с результатами
        for row in results:
            print({'employer_name': row[0], 'vacancy_name': row[1],
                   'salary_from': row[2], 'salary_to': row[3],
                   'alternate_url': row[4]
                   })

    def get_avg_salary(self):
        """Получает среднюю зарплату по вакансиям"""
        query = """
        SELECT CAST(AVG(salary_from) AS DECIMAL(10,2))
        FROM vacancies
        """

        result = self._execute_query(query, params=self._connect())
        avg_salary = result[0][0]
        print({'Average salary': float(avg_salary)})

    def get_vacancies_with_higher_salary(self):
        """
        Получает список всех вакансий,
        у которых зарплата выше средней по всем вакансиям
        """
        query = """
                WITH avg_salary AS (
                SELECT AVG(salary_from) AS avg_salary
                FROM vacancies
                )
                SELECT v.name AS name_vacancy
                FROM vacancies v, avg_salary
                WHERE v.salary_from > avg_salary.avg_salary;
                """
        result = self._execute_query(query, params=self._connect())
        for row in result:
            print({"vacancies_higher_average_salaries": row})

    def get_vacancies_with_keyword(self, keyword):
        """
        Получает список всех вакансий,
        в названии которых содержатся переданные в метод слова,
        например python.
        """
        query = """
                SELECT e.name AS employer_name, v.name AS vacancy_name, v.salary_from, v.salary_to, v.alternate_url
                FROM vacancies v
                JOIN employers e ON v.employer_id = e.employer_id
                WHERE v.name ILIKE %s;
                """
        results = self._execute_query(query, (f'%{keyword}%',))
        for row in results:
            print({'Vacancy': row})
