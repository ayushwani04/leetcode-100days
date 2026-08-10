class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        while root is not None:
            
            if val == root.val:
                return root

            elif val<root.val:
                root = root.left

            
                root = root.right

        return None