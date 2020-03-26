import json
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template("base1.html")


@app.route('/member')
def member():
    return render_template("card.html", team=data)


if __name__ == '__main__':
    with open("templates/team.json", encoding='utf-8') as write_file:
        data = json.load(write_file)
    app.run(port=8080, host='127.0.0.1')
