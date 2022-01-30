import requests
from bs4 import BeautifulSoup


class PriceParser:
    """
    Uses BeautifulSoup to parse a given url and return product price
    """
    def __init__(self, url, headers, amount=40):
        self.last_price = amount
        self.current_price = amount
        self.url = url
        self.headers = headers

    def check_price_is_lower(self):
        """
        Parse the given URL
        :return: True if current price is lower than the one set in config
        """
        page = requests.get(self.url, headers=self.headers)
        soup = BeautifulSoup(page.content, 'html.parser')

        try:
            price_span = soup.find('span', attrs={'class': 'int'}).get_text()
            self.current_price = [int(x) for x in price_span.split() if x.isdigit()][0]
        except AttributeError:
            print(f'exception when evaluating price...{AttributeError}')
        return self.current_price < self.last_price
