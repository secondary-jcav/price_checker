import json
from price_check import PriceParser
from send_email import Emailer


if __name__ == '__main__':
    print('main')
    with open('config.json') as json_secrets:
        config = json.load(json_secrets)
    pc = PriceParser(config['URL'], config['headers'], config['amount'])
    if pc.check_price_is_lower():
        emailer = Emailer(config['username'], config['password'], config['destination_address'])
        if emailer.send_mail(config['amount']):
            print('mail sent')
    else:
        print(f'Price currently is not lower than {config["amount"]}')

