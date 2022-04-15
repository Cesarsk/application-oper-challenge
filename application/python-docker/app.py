import random

from flask import Flask, request
import string_transform, s3, file

api = Flask(__name__)


@api.route('/api/health', methods=['GET'])
def get_health():
    return {"status": "ok"}


@api.route('/api/mirror', methods=['GET'])
def get_mirror():
    word = request.args.get("word")
    return {"transformed": string_transform.transform(word)}


@api.route('/api/upload-random', methods=['POST'])
def post_upload_random():
    min = 0
    max = 9999
    random_number = str(random.randint(min, max))
    filename = f'{random_number}.txt'
    file.create_file(filename, random_number)
    s3.upload_file(file_name=filename, bucket='oper-random-numbers')
    return {"uploaded": "ok"}