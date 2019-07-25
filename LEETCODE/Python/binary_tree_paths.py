# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
 
def dfs(stack, node, res):
    if node.left:
        dfs(stack + [str(node.left.val)], node.left, res)
    if node.right:
        dfs(stack + [str(node.right.val)], node.right, res)
    if not node.left and not node.right:
        res.append('->'.join(stack))
        
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        res = []
        stack = [str(root.val)]
        
        dfs(stack, root, res)
        return res