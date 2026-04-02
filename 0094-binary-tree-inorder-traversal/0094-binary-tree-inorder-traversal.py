# Technique used: Inorder Traversal
# Time complexity: O(N) where N is the nubmer of nodes in the tree
# Space complexity: O(H) where H is the height of the tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        res = []
        
        def dfs(node):
            if not node:
                return
            # Preorder: Root -> Left -> Right
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)
            
        dfs(root)
        return res    