import requests
from abc import ABC, abstractmethod


class Parser(ABC):
    @abstractmethod
    def load_vacancies(self):
        pass


class HH(Parser):
    """
    Класс для работы с API HeadHunter
    Класс Parser является родительским классом, который вам необходимо реализовать
    """

    def __init__(self, keyword):
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': keyword, 'page': 0, 'per_page': 100}
        self.vacancies = []

    def load_vacancies(self):
        """Получение вакансий с сайта"""
        while self.params.get('page') != 1:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            vacancies = response.json()['items']
            self.vacancies.extend(vacancies)
            self.params['page'] += 1
        return self.vacancies
