#Technique used:In order traversal
# Time complexity: O(N)
# Space complexity: O(h) where h is the height of the BST


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        prev = float('-inf')

        def inorder(node):
            nonlocal prev
            if not node:
                return True

            # Check left subtree
            if not inorder(node.left):
                return False

            # Validate current node
            if node.val <= prev:
                return False

            prev = node.val  # update previous value

            # Check right subtree
            return inorder(node.right)

        return inorder(root)
