# Problem Link : https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-ii/
from typing import List
class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        numMeetings = len(startTime)
        free_slot = []
        free_slot.append(startTime[0])
        for i in range(1, numMeetings):
            free_slot.append(startTime[i]-endTime[i-1])
        free_slot.append(eventTime-endTime[-1])
        leftMax, rightMax = free_slot.copy(), free_slot.copy()
        for i in range(1, len(free_slot)):
            leftMax[i] = max(leftMax[i], leftMax[i-1])
        for i in range(len(free_slot)-2, -1, -1):
            rightMax[i] = max(rightMax[i], rightMax[i+1])
        left_check = lambda x : x[0]<=leftMax[x[1]-1] if x[1]>=1 else False
        right_check = lambda x : x[0]<=rightMax[x[1]+2] if x[1]+2<=len(free_slot)-1 else False
        maxFreeTime = -1
        for i in range(numMeetings):
            meetingTime = endTime[i]-startTime[i]
            if left_check([meetingTime, i]) or right_check([meetingTime, i]):
                freeTimeCreated = free_slot[i]+free_slot[i+1]+meetingTime
            else:
                freeTimeCreated = free_slot[i]+free_slot[i+1]
            if freeTimeCreated > maxFreeTime:
                maxFreeTime = freeTimeCreated
            
        return maxFreeTime
    
