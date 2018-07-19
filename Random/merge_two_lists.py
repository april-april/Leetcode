
# Merge two sorted linked lists and 
# return it as a new list.
#(Both lists have same number of elements)

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        
        dummy = current = ListNode(-1)
        
        while l1 and l2:
            if l1.val<=l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        current.next = l1 if l1 else l2 
        return dummy.next
        