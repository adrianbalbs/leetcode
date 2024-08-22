from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        def dfs(root):
            if not root:
                return 0

            ls = max(0, dfs(root.left))
            rs = max(0, dfs(root.right))
            res[0] = max(res[0], root.val + ls + rs)
            return root.val + max(ls, rs)

        dfs(root)
        return res[0]
