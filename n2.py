class Solution:
   def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
       carry = 0
       res = ListNode()
       node = res
       while l1 is not None and l2 is not None:
           digit = l1.val + l2.val + carry
           node.next = ListNode(digit % 10)
           node = node.next
           carry = digit // 10
           l1 = l1.next
           l2 = l2.next
       if l1 is not None or l2 is not None:
           tail = l1 if l1 is not None else l2
           while tail is not None:
               digit = tail.val + carry
               node.next = ListNode(digit % 10)
               node = node.next
               carry = digit // 10
               tail = tail.next
              
       if carry != 0:
           node.next = ListNode(1)
       return res.next
