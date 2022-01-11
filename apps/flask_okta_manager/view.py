from flask_restx import Namespace, Resource
from .parser import okta_login_details
from flask import request
import requests
from config.default import OKTA_ORG_URL
import logging
import json

ns_flask_okta = Namespace('flaskOktaApp', description='Flask okta integration application', ordered=True)
log = logging.getLogger(__name__)


@ns_flask_okta.route('/login')
class FlaskOkta(Resource):

    @ns_flask_okta.expect(okta_login_details, validate=True)
    def post(self):
        args = okta_login_details.parse_args(request, strict=True)
        headers = {'content_type': 'application/json', 'Accept': 'application/json'}
        endpoint = OKTA_ORG_URL + "/api/v1/authn"
        login_response = requests.post(endpoint, json={"username": args.get('username'), "password": args.get('password')}, headers=headers)
        if login_response.status_code == 200:
            return "Hello %s" %args.get('username')
        else:
            return "User not found"
