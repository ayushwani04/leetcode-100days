class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prev = None
        current = head
        
        next_node = 0


        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        return prev