# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return head
        cur = head
        pre = None
        while cur:
            t = cur.next
            cur.next = pre
            pre = cur
            cur = t
        return cur



a = [1,23]
q = a[0:0]
print(q)