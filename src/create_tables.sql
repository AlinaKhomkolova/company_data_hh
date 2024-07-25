-- Удаление таблиц, если они существуют
DROP TABLE IF EXISTS vacancies;
DROP TABLE IF EXISTS employers;
-- Создание таблицы employers
CREATE TABLE employers
(
    employer_id serial PRIMARY KEY,
    name varchar NOT NULL,
    site_url varchar,
    employer_url varchar,
    area_name varchar,
    open_vacancies integer
);
-- Создание таблицы vacancies
CREATE TABLE vacancies
(
    vacancies_id serial PRIMARY KEY,
    employer_id integer NOT NULL,
    name varchar NOT NULL,
    area varchar,
    salary_from integer,
    salary_to integer,
    salary_currency varchar(10),
    experience varchar,
    published_at varchar,
    alternate_url varchar,
    FOREIGN KEY (employer_id) REFERENCES employers (employer_id)
);
