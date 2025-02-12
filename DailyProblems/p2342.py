# Problem Link : https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits/description/?envType=daily-question&envId=2025-02-12
'''
Problem Description:
You are given a 0-indexed array nums consisting of positive integers. You can choose two indices i and j, such that i != j, and the sum of digits of the number nums[i] is equal to that of nums[j].
Return the maximum value of nums[i] + nums[j] that you can obtain over all possible indices i and j that satisfy the conditions.
Example 1:
Input: nums = [18,43,36,13,7]
Output: 54
Explanation: The pairs (i, j) that satisfy the conditions are:
- (0, 2), both numbers have a sum of digits equal to 9, and their sum is 18 + 36 = 54.
- (1, 4), both numbers have a sum of digits equal to 7, and their sum is 43 + 7 = 50.
So the maximum sum that we can obtain is 54.
Example 2:
Input: nums = [10,12,19,14]
Output: -1
Explanation: There are no two numbers that satisfy the conditions, so we return -1.
Constraints:
1 <= nums.length <= 105
1 <= nums[i] <= 109
'''
from typing import List
from collections import defaultdict
### Optimized
class Solution:
    def sum_digits_arthemetic(self, x):
        out = 0
        while x:
            out += x%10
            x = x//10
        return out
    def maximumSum(self, nums: List[int]) -> int:
        ln = len(nums)
        # Get the sum of the digits for each element of the array
        sum_digits_nums = [self.sum_digits_arthemetic(x) for x in nums] # O(n*numDigitsMax(=9))
        c = defaultdict(lambda : (None, None)) # Get max1 and max2 for each sum of digits
        for ind, sd in enumerate(sum_digits_nums):
            max1, max2 = c[sd]
            if max1 is None:
                max1 = nums[ind]
            else:
                if nums[ind] > max1:
                    max2 = max1
                    max1 = nums[ind]
                elif max2 is None or nums[ind]>max2:
                    max2 = nums[ind]
            c[sd] = (max1, max2)
        maxSum = -1 
        for k, v in c.items(): # get the max possible pairwise sum
            if all(v):
                max1, max2 = v
                maxSum = max(max1+max2, maxSum)
        return maxSum
        
