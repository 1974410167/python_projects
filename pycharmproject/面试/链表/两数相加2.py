## 遍历链表的同时，直接新建链表写入

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f'val->{self.val}  next->({self.next})'

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        pre = ListNode(val=(l1.val+l2.val)%10)

        cur = pre

        sign = 0

        if l1.val + l2.val>=10:
            sign = 1
        while l1.next or l2.next:

            l1 = l1.next if l1.next else ListNode()
            l2 = l2.next if l2.next else ListNode()

            cur_val = (l1.val + l2.val + sign) % 10

            cur.next = ListNode(val=cur_val)

            cur = cur.next

            if l1.val + l2.val + sign  >= 10:
                sign = 1
            else:
                sign = 0

        if sign==1:
            cur.next = ListNode(1)

        return pre


l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]
ans = ListNode(l1.pop(0))
m = ans
while l1:
    curnode = ListNode(l1.pop(0))
    ans.next = curnode
    ans = curnode

ans1 = ListNode(l2.pop(0))
m1 = ans1
while l2:
    curnode1 = ListNode(l2.pop(0))
    ans1.next = curnode1
    ans1 = curnode1

s = Solution()
s.addTwoNumbers(m,m1)
