# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if self.dfs(root) != -1:
            return True
        else:
            return False

    def dfs(self, root):
        if not root:
            return 0
        
        left = self.dfs(root.left)
        if left == -1:
            return -1

        right = self.dfs(root.right)
        if right == -1:
            return -1
        
        if abs(left-right) > 1:
            return -1
        
        return max(left,right) + 1
        