# Problem link : https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/?envType=daily-question&envId=2025-02-19

'''
Problem description:
A happy string is a string that:

consists only of letters of the set ['a', 'b', 'c'].
s[i] != s[i + 1] for all values of i from 1 to s.length - 1 (string is 1-indexed).
For example, strings "abc", "ac", "b" and "abcbabcbcb" are all happy strings and strings "aa", "baa" and "ababbc" are not happy strings.

Given two integers n and k, consider a list of all happy strings of length n sorted in lexicographical order.

Return the kth string of this list or return an empty string if there are less than k happy strings of length n.
'''
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        dps = [[] for _ in range(n)]
        # base state
        for c in ['a', 'b', 'c']:
            dps[0].append(c)
        for i in range(n-1):
            for s in dps[i]:
                for c in ['a', 'b', 'c']:
                    if c!=s[-1]:
                        dps[i+1].append(s+c)
        if k<=len(dps[n-1]):
            res = dps[n-1][k-1]
        else:
            res = ""
        return res
