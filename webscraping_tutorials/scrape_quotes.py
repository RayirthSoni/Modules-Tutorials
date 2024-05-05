import requests
import bs4

# url
url = 'https://quotes.toscrape.com/'

# Fetch WebPage
def fetch_webpage(url):
    html_webpage = requests.get(url)
    soup = bs4.BeautifulSoup(html_webpage.text, 'lxml')
    return soup

# Get Author Names on WebPage
def get_author_names():
    author_names = [author.text.strip()
                    for author in soup.find_all('small', class_='author')]
    return list(set(author_names))

# Get All Quotes on WebPage
def get_all_quotes():
    all_quotes = [quote.text.strip()
                  for quote in soup.find_all('span', class_='text')]
    return list(set(all_quotes))


soup = fetch_webpage(url)
author_names = get_author_names()
all_quotes = get_all_quotes()
print(author_names)
print(all_quotes)
