from datetime import date, timedelta


def convert_date(given_date: str) -> date:
    given_date = given_date.split("-")
    req_date = [int(item.lstrip('0')) for item in given_date]
    return date(*req_date)


def get_time_delta(date_from: str, date_to: str) -> list:
    date_from = convert_date(date_from)
    date_to = convert_date(date_to)

    delta = date_to - date_from

    days = []

    for item in range(delta.days + 1):
        day = date_from + timedelta(days=item)
        days.append(day)

    return days
