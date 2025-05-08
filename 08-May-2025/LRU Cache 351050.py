# Problem: LRU Cache - https://leetcode.com/problems/lru-cache/

class ListNode:
    def __init__(self, key, val):
        self.val = val
        self.key = key 
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = ListNode(0, 0)
        self.tail = ListNode(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cache = {}

    def _remove(self, node) -> None:
        prev, next_ = node.prev, node.next 
        prev.next = next_
        next_.prev = prev
    
    def _addToFront(self, node) -> None:
        next_ = self.head.next
        next_.prev = node
        self.head.next = node
        node.next = next_
        node.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        value = node.val
        self._remove(node)
        self._addToFront(node)

        return value


    def put(self, key: int, value: int) -> None:
        new_node = ListNode(key, value)
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._addToFront(new_node)
            self.cache[key] = new_node
            return 
        
        self._addToFront(new_node)
        self.cache[key] = new_node

        if len(self.cache) > self.capacity:
            r_node = self.tail.prev
            self._remove(r_node)
            del self.cache[r_node.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)