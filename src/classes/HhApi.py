import requests

from src.config import formatting_date


class HhApi:
    def __init__(self):
        # Идентификаторы компаний, которые я выбрала
        self.employer_ids = ['2791002', '3529', '6067730', '2625279',
                             '916364', '10413982', '2254473',
                             '658279', '9329536', '1282414']
        # Заголовки запросов.
        self.__headers = {'User-Agent': 'HH-User-Agent'}
        # Параметры запроса
        self.__params = {
            'page': 0,
            'per_page': 20,
            'only_with_vacancies': True
        }

    def request_info(self, url: str, employer_id: str) -> list:
        """Выполняет HTTP-запрос для получения информации по-указанному URL."""
        try:
            # Выполнение GET-запроса к указанному URL
            response = requests.get(url, params=self.__params, headers=self.__headers)
            # Проверка на успешность ответа (статус-код 200)
            response.raise_for_status()
            # Возвращаем данные в формате JSON
            return response.json()
        # В случае ошибки выводим сообщение
        except requests.exceptions.RequestException as e:
            print(f'Ошибка при получении данных о компании {employer_id}: {e}')

    def get_company_info(self, employer_id: str):
        """Извлекает список компаний из API"""
        url = f"https://api.hh.ru/employers/{employer_id}"
        return self.request_info(url, employer_id)

    def get_vacancies_info(self, employer_id: str) -> list:
        """Извлекает список вакансий у компаний по API """
        url = f'https://api.hh.ru/vacancies?employer_id={employer_id}'
        return self.request_info(url, employer_id)['items']

    def get_multiple_vacancies_info(self) -> list:
        """Получает информацию о вакансиях для всех заданных работодателей."""
        vacancies = []  # Инициализация списка для хранения информации о вакансиях
        for employer_id in self.employer_ids:
            # Получение информации о вакансиях для текущего работодателя
            vacancy_info = self.get_vacancies_info(employer_id)

            # Если информация о вакансиях была успешно получена, добавляем её в список
            if vacancy_info:
                vacancies.append(vacancy_info)

        return vacancies

    def get_multiple_companies_info(self) -> list:
        """Получает информацию о нескольких компаниях на основе их идентификаторов"""
        companies_info = []
        for employer_id in self.employer_ids:
            # Получение информации о компании для текущего работодателя
            company_info = self.get_company_info(employer_id)

            # Если информация о компании была успешно получена, добавляем её в список
            if company_info:
                companies_info.append(company_info)

        return companies_info

    def create_vacancy_from_item(self) -> list:
        """Создает список вакансий из данных, полученных от разных компаний"""
        data = self.get_multiple_vacancies_info()  # Получение данных о вакансиях
        vacancies = []

        for sublist in data:
            for item in sublist:
                salary = item.get('salary', {})
                if salary is None:
                    salary_from = None
                    salary_to = None
                    salary_currency = None
                else:
                    salary_from = salary.get('from')
                    salary_to = salary.get('to')
                    salary_currency = salary.get('currency')

                vacancies.append({
                    'vacancies_id': item.get('id'),
                    'employer_id': item.get('employer', {}).get('id'),
                    'name': item.get('name'),
                    'area': item.get('area', {}).get('name'),
                    'salary_from': salary_from,
                    'salary_to': salary_to,
                    'salary_currency': salary_currency,
                    'experience': item.get('experience', {}).get('name', None),
                    'published_at': formatting_date(item.get('published_at')),
                    'alternate_url': item.get('alternate_url')
                })

        return vacancies
