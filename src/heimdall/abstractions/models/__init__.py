from abc import(
    ABCMeta,
    abstractmethod
)


# -----------------------------------------------------------------------------
# CLASS BASE MODEL
# -----------------------------------------------------------------------------
class AbstractModel(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def update(self, fields: dict):
        pass

    @abstractmethod
    def as_dict(self):
        pass

    @abstractmethod
    def load_from_dict(self):
        pass