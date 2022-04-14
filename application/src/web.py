from flask import Flask, request
import string_transform

api = Flask(__name__)


@api.route('/api/health', methods=['GET'])
def get_health():
    return {"status": "ok"}


@api.route('/api/mirror', methods=['GET'])
def get_mirror():
    word = request.args.get("word")
    return {"transformed": string_transform.transform(word)}


# todo: port put in env var
# todo: host put in env var
HOST = '0.0.0.0'
PORT = 4545

if __name__ == '__main__':
    api.run(host=HOST, port=PORT)
