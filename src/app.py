from flask import Flask

from src.assemble import blob

app = Flask(__name__)


@app.route('/')
def hello_world():
    return blob

def launch():
    from waitress import serve
    serve(app, host="0.0.0.0", port=80)
