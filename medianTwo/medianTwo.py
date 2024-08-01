from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # merge and sort
        nums = nums1 + nums2
        nums.sort()

        lnums = len(nums)
        # if even
        if (lnums % 2 == 0) :
            # take average of middle elements
            return (nums[lnums // 2 - 1] + nums[lnums // 2]) / 2

        # if odd
        else :
            return nums[lnums // 2]
