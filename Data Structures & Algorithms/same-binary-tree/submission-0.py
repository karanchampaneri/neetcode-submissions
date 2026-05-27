# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        #base case
        if not p and not q: # both trees empty
            return True

        if not p or not q: # either one different structure
            return False

        # check if p.left == q.left and p.right == q.right
        
        if p.val != q.val: # compares value of node. 
            return False 
        
        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)
        
        return left and right


