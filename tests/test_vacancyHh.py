import pytest
import json
from src.vacancyHh import JSONSaver, Vacancy

@pytest.fixture
def json_saver(tmp_path):
    json_file = tmp_path / "test_vacancies.json"
    return JSONSaver(filename=json_file)

def test_add_vacancy(json_saver):
    vacancy = Vacancy("Python Developer", "", "100 000-150 000 руб.", "Требования: опыт работы от 3 лет...")
    json_saver.add_vacancy(vacancy)
    with open(json_saver.filename, "r") as f:
        data = json.load(f)
    assert len(data) == 1
    assert data[0]["title"] == "Python Developer"

def test_delete_vacancy(json_saver):
    vacancy = Vacancy("Python Developer", "", "100 000-150 000 руб.", "Требования: опыт работы от 3 лет...")
    json_saver.add_vacancy(vacancy)
    json_saver.delete_vacancy(vacancy)
    with open(json_saver.filename, "r") as f:
        data = json.load(f)
    assert len(data) == 0

def test_add_and_delete_vacancy(json_saver):
    vacancy1 = Vacancy("Python Developer", "", "100 000-150 000 руб.", "Требования: опыт работы от 3 лет...")
    vacancy2 = Vacancy("Java Developer", "", "90 000-120 000 руб.", "Требования: опыт работы от 2 лет...")
    json_saver.add_vacancy(vacancy1)
    json_saver.add_vacancy(vacancy2)
    assert len(json_saver.vacancies) == 2
    json_saver.delete_vacancy(vacancy1)
    assert len(json_saver.vacancies) == 1
    json_saver.delete_vacancy(vacancy2)
    assert len(json_saver.vacancies) == 0