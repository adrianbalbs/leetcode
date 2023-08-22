from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        _, IsBalanced = self.isBalancedHelper(root)
        return IsBalanced

    def isBalancedHelper(self, root) -> tuple[int, bool]:
        if not root:
            return (-1, True)

        lHeight, lIsBalanced = self.isBalancedHelper(root.left)
        rHeight, rIsBalanced = self.isBalancedHelper(root.right)

        balance = abs(lHeight - rHeight)
        if balance <= 1 and lIsBalanced and rIsBalanced:
            height = max(lHeight, rHeight) + 1
            return (height, True)
        else:
            return (-1, False)
