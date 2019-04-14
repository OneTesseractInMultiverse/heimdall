from spartan import (
    app
)
from flask import (
    jsonify,
    request,
    url_for
)

from spartan.security.authorization import (
    require_claims
)
from flask_jwt_extended import (
    jwt_required
)


# --------------------------------------------------------------------------
# GET: /
# --------------------------------------------------------------------------
@app.route('/', methods=['GET'])
# @jwt_required
# @require_claims('can_create_data')
def get_root():
    return jsonify(
        {
            "ApiPlatform": "Spartan 1.0",
            "IP Address": request.remote_addr,
            "User Agent": request.headers.get('User-Agent')
        }
    ), 200




