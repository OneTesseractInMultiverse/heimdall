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

    # -------------------------------------------------------------------------
    # METHOD CREATE
    # -------------------------------------------------------------------------
    def create(self, state_data: dict) -> dict:
        try:
            identity_id = str(uuid.uuid4())
            identity = IsxIdentity(
                identity_id=identity_id,
                business_id=state_data["business_id"],
                identity_data=state_data["identity_data"],
                created=datetime.datetime.now(),
                last_modified=datetime.datetime.now(),
                type=state_data["type"]
            )
            self.db.session.add(identity)
            self.db.session.commit()
            return identity.dictionary
        except Exception as e:
            pass
        return {}

    # -------------------------------------------------------------------------
    # METHOD UPDATE
    # -------------------------------------------------------------------------
    def update(self, entity_id, state_data: dict) -> bool:
        try:
            state_data['last_modified'] = datetime.datetime.now()

            update_result = self.db.session.query(IsxIdentity) \
                .filter(IsxIdentity.identity_id == entity_id) \
                .update(state_data)

            self.db.session.commit()
            return update_result
        except Exception as e:
            print(str(e))
        return {}

    # -------------------------------------------------------------------------
    # METHOD DELETE
    # -------------------------------------------------------------------------
    def delete(self, entity_id) -> dict:
        try:
            # Get the item we want to delete
            query_result = self.db.session.query(IsxIdentity) \
                .filter(IsxIdentity.identity_id == str(entity_id)) \
                .all()

            # Delete the item
            self.db.session.query(IsxIdentity) \
                .filter(IsxIdentity.identity_id == str(entity_id)) \
                .delete()
            self.db.session.commit()

            for identity in query_result:
                return identity.dictionary
        except Exception as e:
            print(str(e))
        return {}
