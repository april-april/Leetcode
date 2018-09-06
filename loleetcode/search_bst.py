# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        while(root):
            if root.val == val:
                return root

            elif root.val > val:
                root = root.left

            elif root.val < val:
                root = root.right

        return None

    def searchBST2(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root.val == val:
            return root

        elif root.val > val and root.left:
            return self.searchBST2(root.left, val)

        elif root.val < val and root.right:
            return self.searchBST2(root.right, val)

        return None