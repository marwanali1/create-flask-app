from flask import Blueprint

component_blueprint = Blueprint('component', __name__)

from app.component import views
