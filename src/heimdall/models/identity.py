from heimdall.models.model_base import ModelBase
from heimdall.abstractions.data import (
    AbstractRepository
)
from dateutil.parser import *
from jsonschema import validate, ValidationError


class Identity(ModelBase):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__load_repository_if_available(kwargs)

    # -------------------------------------------------------------------------
    # METHOD LOAD REPOSITORY IF AVAILABLE
    # -------------------------------------------------------------------------
    def __load_repository_if_available(self, arguments: dict):
        if 'repository' in arguments and isinstance(arguments['repository'], AbstractRepository):
            self.__repository = arguments['repository']

    # -------------------------------------------------------------------------
    # PROPERTY IDENTITY
    # -------------------------------------------------------------------------
    @property
    def __identities(self) -> AbstractRepository:
        if self.__repository:
            return self.__repository
        return None

    # -------------------------------------------------------------------------
    # PROPERTY ID
    # -------------------------------------------------------------------------
    @property
    def id(self):
        if self._state and 'identity_id' in self._state:
            return self._state['identity_id']
        return None

    # -------------------------------------------------------------------------
    # PROPERTY BUSINESS ID
    # -------------------------------------------------------------------------
    @property
    def business_id(self):
        if self._state and 'business_id' in self._state:
            return self._state['business_id']
        return None

    # -------------------------------------------------------------------------
    # PROPERTY LAST_MODIFIED
    # -------------------------------------------------------------------------
    @property
    def last_modified(self):
        if self._state and 'last_modified' in self._state:
            return parse(self._state['last_modified'])
        return None

    # -------------------------------------------------------------------------
    # PROPERTY DISABLED
    # -------------------------------------------------------------------------
    @property
    def disabled(self):
        if self._state and 'disabled' in self._state:
            return self._state['disabled']
        return None

    # -------------------------------------------------------------------------
    # METHOD COMMIT
    # -------------------------------------------------------------------------
    def commit(self):
        if self.__identities and self._uncommitted_changes and self.id:
            if self.__identities.update(self.id, self._pending_changes):
                self._clear_changes()
                return True
        return False

    # -------------------------------------------------------------------------
    # METHOD SAVE
    # -------------------------------------------------------------------------
    def save(self):
        if self.__identities and self.state_valid and len(self.model_errors) == 0:
            result = self.__identities.create(self.as_dict())
            if result and isinstance(result, dict):
                self._state = result
                return True
            return False

    # -------------------------------------------------------------------------
    # METHOD LOAD FROM DICT
    # -------------------------------------------------------------------------
    def load_from_dict(self):
        pass

    # -------------------------------------------------------------------------
    # PROPERTY STATE IS VALID
    # -------------------------------------------------------------------------
    @property
    def state_valid(self):
        try:
            validate(instance=self.as_dict(), schema=self.schema)
            return True
        except ValidationError as ve:
            self._add_model_error({
                "title": "Schema Validation Error",
                "message": str(ve.message),
                "cause": str(ve.cause),
                "full_description": str(ve)
            })
            return False

    # -------------------------------------------------------------------------
    # PROPERTY SCHEMA
    # -------------------------------------------------------------------------
    @property
    def schema(self) -> dict:
        return {
            "type": "object",
            "properties": {
                "business_id": {"type": "string"},
                "identity_data": {"type": "object"},
                "disabled": {"type": "boolean"},
                "type": {"type", "string"}
            },
            "required": [
                "business_id",
                "disabled",
                "type"
            ]
        }
