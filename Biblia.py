import requests
from bs4 import BeautifulSoup
from django.http import HttpResponse

page = requests.get('https://www.biblegateway.com/')
# Create a BeautifulSoup object
soup = BeautifulSoup(page.text, 'html.parser')
verse=soup.find(class_='votd-box')
verse_items=verse.find_all('p')
for i in verse_items:
    print(i.get_text())

verse_version=verse.find_all('a',limit=2)
for a in verse_version:
    print(a.get_text())
