from bs4 import BeautifulSoup
import requests

url="https://www.zameen.com/Homes/Bahawalnagar-557-1.html"

def record():
	f=open("hassan .txt","a")
	f.write(scraped_data)
	f.close()
page=requests.get(url)
# print(page.content)
soup=BeautifulSoup(page.content,"html.parser")
# print(soup)
lists=soup.find_all('li',class_="ef447dde")
# print(lists)
counter=0
for list in lists:
	counter=counter+1
	price=list.find('span',class_="f343d9ce").text
	location=list.find('div',class_="_162e6469").text
	last_update=list.find('div',class_="_08b01580").text
	marla=list.find('span',class_="_984949e5").text
	scraped_data=f"{counter}: price is:{price}\nLocation is:{location}\nlast_update is :{last_update}\nmarla is :{marla}\n"
	print(scraped_data)
	record()