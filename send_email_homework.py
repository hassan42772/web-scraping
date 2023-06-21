from bs4 import BeautifulSoup
import requests
import smtplib
import time
# united state dollar
usd_url="https://www.xe.com/currencyconverter/convert/?Amount=1&From=USD&To=PKR"
usd_page=requests.get(usd_url)
usd_soup=BeautifulSoup(usd_page.content,"html.parser")
usd_price=usd_soup.find('p',class_="result__BigRate-sc-1bsijpp-1 iGrAod").text
# British Pounds
gbr_url="https://www.xe.com/currencyconverter/convert/?Amount=1&From=GBP&To=PKR"
gbr_page=requests.get(gbr_url)
gbr_soup=BeautifulSoup(gbr_page.content,"html.parser")
gbr_price=gbr_soup.find('p',class_="result__BigRate-sc-1bsijpp-1 iGrAod").text
#  South Korean Won
skw_url="https://www.xe.com/currencyconverter/convert/?Amount=1&From=KRW&To=PKR"
skw_page=requests.get(skw_url)
skw_soup=BeautifulSoup(skw_page.content,"html.parser")
skw_price=skw_soup.find('p',class_="result__BigRate-sc-1bsijpp-1 iGrAod").text
# Sri Lankan Rupees
sri_url="https://www.xe.com/currencyconverter/convert/?Amount=1&From=LKR&To=PKR"
sri_page=requests.get(sri_url)
sri_soup=BeautifulSoup(sri_page.content,"html.parser")
sri_price=sri_soup.find('p',class_="result__BigRate-sc-1bsijpp-1 iGrAod").text

print(f"UNITED_STATE_DOLLAR_PRICE_IS:{usd_price}\nBRITISH_POND_PRICE_IS:{gbr_price}\nSOUTH_KOREAN_WON_PRICE_IS:{skw_price}\nSRI_LANKAN_PRICE_IS:{sri_price}\n")
# sending mail
while True:
	smt=smtplib.SMTP("smtp.gmail.com",587)
	smt.starttls()
	smt.ehlo()
	smt.login("ranahassan427726@gmail.com","nbebxkllbgcytukt")
	smt.sendmail("ranahassan427726@gmail.com","sufyanrahman48@gmail.com",f"Subject: sufi boo boo rate of currency is\n\n1 UNITED_STATE_DOLLAR_PRICE_IS:{usd_price}PKR\n1 BRITISH_POND_PRICE_IS:{gbr_price}PKR\n 1 SOUTH_KOREAN_WON_PRICE_IS:{skw_price}PKR\n1 SRI_LANKAN_PRICE_IS:{sri_price}PKR\n")
	time.sleep(10000)