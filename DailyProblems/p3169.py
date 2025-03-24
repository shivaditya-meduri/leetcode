# Problem link : https://leetcode.com/problems/count-days-without-meetings/description/?envType=daily-question&envId=2025-03-24
'''
Problem description:
You are given a positive integer days representing the total number of days an employee is available for work (starting from day 1). You are also given a 2D array meetings of size n where, meetings[i] = [start_i, end_i] represents the starting and ending days of meeting i (inclusive).

Return the count of days when the employee is available for work but no meetings are scheduled.

Note: The meetings may overlap.
'''
# Brute force algorithm
from typing import List
class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        all_days = set(range(1, days+1))
        for start_day, end_day in meetings:
            all_days = all_days.difference(set(range(start_day, end_day+1)))
        return len(all_days)

# Efficient solution
from typing import List
class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        if not meetings:
            # no meetings, all days free
            return days
        # sort the meetings and merge
        meetings.sort(key=lambda x : x[0])
        merged = [meetings[0]]
        for start, end in meetings[1:]:
            if start <= merged[-1][1]:
                merged[-1][1] = max(end, merged[-1][1])
            else:
                merged.append([start, end])
        busy_days = sum(end-start+1 for start, end in merged)
        return days - busy_days


a = Solution()
tcs = [[10, [[5,7],[1,3],[9,10]]], [5, [[2,4],[1,3]]], [6, [[1, 6]]]]
a = Solution()
for tc in tcs:
    print(a.countDays(*tc))

'''
Algorithm explained:
1. We sort the meetings based on the start date
2. We create a new list merged where we merge all the overlapping meetings. Fill the merged list with the initially merged element.
3. for every new meeting encountered, we can check if the meeting's start is less than the last meeting end time in which case, we merge the lists and put that at the end
4. Else if there is no overlap, we just add the meeting
5. find all the occupied days and then subract it from all the available days
'''
