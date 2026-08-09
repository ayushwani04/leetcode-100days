class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        while root is not None:

            if p.val<root.val and q.val<root.val:
                root = root.left

            elif p.val>root.val and q.val>root.val:
                root = root.right

            else:
                return root 