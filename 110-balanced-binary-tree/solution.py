from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # The height of a subtree never differs by more than 1
        def getHeight(root) -> int:
            if not root:
                return 0
            lh = getHeight(root.left)
            rh = getHeight(root.right)
            return 1 + max(lh, rh)

        if not root:
            return True
        lh = getHeight(root.left)
        rh = getHeight(root.right)
        return (
            abs(lh - rh) <= 1
            and self.isBalanced(root.left)
            and self.isBalanced(root.right)
        )
