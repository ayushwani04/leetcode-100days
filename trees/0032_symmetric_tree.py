class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if root is None:
            return True
        return self.isMirror(root.left,root.right)

    def isMirror(self,left,right):

        if left is None and right is None:
            return True

        if left is None or right is None:
            return False

        if left.val != right.val:
            return False

        outside = self.isMirror(left.left , right.right)
        inside = self.isMirror(left.right , right.left)

        return outside and inside