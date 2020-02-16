import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
from botutils import date_and_time


def getCurrency():

    url = "https://kur.doviz.com/serbest-piyasa/amerikan-dolari"
    resp = requests.get(url)

    if resp.status_code == 200:
        print("Successfully opened the web page")
        print(date_and_time())
        soup=BeautifulSoup(resp.text,'html.parser')

        l = soup.find("div",{ "class" : "market-data"})

        for i,j in zip(l.findAll("span", {"class" : "value"}), l.findAll("span", {"class" : "name"})):
            print(j.text + " : ",end = '')
            print(i.text)
    else:
        print("Error")

getCurrency()
