from colorama import Fore

import json


def print_vacancies():
    """Takes sorted and filtered vacancies from file 'vacancies.json' and printing all of them."""

    try:
        with open("vacancies.json") as json_file:
            content = json.load(json_file)
            json_file.close()
    except FileNotFoundError:
        print('')

    else:

        vacancies_count = 0
        for vacancy in content:
            print(f'{Fore.LIGHTGREEN_EX}Title: {Fore.CYAN}{vacancy["items"]["name"]}')
            print(f'{Fore.LIGHTGREEN_EX}URL: {Fore.CYAN}{vacancy["items"]["url"]}')

            if vacancy["items"]["salary_from"] == 0:
                print(f'{Fore.LIGHTGREEN_EX}From: {Fore.CYAN}Unknown')
            else:
                print(f'{Fore.LIGHTGREEN_EX}From: {Fore.CYAN}{vacancy["items"]["salary_from"]} '
                      f'{vacancy["items"]["currency"]}')

            if vacancy["items"]["salary_to"] == 0:
                print(f'{Fore.LIGHTGREEN_EX}To: {Fore.CYAN}Unknown')
            else:
                print(f'{Fore.LIGHTGREEN_EX}To: {Fore.CYAN}{vacancy["items"]["salary_to"]} '
                      f'{vacancy["items"]["currency"]}')

            print(f'{Fore.LIGHTGREEN_EX}Requirements: {Fore.CYAN}{vacancy["items"]["requirement"]}')
            print(f'{Fore.LIGHTGREEN_EX}Responsibility: {Fore.CYAN}{vacancy["items"]["responsibility"]}')
            print(f'{Fore.LIGHTGREEN_EX}Position: {Fore.CYAN}{vacancy["items"]["professional_roles"]}')
            print(f'{Fore.LIGHTGREEN_EX}Experience: {Fore.CYAN}{vacancy["items"]["experience"]}')
            print(f'{Fore.LIGHTGREEN_EX}Type of employment: {Fore.CYAN}{vacancy["items"]["employment"]}')
            print(f'{Fore.LIGHTYELLOW_EX}-----------------------------------------------------')

            vacancies_count += 1

        print(f'Count of vacancies: {vacancies_count}\n')
