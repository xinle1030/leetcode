"""
OrderedDict
O(1)
"""

from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.caches = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.caches:
            # Move the key to the end to represent it as most recently used
            self.caches.move_to_end(key)
            return self.caches[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.caches:
            # Move the existing key to the end
            self.caches.move_to_end(key)
        elif len(self.caches) == self.capacity:
            # Remove the first key (least recently used) if capacity is reached
            self.caches.popitem(last=False)
        # Add or update the key in the OrderedDict
        self.caches[key] = value

# Your LRUCache object will be instantiated and called as such:
capacity = 2
obj = LRUCache(capacity)
obj.put(1,1)
obj.put(2,2)
print(obj.get(1))
obj.put(3,3)
print(obj.get(2))
obj.put(4,4)
print(obj.get(1))
print(obj.get(3))
print(obj.get(4))