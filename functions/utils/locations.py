from models.db_models import Ports


def get_dest_codes(destination: str) -> list:
    dest_codes_db = Ports.query.filter_by(parent_slug=destination).all()
    if dest_codes_db:
        dest = [item.code for item in dest_codes_db]
        return dest
    else:
        return [destination]


def get_origin_codes(origin: str) -> list:
    origin_codes_db = Ports.query.filter_by(parent_slug=origin).all()
    if origin_codes_db:
        origin = [item.code for item in origin_codes_db]
        return origin
    else:
        return [origin]