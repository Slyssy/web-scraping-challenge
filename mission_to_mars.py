# import pandas as pd
import requests
from bs4 import BeautifulSoup

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:82.0) Gecko/20100101 Firefox/82.0"}
url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.text, "html.parser")

news_titles = soup.find_all("li", class_="slide")
# news_title = news_titles[0]
print(news_titles)
# latest_title = news_titles[0]
# print(latest_title)
# print(title[0] for title in news_titles)

# for item in news_title:
#     title = find_all('a', {"class": "content_title"}).
#     print(title)
