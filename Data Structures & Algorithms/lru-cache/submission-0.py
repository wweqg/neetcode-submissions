class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.hm = {} # key to Node
        self.cap = capacity
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def remove(self, node):
        prev = node.prev
        ne = node.next
        prev.next = ne
        ne.prev = prev
    
    def insert(self, node):
        ne = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = ne
        ne.prev = node
        

    def get(self, key: int) -> int:
        if key in self.hm:
            node = self.hm[key]
            self.remove(node)
            self.insert(node)
            return node.val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.hm:
            self.remove(self.hm[key])
        self.hm[key] = Node(key, value)
        self.insert(self.hm[key])

        if len(self.hm) > self.cap:
            lru = self.tail.prev
            self.remove(lru)
            del self.hm[lru.key]

        
