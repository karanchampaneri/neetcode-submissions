# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        #base case
        if not root:
            return 0
        
        #subtree depth + 1 for the node calling
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


        #iterative methods.

        #BFS (O(n)) - level order traversal.
        #count number of levels until end.
        #BFS involves a queue
        
        # if not root:
        #     return 0

        # level = 0
        # q = deque([root])

        # while q:
        #     for i in range(len(q)):
        #         node = q.popleft()
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)
        #     level +=1

        # return level


        #DFS without recursion using stack

        # stack = [[root,1]]
        # res = 0
        # while stack:
        #     node, depth = stack.pop()

        #     if node:
        #         res = max(res, depth)
        #         stack.append([node.left,depth +1])
        #         stack.append([node.right,depth +1])

        # return res
