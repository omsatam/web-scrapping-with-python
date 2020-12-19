from plyer import notification
import requests
import time
from bs4 import BeautifulSoup

def notifyme( title,message):
    notification.notify(
    title = title,
    message = message,
    app_icon = 'icon.ico',
    timeout = 15
    )

def getData(url):
    r = requests.get(url)
    return r.text

#corona_data = getData('https://www.worldometers.info/coronavirus/')
 
if __name__ == "__main__":
    # notifyme('om','lets complete projects together')
    
    corona_data = getData('https://www.mohfw.gov.in/')
    # print(corona_data)
    soup = BeautifulSoup(corona_data,'html.parser')
    # print(soup.prettify())
    data = ''
    for tr in soup.find('table').find_all('tr')   : 
        data += tr.get_text()
        data = data.split('\n\n')
        data = data[1:]
        # for item in data:
        #     print(item)

states = ['maharashtra','telangana','uttarpradesh','bihar']

for item in data:
    datalist = item.split('\n')
    if datalist in states:
        text = f'State {datalist[1]}\nIndian : {datalist[2]} & Foreign : {datalist[3]}\nCured : {datalist[4]}\nDeaths : {datalist[5]}'
        notifyme("Cases of covid19" ,text)
time.sleep(3600)