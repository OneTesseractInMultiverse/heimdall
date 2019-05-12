from heimdall.abstractions.data import AbstractRepository
from heimdall.persistence.dao import IsxClaim


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
            query_result = self.db.session.query(IsxClaim) \
                .filter(IsxClaim.application_id == str(entity_id)) \
                .all()
            for identity in query_result:
                return identity.dictionary
        except Exception as e:
            pass
        return {}

    def create(self, state_data: dict) -> dict:
        pass

    def update(self, entity_id, state_data: dict) -> bool:
        pass

    def delete(self, entity_id) -> dict:
        pass