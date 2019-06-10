from heimdall.abstractions.data import AbstractRepository
from heimdall.persistence.dao import IsxClaimsProvider
import uuid


class ClaimsProviderRepository(AbstractRepository):

    def __init__(self, db):
        self.db = db

    # -------------------------------------------------------------------------
    # METHOD QUERY
    # -------------------------------------------------------------------------
    def query(self, match_pairs: dict) -> list:
        try:
            results = []
            query_result = self.db.session.query(IsxClaimsProvider) \
                .all()
            for claims_provider in query_result:
                results.append(claims_provider.dictionary)
        except Exception as e:
            pass
        return results

    # -------------------------------------------------------------------------
    # METHOD GET
    # -------------------------------------------------------------------------
    def get(self, entity_id) -> dict:
        try:
            query_result = self.db.session.query(IsxClaimsProvider) \
                .filter(IsxClaimsProvider.provider_id == str(entity_id)) \
                .all()
            for claims_provider in query_result:
                return claims_provider.dictionary
        except Exception as e:
            pass
        return {}

    # -------------------------------------------------------------------------
    # METHOD CREATE
    # -------------------------------------------------------------------------
    def create(self, state_data: dict) -> dict:
        try:
            provider_id = str(uuid.uuid4())
            claims_provider = IsxClaimsProvider(
                provider_id=provider_id,
                name=state_data["name"],
                description=state_data["description"],
                is_local=bool(state_data["is_local"]),
                config=state_data["config"],
                implementation_class=state_data["implementation_class"],
                credentials=state_data["credentials"]
            )
            self.db.session.add(claims_provider)
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
            update_result = self.db.session.query(IsxClaimsProvider) \
                .filter(IsxClaimsProvider.provider_id == entity_id)\
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
            query_result = self.db.session.query(IsxClaimsProvider) \
                .filter(IsxClaimsProvider.provider_id == str(entity_id))\
                .all()

            # Delete the item
            self.db.session.query(IsxClaimsProvider) \
                .filter(IsxClaimsProvider.provider_id == str(entity_id)) \
                .delete()
            self.db.session.commit()

            for claims_provider in query_result:
                return claims_provider.dictionary
        except Exception as e:
            print(str(e))
        return {}
