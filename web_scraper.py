import smtplib
import requests
from bs4 import BeautifulSoup



"""

"""


URL = 'https://www.game.es/VIDEOJUEGOS/ROL/PLAYSTATION-4/THE-WITCHER-3-WILD-HUNT-GOTY/129225'

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/92.0.4515.131 Safari/537.36'}





def check_price():
    """
    Parse the given URL
    :return: amount in euros for the specified item
    """
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    # with open('soup.txt', 'w') as s:
    #     s.write(str(soup))
    amount = 180

    try:
        price_span = soup.find('span', attrs={'class': 'int'}).get_text()
        int_price = [int(x) for x in price_span.split() if x.isdigit()][0]
        # amount = eval(price_in_euros[:3].replace(',', '.'))  # get rid of currency symbol and change the string to float
    except TypeError:
        print('exception when evaluating price')
    return int_price


def send_mail(price):
    server = smtplib.SMTP('smtp.gmail', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('username','password') # get values from credentials file here
    subject = 'Price fell down'
    body = f'Deskmini x300 is currently {price} at Amazon'
    message = f'Subject: {subject}\n\n{body}'
    server.sendmail('username', 'username', message)
    server.quit()

# TODO: add classes, add email & password


if __name__ == '__main__':
    print('main')
    check_price()
