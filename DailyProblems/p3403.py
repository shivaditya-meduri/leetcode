# Problem link : https://leetcode.com/problems/find-the-lexicographically-largest-string-from-the-box-i/?envType=daily-question&envId=2025-06-04
class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends==1:
            return word
        word_list = list(word)
        max_letter = max(word_list)
        candidates = []
        for max_letter_index, l in enumerate(word_list):
            if l == max_letter:
                up_to = min(len(word_list)-numFriends+1, len(word_list)-max_letter_index)
                candidates.append(word[max_letter_index:max_letter_index+up_to])
        return max(candidates)
