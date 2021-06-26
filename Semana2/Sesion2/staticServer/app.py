from flask import Flask
from flask import send_file
from flask.helpers import send_from_directory

app = Flask(__name__)
@app.route('/robots.txt')
def robots():
    return send_file('robots.txt')

@app.route('/assets/<path:filename>')
def assets(filename):
    return send_from_directory('assets', filename)

@app.route('/css/<name>.css')
def css(name):
    return send_from_directory('assets', f"{name}.css") 