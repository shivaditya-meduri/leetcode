# Problem link : https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-ii/?envType=daily-question&envId=2025-04-03
'''
Problem description:
You are given a 0-indexed integer array nums.

Return the maximum value over all triplets of indices (i, j, k) such that i < j < k. If all such triplets have a negative value, return 0.

The value of a triplet of indices (i, j, k) is equal to (nums[i] - nums[j]) * nums[k].
'''
from typing import List
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        prefix_max = [None for _ in range(n)]
        maxV = -float('inf')
        for i in range(n):
            maxV = max(maxV, nums[i])
            prefix_max[i] = maxV
        suffix_max = [None for _ in range(n)]
        maxV = -float('inf')
        for i in range(n-1, -1, -1):
            maxV = max(nums[i], maxV)
            suffix_max[i] = maxV
        maxV = -float('inf')
        for j in range(1, n-1):
            tripVal = (prefix_max[j-1] - nums[j])*suffix_max[j+1]
            maxV = max(tripVal, maxV)
        return max(maxV, 0)

a = Solution()
tcs = [[12,6,1,2,7], [1,10,3,4,19], [1,2,3]]
for tc in tcs:
    print(a.maximumTripletValue(tc))

'''
Algorithm explained:
1. In the brute force approach we explore all combinations of i, j, k which has a time complexity of O(n^3)
2. Since we are trying to maximize (nums[i]-nums[j])*nums[k], for a given j, we want the max possible values of nums[i] and nums[k]
3. So, we can have a max prefix array (maxPrefix[i]=max(nums[0]. nums[1], ... nums[i]) and a max suffix array (maxSuffixArray[i] = max(nums[i], nums[i+1},...nums[len(nums)-1]))
4. For a given j, the max triplet value will be (maxPrefix[i-1]-nums[j])*maxSuffix(nums[j+1])
5. So computing the max Prefix and suffix arrays is O(n) operation and exploring all the js is another O(n) operation, so we reduced the time complexity from O(n^3) to O(n)
'''
