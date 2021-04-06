
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next or not k: return head
        tmp, count= head, 0
        # 得到链表长度
        while tmp:
            tmp = tmp.next
            count += 1
        # 取余，因为如果链表长度是5，但是k是11，本质上和k=1是一样的效果。并且下边for循环fast.next会报错。
        k = k % count
        if k == 0:
            return head
        fast = slow = head

        for i in range(k):
            fast = fast.next

        while fast.next:
            fast = fast.next
            slow = slow.next
        newHead = slow.next
        slow.next = None
        fast.next = head
        return newHead


