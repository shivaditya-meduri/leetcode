# Problem link : https://leetcode.com/problems/sum-of-all-subset-xor-totals/description/?envType=daily-question&envId=2025-04-05
'''
Problem description:
The XOR total of an array is defined as the bitwise XOR of all its elements, or 0 if the array is empty.

For example, the XOR total of the array [2,5,6] is 2 XOR 5 XOR 6 = 1.
Given an array nums, return the sum of all XOR totals for every subset of nums. 

Note: Subsets with the same elements should be counted multiple times.

An array a is a subset of an array b if a can be obtained from b by deleting some (possibly zero) elements of b.
'''
class Solution:
    def getSubsets(self, nums):
        out = []
        curr = []
        def dfs(i):
            if i>= len(nums):
                out.append(curr.copy())
                return
            # include element i
            curr.append(nums[i])
            dfs(i+1)
            # exclude element i
            curr.pop()
            dfs(i+1)
        dfs(0)
        return out
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        total_xor = 0
        for subset in self.getSubsets(nums):
            comb_xor = 0
            for e in subset:
                comb_xor = comb_xor ^ e
            total_xor = total_xor + comb_xor
        return total_xor

'''
Algorithm explained:
1. the tricky part of this problem is to find all the subsets of a given array (powerset)
2. It can be accomplished using itertools, but it is beneficial to be able to write the subset algorithm yourself
3. For every element, we just decide to keep or or not keep it. We can start with element 0 and if we decide to keep it, then we append it and move to the next element, or we pop it and we move to the next element
4. It is a dfs based algorithm and if the index reaches the end of the array, then we just add it to the result.
5. Once we have the subsets, it is easy to find the combination xor total and then the sum of the xor totals.
'''
