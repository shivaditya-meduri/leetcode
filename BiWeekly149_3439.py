# Problem link : https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-i/description/
from typing import List
class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        numMeetings = len(startTime)
        free_time = []
        for i in range(numMeetings+1):
            if i==0:
                free_time.append(startTime[i])
            elif i==numMeetings:
                free_time.append(eventTime-endTime[numMeetings-1])
            else:
                free_time.append(startTime[i]-endTime[i-1])
        # if we only merge consecutive time slots, k+1 merges should result from k shifts
        # So, find the max sum of k+1 consecutive time slots
        window_sum = sum(free_time[:k+1])
        max_free_time = window_sum
        for i in range(1, len(free_time)-k):
            window_sum = window_sum - free_time[i-1] + free_time[i+k]
            max_free_time = max(window_sum, max_free_time)
        return max_free_time
