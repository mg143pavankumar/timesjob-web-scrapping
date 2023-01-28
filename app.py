from bs4 import BeautifulSoup
import requests as rq
import time

print("Put some skill that you are not familar with")
unfamiliar_skill = input(">")
print(f"Filtering out {unfamiliar_skill}")


def find_jobs(keyword, location):

    # fetching html text from the website
    html_text = rq.get(
        f'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords={keyword}&txtLocation={location}').text

    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_="clearfix job-bx wht-shd-bx")

    for index, job in enumerate(jobs):
        published_date = job.find('span', class_="sim-posted").span.text

        if "few" in published_date:
            company_name = job.find(
                'h3', class_="joblist-comp-name").text.strip()
            skills = job.find(
                'span', class_="srp-skills").text.replace(' ', "")
            more_info = job.header.h2.a['href']

            job_location = job.find(
                'ul', class_="top-jd-dtl clearfix").span["title"]

            if unfamiliar_skill not in skills:
                with open(f'./job-posts/{index}.txt', 'w') as f:
                    f.write(f'Company Name: {company_name.strip()}\n')
                    f.write(f'Required Skills: {skills.strip()}\n')
                    f.write(f"Location: {job_location}\n")
                    f.write(f"More Info: {more_info}\n")

                print(f"File saved: {index}")


if __name__ == "__main__":

    while True:
        find_jobs("Python", "India")

        time_wait = 10

        print(f'Waiting {time_wait} minutes...')
        time.sleep(time_wait * 60)
