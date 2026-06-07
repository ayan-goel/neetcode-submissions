class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.hm = {}
        self.capacity = capacity
        
        self.left = Node(0, 0)
        self.right = Node(0, 0)

        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        prev = node.prev
        next = node.next

        prev.next = next
        next.prev = prev

    def insert(self, node):

        prev = self.right.prev
        prev.next = node
        node.prev = prev

        node.next = self.right
        self.right.prev = node


    def get(self, key: int) -> int:

        if key not in self.hm:
            return -1
        
        node = self.hm[key]

        self.remove(node)
        self.insert(node)

        return node.value

    def put(self, key: int, value: int) -> None:

        if key in self.hm:
            old = self.hm[key]
            self.remove(old)
        
        new = Node(key, value)
        self.hm[key] = new
        self.insert(new)

        if len(self.hm) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.hm[lru.key]

        
