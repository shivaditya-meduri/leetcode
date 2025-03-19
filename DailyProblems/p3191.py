# Problem link : https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-i/description/?envType=daily-question&envId=2025-03-19
'''
Problem description:
You are given a binary array nums.

You can do the following operation on the array any number of times (possibly zero):

Choose any 3 consecutive elements from the array and flip all of them.
Flipping an element means changing its value from 0 to 1, and from 1 to 0.

Return the minimum number of operations required to make all elements in nums equal to 1. If it is impossible, return -1.
'''
from typing import List
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        if all(nums):
            return 0
        opsCount = 0
        for i in range(n-2):
            if nums[i] == 0:
                nums[i] = 1 - nums[i]
                nums[i+1] = 1 - nums[i+1]
                nums[i+2] = 1 - nums[i+2]
                opsCount += 1
        # if all(nums[(i+1):]):
        # Slicing will create new list in memory
        #     return opsCount
        if all(x == 1 for x in nums[i+1:]):
            # Using a generator will avoid slicing (creation of new list in memory) which is more efficient
            return opsCount
        return -1
