# Push Dominoes
# Problem link : https://leetcode.com/problems/push-dominoes/description/?envType=daily-question&envId=2025-05-02
# Brute force solution
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        # Brute force O(n^2) time and O(n) space solution
        n = len(dominoes)
        curr_state = list(dominoes)
        while True:
            new_state = curr_state.copy()
            changes = 0
            for idx, di in enumerate(curr_state):
                prv = curr_state[idx-1] if idx>=1 else "."
                nxt = curr_state[idx+1] if idx<(n-1) else "."
                if di == ".":
                    if prv=="R" and (nxt=="." or nxt=="R"):
                        new_state[idx] = "R"
                        changes += 1
                    elif (prv=="." or prv=="L") and nxt=="L":
                        new_state[idx] = "L"
                        changes += 1
            if changes == 0:
                return "".join(curr_state)
            else:
                curr_state = new_state
        return
# Efficient solution using segment by forces trick
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        # O(n) space time solution
        n = len(dominoes)
        dominoes = list("L"+dominoes+"R") # Adding padding dominoes
        last_i, last_p = 0, "L"
        for curr_i in range(1, n+2):
            curr_p = dominoes[curr_i]
            if curr_p == ".":
                continue
            if curr_p == last_p:
                for j in range(last_i+1, curr_i):
                    dominoes[j] = curr_p
            elif curr_p=="L" and last_p=="R":
                p1, p2 = last_i+1, curr_i-1
                while p1<p2:
                    dominoes[p1] = "R"
                    dominoes[p2] = "L"
                    p1 += 1
                    p2 -= 1
            last_p, last_i = curr_p, curr_i
        return "".join(dominoes[1:-1])
a = Solution()
tcs = ["RR.L", ".L.R...LR..L.."]
for tc in tcs:
    print(a.pushDominoes(tc))

'''
Algorithm explained:
1. Traverse from left to right and keep track of the last non"." domino
2. When you encounter a non-"." domino, and if the last state and the current state is the same, then all the dominoes in between will be that state
3. When you encounter a situation where last state is R and curr state is left, then the first of the dominoes in between will be converted to R and the second half to L
4. Other wise, then the dominoes in between will remain .
5. This algorithm requies visiting each cell only once, so it is O(n) solution
'''

'''
