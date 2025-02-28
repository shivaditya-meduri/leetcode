# Problem link : https://leetcode.com/problems/shortest-common-supersequence/description/?envType=daily-question&envId=2025-02-28
'''
Problem description:
Given two strings str1 and str2, return the shortest string that has both str1 and str2 as subsequences. If there are multiple valid strings, return any of them.

A string s is a subsequence of string t if deleting some number of characters from t (possibly 0) results in the string s.
'''
from functools import lru_cache
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        ### Backtracking solution using caching
        @lru_cache(None)
        def backtrack(i, j):
            if i==len(str1):
                return str2[j:]
            if j==len(str2):
                return str1[i:]
            if str1[i]==str2[j]:
                return str1[i]+backtrack(i+1, j+1)
            res1 = str1[i]+backtrack(i+1, j)
            res2 = str2[j]+backtrack(i, j+1)
            if len(res1)<len(res2):
                return res1
            else:
                return res2
        
        return backtrack(0, 0)

a = Solution()
tcs = [["abac", "cab"], ["aaaaaaaa", "aaaaaaaa"]]
for tc in tcs:
    print(a.shortestCommonSupersequence(*tc))
