from typing import List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        
        traversal = [[]]
        queue = deque([root])
        depth = 1
        
        while queue:
            length = len(queue)
            for i in range(length):
                node = queue.popleft()
                if len(traversal) < depth:
                    traversal.insert(0, [])
                traversal[0].append(node.val)

                if node.left != None:
                    queue.append(node.left)
                if node.right != None:
                    queue.append(node.right)
            depth += 1
        return traversal