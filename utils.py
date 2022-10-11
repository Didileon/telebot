import requests
import json
from configu import keys



class APIException(Exception):
    pass

class Converter:
    @staticmethod
    def get_price(base, quote, amount):
        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIException (f'Не удалось обработать валюту {base}')
        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {quote}')

        if base == quote:
            raise APIException(f'Невозможно провести одинаковые валюты {base}.')

        try:
            amount = float(amount.replace(',', '.'))
        except ValueError:
            raise APIException(f'Не удалось обработать количество {amount}')


        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        resp = json.loads(r.content)
        new_price = resp[base_ticker] * amount
        new_price = round(new_price, 3)
        message = f'Цена {amount} {base} в  {quote} : {new_price}'
        return message

