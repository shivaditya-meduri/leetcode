# Problem link : https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/description/?envType=daily-question&envId=2025-02-05

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        else:
            mismatches = []
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    mismatches.append(i)
            if len(mismatches) == 2:
                if s1[mismatches[0]]==s2[mismatches[1]] and s1[mismatches[1]]==s2[mismatches[0]]:
                    return True
                else:
                    return False
            else:
                return False
