# Problem link : https://leetcode.com/problems/check-if-number-is-a-sum-of-powers-of-three/?envType=daily-question&envId=2025-03-04

'''
Problem description:
Given an integer n, return true if it is possible to represent n as the sum of distinct powers of three. Otherwise, return false.

An integer y is a power of three if there exists an integer x such that y == 3x.
'''

class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        # Represent the given decimal positive integer as a ternary number (base 3) using the division algorithm
        # There can only exist one canonical representation (math proof exists) of a number in any base.
        # Check if we can't do it with distinct powers, remainders > 1 exist, then just return False
        while n!=0:
            if n%3 == 2:
                return False
            n = n//3
        return True


a = Solution()
tcs = [12, 91, 5, 15]
for tc in tcs:
    print(a.checkPowersOfThree(tc))
