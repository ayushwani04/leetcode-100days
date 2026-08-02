class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        
        if p is None and q is None:
            return True

        if p is None or q is None :
            return False

        if p.val!=q.val:
            return False

        left_same = self.isSameTree(p.left,q.left)
        right_same = self.isSameTree(p.right,q.right)

        return left_same and right_same
