import os
import datetime

import pytest

from functions.utils.prices import price_parser, get_averages, price_converter

os.environ['OPENEXCHANGERATES_URL'] = 'https://openexchangerates.org/api/historical/2013-02-16.json'


@pytest.mark.parametrize('price, expected', [
    ('1234', 1234.0),
    ('1234 PLN', 393.85),
    ('1234PLN', 393.85),
    ('1234 EUR', 1649.5)
])
def test_price_converter(price, expected):
    assert price_converter(price) == expected


@pytest.mark.parametrize('price, expected', [
    ('1234', (1234.0, None)),
    ('1234,0PLN', (1234.0, 'PLN')),
    ('1234.0PLN', (1234.0, 'PLN')),
    ('1234.0 PLN', (1234.0, 'PLN')),
    ('1234,0 PLN', (1234.0, 'PLN')),
    ('PLN 1234', (1234.0, 'PLN'))
])
def test_price_parser(price, expected):
    assert price_parser(price) == expected


@pytest.mark.parametrize('prices, nullable, expected', [
    ([{'price': 736, 'day': datetime.date(2016, 1, 1)}, {'price': 710, 'day': datetime.date(2016, 1, 1)},
      {'price': 1200, 'day': datetime.date(2016, 1, 1)}, {'price': 736, 'day': datetime.date(2016, 1, 2)},
      {'price': 710, 'day': datetime.date(2016, 1, 2)}, {'price': 1200, 'day': datetime.date(2016, 1, 2)},
      {'price': 736, 'day': datetime.date(2016, 1, 3)}, {'price': 710, 'day': datetime.date(2016, 1, 3)},
      {'price': 1200, 'day': datetime.date(2016, 1, 3)}, {'price': 736, 'day': datetime.date(2016, 1, 4)}],
     None,
     [{'average_price': 882.0, 'day': '2016-01-01'},
      {'average_price': 882.0, 'day': '2016-01-02'},
      {'average_price': 882.0, 'day': '2016-01-03'},
      {'average_price': 736.0, 'day': '2016-01-04'}]
     ),
    ([{'price': 736, 'day': datetime.date(2016, 1, 1)}, {'price': 710, 'day': datetime.date(2016, 1, 1)},
      {'price': 1200, 'day': datetime.date(2016, 1, 1)}, {'price': 736, 'day': datetime.date(2016, 1, 2)},
      {'price': 1200, 'day': datetime.date(2016, 1, 1)}, {'price': 736, 'day': datetime.date(2016, 1, 2)},
      {'price': 710, 'day': datetime.date(2016, 1, 2)}, {'price': 1200, 'day': datetime.date(2016, 1, 2)},
      {'price': 736, 'day': datetime.date(2016, 1, 3)}, {'price': 710, 'day': datetime.date(2016, 1, 3)},
      {'price': 1200, 'day': datetime.date(2016, 1, 3)}, {'price': 736, 'day': datetime.date(2016, 1, 4)}],
     True,
     [{'average_price': 961.5, 'day': '2016-01-01'},
      {'average_price': 845.5, 'day': '2016-01-02'},
      {'average_price': 882.0, 'day': '2016-01-03'},
      {'average_price': None, 'day': '2016-01-04'}]
     ),
])
def test_get_averages(prices, nullable, expected):
    assert get_averages(prices, nullable) == expected
