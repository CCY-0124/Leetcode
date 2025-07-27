# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:
            return []
        
        queue = collections.deque([root])
        result = []

        while queue:
            level = None
            for i in range(len(queue)):
                print(len(queue))
                cur = queue.popleft()
                if i == 0:
                    level = cur.val #only change level value if it is the last of this level
                if cur.right:
                    queue.append(cur.right)
                if cur.left:
                    queue.append(cur.left)
            result.append(level)
        
        return result