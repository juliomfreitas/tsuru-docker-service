import os

import flask
from flask import request

from .adapters import get_adapter
from .model import ContainerModel

app = flask.Flask(__name__)
app.debug = os.environ.get('DEBUG', '0') in ('true', 'True', '1')


@app.route("/resources/<name>/bind-app", methods=["POST"])
def bind_app(name):
    return "", 201


@app.route("/resources/<name>/bind-app", methods=["DELETE"])
def unbind_app(name):
    return "", 200


@app.route("/resources/<name>/bind", methods=["POST"])
def bind_unit(name):
    return "", 201


@app.route("/resources/<name>/bind", methods=["DELETE"])
def unbind_unit(name):
    return "", 200


@app.route("/resources", methods=["POST"])
def add_instance():
    plan = request.form.get('plan')

    if not plan:
        return "plan is required", 400

    adapter = get_adapter(plan)

    container = adapter.create_container()

    ContainerModel.create(container)

    return "", 201


@app.route("/resources/<name>", methods=["DELETE"])
def remove_instance(name):
    return "", 200


@app.route("/resources/<name>/status", methods=["GET"])
def status(name):
    return msg, 500


@app.route("/resources/plans", methods=["GET"])
def plans():
    return json.dumps(active_plans()), 200
