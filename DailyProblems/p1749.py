# Problem link : https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/description/?envType=daily-question&envId=2025-02-26
'''
Problem description:
You are given an integer array nums. The absolute sum of a subarray [numsl, numsl+1, ..., numsr-1, numsr] is abs(numsl + numsl+1 + ... + numsr-1 + numsr).

Return the maximum absolute sum of any (possibly empty) subarray of nums.

Note that abs(x) is defined as follows:

If x is a negative integer, then abs(x) = -x.
If x is a non-negative integer, then abs(x) = x.
'''
from typing import List
class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        # Uses Kadane's algorithm
        if len(nums)==0:
            return 0
        maxSum = -float('inf')
        currSumMin, currSumMax = 0, 0
        for n in nums:
            currSumMin = min(currSumMin+n, n)
            currSumMax = max(currSumMax+n, n)
            maxSum = max(-currSumMin, currSumMax, maxSum)
        return maxSum

a = Solution()
tcs = [[1,-3,2,3,-4], [2,-5,1,-4,3,-2]]
for tc in tcs:
    print("Max Sum: ", a.maxAbsoluteSum(tc))

