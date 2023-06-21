from bs4 import BeautifulSoup
import requests
import smtplib 
import time
from csv import writer
for i in range(1,4):
	zameen_url=f"https://www.zameen.com/Homes/Bahawalnagar-557-{i}.html?load_all_prop=1"
	zameen_page=requests.get(zameen_url)
	zameen_soup=BeautifulSoup(zameen_page.content,"html.parser")
	bwn_zameen=zameen_soup.find_all('div',class_="_732aff15 c7b81b5c")
	with open("zameen.csv","a",newline="")as f:
		zmn=writer(f)
		header=["PRICE","LOCATION","UPDATE"]
		zmn.writerow(header)
		for zameen in bwn_zameen:
			price=zameen.find('div',class_="_7ac32433").text
			location=zameen.find('div',class_="_162e6469").text
			update=zameen.find('span',class_="d77ff1d8").text
			info=[price,location,update]
			print(info)
			zmn.writerow(info)


