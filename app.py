from flask import Flask, render_template, request
import os
import logging as logger
from utils import http_unprocessable_entity, http_bad_request
from controller import counter

BASE_URL = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__,
            static_url_path='',
            static_folder='views/static/', 
            template_folder='views/templates')


@app.route('/')
def index():
    args = {}
    return render_template('index.html', **args)

@app.route('/word_counter/', methods=['POST'])
def word_counter():
    try:
        request_data = request.get_json()
        return counter.parse_counters(request_data['message'])

    except TypeError as exception:
        return http_unprocessable_entity(str(exception), None)
    except ValueError as exception:
        return http_unprocessable_entity(str(exception), None)
    except KeyError as exception:
        return http_bad_request(f'missing key {str(exception)} in request JSON body', None)


app.run(app='0.0.0.0')
