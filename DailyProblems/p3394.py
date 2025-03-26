# Problem link : https://leetcode.com/problems/check-if-grid-can-be-cut-into-sections/description/?envType=daily-question&envId=2025-03-25
'''
Problem description:
You are given an integer n representing the dimensions of an n x n grid, with the origin at the bottom-left corner of the grid. You are also given a 2D array of coordinates rectangles, where rectangles[i] is in the form [startx, starty, endx, endy], representing a rectangle on the grid. Each rectangle is defined as follows:

(startx, starty): The bottom-left corner of the rectangle.
(endx, endy): The top-right corner of the rectangle.
Note that the rectangles do not overlap. Your task is to determine if it is possible to make either two horizontal or two vertical cuts on the grid such that:

Each of the three resulting sections formed by the cuts contains at least one rectangle.
Every rectangle belongs to exactly one section.
Return true if such cuts can be made; otherwise, return false.
'''
from typing import List
class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        x_sections, y_sections = [], []
        for start_x, start_y, end_x, end_y in rectangles:
            x_sections.append([start_x, end_x])
            y_sections.append([start_y, end_y])
        # Checking for vertical cuts
        x_sections.sort(key=lambda x : x[0])
        x_merged = [x_sections[0]]
        for s_x, e_x in x_sections:
            if s_x < x_merged[-1][1]:
                x_merged[-1][1] = max(e_x, x_merged[-1][1])
            else:
                x_merged.append([s_x, e_x])
        if len(x_merged)>=3:
            return True
        # Checking for horizontal cuts
        y_sections.sort(key=lambda x : x[0])
        y_merged = [y_sections[0]]
        for s_y, e_y in y_sections[1:]:
            if s_y < y_merged[-1][1]:
                y_merged[-1][1] = max(y_merged[-1][1], e_y)
            else:
                y_merged.append([s_y, e_y])
        if len(y_merged)>=3:
            return True
        return False

tcs = [[5, [[1,0,5,2],[0,2,2,4],[3,2,5,3],[0,4,4,5]]], [4, [[0,0,1,1],[2,0,3,4],[0,2,2,3],[3,0,4,3]]], [4, [[0,2,2,4],[1,0,3,2],[2,2,3,4],[3,0,4,2],[3,2,4,4]]]]
a = Solution()
for tc in tcs:
    print(a.checkValidCuts(*tc))


'''
Algorithm explained:
1. Each rectangle has an x_range and y_range which can be identified
2. Once we have the x_ranges, we can merge overlapping ranges to create sections which are divided and which can be cut using vertical lines. We can do the same thing with y_ranges.
3. We can merge the x/y ranges by sorting them based on range[0] and then merging by seeing if the range[1] is less than the next item
4. Count the number of x_sections and if it is >=3, then we can make 3 vertical cuts. We can apply similar logic with the y_sections and horizontal cuts.
'''
