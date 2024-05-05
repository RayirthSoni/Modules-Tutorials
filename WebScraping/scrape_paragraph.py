import requests
import bs4
import pandas as pd
import os
import re

# Folder Path where text will be written
base_path = os.getcwd()
text_folder_path = os.path.join(base_path, 'WebScraping', 'Paragraph Text')


# url from which to fetch data
url = 'https://en.wikipedia.org/wiki/India'

# Html Content for webpage
html_content = requests.get(url)

# soup object for html page
soup = bs4.BeautifulSoup(html_content.text, 'lxml')


def get_webpage():
    try:
        html_content = requests.get(url)
        soup = bs4.BeautifulSoup(html_content.text, 'lxml')
        return soup
    except Exception as e:
        print(e)
        
def get_paragraph_text():
    try:
        entire_paragraph = ''
        # html paragraphs to write in the file
        paragraphs_html = soup.find_all('p')
        paragraphs_html = paragraphs_html[:5]
        for paragraph in paragraphs_html:
            paragraph_text = paragraph.text
            pattern = r'\[[^\]]*\]'
            paragraph_text = re.sub(pattern, '', paragraph_text)
            entire_paragraph += paragraph_text.strip()
        return entire_paragraph
    
    except Exception as e:
        print(e)


soup = get_webpage()
entire_paragraph = get_paragraph_text()

