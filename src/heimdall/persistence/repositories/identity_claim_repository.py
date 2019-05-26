from heimdall.abstractions.data import AbstractRepository
from heimdall.persistence.dao import IsxIdentityClaim


class IdentityClaimRepository(AbstractRepository):

    def __init__(self, db):
        self.db = db

    # -------------------------------------------------------------------------
    # METHOD QUERY
    # -------------------------------------------------------------------------
    def query(self, match_pairs: dict) -> list:
        try:
            results = []
            query_result = self.db.session.query(IsxIdentityClaim) \
                .all()
            for identity_claim in query_result:
                results.append(identity_claim.dictionary)
        except Exception as e:
            pass
        return results

    # -------------------------------------------------------------------------
    # METHOD GET
    # -------------------------------------------------------------------------
    def get(self, entity_id, **params) -> dict:
        try:
            query_result = self.db.session.query(IsxIdentityClaim) \
                .filter(IsxIdentityClaim.claim_id == str(entity_id),
                        IsxIdentityClaim.application_id == str(params["application_id"]),
                        IsxIdentityClaim.identity_id == str(params["identity_id"])) \
                .all()
            for identity_claim in query_result:
                return identity_claim.dictionary
        except Exception as e:
            pass
        return {}

    # -------------------------------------------------------------------------
    # METHOD CREATE
    # -------------------------------------------------------------------------
    def create(self, state_data: dict) -> dict:
        try:
            identity_claim = IsxIdentityClaim(
                claim_id=state_data["claim_id"],
                application_id=state_data["application_id"],
                identity_id=state_data["identity_id"],
                from_date=state_data["from_date"],
                until_date=state_data["until_date"]
            )
            self.db.session.add(identity_claim)
            self.db.session.commit()
            return identity_claim.dictionary
        except Exception as e:
            print(str(e))
        return {}

    # -------------------------------------------------------------------------
    # METHOD UPDATE
    # -------------------------------------------------------------------------
    def update(self, entity_id, state_data: dict, **params) -> bool:
        try:
            update_result = self.db.session.query(IsxIdentityClaim) \
                .filter(IsxIdentityClaim.claim_id == entity_id,
                        IsxIdentityClaim.application_id == str(params["application_id"]),
                        IsxIdentityClaim.identity_id == str(params["identity_id"]))\
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
            query_result = self.db.session.query(IsxIdentityClaim) \
                .filter(IsxIdentityClaim.claim_id == str(entity_id),
                        IsxIdentityClaim.application_id == str(params["application_id"]),
                        IsxIdentityClaim.identity_id == str(params["identity_id"])) \
                .all()

            # Delete the item
            self.db.session.query(IsxIdentityClaim) \
                .filter(IsxIdentityClaim.claim_id == str(entity_id),
                        IsxIdentityClaim.application_id == str(params["application_id"]),
                        IsxIdentityClaim.identity_id == str(params["identity_id"])
                        ) \
                .delete()
            self.db.session.commit()

            for identity_claim in query_result:
                return identity_claim.dictionary
        except Exception as e:
            print(str(e))
        return {}
