# -*- encoding: utf8 -*-
import collections
class LRUCache(collections.OrderedDict):
    def __init__(self, size=5):
        self.size = size
        self.cache = collections.OrderedDict()

    def get(self, key):
        if key in self.cache:
            value = self.cache.pop(key)
            self.cache.__setitem__(key, value)
            return value
        else:
            value = None
            return value

    def set(self, key, value):
        if key in self.cache and self.size < len(self.cache):
            del self.cache[key]

        elif self.size == len(self.cache):
            self.cache.popitem(last=False)

        self.cache.__setitem__(key, value)

obj = LRUCache()
obj.set(1, 2)
obj.set(2, 3)
obj.set(3, 4)
obj.set(4, 5)
obj.set(5, 6)
obj.set(6, 7)

print obj.cache