from os.path import abspath, dirname
import sys
from get_best_sentences import generate_sentences
from flask import Flask, json, request, Response
import torch
import string
import random
from flask_cors import CORS, cross_origin
from data import Preprocess

app = Flask(__name__)
#app.config['JSON_AS_ASCII'] = False
cors = CORS(app, resources={r"/generate-questions": {"origins": "*"}, "/get-random-doc": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

sys.path.insert(0, dirname(dirname(abspath(__file__))))

@app.after_request
def after_request(response):
    header = response.headers
    header['Access-Control-Allow-Origin'] = '*'
    return response

@app.route("/")
def hello():
    return f"Hello, World!{torch.cuda.is_available()}"


@app.route("/generate-questions", methods=['POST', 'OPTIONS'])
@cross_origin(origin='*')
def generate_questions():
    if request.json:
        letters = string.ascii_letters
        file_name = ''.join(random.choice(letters) for i in range(10)) + ".json"
        file_path = f"./temp_files/{file_name}"
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(request.json, f, ensure_ascii=False, indent=4)
        dataset = Preprocess(file_path, 'dbmdz/bert-base-turkish-cased')
        dataset.save(f'../data/bert/dbmdz/bert-base-turkish-cased/requests/{file_name}')
        resp = json.dumps({"data":generate_sentences(file_name)}, ensure_ascii=False)
        response = Response(resp, content_type="application/json; charset=utf-8",status=200)
    else:
        response = Response(status=400)
    return response

@app.route("/get-random-doc", methods=['GET', 'OPTIONS'])
@cross_origin(origin='*')
def get_random_doc():
    f = open('../data/turquad/test_delex.json', "r")
    dataset = json.load(f)
    rand_doc = random.choice(dataset['data'])
    resp = json.dumps(rand_doc, ensure_ascii=False)
    response = Response(resp, content_type="application/json; charset=utf-8",status=200)
    return response


if __name__ == '__main__':
    print("App is now running on 0.0.0.0:5000 !")
    app.run('0.0.0.0', 5000, debug=True)
