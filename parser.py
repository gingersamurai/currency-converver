import json
from pprint import pprint
from unicodedata import decimal
import requests
from bs4 import BeautifulSoup
from decimal import Decimal



def convert(amount, cur_from, cur_to):
    data = parse()
    to_rub = lambda cnt, code: Decimal(str(cnt)) * Decimal(str(data['Valute'][code]['Value'])) / Decimal(str(data['Valute'][code]['Nominal']))
    from_rub = lambda cnt, res_code: Decimal(str(cnt)) / Decimal(str(data['Valute'][res_code]['Value'])) * Decimal(str(data['Valute'][res_code]['Nominal']))
    if cur_from != 'RUB':
        res = to_rub(amount, cur_from)
        amount = res
    if cur_to != 'RUB':
        res = from_rub(amount, cur_to)
    res = res.quantize(Decimal('1.0000'))
    return res
    

def parse() -> dict:
    data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
    return data.json()


if __name__ == '__main__':
    cur_from = input("введи какую валюту хотите поменять: ").upper()
    cur_to = input("введите, на какую валюту хотите поменять: ").upper()
    amount = input("введите количество вашей валюты: ")
    
    res = convert(amount, cur_from, cur_to)

    print(f'результат: {res} {cur_to}')
