# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        curr = res
        while list1 or list2:
            if list1 and list2:
                if list1.val < list2.val:
                    tmp = ListNode(list1.val)
                    list1 = list1.next
                    curr.next = tmp
                    curr = curr.next
                else:
                    tmp = ListNode(list2.val)
                    list2 = list2.next
                    curr.next = tmp
                    curr = curr.next
            
            elif list1:
                curr.next = list1
                list1 = None
            
            else:
                curr.next = list2
                list2 = None
        
        return res.next