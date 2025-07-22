# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        counter = 0
        dummy = ListNode(0)
        dummy.next = head
        current = dummy

        while current.next:
            counter += 1
            current = current.next

        node_to_delete = counter - n

        current = dummy

        for i in range(node_to_delete):
            current = current.next

        current.next = current.next.next

        return dummy.next
        

        