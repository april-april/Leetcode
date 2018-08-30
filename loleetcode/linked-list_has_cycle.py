def hasCycle(head):
    try:
        slow = head
        fast = head.next
        while slow is not fast:
            slow = slow.next
            fast = fast.next.next
        return True
    except:
        return False


# more intuitive solution

class Solution(object):
    def hasCycle2(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        setNodes = set()

        while head is not None:
            if id(head) in setNodes:
                return True

            setNodes.add(id(head))
            head = head.next

        return False 