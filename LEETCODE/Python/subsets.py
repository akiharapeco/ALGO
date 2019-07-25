from typing import List

def dfs(nums, index, path, res):
    res.append(path)
    for i in range(index, len(nums)):
        dfs(nums, i+1, path+[nums[i]], res)

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        dfs(sorted(nums), 0, [], res)
        return res