# simple solution: iterative through the tree and compare
# the absolute value of current node - target
# return the val of the node that has the lowest abs val

class Solution(object):
    def closestValue(self, root, target):
        x = root.val
        while root:
            if abs(root.val - target) < abs(x - target):
                x = root.val
            root = root.left if target < root.val else root.right
        return x