
class Vacancy:
    """
    Class that initializing vacancy with using variables and have method for sorting them
     by salary from high to low.
    """

    def __init__(self, name: str, url: str, salary_from: int, salary_to: int, requirement: str,
                 responsibility: str, professional_roles: str, experience: str, employment: str):

        self.name = name
        self.url = url
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.currency = 'руб.'
        self.requirement = requirement.replace('<highlighttext>', '').replace('</highlighttext>', '')
        self.responsibility = responsibility.replace('<highlighttext>', '').replace('</highlighttext>', '')
        self.professional_roles = professional_roles
        self.experience = experience
        self.employment = employment

    @staticmethod
    def sorted_by_salary(not_sorted_vacancies: list):
        """
        Method that sorting vacancies by salary from high to low.
        :param not_sorted_vacancies: united list with samples of vacancies.
        :return: sorted list with samples of vacancies.
        """
        count_of_vacancies = len(not_sorted_vacancies)
        sorted_vacancies = []
        highest_salary_from_value = 0
        highest_salary_from_sample = None

        while len(sorted_vacancies) != count_of_vacancies:

            for vacancy in not_sorted_vacancies:
                if vacancy.salary_from >= highest_salary_from_value:
                    highest_salary_from_value = vacancy.salary_from
                    highest_salary_from_sample = vacancy

            sorted_vacancies.append(highest_salary_from_sample)
            not_sorted_vacancies.remove(highest_salary_from_sample)

            highest_salary_from_value = 0

        return sorted_vacancies
