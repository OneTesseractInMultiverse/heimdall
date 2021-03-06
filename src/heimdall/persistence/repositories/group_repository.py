from heimdall.abstractions.data import AbstractRepository
from heimdall.persistence.dao import IsxGroup
import uuid


class GroupRepository(AbstractRepository):

    def __init__(self, db):
        self.db = db

    # -------------------------------------------------------------------------
    # METHOD QUERY
    # -------------------------------------------------------------------------
    def query(self, match_pairs: dict) -> list:
        try:
            results = []
            query_result = self.db.session.query(IsxGroup) \
                .all()
            for group in query_result:
                results.append(group.dictionary)
        except Exception as e:
            pass
        return results

    # -------------------------------------------------------------------------
    # METHOD GET
    # -------------------------------------------------------------------------
    def get(self, entity_id) -> dict:
        try:
            query_result = self.db.session.query(IsxGroup) \
                .filter(IsxGroup.group_id == str(entity_id)) \
                .all()
            for group in query_result:
                return group.dictionary
        except Exception as e:
            pass
        return {}

    # -------------------------------------------------------------------------
    # METHOD CREATE
    # -------------------------------------------------------------------------
    def create(self, state_data: dict) -> dict:
        try:
            group_id = str(uuid.uuid4())
            group = IsxGroup(
                group_id=group_id,
                application_id=state_data["application_id"],
                name=state_data["name"],
                description=state_data["description"],
                properties=state_data["properties"],
            )
            self.db.session.add(group)
            self.db.session.commit()
            return group.dictionary
        except Exception as e:
            pass
        return {}

    # -------------------------------------------------------------------------
    # METHOD UPDATE
    # -------------------------------------------------------------------------
    def update(self, entity_id, state_data: dict) -> bool:
        try:
            update_result = self.db.session.query(IsxGroup) \
                .filter(IsxGroup.group_id == entity_id)\
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
            query_result = self.db.session.query(IsxGroup) \
                .filter(IsxGroup.group_id == str(entity_id))\
                .all()

            # Delete the item
            self.db.session.query(IsxGroup) \
                .filter(IsxGroup.application_id == str(entity_id)) \
                .delete()
            self.db.session.commit()

            for group in query_result:
                return group.dictionary
        except Exception as e:
            print(str(e))
        return {}
