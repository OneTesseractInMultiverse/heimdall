from heimdall.abstractions.data import AbstractRepository
from heimdall.persistence.dao import IsxApplicationProvider
import datetime


class ApplicationProviderRepository(AbstractRepository):

    def __init__(self, db):
        self.db = db

    # -------------------------------------------------------------------------
    # METHOD QUERY
    # -------------------------------------------------------------------------
    def query(self, match_pairs: dict) -> list:
        try:
            results = []
            query_result = self.db.session.query(IsxApplicationProvider) \
                .all()
            for application_provider in query_result:
                results.append(application_provider.dictionary)
        except Exception as e:
            pass
        return results

    # -------------------------------------------------------------------------
    # METHOD GET
    # -------------------------------------------------------------------------
    def get(self, entity_id, **params) -> dict:
        try:
            query_result = self.db.session.query(IsxApplicationProvider) \
                .filter(IsxApplicationProvider.provider_id == str(entity_id),
                        IsxApplicationProvider.application_id == str(params["application_id"])) \
                .all()
            for application_provider in query_result:
                return application_provider.dictionary
        except Exception as e:
            pass
        return {}

    # -------------------------------------------------------------------------
    # METHOD CREATE
    # -------------------------------------------------------------------------
    def create(self, state_data: dict) -> dict:
        try:
            application_provider = IsxApplicationProvider(
                provider_id=state_data["provider_id"],
                application_id=state_data["application_id"],
                created=datetime.datetime.now()
            )
            self.db.session.add(application_provider)
            self.db.session.commit()
            return application_provider.dictionary
        except Exception as e:
            print(str(e))
        return {}

    # -------------------------------------------------------------------------
    # METHOD UPDATE
    # -------------------------------------------------------------------------
    def update(self, entity_id, state_data: dict, **params) -> bool:
        try:
            update_result = self.db.session.query(IsxApplicationProvider) \
                .filter(IsxApplicationProvider.provider_id == str(entity_id),
                        IsxApplicationProvider.application_id == str(params["application_id"])) \
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
            query_result = self.db.session.query(IsxApplicationProvider) \
                .filter(IsxApplicationProvider.provider_id == str(entity_id),
                        IsxApplicationProvider.application_id == str(params["application_id"])) \
                .all()

            # Delete the item
            self.db.session.query(IsxApplicationProvider) \
                .filter(IsxApplicationProvider.provider_id == str(entity_id),
                        IsxApplicationProvider.application_id == str(params["application_id"])) \
                .delete()
            self.db.session.commit()

            for application_provider in query_result:
                return application_provider.dictionary
        except Exception as e:
            print(str(e))
        return {}
