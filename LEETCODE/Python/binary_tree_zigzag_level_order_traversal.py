from typing import List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []     
        node_list = deque([root])
        res = [[]]       
        depth = 1 
        while node_list:
            if len(res) < depth:
                res.append([])
            size = len(node_list)
            for i in range(size):
                node = node_list.popleft()
                res[-1].append(node.val)
                if node.left != None:
                    node_list.append(node.left)
                if node.right != None:
                    node_list.append(node.right)               
            if depth % 2 == 0:
                res[-1] = res[-1][::-1]
            depth += 1
        return res