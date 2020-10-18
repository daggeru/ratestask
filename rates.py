from flask import request, jsonify

from functions.get_rates import get_rates_db, get_rates_null_db
from functions.post_rates import post_rates_db
from webapp.app import app


@app.route('/')
def health():
    return jsonify('healthy'), 200


@app.route('/rates', methods=['GET'])
def get_rates():
    try:
        date_from = request.args['date_from']
        date_to = request.args['date_to']
        origin = request.args['origin']
        destination = request.args['destination']
    except KeyError:
        return jsonify({'error_message': 'Please provide all demanded data'}), 400
    rates = get_rates_db(
        date_from=date_from,
        date_to=date_to,
        origin=origin,
        destination=destination
    )
    return jsonify(rates), 200


@app.route('/rates_null', methods=['GET'])
def get_rates_null():
    try:
        date_from = request.args['date_from']
        date_to = request.args['date_to']
        origin = request.args['origin']
        destination = request.args['destination']
    except KeyError:
        return jsonify({'error_message': 'Please provide all demanded data'}), 400
    rates_null = get_rates_null_db(
        date_from=date_from,
        date_to=date_to,
        origin=origin,
        destination=destination
    )
    return jsonify(rates_null), 200


@app.route('/rates', methods=['POST'])
def post_rates():
    try:
        date_from = request.args['date_from']
        date_to = request.args['date_to']
        origin_code = request.args['origin_code']
        destination_code = request.args['destination_code']
        price = request.args['price']
    except KeyError:
        return jsonify({'error_message': 'Please provide all demanded data'}), 400
    post_rates_db(
        date_from=date_from,
        date_to=date_to,
        origin_code=origin_code,
        destination_code=destination_code,
        price=price
    )
    return jsonify("OK"), 200
