from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return
        length = len(nums)
        j = 0
        for i in range(length-1):
            if nums[i-j] == val:
                length -= 1
                nums[:] = nums[:i-j] + nums[i-j+1:]
                j += 1
        if nums[-1] == val:
            length -= 1
            nums[:] = nums[:-1]