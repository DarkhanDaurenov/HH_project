from src.hhabc import AbstractFileSaver
import json
from typing import List


class Vacancy:
    def __init__(self, title: str, link: str, salary: str, description: str):
        """Конструктор класса Vacancy."""
        self.title = title
        self.link = link
        self.salary = salary
        self.description = description

    def validate_salary(self) -> None:
        """Метод для проверки зарплаты."""
        if not self.salary:
            self.salary = "Зарплата не указана"

    def __lt__(self, other) -> bool:
        return self.salary == other.salary

    def __gt__(self, other) -> bool:
        return self.salary == other.salary


class JSONSaver(AbstractFileSaver):
    def __init__(self, filename: str = "vacancies.json"):
        """Конструктор класса JSONSaver."""
        self.filename = filename
        self.vacancies = []

    def add_vacancy(self, vacancy: dict) -> None:
        """Метод для добавления вакансии в JSON файл."""
        self.vacancies.append(vacancy)
        self.save_to_file()

    def delete_vacancy(self, vacancy: dict) -> None:
        """Метод для удаления вакансии из JSON файла."""
        self.vacancies.remove(vacancy)
        self.save_to_file()

    def filter_vacancies(self, criteria: str) -> List[dict]:
        """Метод для фильтрации вакансий."""
        filtered_vacancies = []
        for vacancy in self.vacancies:
            if criteria in vacancy.values():
                filtered_vacancies.append(vacancy)
        return filtered_vacancies

    def save_to_file(self) -> None:
        """Метод для сохранения вакансий в JSON файл."""
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(self.vacancies, f, ensure_ascii=False)






























