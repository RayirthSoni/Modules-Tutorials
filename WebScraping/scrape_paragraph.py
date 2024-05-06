import requests
import bs4
import os
import re

# path for directory on which will be working on 
CURRENT_WORKING_DIRECTORY_PATH = os.getcwd()
# path for webscarping folder
WEBSCRAPING_FOLDER_PATH = os.path.join(CURRENT_WORKING_DIRECTORY_PATH, 'WebScraping')

# url from which to fetch data
WEBPAGE_URL = 'https://en.wikipedia.org/wiki/India'

# Html Content for webpage
html_content = requests.get(WEBPAGE_URL)

# soup object for html page
soup = bs4.BeautifulSoup(html_content.text, 'lxml')

# Function to create folder
def create_folder(folder_name):
    
    try:
        
        text_folder_path = os.path.join(CURRENT_WORKING_DIRECTORY_PATH,folder_name)
        
        if not os.path.exists(text_folder_path):
            os.makedirs(text_folder_path)
            print(f'Folder Created at : {text_folder_path}')
            
        else:
            print(f'Folder Already exists at : {text_folder_path}')
    
    except Exception as e:
        print(e)



def get_webpage():

    try:
        
        html_content = requests.get(WEBPAGE_URL)
        soup = bs4.BeautifulSoup(html_content.text, 'lxml')

        return soup
    
    except Exception as e:
        print(e)


def get_paragraph_text():

    try:
        # text to add entire paragraph
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

def write_content_to_file():
    
    create_folder
    
    try:
        
        pass
    
    except Exception as e:
        print(e)
    


soup = get_webpage()
entire_paragraph = get_paragraph_text()
