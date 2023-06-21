from bs4 import BeautifulSoup
import requests


url="https://apnaphone.pk/"

page=requests.get(url)
# print(page.content)

soup=BeautifulSoup(page.content,"html parser")
print(soup)

# lists=soup.find_all('div',class_="col px-2 product-box mb-3 ")
# print(lists)