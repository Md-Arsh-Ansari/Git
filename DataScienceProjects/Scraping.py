from bs4 import BeautifulSoup
import requests


html = requests.get(
    "https://www.timesjobs.com/candidate/job-search.html?from=submit&actualTxtKeywords=Data%20Scientist&searchBy=0&rdoOperator=OR&searchType=personalizedSearch&luceneResultSize=97&postWeek=7&txtKeywords=data%20scientist&pDate=I&sequence=1&startPage=1")
print(f"This is response from the webseite: {html}\n")

html_text = requests.get(
    "https://www.timesjobs.com/candidate/job-search.html?from=submit&actualTxtKeywords=Data%20Scientist&searchBy=0&rdoOperator=OR&searchType=personalizedSearch&luceneResultSize=97&postWeek=7&txtKeywords=data%20scientist&pDate=I&sequence=1&startPage=1").text  # this .text will bring the html text from the page.


# could also use "lxml" or "html5lib" or "html.parser" but use "html.parser".
soup = BeautifulSoup(html_text, "html.parser")
jobs = soup.find_all("li", class_="clearfix job-bx wht-shd-bx")
count = 1
for job in jobs:

    company_name = job.find(
        'h3', class_='joblist-comp-name').text  # This .text bring only the text inside h3 tag and class joblist....
    skills = job.find("span", class_="srp-skills").text

    # Because this is a header. and "soup.find_all" applies inside only li tag.
    ###################more_info = job.header.h2.a['href']

    print(f"{count}. Company Name: {company_name.strip()}\n")
    print(f"Required Skill: {skills.strip()}\n")
    ##################print(f"More Info: {more_info}\n")
    print("\n\n")
    count += 1
