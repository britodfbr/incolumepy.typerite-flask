from flask import Flask
from incolumepy.typerite_flask.ext.webui.main import bp
from incolumepy.typerite_flask.ext import webui


def minimal_app():
    app = Flask(__name__)
    # app.register_blueprint(bp)

    @app.route("/hello")
    def hello():
        return "<p>Hello, World!</p>"
    return app


def create_app():
    app = minimal_app()
    webui.init_app(app)
    return app
