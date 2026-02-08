# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Technique used: Recursive Approach(DFS)
# Time complexity: O(N)
# Space complexity: O(H)
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root:
            return True

        return self.isMirror(root.right, root.left)
    def isMirror(self, left, right):
        if not right and not left:
            return True
        if not right or not left:
            return False
        return (left.val == right.val and self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left))