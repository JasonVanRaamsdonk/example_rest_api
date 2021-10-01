# export FLASK_APP=app.py | export FLASK_ENV=development
from flask import Flask
import json

app = Flask(__name__)

with open("links.json") as json_file:
    jsonObject = json.load(json_file)
    json_file.close()


@app.route('/', methods=['POST'])
def index():
    return 'Hello!'


@app.route('/resourcehelp', methods=['POST'])
def get_help():
    return {
        "response": "Enter a command for a Workday Internal Service:\n"
                    "- `orbit`\n"
                    "- `nexus`\n"
                    "- `workspace`\n"
                    "- `ergotool`\n"
                    "- `zoom`\n"
                    "- `peakon`\n"
    }


@app.route('/compass', methods=['POST'])
def get_compass():
    return {
        "response": f"{jsonObject['compass']}"
    }


@app.route('/workspace', methods=['POST'])
def get_workspace():
    return {
        "response": f"{jsonObject['workspace']}"
    }


@app.route('/nexus', methods=['POST'])
def get_nexus():
    return {
        "response": f"{jsonObject['nexus']}"
    }


@app.route('/ergotool', methods=['POST'])
def get_ergotool():
    return {
        "response": f"{jsonObject['ergotool']}"
    }


@app.route('/zoom', methods=['POST'])
def get_zoom():
    return {
        "response": f"{jsonObject['zoom']}"
    }


@app.route('/peakon', methods=['POST'])
def get_peakon():
    return {
        "response": f"{jsonObject['peakon']}"
    }


@app.route('/orbit', methods=['POST'])
def get_orbit():
    return {
        "response": f"{jsonObject['orbit']}"
    }


@app.route('/covidpdf', methods=['POST'])
def get_s3_pdf():
    return {
        "response": f"{jsonObject['covidpdf']}"
    }