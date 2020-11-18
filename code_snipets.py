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