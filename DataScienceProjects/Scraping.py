from bs4 import BeautifulSoup

import requests

html = requests.get(
    "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=")
print(f"This is response from the webseite: {html}\n")

html_text = requests.get(
    "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=").text  # this .text will bring the html text from the page.

# could also use "lxml" or "html5lib" or "html.parser" but use "html.parser".
soup = BeautifulSoup(html_text, "html.parser")
job = soup.find("li", class_="clearfix job-bx wht-shd-bx")
print(job)
