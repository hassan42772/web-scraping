from bs4 import BeautifulSoup
import requests 
import time
import smtplib
from csv import writer
for i in range(1,5):
	url_lahore=f"https://www.pakwheels.com/used-cars/search/-/ct_lahore/?page={i}"
	lahore_page=requests.get(url_lahore)
	lahore_soup=BeautifulSoup(lahore_page.content,"html.parser")
	lahore_cars=lahore_soup.find_all('div',class_="col-md-9 grid-style")
	with open("cars.csv","a",newline="")as f:
		cars_csv=writer(f)
		header=["car_name","car_price","car_update"]
		cars_csv.writerow(header)
		for cars in lahore_cars:
			car_name=cars.find('a',class_="car-name ad-detail-path")
			car_name=car_name["title"]
			car_price=cars.find('div',class_="price-details generic-dark-grey").text.replace("\n\n","").replace("   ","").replace("\n","")
			car_update=cars.find('div',class_="pull-left dated").text
			scrapped_car_data=[car_name,car_price,car_update]
			print(scrapped_car_data)
			cars_csv.writerow(scrapped_car_data)
