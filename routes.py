from flask import request, Blueprint, render_template
import os.path
from json import dumps

from data import get_json_reponse


routes = Blueprint('routes', __name__)

# Upload folder
UPLOAD_FOLDER = 'csv'


@routes.route('/', methods=['GET', 'POST'])
def homepage():
    if request.method == 'POST':
        file = request.files['file']
        file.save(os.path.join(UPLOAD_FOLDER, file.filename))
    return render_template('index.html')




@routes.route('/data/api/', methods=['GET', 'POST'])
def get_data():
    if request.method == 'GET':
        requesting_csv_file = './csv/{}'.format(request.args.get('file'))

        if os.path.isfile(requesting_csv_file):
            output = get_json_reponse(requesting_csv_file)
            return dumps(output)
        else:
            return dumps({
                'status_code': 404,
                'error_status': 'file not found'
            })
