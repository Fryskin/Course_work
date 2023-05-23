import json
import os
from abc import ABC, abstractmethod


class Saver(ABC):
    """The abstract class with abstract methods for adding, filtrating and deleting received vacancies from API."""
    @staticmethod
    @abstractmethod
    def add_vacancies(sorted_vacancies: list, top_vacancies: int):
        """
        Makes .json file with vacancies.
        :param sorted_vacancies: vacancies that were sorted by salary from high to low.
        :param top_vacancies: count of vacancies that were sorted by salary from and will be 'dumped' to .json file
        :return: nothing. But initializing the 'vacancies.json' for subsequent filtration or printing.
        """
        pass

    @staticmethod
    @abstractmethod
    def get_vacancies_by_salary(salary_from: int):
        """
        Filtrating vacancies from file 'vacancies.json' and
         makes .json file with vacancies that filtered by 'salary_from'.
        :param salary_from: value that will be used to filtrate vacancies.
        :return: nothing. But deleting old file 'vacancies.json' and initializing the new file 'vacancies.json'
         that will be filtered by 'salary_from' for subsequent printing.
        """
        pass

    @staticmethod
    @abstractmethod
    def delete_vacancies():
        """Deleting file 'vacancies.json' """
        pass


class JSONSaver(Saver):
    """The abstract class with methods for adding, filtrating and deleting received vacancies from API."""
    @staticmethod
    def add_vacancies(sorted_vacancies: list, top_vacancies: int):
        """
        Makes .json file with vacancies.
        :param sorted_vacancies: vacancies that were sorted by salary from high to low.
        :param top_vacancies: count of vacancies that were sorted by salary from and will be 'dumped' to .json file
        :return: nothing. But initializing the 'vacancies.json' for subsequent filtration or printing.
        """
        iteration_count = 0

        for vacancy_sample in sorted_vacancies:
            vacancy_to_json = {"items": {
                    "name": vacancy_sample.name,
                    "url": vacancy_sample.url,
                    "salary_from": vacancy_sample.salary_from,
                    "salary_to": vacancy_sample.salary_to,
                    "currency": vacancy_sample.currency,
                    "requirement": vacancy_sample.requirement,
                    "responsibility": vacancy_sample.responsibility,
                    "professional_roles": vacancy_sample.professional_roles,
                    "experience": vacancy_sample.experience,
                    "employment": vacancy_sample.employment,
                }
            }

            with open("vacancies.json", "a") as json_file:
                if os.stat("vacancies.json").st_size == 0:
                    json.dump([vacancy_to_json], json_file, indent=4)

                    json_file.close()

                else:
                    with open("vacancies.json") as json_file_read:
                        content = json.load(json_file_read)
                        json_file_read.close()

                    with open("vacancies.json", 'w') as json_file_write:
                        content.append(vacancy_to_json)
                        json.dump(content, json_file_write, indent=4)
                        json_file_write.close()

            iteration_count += 1
            if iteration_count == top_vacancies:
                break

    @staticmethod
    def get_vacancies_by_salary(salary_from: int):
        """
        Filtrating vacancies from file 'vacancies.json' and
         makes .json file with vacancies that filtered by 'salary_from'.
        :param salary_from: value that will be used to filtrate vacancies.
        :return: nothing. But deleting old file 'vacancies.json' and initializing the new file 'vacancies.json'
         that will be filtered by 'salary_from' for subsequent printing.
        """

        vacancies_sorted_by_salary = []
        try:
            with open("vacancies.json") as json_file_read:
                content = json.load(json_file_read)
                json_file_read.close()
                os.remove("vacancies.json")
        except FileNotFoundError:
            print('')
        else:

            for vacancy in content:
                if vacancy["items"]["salary_from"] >= salary_from:
                    vacancies_sorted_by_salary.append(vacancy)

            with open("vacancies.json", 'w') as json_file_write:
                content = vacancies_sorted_by_salary
                json.dump(content, json_file_write, indent=4)
                json_file_write.close()

    @staticmethod
    def delete_vacancies():
        """Deleting file 'vacancies.json' """

        try:
            os.remove("vacancies.json")
        except FileNotFoundError:
            print('')
