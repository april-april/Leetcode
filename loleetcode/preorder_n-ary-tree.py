class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res = []
        stack = root and [root]
        
        while stack:
            node = stack.pop()
            res.append(node.val)
            for child in node.children[::-1]: 
                stack.append(child)
        return res

