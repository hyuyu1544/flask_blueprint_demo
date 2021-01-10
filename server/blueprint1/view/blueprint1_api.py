from flask_restful import Resource


class Blueprint1_Api(Resource):
    def get(self):
        return {
            'status': 'ok',
            'context': 'GET method for Blueprint1_Api.',
        }

    def post(self):
        return {
            'status': 'ok',
            'context': 'POST method for Blueprint1_Api.',
        }
