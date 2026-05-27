# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        #same pattern as max depth.
        #base case is None, for each node swap left and right recursively.

        if not root:
            return root

        #swap
        temp = root.left
        root.left = root.right
        root.right = temp

        #repeat on subtrees
        self.invertTree(root.right)
        self.invertTree(root.left)

        return root

