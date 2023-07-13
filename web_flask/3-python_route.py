#!/usr/bin/python3
"""3. Python is cool! - starts a
Flask web application: must be
listening on 0.0.0.0, port 50003
New route - /python/<text>: display “Python ”,
followed by the value of the text variable"""


from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_world():
    """Returns a string"""
    return "Hello HBNB!"


@app.route('/hbnb')
def hello():
    """Return a string"""
    return "HBNB"


@app.route('/c/<text>')
def c_text(text):
    """display “C ” followed by the
    value of the text variable """
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


@app.route('/python/')
@app.route('/python/<text>')
def python_text(text='is cool'):
    """display “Python ”, followed by the value
    of the text variable"""
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
