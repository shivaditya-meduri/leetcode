# Problem link : https://leetcode.com/problems/partition-array-according-to-given-pivot/description/?envType=daily-question&envId=2025-03-03
'''
Problem description:
You are given a 0-indexed integer array nums and an integer pivot. Rearrange nums such that the following conditions are satisfied:

Every element less than pivot appears before every element greater than pivot.
Every element equal to pivot appears in between the elements less than and greater than pivot.
The relative order of the elements less than pivot and the elements greater than pivot is maintained.
More formally, consider every pi, pj where pi is the new position of the ith element and pj is the new position of the jth element. If i < j and both elements are smaller (or larger) than pivot, then pi < pj.
Return nums after the rearrangement.
'''
from typing import List
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        # Brute Force
        before, equal, after = [], [], []
        for n in nums:
            if n < pivot:
                before.append(n)
            elif n==pivot:
                equal.append(n)
            else:
                after.append(n)
        return before + equal + after


a = Solution()
tcs = [[[9,12,5,10,14,3,10], 10], [[-3,4,3,2], 2]]
for tc in tcs:
    print(a.pivotArray(*tc))
