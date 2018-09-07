class Node:
	def __init__(self,key):
		self.left = None
		self.right = None
		self.val = key

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
        if (k - root.val) in dict:
            return True
        dict.add(root.val)

        return self.find(root.left, k, dict) or self.find(root.right, k, dict)
    
    def findTarget2(self, root, k):
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

    def findTarget3(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """

        s = set()
        def dfs(root):
            if not root:
                return False
            temp = k - root.val
            if temp in s:    
                return True
            s.add(root.val)
            return dfs(root.left) or dfs(root.right)
        return dfs(root)

def main():
    root = Node(1)
    root.left	 = Node(2)
    root.right	 = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    two_sum = Solution()
    print(two_sum.findTarget(root, 6))
    print(two_sum.findTarget2(root, 6))
    print(two_sum.findTarget3(root, 6))


if __name__ == "__main__":
    main()
