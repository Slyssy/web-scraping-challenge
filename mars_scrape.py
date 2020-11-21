import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions

# Setting up FireFox webdriver
def configure_firefox_driver():
    firefox_options = FirefoxOptions()
    firefox_options.add_argument("--headless")
    driver = webdriver.Firefox(options=firefox_options)

    return driver


driver = configure_firefox_driver()
mars_dict = {}


def scrape(driver):

    # Mars News
    url = "https://mars.nasa.gov/news/"
    driver.get(url)
    driver.implicitly_wait(10)
    html = driver.page_source

    # Parsing with bs4
    soup = BeautifulSoup(html, "html.parser")

    # Finding news titles
    news_titles = soup.find_all("li", class_="slide")

    # Grabbing latest news title and adding it to a dict
    latest_story = news_titles[1].find("div", class_="content_title")
    mars_dict["news_title"] = latest_story.text.strip()

    # Grabbing latest news paragraph text and adding to a dict
    article = news_titles[1].find("div", class_="article_teaser_body")
    mars_dict["news_p"] = article.text.strip()

    # JPL Mars Space Images - Featured Image Starts Here
    base_url = "https://www.jpl.nasa.gov"
    url = base_url + "/spaceimages/?search=&category=Mars"

    driver.get(url)
    driver.implicitly_wait(10)

    # Scraping with Selenium
    driver.find_element_by_link_text("FULL IMAGE").click()
    driver.find_element_by_partial_link_text("more info").click()
    driver.implicitly_wait(10)
    html = driver.page_source

    # Parsing with bs4
    soup = BeautifulSoup(html, "html.parser")
    main_image = soup.find_all("img", class_="main_image")

    # Grabbing image src from inside the image class "main image"
    src = ""
    for image in main_image:
        src = image["src"]

    mars_dict["featured_image_url"] = "https://www.jpl.nasa.gov" + src

    # Mars Facts Starts Here
    page = requests.get("https://space-facts.com/mars/")
    # Parsing with bs4
    soup = BeautifulSoup(page.content, "html.parser")
    tables = soup.find_all("table")

    # Indexing to grab info for the 1st table and converting table to pandas DataFrame
    table = tables[0]
    tab_data = [
        [cell.text for cell in row.find_all(["th", "td"])]
        for row in table.find_all("tr")
    ]
    df = pd.DataFrame(tab_data)
    # Renaming DF Columns
    df.rename(columns={0: "", 1: ""}, inplace=True)
    # Converting DataFrame to an HTML table
    mars_dict["mars_facts"] = df.to_html(index=False)

    # Mars Hemispheres Starts Here
    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    firefox_options = FirefoxOptions()
    firefox_options.add_argument("--headless")
    driver = webdriver.Firefox(options=firefox_options)
    driver.get(url)
    driver.implicitly_wait(10)

    links = driver.find_elements_by_partial_link_text("Enhanced")
    link_name_list = [link.text for link in links]

    # Iterating through links by using href attribute
    hrefs = [link.get_attribute("href") for link in links]

    # Iterating throug hrefs to extract src attribute
    image_url_list = []
    for href in hrefs:
        driver.get(href)
        image_src = driver.find_element_by_class_name("wide-image")
        image_urls = image_src.get_attribute("src")
        # Appending image urls for loop output to a list
        image_url_list.append(image_urls)
    # Combine link_name_list and image_url_list to a list of tuples
    list_tuples = tuple(zip(link_name_list, image_url_list))

    # Define keys to be used in dictionaries
    keys = ("title", "img_url")

    # Zipping keys to tuples for each tuple in the list of tuples
    # Using dict comprehension to return a list of dictionaries.
    mars_dict["mars_hemispheres"] = [dict(zip(keys, tuple)) for tuple in list_tuples]

    return mars_dict
    driver.close()


scrape(driver)
print(mars_dict)
