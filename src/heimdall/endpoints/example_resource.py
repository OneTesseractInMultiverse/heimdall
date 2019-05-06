from heimdall import (
    app
)
from flask import (
    jsonify,
    request,
    url_for
)

from heimdall.security.authorization import (
    require_claims
)
from flask_jwt_extended import (
    jwt_required
)

from heimdall import db
from heimdall.persistence.repositories.identity_group_repository import IdentityGroupRepository

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


@app.route('/test', methods=['GET'])
def test_get_applications():
    application_repository = IdentityGroupRepository(db=db)
    return jsonify(
        application_repository.query({})
    )




