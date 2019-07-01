from heimdall import (
    app,
    applications
)
from flask import (
    jsonify,
    request
)
from heimdall.models.application import Application


@app.route('/api/v1/application', methods=['GET'])
def get_applications():
    try:
        query_string = request.args
        results = applications.query(query_string)
        return jsonify(results), 200
    except Exception as e:
        return jsonify({
            "msg": "Unable to complete request",
            "details": str(e)
        }), 500


@app.route('/api/v1/application/<application_id>', methods=['GET'])
def get_application(application_id):
    try:
        result = applications.get(entity_id=application_id)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({
            "msg": "Unable to complete request",
            "details": str(e)
        }), 500


@app.route('/api/v1/application', methods=['POST'])
def post_application():
    try:

        if not request.is_json:
            return jsonify({
                "msg": "This API only supports JSON"
            }), 400
        data = request.get_json()

        application = Application(
            repository=applications,
            state=data
        )

        if not application.state_valid:
            return jsonify({
                "msg": "Request is not valid",
                "errors": application.model_errors
            }), 400

        if application.save():
            return jsonify(application.as_dict()), 201

        return jsonify({
            "error": "Unable to create application definition",
            "errors": application.model_errors
        }), 500

    except Exception as e:
        return jsonify({
            "msg": "Unable to complete request",
            "details": str(e)
        }), 500


@app.route('/api/v1/application/<application_id>', methods=['PUT'])
def put_application(application_id):
    try:

        if not request.is_json:
            return jsonify({
                "msg": "This API only supports JSON"
            }), 400
        data = request.get_json()

        application = Application(
            repository=applications,
            state={"application_id": application_id}
        )

        application.update(data)

        if application.commit():
            return jsonify({
                "msg": "application updated"
            }), 200

        return jsonify({
            "error": "Unable to create application definition",
            "errors": application.model_errors
        }), 500

    except Exception as e:
        return jsonify({
            "msg": "Unable to complete request",
            "details": str(e)
        }), 500