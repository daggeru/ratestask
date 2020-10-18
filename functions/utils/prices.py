import os

from price_parser import Price as pp
import requests

from models.db_models import Prices


def price_converter(price: str) -> float:
    price_amount, price_currency = price_parser(price)

    if price_currency and price_currency != 'USD':
        app_id = os.getenv('APP_ID')
        openexchange_url = os.getenv('OPENEXCHANGERATES_URL')

        url = f'{openexchange_url}?app_id={app_id}'
        r = requests.get(url)
        rates = r.json()['rates']

        converted_price = price_amount / rates[price_currency]

        return round(converted_price, 2)
    else:
        return price_amount


def price_parser(price_to_parse: str) -> tuple:
    price = pp.fromstring(price_to_parse)
    return price.amount_float, price.currency


def get_prices(dest_codes: list, origin_codes: list, date_from: str, date_to: str) -> list:
    prices_list = []
    for origin in origin_codes:
        prices_orig = Prices.query.filter_by(orig_code=origin)
        for dest in dest_codes:
            prices_dest = prices_orig.filter_by(dest_code=dest)
            prices_day = prices_dest.filter(Prices.day >= date_from).filter(Prices.day <= date_to).all()
            prices_list.extend(prices_day)
    prices = [{'price': item.price, 'day': item.day} for item in prices_list]
    return prices


def get_averages(prices: list, nullable=None) -> list:
    averages = []
    total = 0
    count = 0
    date_range = sorted(set([price['day'] for price in prices]))

    for day in date_range:
        for item in prices:
            if item['day'] == day:
                total = (total + int(item['price']))
                count += 1

        if count == 0:
            continue
        elif nullable and count < 3:
            averages.append({'day': day.strftime("%Y-%m-%d"), 'average_price': None})
        else:
            averages.append({'day': day.strftime("%Y-%m-%d"), 'average_price': round(total / count, 2)})

        total = 0
        count = 0
    return averages
