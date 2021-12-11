import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest
import time

def to_infinity():
    index = 0
    while True:
        yield index
        index += 1



search = input('Search jobs, companies : ')


currentTime = time.strftime("%H:%M:%S")
currentTime = f"{search} {currentTime} wuzzaf.csv"
currentTime = str(currentTime)

for page in to_infinity():
    result = requests.get(f'https://wuzzuf.net/search/jobs/?q={search}&start={str(page)}')

    src = result.content

    soup = BeautifulSoup(src, "lxml")

    try:
        search_result = soup.find("p", {"class": "css-1f19b85"}).text
        print(search_result)
        quit()
    except:
        pass




    job_titles = soup.find_all("h2", {"class": "css-m604qf"})
    company_names = soup.find_all("a", {"class": "css-17s97q8"})
    locations_names = soup.find_all("span", {"class": "css-5wys0k"})
    job_skills = soup.find_all("div", {"class": "css-y4udm8"})



    job_title = []
    company_name = []
    locations_name = []
    skills = []
    links = []

    for i in range(len(job_titles)):
        job_title.append(job_titles[i].text)
        links.append("https://wuzzuf.net" + job_titles[i].find("a").attrs['href'])
        company_name.append(company_names[i].text)
        locations_name.append(locations_names[i].text)
        skills.append(job_skills[i].text)
        
    if job_title == []:
        break
        


    

    file_list = [job_title, company_name, locations_name, skills, links]
    exported = zip_longest(*file_list)
    with open(currentTime, "a") as myfile:
        wr = csv.writer(myfile)
        wr.writerow(["Job Title", "Company Name", "Location", "Skills", "links"])
        wr.writerows(exported)
