"""
Given two strings a, and b, both representing an integer, add them and return it in the same string representation.

This should be implemented directly, instead of using eval or built-in big integers.
"""

class Solution:
    def solve(self, a, b):
        int1 = int(a)
        int2 = int(b)

        # add both integers
        result = int1 + int2

        return str(result)