from typing import List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def appendOnSameLevel(t, level, depth):
    if t == None:
        return 
    if len(level) < depth:
        level.append([])
    level[depth-1].append(t.val)
    appendOnSameLevel(t.left, level, depth+1) 
    appendOnSameLevel(t.right, level, depth+1)
    return 

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        level_list = [[root.val]]
        if root.left == None and root.right == None:
            return level_list

        appendOnSameLevel(root.left, level_list, 2) 
        appendOnSameLevel(root.right, level_list, 2)
        return level_list