# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)  # Dummy node to handle edge cases
        left = dummy
        right = head
        
        # Move the right pointer n steps ahead
        for _ in range(n):
            right = right.next
        
        # Move both pointers until right reaches the end
        while right:
            left = left.next
            right = right.next
        
        # Skip the nth node
        left.next = left.next.next
        
        return dummy.next  # Return the head of the modified list