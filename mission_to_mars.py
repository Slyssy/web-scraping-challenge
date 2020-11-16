# import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

def get_html(url, wait):

    fireFoxOptions = webdriver.FirefoxOptions()
    fireFoxOptions.set_headless()
    driver = webdriver.Firefox(firefox_options=fireFoxOptions)
    
    # driver = webdriver.Firefox()
    driver.get(url)
    driver.implicitly_wait(wait)
    html = driver.page_source
    driver.close()

    return html

# headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:82.0) Gecko/20100101 Firefox/82.0"}
url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
html = get_html(url, wait=5)
print(html)
# r = requests.get(url, headers=headers)
soup = BeautifulSoup(html, "html.parser")

news_titles = soup.find_all("li", class_="slide")
latest_story = news_titles[0].find("h3").text
print(latest_story)
# latest_title = news_titles[0]
# print(latest_title)
# print(title[0] for title in news_titles)

# for item in news_title:
#     title = find_all('a', {"class": "content_title"}).
#     print(title)
# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context
