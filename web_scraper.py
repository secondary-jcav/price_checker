import requests
from bs4 import BeautifulSoup
import smtplib


URL = 'https://www.amazon.es/ASRock-90BXG3T01-A10GA0W-Barebone-Deskmini-X300/dp/B08NWHGTQQ/ref=sr_1_1?__mk_es_ES=' \
      '%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=deskmini+x300&qid=1630844246&sr=8-1'

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/92.0.4515.131 Safari/537.36'}


def check_price():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    amount = 180

    try:
        price_in_euros = soup.find(id='priceblock_ourprice').get_text()
        amount = eval(price_in_euros[:3].replace(',', '.'))  # get rid of currency symbol and change the string to float
    except TypeError:
        print('exception when evaluating price')
    return amount


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



