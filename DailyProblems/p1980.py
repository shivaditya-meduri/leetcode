# Problem link : https://leetcode.com/problems/find-unique-binary-string/description/?envType=daily-question&envId=2025-02-20
'''
Problem Description:
Given an array of strings nums containing n unique binary strings each of length n, return a binary string of length n that does not appear in nums. If there are multiple answers, you may return any of them.
'''
from typing import List
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        res = []
        for ind, ni in enumerate(nums):
            if ni[ind] == "0":
                res.append("1")
            else:
                res.append("0")
        return "".join(res)
a = Solution()
tcs = [["01","10"], ["00","01"], ["111","011","001"]]
for tc in tcs:
    print(a.findDifferentBinaryString(tc))
