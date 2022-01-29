import smtplib
import requests
from bs4 import BeautifulSoup
import json


def check_price_is_lower():
    """
    Parse the given URL
    :return: True if current price is lower than the one set in config
    """
    with open('config.json') as json_secrets:
        config = json.load(json_secrets)

    int_price = config['amount']
    page = requests.get(config['URL'], headers=config['headers'])
    soup = BeautifulSoup(page.content, 'html.parser')

    try:
        price_span = soup.find('span', attrs={'class': 'int'}).get_text()
        int_price = [int(x) for x in price_span.split() if x.isdigit()][0]
    except AttributeError as e:
        print(f'exception when evaluating price...{e}')
    return int_price < config['amount']


def send_mail():
    with open('config.json') as json_secrets:
        config = json.load(json_secrets)
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(config['username'], config['password'])
        subject = 'Price fell down'
        body = f'Test mail'
        message = f'Subject: {subject}\n\n{body}'
        server.sendmail(config['username'], config['destination_address'], message)
        server.quit()
    except smtplib.SMTPException as e:
        print(f'Something went wrong...{e}')


# TODO: add classes, add email & password


if __name__ == '__main__':
    print('main')
    if check_price_is_lower():
        send_mail()
        print('price is lower than 40')
