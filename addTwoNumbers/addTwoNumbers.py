from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def parseNum(self, l: Optional[ListNode]) -> int:
        result = 0
        place = 1
        while l is not None:
            result += l.val * place
            place *= 10
            l = l.next

        return result

    def parseList(self, num: int) -> Optional[ListNode]:
        l = ListNode()
        sl = l

        i = 1
        while num != 0:
            digit = (num // (10 ** (i - 1))) % 10
            l.val = digit
            num -= digit * (10 ** (i - 1))
            i += 1
            if (num != 0):
                l.next = ListNode()
                l = l.next

        return sl

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num = self.parseNum(l1) + self.parseNum(l2)
        return self.parseList(num)
