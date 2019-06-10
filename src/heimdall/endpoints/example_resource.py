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
from heimdall.persistence.repositories.application_ownership_repository import ApplicationOwnershipRepository

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
    group_repository = ApplicationOwnershipRepository(db=db)
    return jsonify(
        group_repository.query({})
    )


@app.route('/test/<entity_id>/<application_id>', methods=['GET'])
def test_get_application(entity_id, application_id):
    group_repository = ApplicationOwnershipRepository(db=db)
    return jsonify(
        group_repository.get(entity_id, application_id=application_id)
    )


@app.route('/test/create', methods=['POST', 'GET'])
def test_create_application():
    state_data = {
        'identity_id': '20362c60-569b-4ce1-a502-f1674f3dabda',
        'application_id': '012ad4b8-0c25-4315-bac5-57713c36a408',
        'from_date': '2019-05-30 03:30:23.739795',
        'until_date': '2019-06-13 03:30:23.739795',
        'is_owner': False,
        'is_manager': True,
        'configuration': {"user_name": "Jane"}
    }
    application_ownership = ApplicationOwnershipRepository(db=db)
    return jsonify(
        application_ownership.create(state_data)
    )


@app.route('/test/update/<entity_id>/<application_id>', methods=['PUT'])
def test_update_application(entity_id, application_id):
    state_data = {
        'identity_id': '20362c60-569b-4ce1-a502-f1674f3dabda',
        'application_id': '012ad4b8-0c25-4315-bac5-57713c36a408',
        'created': '2019-05-30 03:30:23.739795',
        'until_date': '2019-06-13 03:30:23.739795',
        'is_owner': False,
        'is_manager': True,
        'configuration': {"user_name": "Jane was changed"}
    }
    group_repository = ApplicationOwnershipRepository(db=db)
    return jsonify(
        group_repository.update(entity_id, state_data, application_id=application_id)
    )


@app.route('/test/delete/<entity_id>/<application_id>', methods=['DELETE'])
def test_delete_application(entity_id, application_id):
    group_repository = ApplicationOwnershipRepository(db=db)
    return jsonify(
        group_repository.delete(entity_id, application_id=application_id)
    )


"""
@app.route('/test/<entity_id>/<application_id>/<identity_id>', methods=['GET'])
def test_get_application(entity_id, application_id, identity_id):
    group_repository = IdentityClaimRepository(db=db)
    return jsonify(
        group_repository.get(entity_id, application_id, identity_id)
    )


@app.route('/test/create', methods=['POST', 'GET'])
def test_create_application():
    state_data = {
        'claim_id': '8c750c8e-0c72-4703-91e1-e25b989572b6',
        'application_id': '79a31f70-da87-41b3-b9a6-f946d394b387',
        'identity_id': "a3ecd0ed-9c7f-4ec6-874f-4abca203032c",
        'from_date': '2019-04-22',
        'until_date': '2019-10-05'
    }
    group_repository = IdentityClaimRepository(db=db)
    return jsonify(
        group_repository.create(state_data)
    )


@app.route('/test/update/<entity_id>/<application_id>/<identity_id>', methods=['PUT'])
def test_update_application(entity_id, application_id, identity_id):
    state_data = {
        'claim_id': '8c750c8e-0c72-4703-91e1-e25b989572b6',
        'application_id': '79a31f70-da87-41b3-b9a6-f946d394b387',
        'identity_id': "a3ecd0ed-9c7f-4ec6-874f-4abca203032c",
        'from_date': '2019-04-22 06:05:57.924838',
        'until_date': '2019-09-05 09:05:57.924838'
    }
    group_repository = IdentityClaimRepository(db=db)
    return jsonify(
        group_repository.update(entity_id, state_data, application_id, identity_id)
    )


@app.route('/test/delete/<entity_id>/<application_id>/<identity_id>', methods=['DELETE'])
def test_delete_application(entity_id, application_id, identity_id):
    group_repository = IdentityClaimRepository(db=db)
    return jsonify(
        group_repository.delete(entity_id, application_id, identity_id)
    )
"""

"""
Claim Provider

@app.route('/test', methods=['GET'])
def test_get_applications():
    group_repository = ClaimsProviderRepository(db=db)
    return jsonify(
        group_repository.query({})
    )


@app.route('/test/<entity_id>', methods=['GET'])
def test_get_application(entity_id):
    group_repository = ClaimsProviderRepository(db=db)
    return jsonify(
        group_repository.get(entity_id)
    )


@app.route('/test/create', methods=['POST', 'GET'])
def test_create_application():
    state_data = {
        'name': 'External Provider #2',
        'description': "Facebook Provider",
        'is_local': False,
        'config': {"configuration": "This is a test configuration"},
        'implementation_class': "Class name",
        'credentials': {
            "app_name": "application_name",
            "password": "7654dcs"
        }
    }
    group_repository = ClaimsProviderRepository(db=db)
    return jsonify(
        group_repository.create(state_data)
    )


@app.route('/test/update/<entity_id>', methods=['PUT'])
def test_update_application(entity_id):
    state_data = {
        'name': 'External Provider #2',
        'description': "Facebook Provider (test)",
        'is_local': False,
        'config': {"configuration": "This is a(not) test configuration"},
        'implementation_class': "Class name",
        'credentials': {
            "app_name": "application_name",
            "password": "7654dcc"
        }
    }
    group_repository = ClaimsProviderRepository(db=db)
    return jsonify(
        group_repository.update(entity_id, state_data)
    )


@app.route('/test/delete/<entity_id>', methods=['DELETE'])
def test_delete_application(entity_id):
    group_repository = ClaimsProviderRepository(db=db)
    return jsonify(
        group_repository.delete(entity_id)
    )
"""

"""
# Identity Type

@app.route('/test', methods=['GET'])
def test_get_applications():
    identity_repository = IdentityTypeRepository(db=db)
    return jsonify(
        identity_repository.query({})
    )


@app.route('/test/<entity_id>', methods=['GET'])
def test_get_application(entity_id):
    identity_repository = IdentityTypeRepository(db=db)
    return jsonify(
        identity_repository.get(entity_id)
    )


@app.route('/test/create', methods=['POST', 'GET'])
def test_create_application():
    state_data = {
        'type_name': 'extra_type',
        'description': 'Test type, delete soon'
    }
    identity_repository = IdentityTypeRepository(db=db)
    return jsonify(
        identity_repository.create(state_data)
    )


@app.route('/test/update/<entity_id>', methods=['PUT'])
def test_update_application(entity_id):
    state_data = {
        'type_name': 'super_extra_type',
        'description': 'Test type, delete soon'
    }
    identity_repository = IdentityTypeRepository(db=db)
    return jsonify(
        identity_repository.update(entity_id, state_data)
    )


@app.route('/test/delete/<entity_id>', methods=['DELETE'])
def test_delete_application(entity_id):
    identity_repository = IdentityTypeRepository(db=db)
    return jsonify(
        identity_repository.delete(entity_id)
    )
"""

"""
# Identity

@app.route('/test', methods=['GET'])
def test_get_applications():
    identity_repository = IdentityRepository(db=db)
    return jsonify(
        identity_repository.query({})
    )


@app.route('/test/<entity_id>', methods=['GET'])
def test_get_application(entity_id):
    identity_repository = IdentityRepository(db=db)
    return jsonify(
        identity_repository.get(entity_id)
    )


@app.route('/test/create', methods=['POST', 'GET'])
def test_create_application():
    state_data = {
        'business_id': 'asdkhj234jkh342',
        'identity_data': {"user_name": "Pedro Guzman", "department": "Development"},
        'disabled': bool(False),
        'type': 'user_identity'
    }
    identity_repository = IdentityRepository(db=db)
    return jsonify(
        identity_repository.create(state_data)
    )


@app.route('/test/update/<entity_id>', methods=['PUT'])
def test_update_application(entity_id):
    state_data = {
        'business_id': 'asdkhj234jkh342',
        'identity_data': {"user_name": "Pedro Guzman", "department": "Research"},
        'disabled': bool(False),
        'type': 'user_identity'
    }
    identity_repository = IdentityRepository(db=db)
    return jsonify(
        identity_repository.update(entity_id, state_data)
    )


@app.route('/test/delete/<entity_id>', methods=['DELETE'])
def test_delete_application(entity_id):
    identity_repository = IdentityRepository(db=db)
    return jsonify(
        identity_repository.delete(entity_id)
    )
"""

"""
# Application

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
"""