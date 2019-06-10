from heimdall.abstractions.data import AbstractRepository
from heimdall.persistence.dao import IsxClaim
import uuid


class ClaimRepository(AbstractRepository):

    def __init__(self, db):
        self.db = db

    # -------------------------------------------------------------------------
    # METHOD QUERY
    # -------------------------------------------------------------------------
    def query(self, match_pairs: dict) -> list:
        try:
            results = []
            query_result = self.db.session.query(IsxClaim) \
                .all()
            for claim in query_result:
                results.append(claim.dictionary)
        except Exception as e:
            pass
        return results

    # -------------------------------------------------------------------------
    # METHOD GET
    # -------------------------------------------------------------------------
    def get(self, entity_id) -> dict:
        try:
            query_result = self.db.session.query(IsxClaim) \
                .filter(IsxClaim.claim_id == str(entity_id)) \
                .all()
            for claim in query_result:
                return claim.dictionary
        except Exception as e:
            pass
        return {}

    # -------------------------------------------------------------------------
    # METHOD CREATE
    # -------------------------------------------------------------------------
    def create(self, state_data: dict) -> dict:
        try:
            claim_id = uuid.uuid4()
            claim = IsxClaim(
                claim_id=str(claim_id),
                application_id=state_data["application_id"],
                value=state_data["value"],
                description=state_data["description"]
            )
            self.db.session.add(claim)
            self.db.session.commit()
            return claim.dictionary
        except Exception as e:
            print(str(e))
        return {}

    # -------------------------------------------------------------------------
    # METHOD UPDATE
    # -------------------------------------------------------------------------
    def update(self, entity_id, state_data: dict) -> bool:
        try:
            update_result = self.db.session.query(IsxClaim) \
                .filter(IsxClaim.claim_id == str(entity_id)) \
                .update(state_data)

            self.db.session.commit()
            return update_result
        except Exception as e:
            print(str(e))
        return {}

    # -------------------------------------------------------------------------
    # METHOD UPDATE
    # -------------------------------------------------------------------------
    def delete(self, entity_id) -> dict:
        try:
            # Get the item we want to delete
            query_result = self.db.session.query(IsxClaim) \
                .filter(IsxClaim.claim_id == str(entity_id)) \
                .all()

            # Delete the item
            self.db.session.query(IsxClaim) \
                .filter(IsxClaim.claim_id == str(entity_id)) \
                .delete()
            self.db.session.commit()

            for claim in query_result:
                return claim.dictionary
        except Exception as e:
            print(str(e))
        return {}
