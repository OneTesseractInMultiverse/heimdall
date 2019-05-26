from heimdall.abstractions.data import AbstractRepository
from heimdall.persistence.dao import IsxIdentityType


class IdentityTypeRepository(AbstractRepository):

    def __init__(self, db):
        self.db = db

    # -------------------------------------------------------------------------
    # METHOD QUERY
    # -------------------------------------------------------------------------
    def query(self, match_pairs: dict) -> list:
        try:
            results = []
            query_result = self.db.session.query(IsxIdentityType) \
                .all()
            for identity_type in query_result:
                results.append(identity_type.dictionary)
        except Exception as e:
            pass
        return results

    # -------------------------------------------------------------------------
    # METHOD GET
    # -------------------------------------------------------------------------
    def get(self, entity_id) -> dict:
        try:
            query_result = self.db.session.query(IsxIdentityType) \
                .filter(IsxIdentityType.type_name == str(entity_id)) \
                .all()
            for identity_type in query_result:
                return identity_type.dictionary
        except Exception as e:
            pass
        return {}

    # -------------------------------------------------------------------------
    # METHOD CREATE
    # -------------------------------------------------------------------------
    def create(self, state_data: dict) -> dict:
        try:
            identity_type = IsxIdentityType(
                type_name=state_data["type_name"],
                description=state_data["description"]
            )
            self.db.session.add(identity_type)
            self.db.session.commit()
            return identity_type.dictionary
        except Exception as e:
            pass
        return {}

    # -------------------------------------------------------------------------
    # METHOD UPDATE
    # -------------------------------------------------------------------------
    def update(self, entity_id, state_data: dict) -> bool:
        try:
            update_result = self.db.session.query(IsxIdentityType) \
                .filter(IsxIdentityType.type_name == entity_id) \
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
            query_result = self.db.session.query(IsxIdentityType) \
                .filter(IsxIdentityType.type_name == str(entity_id)) \
                .all()

            # Delete the item
            self.db.session.query(IsxIdentityType) \
                .filter(IsxIdentityType.type_name == str(entity_id)) \
                .delete()
            self.db.session.commit()

            for identity_type in query_result:
                return identity_type.dictionary
        except Exception as e:
            print(str(e))
        return {}
