# Technique used: Inorder traversal
# Time complexity: O(N)
# Space complexity: O(1)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        # Tracking variables
        current_val = None
        current_count = 0
        max_count = 0
        modes = []
        
        def inorder(node):
            nonlocal current_val, current_count, max_count, modes
            if not node:
                return
            
            # 1. Traverse Left
            inorder(node.left)
            
            # 2. Process Current Node
            if node.val == current_val:
                current_count += 1
            else:
                current_val = node.val
                current_count = 1
            
            # Evaluate the current streak against the max streak
            if current_count > max_count:
                max_count = current_count
                modes = [node.val]  # Found a new clear leader, reset the list
            elif current_count == max_count:
                modes.append(node.val)  # Tied with the max leader, add to list
                
            # 3. Traverse Right
            inorder(node.right)
            
        # Kick off the traversal from the root
        inorder(root)
        return modes