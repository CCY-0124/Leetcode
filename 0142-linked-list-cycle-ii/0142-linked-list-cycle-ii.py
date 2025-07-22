# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        seen = {}
        current = head
        index = 0

        while current:
            if current in seen:
                return current
            seen[current] = index
            index += 1
            current = current.next
        
        return None
        