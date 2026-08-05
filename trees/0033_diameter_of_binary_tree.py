class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        diameter=[0]

        def depth(node):

            if node is None:
                return 0

            left_depth = depth(node.left)
            right_depth = depth(node.right)

            diameter[0] = max(diameter[0],left_depth+right_depth)

            return 1 + max(left_depth,right_depth)

        depth(root)

        return diameter[0]
