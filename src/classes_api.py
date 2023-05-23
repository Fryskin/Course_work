from abc import ABC, abstractmethod
import requests
import json
import os
import time


class SitesAPI(ABC):
    """The abstract class that contains abstract method for api classes that receiving vacancies from API."""

    @abstractmethod
    def get_vacancies(self, search_query: str, keywords: str, top_vacancies: int):
        """
        The method that receiving vacancies from API.
        :param search_query: search query that user entering in def 'user_interaction()'.
            Also. This param for injecting in API's url.

        :param keywords: keywords that user entering in def 'user_interaction()'.
            Also. This param for injecting in API's url.

        :param top_vacancies: count of vacancies that will be print after processing (entering in 'user_interaction()').
        :return: nothing. But initializing the 'head_hunter_jobs.json' for subsequent sorting and filtration.
        """
        pass


class HeadHunterAPI(SitesAPI):
    """The class that contains method for receiving vacancies from 'hh.ru' API."""

    def get_vacancies(self, search_query: str, keywords: str, top_vacancies: int):
        """
        The method that receiving vacancies from 'hh.ru' API.

        :param search_query: search query that user entering in def 'user_interaction()'.
            Also. This param for injecting in API's url.

        :param keywords: keywords that user entering in def 'user_interaction()'.
            Also. This param for injecting in API's url.

        :param top_vacancies: count of vacancies that will be print after processing (entering in 'user_interaction()')
        :return: nothing. But initializing the 'head_hunter_jobs.json' for subsequent sorting and filtration.
        """

        page_number = 0
        pages_count = 1

        while page_number < pages_count:

            hh_api = f'https://api.hh.ru/vacancies?text={search_query.replace(" ", "&")}&' \
                     f'description={keywords.replace(" ", "&")}&area=1&page={page_number}&per_page=100'

            response = requests.get(hh_api, headers={"User-Agent": "K_ParserApp/1.0"})
            response_json = response.json()

            if len(response_json["items"]) == 0:
                time.sleep(0.25)
                break

            else:
                with open('head_hunter_jobs.json', 'a') as add_file:
                    if os.stat('head_hunter_jobs.json').st_size == 0:
                        json.dump(response_json["items"], add_file, indent=4)
                        add_file.close()

                        if len(response_json["items"]) < top_vacancies:
                            pages_count += 1

                    else:
                        with open('head_hunter_jobs.json', encoding="utf-8") as json_file_read:
                            content = json.load(json_file_read)
                            json_file_read.close()
                            for vacancy in response_json["items"]:
                                content.append(vacancy)

                        with open('head_hunter_jobs.json', 'w') as json_file_write:
                            json.dump(content, json_file_write, indent=4)
                            json_file_write.close()

                    page_number += 1
                    time.sleep(0.25)

        print(f"LOADING: 50%")


class SuperJobAPI(SitesAPI):
    """The class that contains method for receiving vacancies from 'superjob.ru' API."""

    def get_vacancies(self, search_query: str, keywords: str, top_vacancies: int):
        """
        The method that receiving vacancies from 'superjob.ru' API.

        :param search_query: search query that user entering in def 'user_interaction()'.
            Also. This param for injecting in API's url.

        :param keywords: keywords that user entering in def 'user_interaction()'.
            Also. This param for injecting in API's url.

        :param top_vacancies: count of vacancies that will be print after processing (entering in 'user_interaction()').
        :return: nothing. But initializing the 'head_hunter_jobs.json' for subsequent filtration.
        """

        superjob_key = os.getenv('SUPERJOB_KEY')
        headers = {"X-Api-App-Id": superjob_key}
        superjob_api = 'https://api.superjob.ru/2.0/vacancies'

        page_number = 0
        pages_count = 1

        while page_number < pages_count:

            response = requests.get(superjob_api, headers=headers, params=f"keyword={search_query.replace(' ', '&')}"
                                                                          f"&{keywords.replace(' ', '&')}"
                                                                          f"&page={page_number}"
                                                                          f"&count=100")

            response_json = response.json()

            if len(response_json["objects"]) == 0:
                time.sleep(0.25)
                break

            else:
                with open('super_job_jobs.json', 'a') as add_file:
                    if os.stat('super_job_jobs.json').st_size == 0:
                        json.dump(response_json["objects"], add_file, indent=4)
                        add_file.close()

                        if len(response_json["objects"]) < top_vacancies:
                            pages_count += 1

                    else:
                        with open('super_job_jobs.json', encoding="utf-8") as json_file_read:
                            content = json.load(json_file_read)
                            json_file_read.close()
                            for vacancy in response_json["objects"]:
                                content.append(vacancy)

                        with open('super_job_jobs.json', 'w') as json_file_write:
                            json.dump(content, json_file_write, indent=4)
                            json_file_write.close()

                    page_number += 1
                    time.sleep(0.25)

        print(f"LOADING: 100%\n")
        time.sleep(0.25)
