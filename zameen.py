from bs4 import BeautifulSoup
import requests






url="https://www.zameen.com/Homes/Bahawalnagar-557-1.html"
def record():
    f=open("values.txt","a")
    f.write(scrapped_data)
    f.close()

page=requests.get(url)
# print(page.content)

soup=BeautifulSoup(page.content,"html.parser")
# print(soup)

lists=soup.find_all('li',class_="ef447dde")
# print(lists)

counter = 0
for list in lists:
    counter = counter+1
    price=list.find('span',class_="f343d9ce").text
    loction=list.find('div',class_="_162e6469").text
    update=list.find('div',class_="_08b01580").text
    scrapped_data=f"{counter}: Price is: {price}\n Location is: {loction}\n Last Update is:  {update}\n"  
    print(scrapped_data)    
    record()