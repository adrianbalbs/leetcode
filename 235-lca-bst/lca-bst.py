
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return root
    def binarySearch(self, root: 'TreeNode', val: 'TreeNode') -> 'TreeNode':
        if root is None or root.val == val:
            return root

        if root.val < val:
            return self.binarySearch(root.right, val)

        return self.binarySearch(root.left, val)
