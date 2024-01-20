from typing import OrderedDict

"""
Your LRUCache object will be instantiated and called as such:
obj = LRUCache(capacity)
param_1 = obj.get(key)
obj.put(key,value)
"""


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache.get(key)
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        self.cache[key] = value
        self.cache.move_to_end(key)
        if self.capacity == len(self.cache):
            self.cache.popitem(last=False)
