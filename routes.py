from flask import request, Blueprint, render_template, redirect, url_for
import os.path
from json import dumps

from werkzeug.utils import redirect

from data import get_json_reponse


routes = Blueprint('routes', __name__)

# Upload folder
UPLOAD_FOLDER = 'csv'


@routes.route('/', methods=['GET', 'POST'])
def homepage():
    if request.method == 'POST':
        file = request.files['file']
        try:
            file.save(os.path.join(UPLOAD_FOLDER, file.filename))
            return redirect(url_for('routes.get_data', csv_file=file.filename))
        except FileNotFoundError:
            return render_template("index.html")
    return render_template('index.html')


@routes.route('/data/api/<csv_file>', methods=['GET'])
def get_data(csv_file):
    if request.method == 'GET':
        requesting_csv_file = './csv/{}'.format(csv_file)

        if os.path.isfile(requesting_csv_file):
            output = get_json_reponse(requesting_csv_file)
            return dumps(output)
        else:
            return dumps({
                'status_code': 404,
                'error_status': 'file not found'
            })
