# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        while root:
            # Case 1: Both values are in the right subtree
            if p.val > root.val and q.val > root.val:
                root = root.right
            # Case 2: Both values are in the left subtree
            elif p.val < root.val and q.val < root.val:
                root = root.left
            # Case 3: We found the split point (the LCA)
            else:
                return root