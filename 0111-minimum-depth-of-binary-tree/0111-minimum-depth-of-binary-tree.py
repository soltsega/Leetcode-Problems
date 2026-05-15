from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # Edge case: Empty tree has a depth of 0
        if not root:
            return 0
        
        # Initialize queue with the root node and its depth of 1
        queue = deque([(root, 1)])
        
        while queue:
            node, depth = queue.popleft()
            
            # The moment we hit the first leaf node, return its depth
            if not node.left and not node.right:
                # For Ex 1: hits node 9 at depth 2 and returns
                # For Ex 2: travels all the way down to node 6 and returns 5
                return depth
            
            # If left child exists, push it to the queue with incremented depth
            if node.left:
                queue.append((node.left, depth + 1))
                
            # If right child exists, push it to the queue with incremented depth
            if node.right:
                queue.append((node.right, depth + 1))