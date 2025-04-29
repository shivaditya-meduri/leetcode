# Problem link : https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/description/?envType=daily-question&envId=2025-04-29
'''
Problem description:
For a given integer array nums and a positive integer k,
return the number of subarrays that have at least k occurrences of the maximum of the nums array
'''
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
      # Sliding window solution : O(n) time and O(1) space complexity
      max_n = max(nums)
      l, max_count, res = 0, 0, 0
      for r in range(len(nums)):
        if nums[r] == max_n:
          max_count += 1
        while (max_count>k) or (l<=r and max_count==k and nums[l]!=max_n):
          if nums[l] == max_n:
            max_count -= 1
          l += 1
        if max_count == k:
          res += (l+1)
      return res

'''
Algorithm explained:
1. The brute force solution would be to test every possible sub array to calculate the count of subarrays with atleast k occurrences of max number. This is an O(n^2) solution.
2. Using the sliding window approach, we can find the minimum subarray ending at right pointer and add all the encompassing left sub arrays to res
3. So, we set l to 0 and find the first r with a count of k and then find the max left so the condition is still satisfied and add all left encompassing sub arrays to the result.
'''

