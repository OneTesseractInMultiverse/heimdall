from heimdall import (
    app,
    identities
)
from flask import (
    jsonify,
    request
)
from heimdall.models.identity import Identity


@app.route('/api/v1/identity', methods=['GET'])
def get_identities():
    try:
        query_string = request.args
        results = identities.query(query_string)
        return jsonify(results), 200
    except Exception as e:
        return jsonify({
            "msg": "Unable to complete request",
            "details": str(e)
        }), 500


@app.route('/api/v1/identity/<identity_id>', methods=['GET'])
def get_identity(identity_id):
    try:
        result = identities.get(entity_id=identity_id)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({
            "msg": "Unable to complete request",
            "details": str(e)
        }), 500


@app.route('/api/v1/identity', methods=['POST'])
def post_identity():
    try:
        if not request.is_json:
            return jsonify({
                "msg": "This API only supports JSON"
            }), 400
        data = request.get_json()

        identity = Identity(
            repository=identities,
            state=data
        )

        if not identity.state_valid:
            return jsonify({
                "msg": "Request is not valid",
                "errors": identity.model_errors
            }), 400

        if identity.save():
            return jsonify(identity.as_dict()), 201

        return jsonify({
            "error": "Unable to create identity definition",
            "errors": identity.model_errors
        }), 500

    except Exception as e:
        return jsonify({
            "msg": "Unable to complete request",
            "details": str(e)
        }), 500


@app.route('/api/v1/identity/<identity_id>', methods=['PUT'])
def put_identity(identity_id):
    try:
        if not request.is_json:
            return jsonify({
                "msg": "This API only supports JSON"
            }), 400
        data = request.get_json

        identity = Identity(
            repository=identities,
            state={"identity_id": identity_id}
        )

        identity.update(data)

        if identity.commit():
            return jsonify({
                "msg": "identity updated"
            }), 200

        return jsonify({
            "error": "Unable to update identity definition",
            "errors": identity.model_errors
        }), 500
    except Exception as e:
        return jsonify({
            "msg": "Unable to complete request",
            "details": str(e)
        }), 500
