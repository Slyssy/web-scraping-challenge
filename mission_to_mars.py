# import pandas as pd
import requests
from bs4 import BeautifulSoup

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

r = requests.get("https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest")

print(r.status)
