# Problem link : https://leetcode.com/problems/count-the-number-of-good-subarrays/description/?envType=daily-question&envId=2025-04-17
'''
Count the number of good subarrays:
Given an integer array nums and an integer k, return the number of good subarrays of nums.

A subarray arr is good if there are at least k pairs of indices (i, j) such that i < j and arr[i] == arr[j].

A subarray is a contiguous non-empty sequence of elements within an array.
'''
from typing import List
from collections import defaultdict
class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        n = len(nums)
        same = 0
        right = 0
        c = defaultdict(int)
        res = 0
        for left in range(n):
            while same < k and right < n:
                same += c[nums[right]]
                c[nums[right]] += 1
                right += 1
            if same >= k:
                res += (n-right+1)
            c[nums[left]] -= 1
            same -= c[nums[left]]
        return res
                
tcs = [[[1,1,1,1,1], 10], [[3,1,4,3,2,2,4], 2]]
a = Solution()
for tc in tcs:
    print(a.countGood(*tc))

'''
Algorithm explained:
1. We keep a counter for a subarray left:right with the counts of each of the number
2. When a new element is added, the number of pairs (same variable) increases by the count of the number of element in the sub array
3. If an element is removed, then the number of pairs decreases by the number of times the element is present in the subarray after removal
4. We start with left = 0 and we move right from 0 until the end of the array, if we find a good subarray, then all the indices following right are also good, so we just add the len(nums)-right + 1 to the count of good sub arrays
5. Then we move left by one adjusting the counter and the same variable
6. when left reaches the end, we explored the whole array
7. Since we iterate through an element atmost once, the time complexity is O(n) and the space complexity is O(n) because of the counter dictionary
'''
