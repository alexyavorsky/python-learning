# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        d = [head.val]
        t = head.next
        while t != None:
            d.append(t.val)
            t = t.next
        return d == d[::-1]
