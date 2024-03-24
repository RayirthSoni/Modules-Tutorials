import requests
from bs4 import BeautifulSoup

url = "https://codewithharry.com"

# Step 1 : Get the HTML
r = requests.get(url)
html_content = r.content
# print(r.content)

# Step 2 : Parse the HTML
soup = BeautifulSoup(html_content, "html.parser")
# print(soup.prettify)

# Step 3 : HTML tree traversal
# Commonly used types of objects:
# print(type(title)) # 1 Tag
# print(type(title.string)) # 2 NavigableString
# print(type(soup)) # 3 BeautifulSoup
# 4 Comment

# Get the title of HTML webpage
title = soup.title

# Get all paragraphs from page
paras = soup.find_all("p")
# print(paras)

# Get all anchors from page
anchors = soup.find_all("a")
# print(anchors)

# Get first element in HTML webpaage
# print(soup.find('p'))

# Get class of any element in HTML pahe
# print(soup.find('p')['class'])

# Get all element of a class
# print(soup.find_all("p",class_="mt-2"))

# Get text from the tags/soup
# print(soup.find("p").get_text())
# print(soup.get_text())

# Get all anchors on a webpage
anchors = soup.find_all("a")
all_link = set()

# Get all links on a webpage
for link in anchors:
    if (link.get('href') != '/'):
        linktext = url + link.get("href")
        all_link.add(linktext)

print(all_link)
