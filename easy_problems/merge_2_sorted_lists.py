"""
Given two lists of integers a and b sorted in ascending order, merge them into one large sorted list.

Constraints:
0 ≤ n ≤ 200,000 where n is the length of a
0 ≤ m ≤ 200,000 where m is the length of b

i.e.
a = [5, 10, 15]
b = [3, 8, 9]

Output: [3, 5, 8, 9, 10, 15]
"""

class Solution:
    def solve(self, a, b):
        a_pointer = 0
        b_pointer = 0

        sort_a_b = []

        while a_pointer < len(a) and b_pointer < len(b):
            if b[b_pointer] < a[a_pointer]:
                sort_a_b.append(b[b_pointer])
                b_pointer += 1
            else:
                sort_a_b.append(a[a_pointer])
                a_pointer += 1
            
        while a_pointer < len(a):
            sort_a_b.append(a[a_pointer])
            a_pointer += 1
        
        while b_pointer < len(b):
            sort_a_b.append(b[b_pointer])
            b_pointer += 1

        return sort_a_b