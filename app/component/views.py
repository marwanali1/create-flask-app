from app import api
from flask_restful import Resource


class ComponentEndpoint(Resource):
    def get(self):
        response = {"isComponent": True}
        return response


api.add_resource(ComponentEndpoint, "/endpoint")
