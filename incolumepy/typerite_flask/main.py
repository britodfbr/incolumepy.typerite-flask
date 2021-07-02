from flask import Flask
from incolumepy.typerite_flask.ext.webui.main import bp


def create_app():
    app = Flask(__name__)
    app.register_blueprint(bp)

    @app.route("/hello")
    def hello():
        return "<p>Hello, World!</p>"
    return app
