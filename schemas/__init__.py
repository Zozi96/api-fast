from peewee import ModelSelect

from pydantic.utils import GetterDict


class PeeweeGetterDict(GetterDict):
    def get(self, key, default):
        res = getattr(self._obj, key, default)
        if isinstance(res, ModelSelect):
            return list(res)
        return res
