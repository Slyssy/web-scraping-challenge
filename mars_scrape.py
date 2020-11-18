import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import numpy as np
import time
from selenium.webdriver.support import expected_conditions as EC

def scrape():
    def get_html(url, wait):
    fireFoxOptions = webdriver.FirefoxOptions()
    fireFoxOptions.set_headless()
    driver = webdriver.Firefox(firefox_options=fireFoxOptions)
    driver.get(url)
    driver.implicitly_wait(wait)
    html = driver.page_source
    driver.close()

    return html

    title, article = mars_news()
    results = {
        "title": title
        "article": article

    }
    return results



def mars_news():
    url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    html = get_html(url, wait=5)
    
    news_titles = soup.find_all("li", class_="slide")
    latest_story = news_titles[0]
    title = latest_story.find("h3").text.strip()
    article = latest_story.find(
            "div", class_="article_teaser_body"
        ).text.strip()

    return title, article

def jpl_mars_space_images():
    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    html = get_html(url, wait=10)

    driver.find_element_by_link_text("FULL IMAGE").click()
    driver.find_element_by_partial_link_text("more info").click()

    main_image = soup.find_all("img", class_="main_image")

    src = ""
    for image in main_image:
        src = image["src"]

    featured_image_url = "https://www.jpl.nasa.gov" + src

    return featured_image_url

def mars_facts():
    page = requests.get("https://space-facts.com/mars/")
    soup = BeautifulSoup(page.content, "html.parser")
    tables = soup.find_all("table")

    # Converting table to pandas DataFrame
    table = tables[0]
    tab_data = [
        [cell.text for cell in row.find_all(["th", "td"])] for row in table.find_all("tr")
    ]
    df = pd.DataFrame(tab_data)

    mars_facts_html_table = df.to_html(header=False, index=False)

    return mars_facts_html_table




