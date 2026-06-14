# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        # If the subRoot is empty, it is technically a subtree of any tree
        if not subRoot:
            return True
        
        # Check if the trees rooted at the current nodes are identical
        if self.isSameTree(root, subRoot):
            return True
        
        # Otherwise, recursively check the left and right subtrees
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # If both nodes are null, the trees are identical up to this point
        if not p and not q:
            return True
        
        # If one is null and the other isn't, or the values don't match, they are different
        if not p or not q or p.val != q.val:
            return False
        
        # Recursively check the left and right children
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)