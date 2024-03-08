from abc import ABC, abstractmethod
from typing import List

import requests


class AbstractVacancyAPI(ABC):
    @abstractmethod
    def get_vacancies(self, search_query: str) -> List[dict]:
        """Абстрактный метод для получения вакансий."""
        pass


class HeadHunterAPI(AbstractVacancyAPI):
    def get_vacancies(self, search_query: str) -> List[dict]:
        """Метод для получения вакансий из API HeadHunter."""
        response = requests.get(f"https://api.hh.ru/vacancies?text={search_query}")
        if response.status_code == 200:
            return response.json()['items']
        else:
            return []


class AbstractFileSaver(ABC):
    @abstractmethod
    def add_vacancy(self, vacancy: dict) -> None:
        """Абстрактный метод для добавления вакансии."""
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy: dict) -> None:
        """Абстрактный метод для удаления вакансии."""
        pass

    @abstractmethod
    def filter_vacancies(self, criteria: str) -> List[dict]:
        """Абстрактный метод для фильтрации вакансий."""
        pass

