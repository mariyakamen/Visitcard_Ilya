from flask import Flask

from src.assemble import blob

app = Flask(__name__)


@app.route('/')
def hello_world():
    return blob

app.run(host='0.0.0.0')
