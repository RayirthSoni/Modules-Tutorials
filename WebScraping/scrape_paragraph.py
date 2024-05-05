import requests
import bs4
import pandas as pd
import os

# url from which to fetch data
url = 'https://en.wikipedia.org/wiki/India'

html_content = requests.get(url)

# soup object for html page
soup = bs4.BeautifulSoup(html_content.text, 'lxml')

paragraph = soup.find_all('p')
