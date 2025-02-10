# Problem link : https://leetcode.com/problems/clear-digits/description/?envType=daily-question&envId=2025-02-10

class Solution:
    # Using stack
    def clearDigits(self, s: str) -> str:
        stack = []
        for c in s:
            if c.isdigit():
                if stack:  # Remove the closest non-digit (last character in stack)
                    stack.pop()
            else:
                stack.append(c)  # Push non-digit characters
        return "".join(stack)
