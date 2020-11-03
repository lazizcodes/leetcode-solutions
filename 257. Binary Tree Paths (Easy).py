class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        
        def helper(root, s, res):
            if not root.left and not root.right:
                res.append(s + str(root.val))
            if root.left:
                helper(root.left, s + str(root.val) + '->', res)
            if root.right:
                helper(root.right, s + str(root.val) + '->', res)
        
        res = []
        helper(root, '', res)
        
        return res