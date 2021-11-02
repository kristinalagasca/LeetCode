"""
Given an array nums of integers, return how many of them contain an even number of digits.
"""

class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        count = 0

        for i in range(0, len(nums)):
            if len(str(nums[i])) % 2 == 0:
                count += 1
            else:
                print("Odd digit here")

        return count
