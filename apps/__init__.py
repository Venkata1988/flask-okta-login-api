import logging
from flask import Blueprint
from flask_restx import Api
from apps.flask_okta_manager.view import ns_flask_okta
from config.default import FLASK_ENDPOINT

log = logging.getLogger(__name__)
blueprint = Blueprint('api', __name__, url_prefix=FLASK_ENDPOINT)
api = Api(version='1.0', title='Flask Okta Manager', doc='/docs', description='Flask Okta integration API', ordered=True)
api.init_app(blueprint)
api.add_namespace(ns_flask_okta)
