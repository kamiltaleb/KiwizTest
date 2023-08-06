from flasgger import Swagger
from flask import Flask

# Create the Flask app
def create_app():
    app = Flask(__name__)
    Swagger(app)
    from .routes import bp
    app.register_blueprint(bp)

    return app
