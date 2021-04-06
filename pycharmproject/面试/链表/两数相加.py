## 先遍历两个链表拿出值，在把值写进链表，笨拙无比

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

s = [7,2,4,3]
s1 = [5,6,4]
#
# r = []
# t = 0
# while len(s) and len(s1):
#     i = s.pop() + s1.pop()
#     j = i
#     i = i % 10
#     r.append(i + t)
#     if j>=10:
#         t = 1
#     else:
#         t = 0
#
# if s:
#     r +=s
# if s1:
#     r +=s1
# print(r)
#
#
# ans = ListNode(r.pop())
ans = ListNode(s.pop(0))
m = ans
while s:
    curnode = ListNode(s.pop(0))
    ans.next = curnode
    ans = curnode
print(m)

ans = ListNode(s1.pop())
n = ans
while s1:
    curnode = ListNode(s1.pop())
    ans.next = curnode
    ans = curnode
print(n)



ss = []

ss.append(m.val)
while m.next:
    m = m.next
    ss.append(m.val)

print(ss)

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        # 把两个链表，变为两个list
        list1 = []
        list2 = []
        list1.append(l1.val)
        list2.append(l2.val)

        while l1.next:
            l1 = l1.next
            list1.append(l1.val)
        while l2.next:
            l2 = l2.next
            list2.append(l2.val)
        # 获得链表的list表现形式
        r = []
        t = 0
        while len(list1) and len(list2):
            i = list1.pop() + list2.pop()
            j = i
            i = i % 10
            r.append(i + t)
            if j >= 10:
                t = 1
            else:
                t = 0

        if list1:
            r = r+list1
        if list2:
            r = r+list2
        # 把list建立为链表
        ans = ListNode(r.pop())
        m = ans
        while r:

            curnode = ListNode(r.pop())

            ans.next = curnode

            ans = curnode

        return m


