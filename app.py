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


@app.route('/ergotool', methods=['POST'])
def get_ergotool():
    return {
        "response": "https://workday.okta.com/home/workdayprod_workdayonlineergotool_1/"
                    "0oa11pvpk7ter2pgx1e8/52283?fromHome=true"
    }


@app.route('/zoom', methods=['POST'])
def get_zoom():
    return {
        "response": ":rocket https://workday.okta.com/home/workdayprod_zoom_1/0oa1c5jdgpplBhdd51d8/aln1c5jzrfoz"
                    "vsT0C1d8?fromHome=true"
    }


@app.route('/peakon', methods=['POST'])
def get_peakon():
    return {
        "response": "https://workday.okta.com/home/peakon/0oa1isjt0i7FgeOSZ1d8/aln1dvyaylgKQA6qT1d8?fromHome=true"
    }


@app.route('/orbit', methods=['POST'])
def get_orbit():
    return {
        "response": "https://sites.google.com/workday.com/pt-early-talent-orbit/home"
    }
