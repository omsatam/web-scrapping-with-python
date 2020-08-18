import requests
from bs4 import BeautifulSoup
import smtplib

url = 'https://www.amazon.in/Redmi-Note-Pro-Storage-Processor/dp/B07X4PKGSN'

headers = {'user agent':'Mozilla/5.0 (Linux; Android 9; Redmi 6 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36'}
def check_price():
	web = requests.get(url,headers = headers).text
	soup = BeautifulSoup(web,'html.parser')
	soup.prettify()
	price = soup.find(id ="priceblock_dealprice")
	price = price.get_text()
	print(price)
	actual_price = float(price[2:4])
	print(actual_price)
	if actual_price > 15 :
		send_mail()

def send_mail():
	server = smtplib.SMTP('smtp.gmail.com',587)
	server.ehlo()
	server.starttls()
	server.ehlo()
	
	server.login('satamom254@gmail.com','ydcpkkzqtdwndcqs')
	subject = 'Price fell down'
	body = 'Hey the product you are looking for is now in your budget. Check the link given below  https://www.amazon.in/Redmi-Note-Pro-Storage-Processor/dp/B07X4PKGSN'
	
	message = f'subject:{subject} \n\n {body}'
	server.sendmail(
	'satamom254@gmail.com',
	'omsatam1005@gmail.com',
	message
	)
	print('Email has been sent successfully')
	server.quit()
	
check_price()