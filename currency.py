from bs4 import BeautifulSoup
import requests
import smtplib
import time
url_usd ="https://www.xe.com/currencyconverter/convert/?Amount=1&From=USD&To=PKR"
page_usd=requests.get(url_usd)
soup_usd=BeautifulSoup(page_usd.content,"html.parser")
usd=soup_usd.find('p',class_="result__BigRate-sc-1bsijpp-1 iGrAod").text


url_yuan ="https://www.xe.com/currencyconverter/convert/?Amount=1&From=CNY&To=PKR"
page_yuan=requests.get(url_yuan)
soup_yuan=BeautifulSoup(page_yuan.content,"html.parser")
yuan=soup_yuan.find('p',class_="result__BigRate-sc-1bsijpp-1 iGrAod").text



url_Kwacha ="https://www.xe.com/currencyconverter/convert/?Amount=1&From=ZMW&To=PKR"
page_kwacha=requests.get(url_Kwacha)
soup_Kwacha=BeautifulSoup(page_kwacha.content,"html.parser")
Kwacha=soup_Kwacha.find('p',class_="result__BigRate-sc-1bsijpp-1 iGrAod").text
print(usd, yuan, Kwacha)

while True:
    smt=smtplib.SMTP("smtp.gmail.com",587)
    smt.ehlo()
    smt.starttls()
    smt.login("chwaleednasir5@gmail.com","aigedagmgmgmpptk")
    smt.sendmail("chwaleednasir5@gmail.com","ranahassan427726@gmail.com",f"Subject:Rate alart of currency\n\n 1 usd value:{usd}PKR\n1 yuan value:{yuan}PKR\n1 Kwacha value:{Kwacha}PKR\n")
    time.sleep(5)