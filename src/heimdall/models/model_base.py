from heimdall.abstractions.models import AbstractModel
from abc import abstractmethod


# -----------------------------------------------------------------------------
# CLASS MODEL BASE
# -----------------------------------------------------------------------------
class ModelBase(AbstractModel):

    # -------------------------------------------------------------------------
    # CLASS CONSTRUCTOR
    # -------------------------------------------------------------------------
    def __init__(self, **kwargs):
        self._state = {}
        self._pending_changes = {}
        self._uncommitted_changes = False
        self.__load_state_if_available(kwargs)

    # -------------------------------------------------------------------------
    # METHOD LOAD STATE IF AVAILABLE
    # -------------------------------------------------------------------------
    def __load_state_if_available(self, arguments: dict):
        if 'state' in arguments:
            self._state = arguments['state']
        else:
            self._state = {}

    # -------------------------------------------------------------------------
    # METHOD CLEAR CHANGES
    # -------------------------------------------------------------------------
    def _clear_changes(self):
        self._pending_changes = {}
        self._uncommitted_changes = False

    # -------------------------------------------------------------------------
    # METHOD UPDATE
    # -------------------------------------------------------------------------
    def update(self, fields: dict):
        for key in fields.keys():
            self._state[key] = fields[key]
            self._pending_changes[key] = fields[key]
        self._uncommitted_changes = True

    @property
    def has_uncommitted_changes(self):
        return self._uncommitted_changes

    # -------------------------------------------------------------------------
    # METHOD UNCOMMITTED CHANGES
    # -------------------------------------------------------------------------
    @property
    def uncommitted_changes(self) -> dict:
        return self._pending_changes

    # -------------------------------------------------------------------------
    # METHOD AS DICT
    # -------------------------------------------------------------------------
    def as_dict(self) -> dict:
        return self._state

    # -------------------------------------------------------------------------
    # METHOD LOAD FROM DICT
    # -------------------------------------------------------------------------
    def load_from_dict(self):
        pass

