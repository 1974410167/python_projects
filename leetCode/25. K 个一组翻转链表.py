# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional

# todo
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        stack = []
        cur = head
        n = 0
        pre = None
        while cur:
            # 入栈
            while n < k:
                stack.append(cur)
                cur = cur.next
                n += 1
            n = 0
            newHead = stack.pop()
            newNext = newHead.next
            newCur = newHead
            while stack:
                newCur.next = stack.pop()
                newCur = newCur.next
            newCur.next = newNext
            pre = newHead
            if cur:
                cur.next = pre
            else:
                return newHead




