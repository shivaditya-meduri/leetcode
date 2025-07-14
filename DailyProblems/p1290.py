# Problem link : https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/description/?envType=daily-question&envId=2025-07-14

class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        num = 0
        curr = head
        while curr:
            num = (num << 1) | curr.val
            curr = curr.next
        return num

# num << 1 shifts the bits by 1. Example 101 becomes 1010 and then we do an or with curr.val which is 0 or 1 and the LSB is updated depending upon the value
