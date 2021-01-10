from flask import Blueprint
from flask_restful import Api
from .view import Blueprint1_Api

Blueprint1 = Blueprint("Blueprint1", __name__)

Blueprint1_restful_api = Api(Blueprint1)

Blueprint1_restful_api.add_resource(Blueprint1_Api, "/blueprint1_api")
