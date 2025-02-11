# Problem link : https://leetcode.com/problems/remove-all-occurrences-of-a-substring/description/?envType=daily-question&envId=2025-02-11
## Using a stack based approach to avoid scanning the string multiple times
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        ls = len(s)
        lp = len(part)
        part_list = list(part)
        stack = []
        for ch in list(s):
            stack.append(ch)
            if len(stack) >= lp:
                if stack[-lp:]==part_list:
                    del stack[-lp:]
        return ''.join(stack)
