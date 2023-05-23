import json

from src.class_vacancy import Vacancy
from src.class_json_saver import JSONSaver
from utils.get_samples_of_vacancies_lists import unite_samples_of_vacancies
from utils.print_vacancies import print_vacancies

from colorama import Fore


def user_interaction():
    """
    Def for interaction with user, takes all variables from user answers and using them in funcs
     that will be called.
    """

    while True:
        choice = input(f"{Fore.LIGHTGREEN_EX}1. Search vacancies.\n2. Exit.\nEnter: ")
        if choice.isdigit() and choice in ('1', '2'):
            if choice == '2':
                break

            elif choice == '1':
                search_query = input(f"{Fore.LIGHTGREEN_EX}Enter search query: ")
                keywords = input("Enter keywords for filtration the vacancies: ")

                while True:
                    top_vacancies = input(f"{Fore.LIGHTGREEN_EX}Enter value of vacancies for the top: ")
                    if top_vacancies.isdigit():
                        top_vacancies = int(top_vacancies)
                        break
                    else:
                        print(f"{Fore.LIGHTRED_EX}It's not a number.\n")
                        continue

                not_sorted_vacancies = unite_samples_of_vacancies(search_query, keywords, top_vacancies)
                sorted_vacancies = Vacancy.sorted_by_salary(not_sorted_vacancies)

                JSONSaver.add_vacancies(sorted_vacancies, top_vacancies)

                try:
                    with open("vacancies.json") as file:
                        pass

                except FileNotFoundError:
                    continue
                    
                task_complete = False
                while task_complete is False:
                    user_choice = input(f'{Fore.LIGHTGREEN_EX}1. Select salary from.\n2. Continue.\nEnter: ')
                    if user_choice.isdigit() and user_choice in ('1', '2'):
                        if user_choice == '1':

                            while True:
                                salary_from = input(f"{Fore.LIGHTGREEN_EX}Enter salary from: ")

                                if not salary_from.isdigit():
                                    print(f"{Fore.LIGHTRED_EX}It's not a number.\n")
                                    continue
                                else:
                                    JSONSaver.get_vacancies_by_salary(int(salary_from))
                                    print_vacancies()
                                    JSONSaver.delete_vacancies()
                                    task_complete = True
                                    break

                        elif user_choice == '2':
                            print_vacancies()
                            JSONSaver.delete_vacancies()
                            break

                    elif user_choice not in ('1', '2') and user_choice.isdigit():
                        print(f"{Fore.LIGHTRED_EX}Here is no such action.\n")
                        continue
                    else:
                        print(f"{Fore.LIGHTRED_EX}It's not a number.\n")
                        continue

        elif choice not in ('1', '2') and choice.isdigit():
            print(f"{Fore.LIGHTRED_EX}Here is no such action.\n")
            continue

        else:
            print(f"{Fore.LIGHTRED_EX}It's not a number.\n")
            continue
