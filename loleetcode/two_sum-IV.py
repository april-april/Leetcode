class Solution:
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        dict = set()
                    
        return self.find(root, k, dict)


    def find(self, root, k, dict):
        if (root == None):
            return False
        elif (k - root.val) in dict:
            return True
        dict.add(root.val)

        return self.find(root.left, k, dict) or self.find(root.right, k, dict)
    
class Solution2(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if not root:
            return False
        bfs, s = [root], set()
        
        for i in bfs:
            if k - i.val in s:
                return True
            s.add(i.val)
            if i.left:
                bfs.append(i.left)
            if i.right:
                bfs.append(i.right)
        return False