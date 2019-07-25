from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            nums1[:n] = nums2[:n]
        elif n > 0:
            if nums1[m-1] <= nums2[n-1]:
                nums1[m+n-1] = nums2[n-1]
                self.merge(nums1, m, nums2, n-1)
            else:
                nums1[m+n-1] = nums1[m-1]
                self.merge(nums1, m - 1, nums2, n)