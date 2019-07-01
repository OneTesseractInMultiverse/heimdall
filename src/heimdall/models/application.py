from heimdall.models.model_base import ModelBase
from heimdall.abstractions.data import (
    AbstractRepository
)
from dateutil.parser import *
from jsonschema import validate, ValidationError


class Application(ModelBase):

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
    # PROPERTY APPLICATIONS
    # -------------------------------------------------------------------------
    @property
    def __applications(self) -> AbstractRepository:
        if self.__repository:
            return self.__repository
        return None

    # -------------------------------------------------------------------------
    # PROPERTY ID
    # -------------------------------------------------------------------------
    @property
    def id(self):
        if self._state and 'application_id' in self._state:
            return self._state['application_id']
        return None

    # -------------------------------------------------------------------------
    # PROPERTY CALLBACK URL
    # -------------------------------------------------------------------------
    @property
    def callback_url(self):
        if self._state and 'callback_url' in self._state:
            return self._state['callback_url']
        return None

    # -------------------------------------------------------------------------
    # PROPERTY PRIVATE KEY
    # -------------------------------------------------------------------------
    @property
    def private_key(self):
        if self._state and 'private_key' in self._state:
            return self._state['private_key']
        return None

    # -------------------------------------------------------------------------
    # PROPERTY PUBLIC KEY
    # -------------------------------------------------------------------------
    @property
    def public_key(self):
        if self._state and 'public_key' in self._state:
            return self._state['public_key']
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
    # METHOD COMMIT
    # -------------------------------------------------------------------------
    def commit(self):
        if self.__applications and self._uncommitted_changes and self.id:
            if self.__applications.update(self.id, self._pending_changes):
                self._clear_changes()
                return True
        return False

    # -------------------------------------------------------------------------
    # METHOD SAVE
    # -------------------------------------------------------------------------
    def save(self):
        if self.__applications and self.state_valid and len(self.model_errors) == 0:
            result = self.__applications.create(self.as_dict())
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
                "name": {"type": "string"},
                "description": {"type": "string"},
                "callback_url": {"type": "string"},
                "public_key": {"type": "string"},
                "private_key": {"type": "string"},
                "environment": {"type": "string"},
                "configuration": {
                    "type": "object"
                },
                "is_enabled": {"type": "boolean"}
            },
            "required": [
                "name",
                "description",
                "callback_url",
                "environment"
            ]
        }


