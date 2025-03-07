# Problem link : https://leetcode.com/problems/closest-prime-numbers-in-range/description/?envType=daily-question&envId=2025-03-07
'''
Problem description:
Given two positive integers left and right, find the two integers num1 and num2 such that:

left <= num1 < num2 <= right .
Both num1 and num2 are prime numbers.
num2 - num1 is the minimum amongst all other pairs satisfying the above conditions.
Return the positive integer array ans = [num1, num2]. If there are multiple pairs satisfying these conditions, return the one with the smallest num1 value. If no such numbers exist, return [-1, -1].
'''
# Using the algorithm of Sieve of Eratosthenes
from typing import List
class Solution:
    def sieve(self, n):
        # Initialize a list of True values for indices 0 through n
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime

        for p in range(2, int(n ** 0.5) + 1):
            if is_prime[p]:
                for multiple in range(p * p, n + 1, p):
                    is_prime[multiple] = False

        return [num for num, prime in enumerate(is_prime) if prime]
        
    def closestPrimes(self, left: int, right: int) -> List[int]:
        primes = self.sieve(right)
        primes = [p for p in primes if p>=left]
        if len(primes)<2:
            return [-1, -1]
        minDiff = float('inf')
        for i in range(1, len(primes)):
            pd = primes[i]-primes[i-1]
            if pd < minDiff:
                best = [primes[i-1], primes[i]]
                minDiff = pd
        return best
