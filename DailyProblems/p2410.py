# Problem link : https://leetcode.com/problems/maximum-matching-of-players-with-trainers/description/?envType=daily-question&envId=2025-07-13

'''
Problem description:
Given players array consisting of the players' abilities and trainers array with trainers' capacities.
One player can be at max assigned to one trainer and vice versa.
A trainer can be assigned to a player if trainers capacity >= player's ability
Find the max number of (player, trainer) pairs that can be created
'''


from typing import List
class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        # Time complexity =  O(plogp + tlogt + O(max(p, t)))
        # Space complexity = O(1)
        players.sort(reverse=True)
        trainers.sort(reverse=True)
        player_ptr, trainer_ptr = 0, 0
        num_matchings = 0
        while player_ptr < len(players) and trainer_ptr < len(trainers):
            if players[player_ptr] > trainers[trainer_ptr]:
                player_ptr += 1
            else:
                num_matchings += 1
                player_ptr += 1
                trainer_ptr += 1
        return num_matchings

'''
Solution explained:
1. Sort the trainers and the players array in descending order
2. create 2 pointers for trainers array and players array.
3. The idea is to assign the most capable trainer to the most able player and not waste a capable trainer on a weak player
4. If current trainer's ability is greater than the player's ability, then assign, else move the players pointer only
5. return final number of matchings.
'''
