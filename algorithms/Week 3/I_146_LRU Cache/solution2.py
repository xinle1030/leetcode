"""
Use HashMap and Deque
O(N) complexity
"""
from collections import deque

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.caches = {}
        self.q = deque()
        
    def get(self, key: int) -> int:
        retVal = -1
        if key in self.caches:
            self.q.remove(key)
            self.q.append(key)

            retVal = self.caches[key]
        
        return retVal

    def put(self, key: int, value: int) -> None:
        if key in self.caches:
            self.q.remove(key)
        elif key not in self.caches and len(self.caches) == self.capacity:
            poppedKey = self.q.popleft()
            del self.caches[poppedKey]

        self.caches[key] = value
        self.q.append(key)

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