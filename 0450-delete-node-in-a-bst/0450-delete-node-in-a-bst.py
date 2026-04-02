# Technique used: In order traversal
# Time complexity: O(N) where N = height of the tree
# Space complexity: O(N) since we have to traverse across all nodes


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key): # Added 'self'
        if not root:
            return root
        
        # Search for the node
        if key < root.val:
            root.left = self.deleteNode(root.left, key) # Use self.
        elif key > root.val:
            root.right = self.deleteNode(root.right, key) # Use self.
        else:
            # Case 1 & 2: One child or No child
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            
            # Case 3: Two children
            # Find the inorder successor
            temp = self.minValueNode(root.right) # Use self.
            # Replace value
            root.val = temp.val
            # Delete the successor
            root.right = self.deleteNode(root.right, temp.val) # Use self.
            
        return root

    def minValueNode(self, node): # Added 'self'
        current = node
        while current.left:
            current = current.left
        return current