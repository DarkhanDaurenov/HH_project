from src.hhabc import AbstractFileSaver
import json

class Vacancy:
    def __init__(self, title, link, salary, description):
        self.title = title
        self.link = link
        self.salary = salary
        self.description = description

    def validate_salary(self):
        if not self.salary:
            self.salary = "Зарплата не указана"

    def __lt__(self, other):
        return self.salary == other.salary

    def __gt__(self, other):
        return self.salary == other.salary


class JSONSaver(AbstractFileSaver):
    def __init__(self, filename="vacancies.json"):
        self.filename = filename
        self.vacancies = []

    def add_vacancy(self, vacancy):
        self.vacancies.append(vars(vacancy))
        self.save_to_file()

    def delete_vacancy(self, vacancy):
        self.vacancies.remove(vars(vacancy))
        self.save_to_file()

    def filter_vacancies(self, criteria):
        # Пустая реализация метода filter_
        pass

    def save_to_file(self):
        with open(self.filename, 'w') as f:
            json.dump(self.vacancies, f)



























