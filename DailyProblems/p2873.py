# Problem link : https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-i/description/?envType=daily-question&envId=2025-04-02
'''
Problem description:
You are given a 0-indexed integer array nums.

Return the maximum value over all triplets of indices (i, j, k) such that i < j < k. If all such triplets have a negative value, return 0.

The value of a triplet of indices (i, j, k) is equal to (nums[i] - nums[j]) * nums[k].
'''
from typing import List
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        maxValue = -float('inf')
        n = len(nums)
        for i in range(n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    tripletValue = (nums[i] - nums[j]) * nums[k]
                    if tripletValue > maxValue:
                        maxValue = tripletValue
        if maxValue < 0:
            return 0
        return maxValue

  # Algorithm is very simple. No explanation needed
