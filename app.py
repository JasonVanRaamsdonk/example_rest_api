# export FLASK_APP=app.py | export FLASK_ENV=development
from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['POST'])
def index():
    return 'Hello!'


@app.route('/compass', methods=['POST'])
def get_compass():
    return {
        "response": "https://workday.okta.com/home/bookmark/0oa1fkw40y07zvRp11d8/2557?fromHome=true"
    }


@app.route('/workspace', methods=['POST'])
def get_workspace():
    return {
        "response": "https://workday.okta.com/home/salesforce/0oa1g76jnb5KnVX3w1d8/46?fromHome=true"
    }


@app.route('/nexus', methods=['POST'])
def get_nexus():
    return {
        "response": "https://workday.okta.com/home/oidc_client/0oa1iej9pbd7n9VrX1d8/aln177a159h7Zf52X0g8?fromHome=true"
    }
