class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diam = 0

        def dfs(root):
            nonlocal diam

            if not root:
                return 0
            diam_left = dfs(root.left)
            diam_right = dfs(root.right)
            diam = max(diam, diam_left + diam_right)
            return 1 + max(diam_left, diam_right)

        dfs(root)
        return diam
