from flask import jsonify

class ErrorUtil:

    def bad_request(errors):
        message = {
            'status': 400,
            'message': 'Bad Request',
            'errors': str(errors) if errors else []
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

    def internal_error(errors):
        message = {
            'status': 500,
            'message': 'Internal Error',
            'errors': str(errors) if errors else []
        }
        response = jsonify(message)
        response.status_code = 500

        return response
