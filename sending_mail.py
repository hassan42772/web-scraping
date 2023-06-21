from bs4 import BeautifulSoup
import requests 
import smtplib
import time 

# usd currency
usd_url="https://www.xe.com/currencyconverter/convert/?Amount=1&From=USD&To=PKR"
usd_page=requests.get(usd_url)
usd_soup=BeautifulSoup(usd_page.content,"html.parser")
usd_price=usd_soup.find('p',"result__BigRate-sc-1bsijpp-1 iGrAod").text
# ind currency
ind_url="https://www.xe.com/currencyconverter/convert/?Amount=1&From=INR&To=PKR"
ind_page=requests.get(ind_url)
ind_soup=BeautifulSoup(ind_page.content,"html.parser")
ind_price=ind_soup.find('p',"result__BigRate-sc-1bsijpp-1 iGrAod").text
# sar currency
sar_url="https://www.xe.com/currencyconverter/convert/?Amount=1&From=SAR&To=PKR"
sar_page=requests.get(sar_url)
sar_soup=BeautifulSoup(sar_page.content,"html.parser")
sar_price=sar_soup.find('p',"result__BigRate-sc-1bsijpp-1 iGrAod").text

# MYR currency
mar_url="https://www.xe.com/currencyconverter/convert/?Amount=1&From=MYR&To=PKR"
mar_page=requests.get(mar_url)
mar_soup=BeautifulSoup(mar_page.content,"html.parser")
mar_price=mar_soup.find('p',"result__BigRate-sc-1bsijpp-1 iGrAod").text
prices=f"USD_price is :{usd_price}\nIND_PRICE IS :{ind_price}\nSAR_PRICE IS :{sar_price}\nMAR_PRICE IS :{mar_price}\n"
print(prices)

while True:
	smt=smtplib.SMTP("smtp.gmail.com",587)
	smt.ehlo()
	smt.starttls()
	smt.login("ranahassan427726@gmail.com","nbebxkllbgcytukt")
	smt.sendmail("ranahassan427726@gmail.com","Sufyanrahman48@gmail.com",f"Subject:Rate alart of currency\n\n 1 usd value:{usd_price}PKR\n1 indian_rupees value:{ind_price}PKR\n1 saudi_arabian_riyal value:{sar_price}PKR\n1 malaysian_ringget value:{mar_price}\n")
	time.sleep(5)
