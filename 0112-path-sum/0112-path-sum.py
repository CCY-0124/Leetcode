# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        result = set()

        def dfs(root, sum_path):
            nonlocal result
            if not root:
                return 
            if not root.left and not root.right:
                result.add(sum_path + root.val)
            else:
                dfs(root.left, sum_path + root.val)
                dfs(root.right, sum_path + root.val)

        dfs(root,0)
        return targetSum in result

        