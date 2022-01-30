import json
from send_email import Emailer


def test_send_email():
    with open('config.json') as json_secrets:
        config = json.load(json_secrets)
    emailer = Emailer(config['username'], config['password'], 'jcarellanov@gmail.com')
    assert emailer.send_mail()
