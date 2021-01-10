from flask_restful import Resource


class Blueprint2_Api(Resource):
    def get(self):
        return {
            'status': 'ok',
            'context': 'GET method for Blueprint2_Api.',
        }

    def post(self):
        return {
            'status': 'ok',
            'context': 'POST method for Blueprint2_Api.',
        }
