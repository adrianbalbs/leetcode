# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left = self.diameterOfBinaryTree(root.left)
        left = left if left != 0 else 1

        right = self.diameterOfBinaryTree(root.right)
        right = right if right != 0 else 1

        return left + right
