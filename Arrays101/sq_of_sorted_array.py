"""
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in
non-decreasing order.
"""

class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        sq_list = []

        for i in range(0, len(nums)):
            new_val = abs(nums[i]) ** 2
            sq_list.append(new_val)

        return sorted(sq_list)
