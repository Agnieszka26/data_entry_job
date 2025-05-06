from bs4 import BeautifulSoup
import requests

url = 'https://appbrewery.github.io/Zillow-Clone/'

class CollectData:
    def __init__(self):
        html_doc = requests.get(url).text
        self.soup = BeautifulSoup(html_doc, 'html.parser')
        self.addresses =[]
        self.prices = []
        self.links = []
        self.data = []

    def collect_info(self):
        container = self.soup.find_all(name='ul')[2]
        info = container.find_all(name="li")
        for i in info:
            l = i.find("a")
            try:
                link = l.get("href")
            except AttributeError:
                link = "NONE"
            try:
                address = l.getText().strip().replace("|", "")
            except AttributeError:
                address = "NONE"
            try:
                price = i.find(name="div", class_="StyledPropertyCardDataArea-fDSTNn").getText().strip().split("+")[0].split("/")[0]
            except AttributeError:
                price = "None"
            if not price == "None":
                self.prices.append(price)
            self.addresses.append(address)
            self.links.append(link)

    def get_data(self):
        for idx, add in enumerate(self.addresses):
            if add != "NONE" or self.links[idx] != "NONE":
                self.data.append({
                    "address": add,
                    "link": self.links[idx],
                })
        for idx, d in enumerate(self.data):
            d.update({"price": self.prices[idx]})





