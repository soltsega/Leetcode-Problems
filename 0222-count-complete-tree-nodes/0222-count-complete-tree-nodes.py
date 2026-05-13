# Technique used: Depth first search
# Time complexity: O(log^2N) since we use the early exit. The left shift part
# Space complexity: O(1) since we used the iteration technique 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left_h = self.get_left_height(root)
        right_h = self.get_right_height(root)
        
        # If heights match, it's a perfect binary tree
        if left_h == right_h:
            # Formula: (2^height) - 1
            return (1 << left_h) - 1
        
        # Otherwise, count root (1) + left subtree + right subtree
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    def get_left_height(self, node):
        height = 0
        while node:
            height += 1
            node = node.left
        return height

    def get_right_height(self, node):
        height = 0
        while node:
            height += 1
            node = node.right
        return height