from flask import Flask
from flask_cors import CORS
from werkzeug.middleware.proxy_fix import ProxyFix
from apps import blueprint as app_v1
import os

port = int(os.getenv('APP_PORT', 2022))
project_root = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__, instance_relative_config=False)
app.config['BUNDLE_ERRORS'] = True
app.config.from_object('config.default')
app.wsgi_app = ProxyFix(app.wsgi_app)
app.app_context()
CORS(app_v1, supports_credentials=True)
app.register_blueprint(app_v1)



def main():
    app.run(port=port)


if __name__ == '__main__':
    main()