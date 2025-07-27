# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        queue = collections.deque([root])

        while queue:
            level = []
            for _ in range(len(queue)):
                cur = queue.popleft()
                if cur:
                    level.append(cur.val)

                    if cur.left:
                        queue.append(cur.left)
                    else:
                        queue.append(None)
                    if cur.right:
                        queue.append(cur.right)
                    else:
                        queue.append(None)
                        
                else:
                    level.append(None)

            size = len(level)

            if level == level[::-1]:
                continue
            else:
                return False
        
        return True
            