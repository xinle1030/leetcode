"""
Use HashMap and Double Linked List
"""

class LRUCache:

    class Node:
        def __init__(self, key, value) -> None:
            self.key = key
            self.value = value
            self.prev = None
            self.next = None

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.caches = {}

        self.head = self.Node(-1, -1)
        self.tail = self.Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def addNode(self, newNode) -> None:
        curr = self.head.next

        self.head.next = newNode
        newNode.prev = self.head
        
        newNode.next = curr
        curr.prev = newNode
    
    def deleteNode(self, targetNode) -> None:
        prevOne = targetNode.prev
        nextOne = targetNode.next

        prevOne.next = nextOne
        nextOne.prev = prevOne
        
    def get(self, key: int) -> int:
        retValue = -1
        if key in self.caches:
            retNode = self.caches[key]
            retValue = retNode.value

            del self.caches[key]
            self.deleteNode(retNode)
            self.addNode(retNode)

            # point to newly updated node that is placed to the front
            self.caches[key] = self.head.next

        return retValue

    def put(self, key: int, value: int) -> None:
        if key in self.caches:
            retNode = self.caches[key]

            del self.caches[key]
            self.deleteNode(retNode)
        else:
            if len(self.caches) == self.capacity:
                delNode = self.tail.prev
                del self.caches[delNode.key]
                self.deleteNode(delNode)

        self.addNode(self.Node(key, value))
        # point to newly updated node that is placed to the front
        self.caches[key] = self.head.next

# Your LRUCache object will be instantiated and called as such:
capacity = 3
obj = LRUCache(capacity)
print(obj.get(1))
obj.put(1,2)
print(obj.get(1))