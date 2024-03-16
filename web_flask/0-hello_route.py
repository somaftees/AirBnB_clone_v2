#!/usr/bin/python3
""" flask app"""
from flask import Flask, render_template

app = Flask("__name__")


@app.route('/airbnb-onepage/', strict_slashes=False)
def home():
    """ home """
    return render_template("10-hbnb_filters.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
