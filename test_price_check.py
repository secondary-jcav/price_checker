import json
from price_check import PriceParser


def test_initial_amount():
    with open('config.json') as json_secrets:
        config = json.load(json_secrets)
    pc = PriceParser(config['URL'],config['headers'])
    assert pc.last_price == 40


def test_parse():
    with open('config.json') as json_secrets:
        config = json.load(json_secrets)
    pc = PriceParser(config['URL'],config['headers'])
    assert pc.check_price_is_lower()