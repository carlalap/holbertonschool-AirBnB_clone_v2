#!/usr/bin/python3
"""5. Number template! - starts a
Flask web application:...
display a HTML page only if n is an intege"""


from flask import Flask
from flask import render_template


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


@app.route('/number/<int:n>')
def number_text(n):
    """display “n is a number” only
    if n is an integer"""
    n = str(n)
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>')
def html_num(n):
    """display a HTML page only if n is an integer"""
    n = str(n)
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<n>')
def number_odd_or_even(n):
    """display a HTML page only if n is an integer
    odd_or_even """
    if n % 2 == 0:
        number_type = 'even'
    else:
        number_type = 'odd'
    return render_template('6-number_odd_or_even',
                           number=n, number_type=number_type)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
