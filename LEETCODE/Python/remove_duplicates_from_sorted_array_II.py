from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return
        elif nums[0] == nums[1] and nums[1] == nums[2]:
            i = 0
            nums[:] = nums[:2] + nums[3:]
        else:
            i = 1
        while i <= len(nums) - 3:
            if nums[i] == nums[i+1] and nums[i+1] == nums[i+2]:
                if i == 0 or nums[i-1] != nums[i]:
                    nums[:] = nums[:i+2] + nums[i+3:]
                else:
                    nums[:] = nums[:i+1] + nums[i+3:]
            else:
                i+=1