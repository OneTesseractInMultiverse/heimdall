from heimdall.abstractions.data import AbstractRepository
from heimdall.persistence.dao import IsxApplication
import uuid
import datetime


class ApplicationRepository(AbstractRepository):

    def __init__(self, db):
        self.db = db

    # -------------------------------------------------------------------------
    # METHOD QUERY
    # -------------------------------------------------------------------------
    def query(self, match_pairs: dict) -> list:
        try:
            results = []
            query_result = self.db.session.query(IsxApplication) \
                .all()
            for application in query_result:
                results.append(application.dictionary)
        except Exception as e:
            print(str(e))
        return results

    # -------------------------------------------------------------------------
    # METHOD GET
    # -------------------------------------------------------------------------
    def get(self, entity_id) -> dict:
        try:
            query_result = self.db.session.query(IsxApplication)\
                .filter(IsxApplication.application_id == str(entity_id))\
                .all()
            for application in query_result:
                return application.dictionary
        except Exception as e:
            pass
        return {}

    # -------------------------------------------------------------------------
    # METHOD CREATE
    # -------------------------------------------------------------------------
    def create(self, state_data: dict) -> dict:
        try:
            application_id = str(uuid.uuid4())
            application = IsxApplication(
                application_id=application_id,
                name=state_data["name"],
                description=state_data["description"],
                callback_url=state_data["callback_url"],
                public_key=state_data["public_key"],
                private_key=state_data["private_key"],
                environment=state_data["environment"],
                configuration=state_data["configuration"],
                last_modified=datetime.datetime.now(),
                is_enabled=bool(state_data["is_enabled"])
            )
            self.db.session.add(application)
            self.db.session.commit()
            return self.get(application_id)
        except Exception as e:
            pass
        return {}

    # -------------------------------------------------------------------------
    # METHOD UPDATE
    # -------------------------------------------------------------------------
    def update(self, entity_id, state_data: dict) -> bool:
        try:
            update_result = self.db.session.query(IsxApplication) \
                .filter(IsxApplication.application_id == entity_id)\
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
            query_result = self.db.session.query(IsxApplication) \
                .filter(IsxApplication.application_id == str(entity_id))\
                .all()

            # Delete the item
            self.db.session.query(IsxApplication) \
                .filter(IsxApplication.application_id == str(entity_id)) \
                .delete()
            self.db.session.commit()

            for application in query_result:
                return application.dictionary
        except Exception as e:
            print(str(e))
        return {}
