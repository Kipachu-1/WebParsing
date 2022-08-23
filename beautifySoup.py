from bs4 import BeautifulSoup
from download_images import *
import requests
import os
Articles_url = input('Articles Url:')
response = requests.get(Articles_url)
soup = BeautifulSoup(response.text, 'lxml')
file_name = soup.h1.text
file_name = file_name.split()[0].replace('?', 'a')
os.mkdir(file_name)

main(Articles_url, folder_name=file_name)
with open(f'{file_name}\Article_text.txt', 'w+', encoding='utf-8') as file:
    file.write(f'{soup.h1.text}\n')
    tags = soup.find_all(['h3', 'p'])
    s = ' '
    for tag in tags:
        file.write(f'{s.join(tag.text.split())}\n')

with open(f'{file_name}\Article_text.txt', 'r+', encoding='utf-8') as file:
    data = file.read()

    with open(r'C:\Users\arsik\OneDrive\Desktop\WebParsing\no_need_data.txt', 'r', encoding='utf-8') as no_need:
        lines = no_need.readlines()
        for line in lines:
            data = data.replace(line, '')
        


    
    

# for child in soup.recursiveChildGenerator():
#     if child.name:
#         print(child.name)
