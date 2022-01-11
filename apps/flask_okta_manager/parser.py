from flask_restx import reqparse

okta_login_details = reqparse.RequestParser()
okta_login_details.add_argument('username', type=str, trim=True, required=True)
okta_login_details.add_argument('password', type=str, trim=True, required=True)