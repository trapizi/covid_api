import os.path

from flask import request, Blueprint, render_template, redirect, url_for
from json import dumps
from werkzeug.utils import redirect

from data import get_json_reponse


routes = Blueprint('routes', __name__)


@routes.route('/data/api/<csv_file>', methods=['GET'])
def get_data(csv_file):
    if request.method == 'GET':
        requesting_csv_file = './csv/{}'.format(csv_file)
        try:
            output = get_json_reponse(requesting_csv_file)
            return dumps(output)
        except FileNotFoundError:
            return dumps ({
                'status_code': 404,
                'error_status' : 'File not found'
            })