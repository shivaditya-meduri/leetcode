# Problem link : https://leetcode.com/problems/longest-nice-subarray/description/?envType=daily-question&envId=2025-03-20
'''
Problem description:
You are given an array nums consisting of positive integers.

We call a subarray of nums nice if the bitwise AND of every pair of elements that are in different positions in the subarray is equal to 0.

Return the length of the longest nice subarray.

A subarray is a contiguous part of an array.

Note that subarrays of length 1 are always considered nice.
'''
from typing import List
# bit mask solution
class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        maxlen = 1
        for i in range(n):
            mask = 0
            for j in range(i, min(n, i+30)):
                if mask & nums[j] != 0:
                    break
                mask = mask | nums[j]
                maxlen = max(maxlen, j-i+1)
        return maxlen
a = Solution()
tcs = [[1,3,8,48,10], [3,1,5,11,13]]
for tc in tcs:
    print(a.longestNiceSubarray(tc))

'''
Algorithm explained:
1. if 2 numbers have bitwise AND = 0, it means that at any bit position, both numbers don't have a 1
2. As n can take a max value of 10^9 which is 30 bits and it can be only positive integers (non-zeros), we can at max have a sub array of length 30
3. a mask can help us check what are all the bits that are already used. If a new number has a 1 in a postion where mask has one, then it cannot be included in the nice sub array and we break
4. find the max length of the sub array is simple to understand
'''
