from bs4 import BeautifulSoup as soup
import requests
from simple_term_menu import TerminalMenu
import os


class WebScraper:

    def get_all_questions(self, url):
        results = []
        all_questions = []
        years = []
        data_html = requests.get(url)
        data_soup = soup(data_html.text, "html.parser")
        question_container = data_soup.find_all('a', class_='card-link')

        for question in question_container:
            question = question.get('href')
            results.append(question)

        view_links = [link for link in results if link.endswith('/view/')]

        print(view_links)

        for link in view_links:
            url = f"https://www.collegenote.net{link}"
            # years.append(url.split('/')[-4])
            data_html = requests.get(url)
            data_soup = soup(data_html.text, "html.parser")
            question_container = data_soup.find_all(
                'div', class_='col-7')

            for question in question_container:
                question = question.find_all('p')
                # years.append(url.split('/')[-4])
                for q in question:
                    # print(q.text)
                    all_questions.append(q.text)

        return all_questions, years

    def write_to_file(self, questions, years):
        with open("questions.md", "w") as question_file:
            print(years)
            question_file.write("# Questions\n\n")
            # print(questions)
            for question in questions:
                question_file.write(question + "\n\n")

            # for year in years:
            #     question_file.write("##" + year + "\n\n")
            #     for question in questions:
            #         question_file.write(question + "\n\n")

    # def get_subjects_year(self):
    #     print("Enter your semester: ")
    #     user_semester = "fourth"
    #     print("Enter the subject which you want to scrape: ")
    #     subject = TerminalMenu(self.fourth_semester_subjects).show()

    #     print("Enter the year: ")
    #     options = ["2079", "2078", "2076"]
    #     year = TerminalMenu(options).show()

    #     print("You have selected: ")
    #     print(f"Semester: {user_semester}")
    #     print(f"Subject: {self.fourth_semester_subjects[subject]}")
    #     print(f"Year: {options[year]}")

    #     return user_semester, options[year], self.fourth_semester_subjects[subject]

    def scrape_questions(self):
        # semester, year, subject = self.get_subjects_year()
        url = f"https://www.collegenote.net/pastpapers/TU/CSIT/31/computer-networks/"
        questions, years = self.get_all_questions(url)
        print(years)
        self.write_to_file(questions, years)


scraper = WebScraper()
scraper.scrape_questions()
# scraper.print_sorted_questions()

os.system(
    "mdpdf -o questions.pdf questions.md"
)
