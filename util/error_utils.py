from flask import jsonify

class ErrorUtil:

    def bad_request():
        message = {
            'status': 400,
            'message': 'Bad Request',
            'errors': 'Invalid Car Id',
        }
        response = jsonify(message)
        response.status_code = 400

        return response

    def not_found():
        message = {
            'status': 404,
            'message': 'Not Found',
            'errors': 'Car Does Not Exist'
        }
        response = jsonify(message)
        response.status_code = 404

        return response

    def internal_error():
        message = {
            'status': 500,
            'message': 'Internal Error',
            'errors': 'Unknown'
        }
        response = jsonify(message)
        response.status_code = 500

        return response
