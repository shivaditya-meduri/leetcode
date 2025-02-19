# Problem link : https://leetcode.com/problems/construct-smallest-number-from-di-string/description/?envType=daily-question&envId=2025-02-18

'''
Problem descripion:
You are given a 0-indexed string pattern of length n consisting of the characters 'I' meaning increasing and 'D' meaning decreasing.

A 0-indexed string num of length n + 1 is created using the following conditions:

num consists of the digits '1' to '9', where each digit is used at most once.
If pattern[i] == 'I', then num[i] < num[i + 1].
If pattern[i] == 'D', then num[i] > num[i + 1].
Return the lexicographically smallest possible string num that meets the conditions.
'''
class Solution:
    def smallestNumber(self, pattern: str) -> str:
        ### Dynamic Programming Approach
        n = len(pattern)
        dps = [[] for _ in range(n+1)]
        candidates = list(map(str, range(1, 10)))
        # Base state
        for c in candidates:
            dps[0].append(c)
        for i in range(n):
            for curr in dps[i]:
                for c in candidates:
                    if c not in curr:
                        if pattern[i] == "I":
                            if int(curr[-1]) < int(c):
                                dps[i+1].append(curr+c)
                        else:
                            if int(curr[-1]) > int(c):
                                dps[i+1].append(curr+c)
        return dps[n][0]
    
class Solution:
    def smallestNumber(self, pattern: str) -> str:
        ### More efficient Greedy approach
        result = []
        stack = []
        for i in range(len(pattern) + 1):
            # Push the current digit onto the stack
            stack.append(str(i + 1))
            # If we reached the end or the next pattern is 'I', pop from stack
            if i == len(pattern) or pattern[i] == 'I':
                while stack:
                    result.append(stack.pop())
        return "".join(result)

a = Solution()
tcs = ["IIIDIDDD", "DDD"]
for tc in tcs:
    print(a.smallestNumber(tc))
