# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0

        result = 1
        queue = collections.deque([root])

        while queue:
            for i in range(len(queue)):
                cur = queue.popleft()
                if not cur.left and not cur.right:
                    return result
                else:
                    if cur.left:
                        queue.append(cur.left)
                    if cur.right:
                        queue.append(cur.right)
            result +=1

        return result
