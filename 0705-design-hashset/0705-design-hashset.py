class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None

class MyHashSet:
    def __init__(self):
        self.key_space = 1009  
        self.buckets = [Node() for _ in range(self.key_space)]  # Sentinel head nodes

    def _hash(self, key: int) -> int:
        return key % self.key_space

    def add(self, key: int) -> None:
        index = self._hash(key)
        curr = self.buckets[index]
        while curr.next:
            if curr.next.val == key:
                return  # Key already exists
            curr = curr.next
        curr.next = Node(key)  # Add new key at the end

    def remove(self, key: int) -> None:
        index = self._hash(key)
        curr = self.buckets[index]
        while curr.next:
            if curr.next.val == key:
                curr.next = curr.next.next  # Delete node
                return
            curr = curr.next

    def contains(self, key: int) -> bool:
        index = self._hash(key)
        curr = self.buckets[index].next
        while curr:
            if curr.val == key:
                return True
            curr = curr.next
        return False