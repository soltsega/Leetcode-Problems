# Technique used: DFS
# Time complexity: O(N) where N is the number of nodes
# Space complexity: O(logN) where logN = the height of the tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        total_result = 0

        if root.left and not root.left.left and not root.left.right:
            total_result += root.left.val
        else:
            total_result += self.sumOfLeftLeaves(root.left)

        total_result += self.sumOfLeftLeaves(root.right)
        return total_result    
        