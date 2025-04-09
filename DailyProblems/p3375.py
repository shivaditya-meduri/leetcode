# Problem link : https://leetcode.com/problems/minimum-operations-to-make-array-values-equal-to-k/description/?envType=daily-question&envId=2025-04-09
'''
Problem description:
You are given an integer array nums and an integer k.

An integer h is called valid if all values in the array that are strictly greater than h are identical.

For example, if nums = [10, 8, 10, 8], a valid integer is h = 9 because all nums[i] > 9 are equal to 10, but 5 is not a valid integer.

You are allowed to perform the following operation on nums:

Select an integer h that is valid for the current values in nums.
For each index i where nums[i] > h, set nums[i] to h.
Return the minimum number of operations required to make every element in nums equal to k. If it is impossible to make all elements equal to k, return -1.
'''
from typing import List
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums_distinct = list(set(nums))
        nums_distinct.sort()
        if k > nums_distinct[0]:
            return -1
        ln = len(nums_distinct)
        if k in nums_distinct:
            kIndex = nums_distinct.index(k)
        else:
            return len(nums_distinct)
        return ln-kIndex-1

# The question can be solved using basic common sense
