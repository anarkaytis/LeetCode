# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = 0
        start = head
        while start is not None:
            l += 1
            start = start.next
        for i in range(l // 2):
            if head is None:
                break
            head = head.next 
        return head
