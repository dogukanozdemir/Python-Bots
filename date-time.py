import requests
from bs4 import BeautifulSoup

def date_and_time():
    url = "https://www.timeanddate.com/worldclock/timezone/utc3"
    resp = requests.get(url)

    if resp.status_code == 200:
        soup=BeautifulSoup(resp.text,'html.parser')
        # time
        dateres = soup.find("div", {"class" : "three columns tc"})
        time = dateres.find("span").text
        date = dateres.find("p").text

        return str(date + " - " + time)
    else:
        return None
