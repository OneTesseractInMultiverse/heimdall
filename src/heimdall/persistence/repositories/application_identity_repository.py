from heimdall.abstractions.data import AbstractRepository
from heimdall.persistence.dao import IsxApplicationIdentity
import datetime


class ApplicationIdentityRepository(AbstractRepository):

    def __init__(self, db):
        self.db = db

    # -------------------------------------------------------------------------
    # METHOD QUERY
    # -------------------------------------------------------------------------
    def query(self, match_pairs: dict) -> list:
        try:
            results = []
            query_result = self.db.session.query(IsxApplicationIdentity) \
                .all()
            for application_identity in query_result:
                results.append(application_identity.dictionary)
        except Exception as e:
            pass
        return results

    # -------------------------------------------------------------------------
    # METHOD GET
    # -------------------------------------------------------------------------
    def get(self, entity_id, **params) -> dict:
        try:
            query_result = self.db.session.query(IsxApplicationIdentity) \
                .filter(IsxApplicationIdentity.identity_id == str(entity_id),
                        IsxApplicationIdentity.application_id == str(params["application_id"])) \
                .all()
            for application_identity in query_result:
                return application_identity.dictionary
        except Exception as e:
            pass
        return {}

    # -------------------------------------------------------------------------
    # METHOD CREATE
    # -------------------------------------------------------------------------
    def create(self, state_data: dict) -> dict:
        try:
            application_identity = IsxApplicationIdentity(
                identity_id=state_data["identity_id"],
                application_id=state_data["application_id"],
                created=datetime.datetime.now()
            )
            self.db.session.add(application_identity)
            self.db.session.commit()
            return application_identity.dictionary
        except Exception as e:
            print(str(e))
        return {}

    # -------------------------------------------------------------------------
    # METHOD UPDATE
    # -------------------------------------------------------------------------
    def update(self, entity_id, state_data: dict, **params) -> bool:
        try:
            update_result = self.db.session.query(IsxApplicationIdentity) \
                .filter(IsxApplicationIdentity.identity_id == str(entity_id),
                        IsxApplicationIdentity.application_id == str(params["application_id"])) \
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
            query_result = self.db.session.query(IsxApplicationIdentity) \
                .filter(IsxApplicationIdentity.identity_id == str(entity_id),
                        IsxApplicationIdentity.application_id == str(params["application_id"])) \
                .all()

            # Delete the item
            self.db.session.query(IsxApplicationIdentity) \
                .filter(IsxApplicationIdentity.identity_id == str(entity_id),
                        IsxApplicationIdentity.application_id == str(params["application_id"])) \
                .delete()
            self.db.session.commit()

            for application_identity in query_result:
                return application_identity.dictionary
        except Exception as e:
            print(str(e))
        return {}
