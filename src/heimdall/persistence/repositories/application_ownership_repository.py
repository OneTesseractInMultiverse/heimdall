from heimdall.abstractions.data import AbstractRepository
from heimdall.persistence.dao import IsxApplicationOwnership
import datetime


class ApplicationOwnershipRepository(AbstractRepository):

    def __init__(self, db):
        self.db = db

    # -------------------------------------------------------------------------
    # METHOD QUERY
    # -------------------------------------------------------------------------
    def query(self, match_pairs: dict) -> list:
        try:
            results = []
            query_result = self.db.session.query(IsxApplicationOwnership) \
                .all()
            for application_ownership in query_result:
                results.append(application_ownership.dictionary)
        except Exception as e:
            pass
        return results

    # -------------------------------------------------------------------------
    # METHOD GET
    # -------------------------------------------------------------------------
    def get(self, entity_id, **params) -> dict:
        try:
            query_result = self.db.session.query(IsxApplicationOwnership)\
                .filter(IsxApplicationOwnership.identity_id == str(entity_id),
                        IsxApplicationOwnership.application_id == str(params["application_id"]))\
                .all()
            for application_ownership in query_result:
                return application_ownership.dictionary
        except Exception as e:
            pass
        return {}

    # -------------------------------------------------------------------------
    # METHOD CREATE
    # -------------------------------------------------------------------------
    def create(self, state_data: dict, **params) -> dict:
        try:
            application_ownership = IsxApplicationOwnership(
                identity_id=state_data["identity_id"],
                application_id=state_data["application_id"],
                created=datetime.datetime.now(),
                from_date=state_data["from_date"],
                until_date=state_data["until_date"],
                is_owner=state_data["is_owner"],
                is_manager=state_data["is_manager"],
                configuration=state_data["configuration"]
            )
            self.db.session.add(application_ownership)
            self.db.session.commit()
            return application_ownership.dictionary
        except Exception as e:
            print(str(e))
        return {}

    # -------------------------------------------------------------------------
    # METHOD UPDATE
    # -------------------------------------------------------------------------
    def update(self, entity_id, state_data: dict, **params) -> bool:
        try:
            update_result = self.db.session.query(IsxApplicationOwnership) \
                .filter(IsxApplicationOwnership.identity_id == str(entity_id),
                        IsxApplicationOwnership.application_id == str(params["application_id"])) \
                .update(state_data)

            self.db.session.commit()
            return update_result
        except Exception as e:
            print(str(e))
        return {}

    # -------------------------------------------------------------------------
    # METHOD DELETE
    # -------------------------------------------------------------------------
    def delete(self, entity_id, **params) -> dict:
        try:
            # Get the item we want to delete
            query_result = self.db.session.query(IsxApplicationOwnership) \
                .filter(IsxApplicationOwnership.identity_id == str(entity_id),
                        IsxApplicationOwnership.application_id == str(params["application_id"])) \
                .all()

            # Delete the item
            self.db.session.query(IsxApplicationOwnership) \
                .filter(IsxApplicationOwnership.identity_id == str(entity_id),
                        IsxApplicationOwnership.application_id == str(params["application_id"])) \
                .delete()
            self.db.session.commit()

            for application_ownership in query_result:
                return application_ownership.dictionary
        except Exception as e:
            print(str(e))
        return {}