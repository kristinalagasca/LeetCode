"""
Given a list of numbers nums and a number k, return whether any two elements from the list add up to k. You may not use the same element twice.

Note: Numbers can be negative or 0.
"""

class Solution:
    def solve(self, nums, k):
        if len(nums) == 1:
            return False
        s = set(nums)
        for i in nums:
            if k - i in s:
                if k - i == i:
                    if nums.count(i) <= 1:
                        continue
                return True
        return False
