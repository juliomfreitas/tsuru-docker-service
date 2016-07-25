# coding: utf-8

import flask
import os

app = flask.Flask(__name__)
app.debug = os.environ.get('DEBUG', '0') in ('true', 'True', '1')


@app.route("/resources/<name>/bind-app", methods=["POST"])
def bind_app(name):
    pass


@app.route("/resources/<name>/bind-app", methods=["DELETE"])
def unbind_app(name):
    pass


@app.route("/resources/<name>/bind", methods=["POST"])
def bind_unit(name):
    pass


@app.route("/resources/<name>/bind", methods=["DELETE"])
def unbind_unit(name):
    pass


@app.route("/resources", methods=["POST"])
def add_instance():
    pass


@app.route("/resources/<name>", methods=["DELETE"])
def remove_instance(name):
    pass


@app.route("/resources/<name>/status", methods=["GET"])
def status(name):
    pass


@app.route("/resources/plans", methods=["GET"])
def plans():
    pass
