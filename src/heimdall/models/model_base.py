from heimdall.abstractions.models import AbstractModel


class ModelBase(AbstractModel):

    def __init__(self):
        self._state = {}
        self._pending_changes = {}
        self._uncommitted_changes = False

    def _clear_changes(self):
        self._pending_changes = {}
        self._uncommitted_changes = False

    def update(self, fields: dict):
        for key in fields.keys():
            self._state[key] = fields[key]
            self._pending_changes[key] = fields[key]
        self._uncommitted_changes = True

    def as_dict(self):
        pass

    def load_from_dict(self):
        pass

