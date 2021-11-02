"""
Question: Given a binary array nums, return the maximum number of consecutive 1's in the array.
"""

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        result = 0

        for i in range(0, len(nums)):
            if nums[i] == 0:
                count = 0
            else:
                count += 1
                result = max(result, count)

        return result
