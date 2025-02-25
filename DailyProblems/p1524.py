# Problem link : https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/description/?envType=daily-question&envId=2025-02-25
'''
Problem description:
Given an array of integers arr, return the number of subarrays with an odd sum.

Since the answer can be very large, return it modulo 10**9 + 7.
'''
from typing import List
class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        ### Efficient solution
        n = len(arr)
        cumSumArr = []
        currSum = 0
        for a in arr:
            currSum += a
            cumSumArr.append(currSum)
        numEvenSums, numOddSums = 0, 0
        res = 0
        for ci in cumSumArr:
            if ci%2==1:
                res = (res + (1+numEvenSums))%(7+10**9)
                numOddSums += 1
            else:
                res = (res+numOddSums)%(7+10**9)
                numEvenSums += 1
        return res%(7+10**9)

a = Solution()
tcs = [[1,3,5], [2, 4, 6], [1, 2, 3, 4, 5, 6, 7]]
for tc in tcs:
    print(a.numOfSubarrays(arr=tc))
