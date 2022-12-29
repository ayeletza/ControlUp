
# Imports:
import urllib.request
from bs4 import BeautifulSoup
import urllib
from Constants import WEB_CLASS, HIGHEST_PRICE_TTL, LOWEST_PRICE_TTL, AVG_PRICE_TTL


class STN:
    '''
    A class to connect a website using a given url and read data from the website.
    '''
    def __init__(self):
        #Scrape Overcast zap url
        self.opener = urllib.request.build_opener()
        self.opener.addheaders = [('User-agent', 'Mozilla/5.0')]

    def web_opener(self, url):
        '''
        A function to open website and convert it into lxml file.
        :param url: a url to open.
        :return: None.
        '''
        self.response = self.opener.open(url)
        self.text_url = self.response.read()
        self.xml_data = BeautifulSoup(self.text_url, 'lxml')

    def get_prices(self):
        '''
        A function to read specific data from the website and calculate the required data.
        :return: A dictionary contains the required data.
        '''
        table = self.xml_data.select(WEB_CLASS)
        raw_costs = [float(ele.text.split()[0].replace(',', '')) for ele in table]
        hp = max(raw_costs)
        lp = min(raw_costs)
        ap = sum(raw_costs) / len(raw_costs)
        return {HIGHEST_PRICE_TTL: hp, LOWEST_PRICE_TTL: lp, AVG_PRICE_TTL: ap}
