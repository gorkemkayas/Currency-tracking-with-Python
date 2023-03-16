import requests
from bs4 import BeautifulSoup
import time



while True:
    url = "https://www.doviz.com"
    response = requests.get(url)
    html_content = response.content
    type = []
    value = []
    soup = BeautifulSoup(html_content,"html.parser")
    for j in (soup.find_all("span",{"class":"name"})):
        type.append(j.text)
    for k in (soup.find_all("span",{"class":"value"})):
        value.append(k.text)
    for n in zip(type,value):
        print(n[0],": ",n[1])
        time.sleep(1.5)
    print("\n")


