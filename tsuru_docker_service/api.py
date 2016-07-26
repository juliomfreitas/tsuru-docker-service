import os

import flask
import json

from flask import request

from .adapters import get_adapter, AdapterNotFound, adapters_mapping
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

    instance_name = request.form.get('name')
    if not instance_name:
        return "name of the instance is required", 400

    try:
        adapter = get_adapter(plan)
    except AdapterNotFound as exc:
        return exc.message, 400

    adapter.create_container(instance_name=instance_name)
    ContainerModel().create_from_adapter(adapter)

    return "", 201


@app.route("/resources/<name>", methods=["DELETE"])
def destroy_instance(name):
    data = ContainerModel().get(instance_name=name)
    try:
        adapter = get_adapter(data["name"], container_id=data['container_id'])
    except AdapterNotFound as exc:
        return exc.message, 400

    adapter.destroy_container()
    ContainerModel().destroy(instance_name=name)

    return "", 200


@app.route("/resources/<name>/status", methods=["GET"])
def status(name):
    return "", 500


@app.route("/resources/plans", methods=["GET"])
def plans():
    description_plans = [{"name": name, "description": ""}
                         for name in list(adapters_mapping.keys())]

    return json.dumps(description_plans), 200
