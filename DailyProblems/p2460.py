# Problem link : https://leetcode.com/problems/apply-operations-to-an-array/description/?envType=daily-question&envId=2025-03-01
'''
Problem Description:
You are given a 0-indexed array nums of size n consisting of non-negative integers.

You need to apply n - 1 operations to this array where, in the ith operation (0-indexed), you will apply the following on the ith element of nums:

If nums[i] == nums[i + 1], then multiply nums[i] by 2 and set nums[i + 1] to 0. Otherwise, you skip this operation.
After performing all the operations, shift all the 0's to the end of the array.

For example, the array [1,0,2,0,0,1] after shifting all its 0's to the end, is [1,2,1,0,0,0].
Return the resulting array.

Note that the operations are applied sequentially, not all at once.
'''
from typing import List
class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        ### Without initializing another array - Memory efficient
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
        zCount = 0
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                nums.pop(i)
                zCount += 1
            else:
                i += 1
        for _ in range(zCount):
            nums.append(0)
        return nums


a = Solution()
tcs = [[1,2,2,1,1,0], [0,1], [847,847,0,0,0,399,416,416,879,879,206,206,206,272]]
for tc in tcs:
    print(a.applyOperations(tc))
