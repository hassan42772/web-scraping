from bs4 import BeautifulSoup
import requests
import time 
import smtplib
from csv import writer
for i in range(1,5):
	url_lahore=f"https://www.pakwheels.com/used-cars/search/-/ct_lahore/?page={i}"
	lahore_page=requests.get(url_lahore)
	lahore_soup=BeautifulSoup(lahore_page.content,"html.parser")
	car_lahore=lahore_soup.find_all('div',class_="col-md-9 grid-style")
	with open("cars.csv","a",newline="")as f:
		thewter=writer(f)
		header=["lahore_car_name","lahore_car_price","lahore_car_update"]
		thewter.writerow(header)
		for cars in car_lahore:
			lahore_car_name=cars.find('a',class_="car-name ad-detail-path")
			lahore_car_name=lahore_car_name["title"]
			lahore_car_price=cars.find('div',class_="price-details generic-dark-grey").text.replace("\n\n","").replace("\n","").replace("  ","")
			lahore_car_update=cars.find('div',class_="pull-left dated").text
			info=[lahore_car_name,lahore_car_price,lahore_car_update]
			print(info)
			thewter.writerow(info)


