from flask import Flask, render_template


def create_app():
    app = Flask(__name__)

    @app.route("/hello")
    def hello():
        return "<p>Hello, World!</p>"
    return app
