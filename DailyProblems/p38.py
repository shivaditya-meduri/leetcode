# Count and Say
# Problem link : https://leetcode.com/problems/count-and-say/description/?envType=daily-question&envId=2025-04-18
'''
Problem description:
The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

countAndSay(1) = "1"
countAndSay(n) is the run-length encoding of countAndSay(n - 1).
Run-length encoding (RLE) is a string compression method that works by replacing consecutive identical characters (repeated 2 or more times) with the concatenation of the character and the number marking the count of the characters (length of the run). For example, to compress the string "3322251" we replace "33" with "23", replace "222" with "32", replace "5" with "15" and replace "1" with "11". Thus the compressed string becomes "23321511".

Given a positive integer n, return the nth element of the count-and-say sequence.
'''
class Solution:
    def getRLE(self, s: str) -> str:
        out = ""
        char_count = 0
        prev = s[0]
        for si in s:
            if si == prev:
                char_count += 1
            else:
                out += f"{char_count}{prev}"
                char_count = 1
                prev = si
        out += f"{char_count}{prev}"
        return out
    def countAndSay(self, n: int) -> str:
        o = "1"
        for _ in range(n-1):
            o = self.getRLE(o)
        return o

a = Solution()
tcs = [4, 1]
for tc in tcs:
    print(a.countAndSay(tc))

# The code is self explanatory. This problem is simple and doesn't need a separate algorithm explained section.
