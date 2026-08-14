class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        p1 = list1
        p2 = list2

        dummy = ListNode()
        tail = dummy

        while p1 and p2:
            if p1.val <= p2.val:
                tail.next = p1
                tail = tail.next
                p1 = p1.next
            else:
                tail.next = p2
                tail = tail.next
                p2 = p2.next
  
        if p1:
            tail.next = p1
        else:
            tail.next = p2
        return dummy.next