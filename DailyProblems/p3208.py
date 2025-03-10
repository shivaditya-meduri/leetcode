# Problem link : https://leetcode.com/problems/alternating-groups-ii/description/?envType=daily-question&envId=2025-03-09
'''
Problem description:
There is a circle of red and blue tiles. You are given an array of integers colors and an integer k. The color of tile i is represented by colors[i]:

colors[i] == 0 means that tile i is red.
colors[i] == 1 means that tile i is blue.
An alternating group is every k contiguous tiles in the circle with alternating colors (each tile in the group except the first and last one has a different color from its left and right tiles).

Return the number of alternating groups.

Note that since colors represents a circle, the first and the last tiles are considered to be next to each other.
'''
# Brute force approach checking every sliding window
class Solution:
    def checkAlternating(self, arr):
        for i in range(len(arr)-1):
            if arr[i] == arr[i+1]:
                return False
        return True
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)
        count = 0
        for i in range(n):
            if i+k <= n:
                window = colors[i:(i+k)]
            else:
                window = colors[i:]+colors[:(k-(n-i))]
            if self.checkAlternating(window):
                count += 1
        return count



# Efficient solution using diffs array and prefix sums
class Solution():
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        # With Prefix sum and diffs array
        n = len(colors)
        diffs = []
        for i in range(n):
            if colors[i] != colors[(i+1)%n]:
                diffs.append(1)
            else:
                diffs.append(0)
        # Create extended diffs array for sliding window wrap around functionality
        diffs_extended = diffs + diffs
        prefix_sum = [0 for _ in range(len(diffs_extended)+1)]
        for i in range(len(diffs_extended)):
            # prefix[i] is sum of first i elements
            prefix_sum[i+1] = prefix_sum[i] + diffs_extended[i]
        count = 0
        for i in range(n):
            if prefix_sum[i+k-1]-prefix_sum[i] == k-1:
                count += 1
        return count


tcs = [[[0,1,0,1,0], 3], [[0,1,0,0,1,0,1], 6], [[1,1,0,1], 4]]
a = Solution()
for tc in tcs:
    print(a.numberOfAlternatingGroups(*tc))
