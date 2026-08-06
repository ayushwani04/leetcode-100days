class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if root is None:
            return True

        balanced = [True]

        def height(node):
            if node is None:
                return 0
            
            left_height = height(node.left)
            right_height = height(node.right)

            if abs(left_height - right_height)>1:
                balanced[0] = False

            return 1 + max(left_height , right_height)

        height(root)

        return balanced[0]