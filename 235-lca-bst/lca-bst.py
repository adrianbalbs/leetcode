
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Store the paths to both p and q in two lists, obtain it through binary search 
        pathP: list['TreeNode'] = []
        pathQ: list['TreeNode'] = []
        self.binarySearch(root, p, pathP)
        self.binarySearch(root, q, pathQ)

        res = p
        for nodeP, nodeQ in zip(pathP, pathQ):
            if nodeP != nodeQ:
                break
            res = nodeP

        return res 

    def binarySearch(self, root: 'TreeNode', node: 'TreeNode', pathList: list['TreeNode']) -> 'TreeNode':
        if root is None:
            return root
        elif root.val == node.val:
            pathList.append(root)
            return root

        if root.val < node.val:
            pathList.append(root)
            return self.binarySearch(root.right, node, pathList)

        pathList.append(root)
        return self.binarySearch(root.left, node, pathList)
