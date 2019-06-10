from heimdall.abstractions.data import AbstractRepository
from heimdall.persistence.dao import IsxProfile
import uuid


class ProfileRepository(AbstractRepository):

    def __init__(self, db):
        self.db = db

    # -------------------------------------------------------------------------
    # METHOD QUERY
    # -------------------------------------------------------------------------
    def query(self, match_pairs: dict) -> list:
        try:
            results = []
            query_result = self.db.session.query(IsxProfile) \
                .all()
            for profile in query_result:
                results.append(profile.dictionary)
        except Exception as e:
            pass
        return results

    # -------------------------------------------------------------------------
    # METHOD GET
    # -------------------------------------------------------------------------
    def get(self, entity_id, **params) -> dict:
        try:
            query_result = self.db.session.query(IsxProfile) \
                .filter(IsxProfile.identity_id == str(entity_id),
                        IsxProfile.application_id == str(params["application_id"])) \
                .all()
            for profile in query_result:
                return profile.dictionary
        except Exception as e:
            pass
        return {}

    # -------------------------------------------------------------------------
    # METHOD CREATE
    # -------------------------------------------------------------------------
    def create(self, state_data: dict) -> dict:
        try:
            profile = IsxProfile(
                identity_id=state_data["identity_id"],
                application_id=state_data["application_id"],
                profile_data=state_data["profile_data"]
            )
            self.db.session.add(profile)
            self.db.session.commit()
            return profile.dictionary
        except Exception as e:
            print(str(e))
        return {}

    # -------------------------------------------------------------------------
    # METHOD UPDATE
    # -------------------------------------------------------------------------
    def update(self, entity_id, state_data: dict, **params) -> bool:
        try:
            update_result = self.db.session.query(IsxProfile) \
                .filter(IsxProfile.identity_id == str(entity_id),
                        IsxProfile.application_id == str(params["application_id"])) \
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
            query_result = self.db.session.query(IsxProfile) \
                .filter(IsxProfile.identity_id == str(entity_id),
                        IsxProfile.application_id == str(params["application_id"])) \
                .all()

            # Delete the item
            self.db.session.query(IsxProfile) \
                .filter(IsxProfile.identity_id == str(entity_id),
                        IsxProfile.application_id == str(params["application_id"])) \
                .delete()
            self.db.session.commit()

            for profile in query_result:
                return profile.dictionary
        except Exception as e:
            print(str(e))
        return {}
