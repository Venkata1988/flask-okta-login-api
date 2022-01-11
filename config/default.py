FLASK_SERVER_NAME = "0.0.0.0"
FLASK_PORT_NO = 2022
FLASK_DEBUG = True
FLASK_ENDPOINT = "/v1/api"

#OKTA configuration
OIDC_CLIENT_SECRETS = "client_secrets.json"
OIDC_COOKIE_SECURE = False
OIDC_CALLBACK_ROUTE = "/oidc/callback"
OIDC_SCOPES = ["openid", "email", "profile"]
SECRET_KEY = "\xffI\x18M\x977\x19,\xd2|\x7f\xbc\xf6J\xc4%"
OIDC_ID_TOKEN_COOKIE_NAME = "oidc_token"
OKTA_ORG_URL = "https://dev-09805266.okta.com"
OKTA_AUTH_TOKEN = "00aYm1nS0zP0aeXhfATfgIgTWhYcoMsGmsOuylksKV"