class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """

        if root is None:
            return  TreeNode(val)

        elif val<root.val:
            root.left = self.insertIntoBST(root.left,val)
        
        else:
            root.right = self.insertIntoBST(root.right,val)

        return root
        