from abc import ABC, abstractmethod
import requests

class AbstractVacancyAPI(ABC):
    @abstractmethod
    def get_vacancies(self, search_query):
        pass

class HeadHunterAPI(AbstractVacancyAPI):
    def get_vacancies(self, search_query):
        response = requests.get(f"https://api.hh.ru/vacancies?text={search_query}")
        if response.status_code == 200:
            return response.json()['items']
        else:
            return []

class Vacancy:
    def __init__(self, title, link, salary, description):
        self.title = title
        self.link = link
        self.salary = salary
        self.description = description


class AbstractFileSaver(ABC):
    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy):
        pass

    @abstractmethod
    def filter_vacancies(self, criteria):
        pass

