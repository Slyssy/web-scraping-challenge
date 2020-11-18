import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import numpy as np
import time
from selenium.webdriver.support import expected_conditions as EC


# def get_html(url, wait):
#     fireFoxOptions = webdriver.FirefoxOptions()
#     fireFoxOptions.set_headless()
#     driver = webdriver.Firefox(firefox_options=fireFoxOptions)
#     driver.get(url)
#     driver.implicitly_wait(wait)
#     html = driver.page_source
#     driver.close()

#     return html


# url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
# html = get_html(url, wait=5)

# soup = BeautifulSoup(html, "html.parser")

# # news_titles = soup.find_all("li", class_="slide")

# # latest = news_titles[0].find("div", class_="content_title")
# # news_title = latest.text.strip()

# # p_text = news_titles[0].find("div", class_="article_teaser_body")
# # news_p = p_text.text.strip()

# article = soup.find("div", class_='list_text')
# news_title = article.find("div", class_="content_title").text
# news_p = article.find("div", class_ ="article_teaser_body").text

# news_titles = soup.find_all("li", class_="slide")
# latest_story = news_titles[0]
# # print(latest_story)
# print(
#     {
#         "article_title": latest_story.find("h3").text.strip(),
#         "article_p": latest_story.find(
#             "div", class_="article_teaser_body"
#         ).text.strip(),
#     }
# )

# # JPL Mars Space Images - Featured Image Starts Here

# def get_html(url, wait):
#     fireFoxOptions = webdriver.FirefoxOptions()
#     fireFoxOptions.set_headless(False)
#     driver = webdriver.Firefox(firefox_options=fireFoxOptions)
#     driver.get(url)
#     driver.implicitly_wait(wait)
#     driver.find_element_by_link_text("FULL IMAGE").click()
#     driver.find_element_by_partial_link_text("more info").click()
#     html = driver.page_source
#     driver.close()
#     return html


# url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
# html = get_html(url, wait=10)

# soup = BeautifulSoup(html, "html.parser")

# main_image = soup.find_all("img", class_="main_image")

# src = ""
# for image in main_image:
#     src = image["src"]

# featured_image_url = "https://www.jpl.nasa.gov" + src

# print(featured_image_url)


# # # Mars Facts Starts Here

# page = requests.get("https://space-facts.com/mars/")
# soup = BeautifulSoup(page.content, "html.parser")
# tables = soup.find_all("table")

# # Converting table to pandas DataFrame
# table = tables[0]
# tab_data = [
#     [cell.text for cell in row.find_all(["th", "td"])] for row in table.find_all("tr")
# ]
# df = pd.DataFrame(tab_data)
# print(df)
# mars_facts_html_table = df.to_html(header=False, index=False)
# print(mars_facts_html_table)

# Mars Hemispheres Starts Here
def get_html(url, wait):
    fireFoxOptions = webdriver.FirefoxOptions()
    fireFoxOptions.set_headless(False)
    driver = webdriver.Firefox(firefox_options=fireFoxOptions)
    driver.get(url)
    driver.implicitly_wait(wait)
    # element = wait.until(EC.element_to_be_clickable)
    links = driver.find_elements_by_partial_link_text("Enhanced")#.click()
    hrefs = [link.get_attribute("href") for link in links]
    for href in hrefs:
        driver.get(href)
        image_src = driver.find_element_by_class_name("wide-image")
        print(image_src.get_attribute("src"))

        
    # html = driver.page_source
    # return html
    # print([link.text for link in links])
    # driver.close()

url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
html = get_html(url, wait=5)

# soup = BeautifulSoup(html, "html.parser")

# print(soup.prettify())
# print([link.text for link in links])