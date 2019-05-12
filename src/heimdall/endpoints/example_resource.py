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
from heimdall.persistence.repositories.application_repository import ApplicationRepository

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
    application_repository = ApplicationRepository(db=db)
    return jsonify(
        application_repository.query({})
    )


@app.route('/test/<entity_id>', methods=['GET'])
def test_get_application(entity_id):
    application_repository = ApplicationRepository(db=db)
    return jsonify(
        application_repository.get(entity_id)
    )


@app.route('/test/create', methods=['POST', 'GET'])
def test_create_application():
    state_data = {
        'name': 'Application #1',
        'description': 'Description placeholder',
        'callback_url': 'http://test.test.com/',
        'public_key': '78r34hy7u8or3ef4',
        'private_key': '0y7u8r3q4hy7u8i',
        'environment': 'Lorem ipsum',
        'configuration': {"version": '1.0'},
        'is_enabled': 'true'
    }
    application_repository = ApplicationRepository(db=db)
    return jsonify(
        application_repository.create(state_data)
    )


@app.route('/test/update/<entity_id>', methods=['PUT'])
def test_update_application(entity_id):
    state_data = {
        'name': 'Application #1',
        'description': 'this description has been changedc',
        'callback_url': 'http://test.test.com/',
        'public_key': '78r34hy7u8or3ef4',
        'private_key': '0y7u8r3q4hy7u8i',
        'environment': 'Lorem ipsum',
        'configuration': {"version": '1.1'},
        'is_enabled': bool('true')
    }
    application_repository = ApplicationRepository(db=db)
    return jsonify(
        application_repository.update(entity_id, state_data)
    )


@app.route('/test/delete/<entity_id>', methods=['DELETE'])
def test_delete_application(entity_id):
    application_repository = ApplicationRepository(db=db)
    return jsonify(
        application_repository.delete(entity_id)
    )
