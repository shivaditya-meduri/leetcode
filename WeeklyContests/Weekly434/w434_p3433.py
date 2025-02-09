# Problem link : https://leetcode.com/problems/count-mentions-per-user/?slug=maximum-frequency-after-subarray-operation&region=global_v2

from typing import List
class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        priority_event = {"OFFLINE":0, "MESSAGE":1}
        events.sort(key = lambda x : (int(x[1]), priority_event[x[0]]))
        user_offline_till = {str(k) : 0 for k in range(numberOfUsers)}
        mentions = {str(k) : 0 for k in range(numberOfUsers)}
        for event in events:
            event_type, ts = event[0], int(event[1])
            if event_type == "OFFLINE":
                uid = event[2]
                user_offline_till[uid] = ts+59
            else:
                if event[2] == "ALL":
                    for k in mentions.keys():
                        mentions[k] += 1
                elif event[2] == "HERE":
                    for k in mentions.keys():
                        if user_offline_till[k]<ts:
                            mentions[k] += 1
                else:
                    for k in event[2].split(" "):
                        mentions[k.replace("id", "")] += 1
        return list(mentions.values())
