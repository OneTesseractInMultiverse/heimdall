from heimdall import (
    app,
    applications
)
from flask import (
    jsonify,
    request
)


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
