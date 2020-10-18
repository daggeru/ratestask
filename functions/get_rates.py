from functions.utils.prices import get_prices, get_averages
from functions.utils.locations import get_dest_codes, get_origin_codes


def get_rates_db(date_from: str, date_to: str, origin: str, destination: str) -> list:
    dest_codes = get_dest_codes(destination=destination)
    origin_codes = get_origin_codes(origin=origin)
    prices = get_prices(dest_codes=dest_codes, origin_codes=origin_codes, date_from=date_from, date_to=date_to)
    averages = get_averages(prices=prices)
    return averages


def get_rates_null_db(date_from: str, date_to: str, origin: str, destination: str) -> list:
    dest_codes = get_dest_codes(destination=destination)
    origin_codes = get_origin_codes(origin=origin)
    prices = get_prices(dest_codes=dest_codes, origin_codes=origin_codes, date_from=date_from, date_to=date_to)
    averages_null = get_averages(prices=prices, nullable=True)
    return averages_null
