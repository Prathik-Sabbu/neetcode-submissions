# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        res = l1

        while l1 and l2:
            value = l1.val + l2.val
            if value < 10:
                l1.val = value

            else:
                second = value // 10
                first = value % 10

                l1.val = first

                if l1.next:
                    l1.next.val += second
                else:
                    l1.next = ListNode(second)
                
            if not l1.next and l2.next:
                l1.next = ListNode(0)

            elif not l2.next and l1.next:
                l2.next = ListNode(0)

            if l1: l1 = l1.next
            if l2: l2 = l2.next
        return res


        