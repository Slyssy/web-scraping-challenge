links = np.arange[1, 4, 1]
url_collected = []

for link in links:
    page = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    driver = webdriver.Firefox()
    driver.get(page)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    urls = [item.get("href") for item in soup.find_all("a")]
    print(urls)

# Snipet to pull images off of a website
for img in soup.find_all("img"):
    temp = img.get('src')
    if temp[:1]=="/":
        image = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars" + temp
    else:
        image = temp
    
    print(image)


     # Print Pretty
     print(soup.prettify(main_image))

#This code will get me a list of link names for Mars Hemispheres
fireFoxOptions = webdriver.FirefoxOptions()
fireFoxOptions.set_headless(False)
driver = webdriver.Firefox(firefox_options=fireFoxOptions)
wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable)
driver.get("https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars")
links= driver.find_elements_by_partial_link_text("Enhanced")
# List comprehension to print out the link names in a list.
print([link.text for link in links])


# print(
#     {
#         "article_title": soup.find("h1", class_="article_title").text.strip(),
#         "article_p": soup.find("div", class_="wysiwyg_content").find_all("p").text.strip(),
#     }
# )


body = soup.body
for paragraph in body.find_all('p'):
    pg = paragraph.text

print(
    {
        "article_title": soup.find("h1", class_="article_title").text.strip(),
        "article_p": pg
    }
)body = soup.body
for paragraph in body.find_all('p'):
    pg = paragraph.text

# Original mars_scrape
def mars_news():
    
    url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    html = get_html(url, wait=5)

    soup = BeautifulSoup(html, "html.parser")

    news_titles = soup.find_all("li", class_="slide")
    latest_story = news_titles[0]
    title = latest_story.find("h3").text.strip()
    article = latest_story.find("div", class_="article_teaser_body").text.strip()

    print(title, article)

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

    print(featured_image_url)

def mars_facts():

    page = requests.get("https://space-facts.com/mars/")
    soup = BeautifulSoup(page.content, "html.parser")
    tables = soup.find_all("table")

    # Converting table to pandas DataFrame
    table = tables[0]
    tab_data = [
        [cell.text for cell in row.find_all(["th", "td"])]
        for row in table.find_all("tr")
    ]
    df = pd.DataFrame(tab_data)

    mars_facts_html_table = df.to_html(header=False, index=False)

    print(mars_facts_html_table)

def mars_hemispheres():

    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    html = get_html(url, wait=5)

    links = driver.find_elements_by_partial_link_text("Enhanced")  # .click()
    hrefs = [link.get_attribute("href") for link in links]
    for href in hrefs:
        driver.get(href)
        image_src = driver.find_element_by_class_name("wide-image")
        image_srcs = image_src.get_attribute("src")

    print(image_srcs)
def mars_dict():
    print({
        "news_title": title,
        "news_p": article,
        "featured_image": featured_image_url,
        "mars_facts_table": mars_facts_html_table,
        "mars_hemisphere_images": image_srcs,
    })
def scrape():
    # title, article = mars_news()
    # results = {"title": title, "article": article}
    # return results

    featured_image = jpl_mars_space_images
    mars_facts_table = mars_facts
    mars_hemisphere_images = mars_hemispheres
    return (mars_dict)

scrape()
