# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if not head.next:
            return head.next
        
        left = right = test = ListNode()
        test.next = head
        n += 1
        while n and right:
            right = right.next 
            n -= 1

        while right:
            right = right.next
            left = left.next
        
        left.next = left.next.next

        return test.next