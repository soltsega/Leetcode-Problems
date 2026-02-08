# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        # If both nodes are null, we've reached the end of the branch successfully
        if not p and not q:
            return True
        
        # If one node is null and the other isn't, OR the values differ, they aren't the same
        if not p or not q or p.val != q.val:
            return False
        
        # Recursively check the left children and the right children
        # Both must return True for the trees to be identical
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)