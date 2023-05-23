from src.class_vacancy import Vacancy
from src.classes_api import HeadHunterAPI, SuperJobAPI
from colorama import Fore

import json
import os


def get_samples_of_vacancies_list_hh_ru(search_query: str, keywords: str, top_vacancies: int):
    """
    Takes vacancies from API, defines variables with params of vacancies, creating with them samples of class 'Vacancy'
     and putting them to list with non-filtrated samples of class 'Vacancy'.
    :param search_query: search query that user entering in def 'user_interaction()'.
     Also. This param for injecting in API's url.

    :param keywords: keywords that user entering in def 'user_interaction()'.
     Also. This param for injecting in API's url.

    :param top_vacancies: count of vacancies that were sorted by salary from and will be 'dumped' to .json file.
    :return: list with non-filtrated samples of class 'Vacancy'.
    """
    vacancies = []

    HeadHunterAPI().get_vacancies(search_query, keywords, top_vacancies)
    try:
        with open("head_hunter_jobs.json") as json_file:
            content = json.load(json_file)
            json_file.close()

    except FileNotFoundError:

        return []

    else:
        vacancy_index = 0
        barrier = len(content)

        for vacancy in content:

            if vacancy["snippet"]["requirement"] is None:
                requirement = "Unknown"
            else:
                requirement = vacancy["snippet"]["requirement"]

            if vacancy["snippet"]["responsibility"] is None:
                responsibility = "Unknown"
            else:
                responsibility = vacancy["snippet"]["responsibility"]

            name = vacancy["name"]
            url = vacancy["alternate_url"]

            professional_roles = vacancy["professional_roles"][0]["name"]
            experience = vacancy["experience"]["name"]
            employment = vacancy["employment"]["name"]

            if vacancy["salary"] is None:
                salary_from = 0
                salary_to = 0

            else:

                if vacancy["salary"]["from"] is None:
                    salary_from = 0
                else:
                    salary_from = vacancy["salary"]["from"]

                if vacancy["salary"]["to"] is None:
                    salary_to = 0
                else:
                    salary_to = vacancy["salary"]["to"]

            vacancies.append(Vacancy(name, url, salary_from, salary_to, requirement, responsibility, professional_roles,
                             experience, employment))

            vacancy_index += 1
            if vacancy_index == barrier:
                os.remove('head_hunter_jobs.json')
                break

        return vacancies


def get_samples_of_vacancies_list_sj_ru(search_query: str, keywords: str, top_vacancies: int):
    """
    Takes vacancies from API, defines variables with params of vacancies, creating with them samples of class 'Vacancy'
     and putting them to list with non-filtrated samples of class 'Vacancy'.
    :param search_query: search query that user entering in def 'user_interaction()'.
     Also. This param for injecting in API's url.

    :param keywords: keywords that user entering in def 'user_interaction()'.
     Also. This param for injecting in API's url.

    :param top_vacancies: count of vacancies that were sorted by salary from and will be 'dumped' to .json file.
    :return: list with non-filtrated samples of class 'Vacancy'.
    """
    vacancies = []

    SuperJobAPI().get_vacancies(search_query, keywords, top_vacancies)
    try:
        with open("super_job_jobs.json") as json_file:
            content = json.load(json_file)
            json_file.close()
    except FileNotFoundError:
        print(f"{Fore.LIGHTRED_EX}Incorrect search query or keywords.")
        return []

    else:
        vacancy_index = 0
        barrier = len(content)

        for vacancy in content:

            if vacancy["education"]["title"] is None:
                requirement = "Unknown"
            else:
                requirement = vacancy["education"]["title"]

            try:
                professional_roles = vacancy["catalogues"][0]["positions"][0]["title"]
            except IndexError:
                professional_roles = 'Unknown'

            finally:
                name = vacancy["profession"]
                url = vacancy["link"]
                responsibility = vacancy["candidat"]
                experience = vacancy["experience"]["title"]
                employment = vacancy["type_of_work"]["title"]
                salary_from = vacancy["payment_from"]
                salary_to = vacancy["payment_to"]

                vacancies.append(Vacancy(name, url, salary_from, salary_to, requirement, responsibility,
                                         professional_roles, experience, employment))

                vacancy_index += 1
                if vacancy_index == barrier:
                    os.remove('super_job_jobs.json')
                    break

        return vacancies


def unite_samples_of_vacancies(search_query: str, keywords: str, top_vacancies: int):
    """
    Takes lists from 'get_samples_of_vacancies_list_hh_ru()' and 'get_samples_of_vacancies_list_sj_ru()'
     and uniting them to one list with non-filtrated samples of class 'Vacancy'.

    :param search_query: search query that user entering in def 'user_interaction()'.
     Also. This param for injecting in API's url.

    :param keywords: keywords that user entering in def 'user_interaction()'.
     Also. This param for injecting in API's url.

    :param top_vacancies: count of vacancies that were sorted by salary from and will be 'dumped' to .json file.
    :return: united list with non-filtrated samples of class 'Vacancy'.
    """
    vacancies_hh_ru = get_samples_of_vacancies_list_hh_ru(search_query, keywords, top_vacancies)
    vacancies_sj_ru = get_samples_of_vacancies_list_sj_ru(search_query, keywords, top_vacancies)
    vacancies_all = vacancies_hh_ru + vacancies_sj_ru

    return vacancies_all
