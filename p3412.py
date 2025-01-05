# Find Mirror Score of a String
# Link : https://leetcode.com/problems/find-mirror-score-of-a-string/description/

class Solution:
    def calculateScore(self, s: str) -> int:
        # Keep track of positions for each character (a-z)
        seen = [[] for _ in range(26)]
        score = 0

        for i, c in enumerate(s):
            code = ord(c) - ord('a')
            comp_code = 25 - code

            # If complement exists, use it
            if seen[comp_code]:
                j = seen[comp_code].pop()
                score += i - j
            # Otherwise store current position
            else:
                seen[code].append(i)

        return score
