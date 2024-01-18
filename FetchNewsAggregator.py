import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


url = input('Enter the URL :')
page = requests.get(url)
soup = BeautifulSoup(page.content,'html.parser')
headlines =soup.find_all('h3')
for headline in headlines:
    print(headline.text,"\n")







    
# def fetchNews(url):
#     headlines =soup.find_all('h3')
#     for headline in headlines:
#         print(headline.text,"\n")
#         fetchNews(url)


# page = requests.get(url)
# news = soup.find('title').get_text()
# print(news)

# for link in soup.find_all('a'):
#     print(link.get('href'))

# <a class="Newsflashesstyles__StyledLinkVerticalMarqueeHeader-sc-v9lyuv-3 fYcjfE" href="/news/news-flash/"><span class="Newsflashesstyles__Title-sc-v9lyuv-5 iRlkAY">מבזקים</span><span class="Newsflashesstyles__CurrentTime-sc-v9lyuv-4 jXFQXY">יום רביעי 17.01.2024</span></a>
#
# driver = webdriver.Chrome('./chromedriver')
# driver.get(url)
# driver.find_element(BY.XPATH,"//a[@class='Newsflashesstyles__StyledLinkVerticalMarqueeHeader-sc-v9lyuv-3 fYcjfE']")