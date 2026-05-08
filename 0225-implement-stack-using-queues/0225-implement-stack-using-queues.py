# Technique used: Using one queue and iteration
# Time complexity: O(n), the push operation. And all others have constant time complexity 
# Space complexity: O(n), for the queue we initialized

from collections import deque

class MyStack:

    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)
        
        # 2. Rotate the queue so the new element is at the front
        # We do this by popping from the front and appending to the back
        # for every element that was already there.
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())

    def pop(self) -> int:
        # The front of the queue is now the "top" of the stack
        return self.queue.popleft()

    def top(self) -> int:
        # Look at the front of the queue because the last element is now at the front(left)
        return self.queue[0]

    def empty(self) -> bool:
        # Check if the queue is empty
        return not self.queue