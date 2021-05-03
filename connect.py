from flask import render_template
from flask.app import Flask
from get_api import get_data, data_header


data = get_data()
app = Flask(__name__)


@app.route('/home')
def home():
    return render_template('home.html', data=data, header=data_header, k=list(data.keys()))


# @app.route('/home')
# def home():
#     return '<h2>Hello world</h2>'


if __name__ == "__main__":
    app.run(debug=True)
