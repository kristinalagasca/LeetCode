"""
You are given a list nums of length n + 1 picked from the range 1, 2, ..., n. By the pigeonhole principle, there must be a duplicate. Find and return it. There is guaranteed to be exactly one duplicate.
Bonus: Can you do this in O(n) time and O(1) space?

Constraints: n ≤ 10,000

i.e. 
Input nums = [1, 2, 3, 1]
Output 1
"""

class Solution:
    def solve(self, nums):

        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return nums[i]
