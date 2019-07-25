from typing import List
from queue import deque

class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        if not preorder:
            return False
        preorder = deque(preorder.split(","))
        queue = deque([preorder.popleft()])
        while queue:
            char = queue.popleft()
            if char == "#":
                continue
            if not preorder:
                return False
            queue.append(preorder.popleft())
            if not preorder:
                return False
            queue.append(preorder.popleft())
        return False if preorder else True