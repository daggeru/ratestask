from functions.utils.prices import price_converter
from functions.utils.times import get_time_delta
from models.db_models import Prices
from webapp.app import db


def post_rates_db(date_from: str, date_to: str, origin_code: str, destination_code: str, price: str) -> None:
    time_delta = get_time_delta(date_from, date_to)
    price_usd = price_converter(price)
    for day in time_delta:
        price_entry = Prices(
            orig_code=origin_code,
            dest_code=destination_code,
            day=day,
            price=price_usd
        )
        db.session.add(price_entry)
    db.session.commit()
