from collections import defaultdict
from collections import deque
"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node.neighbors:
            return Node(node.val, [])
        head = node
        adj_list = defaultdict(list)
        queue = deque([node])
        visited = set()
        while queue:
            if node not in visited:
                visited.add(node)

            for neighbor in node.neighbors:
                if not node or not neighbor:
                    continue
                if neighbor.val not in adj_list[node.val]:
                    adj_list[node.val].append(neighbor.val)
                if neighbor not in visited:
                    queue.append(neighbor)
            node = queue.popleft()
        res = [Node(key, vals) for key, vals in adj_list.items()]
        for node in res:
            node.neighbors = [a  for val in node.neighbors for a in filter(lambda x: x.val == val, res)]
        return res[0]
