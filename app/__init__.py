from config import DevelopmentConfig
from flask import Flask
from flask_restful import Api

api = Api()

def create_app(config=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config)

    from app.component import component_blueprint
    api.init_app(component_blueprint)
    app.register_blueprint(component_blueprint, url_prefix='/component')

    return app
