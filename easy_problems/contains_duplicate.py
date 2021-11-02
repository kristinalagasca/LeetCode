"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every
element is distinct.
"""

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        already_visited = set()  # Constant Time
        match = []

        for number in nums:
            if number not in already_visited:
                already_visited.add(number)
                repeated_value = False
            elif number in already_visited:
                match.append(number)
                return True

        return repeated_value

