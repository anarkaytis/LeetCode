# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = cur = ListNode(0)
        dummy.next = head
        while cur.next:
            first = cur.next 
            if first.next == None:
                break
            second = first.next 
            cur.next = second
            temp = second.next
            second.next = first
            first.next = temp
            cur = first
        return dummy.next
