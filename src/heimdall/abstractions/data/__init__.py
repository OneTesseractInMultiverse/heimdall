from abc import(
    ABCMeta,
    abstractmethod
)


# -----------------------------------------------------------------------------
# CLASS ABSTRACT REPOSITORY
# -----------------------------------------------------------------------------
class AbstractRepository(object):

    __metaclass__ = ABCMeta

    # -------------------------------------------------------------------------
    # METHOD QUERY
    # -------------------------------------------------------------------------
    @abstractmethod
    def query(self, match_pairs: dict) -> list:
        pass

    # -------------------------------------------------------------------------
    # METHOD GET
    # -------------------------------------------------------------------------
    @abstractmethod
    def get(self, entity_id, **params) -> dict:
        pass

    # -------------------------------------------------------------------------
    # METHOD CREATE
    # -------------------------------------------------------------------------
    @abstractmethod
    def create(self, state_data: dict) -> dict:
        pass

    # -------------------------------------------------------------------------
    # METHOD UPDATE ENDS
    # -------------------------------------------------------------------------
    @abstractmethod
    def update(self, entity_id, state_data: dict, **params) -> bool:
        pass

    # -------------------------------------------------------------------------
    # METHOD UPDATE ENDS
    # -------------------------------------------------------------------------
    @abstractmethod
    def delete(self, entity_id, **params) -> dict:
        pass
