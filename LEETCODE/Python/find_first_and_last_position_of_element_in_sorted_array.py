from typing import List
import bisect

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        a = bisect.bisect_left(nums, target)
        b = bisect.bisect_right(nums, target)
        if a == -1 or b == -1 or b - 1 < a:
            return [-1, -1]
        return [a, b-1]