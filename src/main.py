from src.hhabc import HeadHunterAPI
from src.vacancyHh import Vacancy, JSONSaver
from typing import List


def user_interaction() -> None:
    """Функция для взаимодействия с пользователем."""
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

    # Сохранение вакансий в JSON файл
    json_saver = JSONSaver()
    for vacancy in vacancies_list:
        json_saver.add_vacancy(vars(vacancy))

    # Фильтрация вакансий
    filter_criteria = input("Введите критерий для фильтрации вакансий: ")
    filtered_vacancies = json_saver.filter_vacancies(filter_criteria)
    print("Фильтрованные вакансии:")
    for vacancy in filtered_vacancies:
        print(vacancy)


if __name__ == "__main__":
    user_interaction()