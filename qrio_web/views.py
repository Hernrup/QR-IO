from . import app
from flask import make_response, request, jsonify
from qrio_utils import qr, io as input_util
import logging as log
from os import path

@app.route('/v1/qr/', methods=['GET'])
def show_qr_code_from_data():
    data = request.args['data']
    log.debug('QR code requested for: {}'.format(data))
    image = qr.generate_qr_image_to_memory(data)
    response = make_response(image)
    response.headers['Content-Type'] = 'image/svg+xml'
    return response


@app.route('/v1/input/', methods=['POST'])
def input_request():
    print(request.json)
    data = request.json.get('data')
    log.debug('Input data recieved: {}'.format(data))
    if data:
        input_util.send_keys(data)
    return jsonify({'success': True})


@app.route('/v1/connect/')
def show_system_qrcode():
    base_url = app.external_uri if app.external_uri else request.host_url
    data = '{}/v1/input/'.format(base_url)
    log.debug('Connect QR code requested for: {}'.format(data))
    image = qr.generate_qr_image_to_memory(data)
    response = make_response(image)
    response.headers['Content-Type'] = 'image/svg+xml'
    return response


@app.route('/v1/sl4a/')
def show_sl4a_qrcode():
    with open(path.abspath(path.join('sl4a', 'QR-IO.py')), "r") as f:
        data = f.readlines()
    base_url = app.external_uri if app.external_uri else request.host_url
    log.debug('sl4a QR code requested')
    image = qr.generate_qr_image_to_memory(data, error='L')
    response = make_response(image)
    response.headers['Content-Type'] = 'image/svg+xml'
    return response