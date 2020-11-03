class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        if root.left is None and root.right is None:
            return 1
        
        if not root.left:
            return self.minDepth(root.right) + 1
        
        if not root.right:
            return self.minDepth(root.left) + 1
        
        return min(self.minDepth(root.right), self.minDepth(root.left)) + 1