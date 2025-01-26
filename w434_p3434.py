# Problem link : https://leetcode.com/problems/maximum-frequency-after-subarray-operation/description/
# using kadanes algorithm
### Efficient algorithm using Kadane's algorithm
from typing import List
from collections import Counter
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        c = Counter(nums)
        nk = c[k]
        maxfinalKfreq = nk
        for e in c.keys():
            if e == k:
                continue
            scores = []
            for ni in nums:
                if ni == e:
                    scores.append(1)
                elif ni == k:
                    scores.append(-1)
                else:
                    scores.append(0)
            # Kadane's algorithm of maximum subarray sum
            currSum = 0
            maxSum = -float('inf')
            for si in scores:
                if currSum < 0:
                    currSum = 0
                currSum += si
                maxSum = max(maxSum, currSum)
            finalKfreq = nk + maxSum
            maxfinalKfreq = max(maxfinalKfreq, finalKfreq)
        return maxfinalKfreq

a = Solution()
tcs = [[[1,2,3,4,5,6], 1], [[10,2,3,4,5,5,4,3,2,2], 10]]
for nums, k in tcs:
    print(a.maxFrequency(nums, k))
