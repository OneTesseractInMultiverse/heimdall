from heimdall.abstractions.data import AbstractRepository
from heimdall.persistence.dao import IsxIdentity
import uuid
import datetime

class IdentityRepository(AbstractRepository):

    def __init__(self, db):
        self.db = db

    # -------------------------------------------------------------------------
    # METHOD QUERY
    # -------------------------------------------------------------------------
    def query(self, match_pairs: dict) -> list:
        try:
            results = []
            query_result = self.db.session.query(IsxIdentity) \
                .all()
            for identity in query_result:
                results.append(identity.dictionary)
        except Exception as e:
            pass
        return results

    # -------------------------------------------------------------------------
    # METHOD GET
    # -------------------------------------------------------------------------
    def get(self, entity_id) -> dict:
        try:
            query_result = self.db.session.query(IsxIdentity) \
                .filter(IsxIdentity.identity_id == str(entity_id)) \
                .all()
            for identity in query_result:
                return identity.dictionary
        except Exception as e:
            pass
        return {}

    def create(self, state_data: dict) -> dict:
        try:
            identity_id = str(uuid.uuid4())
            identity = IsxIdentity(
                identity_id=identity_id,
                business_id=state_data["business_id"],
                identity_data=state_data["identity_data"],
                callback_url=state_data["callback_url"],
                public_key=state_data["public_key"],
                private_key=state_data["private_key"],
                environment=state_data["environment"],
                configuration=state_data["configuration"],
                last_modified=datetime.datetime.now(),
                is_enabled=bool(state_data["is_enabled"])
            )
            self.db.session.add(application)
            self.db.session.commit()
            return self.get(application_id)
        except Exception as e:
            pass
        return {}

    def update(self, entity_id, state_data: dict) -> bool:
        pass

    def delete(self, entity_id) -> dict:
        pass