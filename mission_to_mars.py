import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
# import numpy as np
# import time
# from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options as FirefoxOptions



# Mars News Starts Here
def get_html(url, wait):
    fireFoxOptions = webdriver.FirefoxOptions()
    fireFoxOptions.set_headless()
    driver = webdriver.Firefox(firefox_options=fireFoxOptions)
    driver.get(url)
    driver.implicitly_wait(wait)
    html = driver.page_source
    driver.close()

    return html


url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
html = get_html(url, wait=5)

soup = BeautifulSoup(html, "html.parser")

# Finding the latest story on the page.
news_titles = soup.find_all("li", class_="slide")
latest_story = news_titles[0]

print(
    {
        "article_title": latest_story.find("h3").text.strip(),
        "article_p": latest_story.find(
            "div", class_="article_teaser_body"
        ).text.strip(),
    }
)

# JPL Mars Space Images - Featured Image Starts Here

def get_html(url, wait):
    fireFoxOptions = webdriver.FirefoxOptions()
    fireFoxOptions.set_headless()
    driver = webdriver.Firefox(firefox_options=fireFoxOptions)
    driver.get(url)
    driver.implicitly_wait(wait)
    driver.find_element_by_link_text("FULL IMAGE").click()
    driver.find_element_by_partial_link_text("more info").click()
    html = driver.page_source
    driver.close()
    return html


url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
html = get_html(url, wait=10)

soup = BeautifulSoup(html, "html.parser")

main_image = soup.find_all("img", class_="main_image")

src = ""
for image in main_image:
    src = image["src"]

featured_image_url = "https://www.jpl.nasa.gov" + src

print(featured_image_url)


# Mars Facts Starts Here

page = requests.get("https://space-facts.com/mars/")
soup = BeautifulSoup(page.content, "html.parser")
tables = soup.find_all("table")

# Converting table to pandas DataFrame
table = tables[0]
tab_data = [
    [cell.text for cell in row.find_all(["th", "td"])] for row in table.find_all("tr")
]
df = pd.DataFrame(tab_data)
print(df)
mars_facts_html_table = df.to_html(header=False, index=False)
print(mars_facts_html_table)

# # Mars Hemispheres Starts Here
firefox_options = FirefoxOptions()
firefox_options.add_argument("--headless")
driver = webdriver.Firefox(options = firefox_options)
url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
firefox_options = FirefoxOptions()
firefox_options.add_argument("--headless")
driver = webdriver.Firefox(options = firefox_options)
driver.get(url)
driver.implicitly_wait(10)

links = driver.find_elements_by_partial_link_text("Enhanced")#.click()
link_name_list = [link.text for link in links]

# Iterating through links by using href attribute
hrefs = [link.get_attribute("href") for link in links]

# Iterating throug hrefs to extract src attribute
image_url_list =[]
for href in hrefs:
    driver.get(href)
    image_src = driver.find_element_by_class_name("wide-image")
    image_urls = (image_src.get_attribute("src"))
    # Appending image urls for loop output to a list
    image_url_list.append(image_urls)

# Creating a dictionary by combining link_name_list and image_url_list
url_dict = dict(zip(link_name_list, image_url_list))
print(url_dict)