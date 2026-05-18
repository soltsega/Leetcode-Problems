# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root):

        result = []

        def dfs(node, path):

            # This will return if the node is non existent
            if not node:
                return

            # add current node to path if the node is existent. We have to cast it to string to concatenate it.
            path += str(node.val)

            # if leaf, save path. This means we have reached the end of the path
            if not node.left and not node.right:
                result.append(path)
                return

            # continue exploring if the node is not leaf
            path += "->"

            # Call the function recursively
            dfs(node.left, path)
            dfs(node.right, path)

        dfs(root, "")

        return result
        