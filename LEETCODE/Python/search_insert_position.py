from typing import List
import bisect

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        index = bisect.bisect_left(nums, target)
        if len(nums) - 1 <= index:
            return index
        elif nums[index + 1] == target:
            return index + 1
        else:
            return index