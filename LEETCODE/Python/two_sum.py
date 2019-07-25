from collections import Counter

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_table = Counter()
        for index, num in enumerate(nums):
            if hash_table[target - num] > 0:
                return hash_table[target-num] - 1, index
            hash_table[num] = index + 1
        