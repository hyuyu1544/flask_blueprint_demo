from flask import Blueprint
from flask_restful import Api
from .view import Blueprint2_Api

Blueprint2 = Blueprint("Blueprint2", __name__)

Blueprint2_restful_api = Api(Blueprint2)

Blueprint2_restful_api.add_resource(Blueprint2_Api, "/blueprint2_api")
