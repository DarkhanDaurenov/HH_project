from src.hhabc import (HeadHunterAPI)
from src.vacancyHh import Vacancy

def user_interaction():
    hh_api = HeadHunterAPI()
    search_query = input("Введите поисковый запрос: ")
    hh_vacancies = hh_api.get_vacancies(search_query)
    vacancies_list = [Vacancy(vacancy['name'], vacancy['alternate_url'], vacancy['salary'], vacancy['snippet']) for
                      vacancy in hh_vacancies]

    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    sorted_vacancies = sorted(vacancies_list, reverse=True)
    top_vacancies = sorted_vacancies[:top_n]
    for vacancy in top_vacancies:
        print(vacancy.title, vacancy.salary)


if __name__ == "__main__":
    user_interaction()