from typing import List

def dfs(nums, index, path, rep):
    if not path in rep:
        rep.append(path)
    for i in range(index, len(nums)):
        dfs(nums, i + 1, path + [nums[i]], rep)

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        rep = []
        dfs(sorted(nums), 0, [], rep)
        return rep