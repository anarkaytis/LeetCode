# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = 0
        cur = head
        while cur:
            l += 1
            cur = cur.next
        if l - n == 0:
            return head.next
        cur = head
        for i in range(l - n - 1):
            cur = cur.next
        cur.next = cur.next.next
        return head
