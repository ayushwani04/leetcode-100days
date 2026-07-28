class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()
        dummy.next = head
        previous = dummy
        current = head

        while current:
            if current.val == val:
                previous.next = current.next
                current = previous.next

            else:
                previous = current
                current = current.next

        return dummy.next