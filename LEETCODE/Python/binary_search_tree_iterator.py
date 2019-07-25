# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from queue import deque

class BSTIterator:
    que = deque()

    def __init__(self, root: TreeNode):
        
        def dfs(root):
            if root == None:
                return
            dfs(root.left)
            self.que.append(root.val)
            dfs(root.right)
        dfs(root)
        
    def next(self) -> int:
        """
        @return the next smallest number         
        """
        node = self.que.popleft()
        return node

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        if not self.que:
            return False
        return True


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()