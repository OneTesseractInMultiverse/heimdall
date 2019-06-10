from heimdall.abstractions.data import AbstractRepository
from heimdall.persistence.dao import IsxGroupClaim


class GroupClaimRepository(AbstractRepository):

    def __init__(self, db):
        self.db = db

    # -------------------------------------------------------------------------
    # METHOD QUERY
    # -------------------------------------------------------------------------
    def query(self, match_pairs: dict) -> list:
        try:
            results = []
            query_result = self.db.session.query(IsxGroupClaim) \
                .all()
            for group_claim in query_result:
                results.append(group_claim.dictionary)
        except Exception as e:
            pass
        return results

    # -------------------------------------------------------------------------
    # METHOD GET
    # -------------------------------------------------------------------------
    def get(self, entity_id, **params) -> dict:
        try:
            query_result = self.db.session.query(IsxGroupClaim) \
                .filter(IsxGroupClaim.claim_id == str(entity_id),
                        IsxGroupClaim.group_id == str(params["group_id"]),
                        IsxGroupClaim.application_id == str(params["application_id"])) \
                .all()
            for group_claim in query_result:
                return group_claim.dictionary
        except Exception as e:
            pass
        return {}

    # -------------------------------------------------------------------------
    # METHOD CREATE
    # -------------------------------------------------------------------------
    def create(self, state_data: dict) -> dict:
        try:
            group_claim = IsxGroupClaim(
                claim_id=state_data["claim_id"],
                group_id=state_data["group_id"],
                application_id=state_data["application_id"]
            )
            self.db.session.add(group_claim)
            self.db.session.commit()
            return group_claim.dictionary
        except Exception as e:
            print(str(e))
        return {}

    # -------------------------------------------------------------------------
    # METHOD UPDATE
    # -------------------------------------------------------------------------
    def update(self, entity_id, state_data: dict, **params) -> bool:
        try:
            update_result = self.db.session.query(IsxGroupClaim) \
                .filter(IsxGroupClaim.claim_id == str(entity_id),
                        IsxGroupClaim.group_id == str(params["group_id"]),
                        IsxGroupClaim.application_id == str(params["application_id"])) \
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
            query_result = self.db.session.query(IsxGroupClaim) \
                .filter(IsxGroupClaim.claim_id == str(entity_id),
                        IsxGroupClaim.group_id == str(params["group_id"]),
                        IsxGroupClaim.application_id == str(params["application_id"])) \
                .all()

            # Delete the item
            self.db.session.query(IsxGroupClaim) \
                .filter(IsxGroupClaim.claim_id == str(entity_id),
                        IsxGroupClaim.group_id == str(params["group_id"]),
                        IsxGroupClaim.application_id == str(params["application_id"])) \
                .delete()
            self.db.session.commit()

            for group_claim in query_result:
                return group_claim.dictionary
        except Exception as e:
            print(str(e))
        return {}
