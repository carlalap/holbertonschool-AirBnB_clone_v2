#!/usr/bin/python3
"""9-cities_by_states.py
Script that starts a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """Remove the current SQLAlchemy Session after each request."""
    storage.close()


@app.route('/states', strict_slashes=False)
def display_states():
    """Display a HTML page with a list of all states."""
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def display_cities_by_states(id):
    """Display a HTML page with the state list by id integer"""
    states = storage.all(State).values()
    for state in states:
        if state.id == id:
            return render_template('9-states.html', state=state)
    return render_template('9-states.html', state=None)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
