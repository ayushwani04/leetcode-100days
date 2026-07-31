class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        current = slow

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        p1 = head
        p2 = prev
        while p2:
            if p1.val!=p2.val:
                return False
            p1 = p1.next
            p2 = p2.next
        return True