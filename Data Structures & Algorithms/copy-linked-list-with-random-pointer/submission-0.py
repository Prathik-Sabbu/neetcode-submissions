"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hashmap = { None: None }
        pass1 = pass2 = head

        while pass1:
            hashmap[pass1] = Node(pass1.val)
            pass1 = pass1.next
        
        while pass2:
            hashmap[pass2].next = hashmap[pass2.next]
            hashmap[pass2].random = hashmap[pass2.random]
            pass2 = pass2.next

        return hashmap[head]