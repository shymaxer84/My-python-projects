import requests
from bs4 import BeautifulSoup

url = input('Enter the URL :')
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
headlines = soup.find_all('h3')
for headline in headlines:
    print(headline.text, "\n")
