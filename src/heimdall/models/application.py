from heimdall.models.model_base import ModelBase
from heimdall.abstractions.data import (
    AbstractRepository
)
from dateutil.parser import *


class Application(ModelBase):

    def __init__(self, **kwargs):
        super().__init__()
        self.__load_state_if_available(kwargs)
        self.__load_repository_if_available(kwargs)

    # -------------------------------------------------------------------------
    # METHOD LOAD STATE IF AVAILABLE
    # -------------------------------------------------------------------------
    def __load_state_if_available(self, arguments: dict):
        if 'state' in arguments:
            self._state = arguments['state']
        else:
            self._state = {}

    # -------------------------------------------------------------------------
    # METHOD LOAD REPOSITORY IF AVAILABLE
    # -------------------------------------------------------------------------
    def __load_repository_if_available(self, arguments: dict):
        if 'repository' in arguments and isinstance(arguments['repository'], AbstractRepository):
            self.__repository = arguments['repository']

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

    def commit(self):
        if self.__applications and self._uncommitted_changes and self.id:
            if self.__applications.update(self.id, self._pending_changes):
                self._clear_changes()
                return True
        return False

    # -------------------------------------------------------------------------
    # METHOD AS DICT
    # -------------------------------------------------------------------------
    def as_dict(self):
        pass

    # -------------------------------------------------------------------------
    # METHOD LOAD FROM DICT
    # -------------------------------------------------------------------------
    def load_from_dict(self):
        pass