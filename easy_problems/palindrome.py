"""
Given a non-negative integer num, return whether it is a palindrome.

i.e.  num = 121, returns True
i.e. num = 43, returns False
"""

class Solution:
    def solve(self, num):
        num_str = str(num)
        left = 0
        right = len(num_str)-1

        while left < right:
            if num_str[left] != num_str[right]:
                return False
            left += 1
            right -= 1
        
        return True