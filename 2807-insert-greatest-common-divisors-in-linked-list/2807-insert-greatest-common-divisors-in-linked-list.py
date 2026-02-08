# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertGreatestCommonDivisors(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head.next == None:
            return head
        node = head
        while node.next != None:
            gcd = ListNode(1, node.next)
            current_node = node
            next_node = node.next
            for i in range(min(current_node.val, next_node.val),1,-1):
                if (current_node.val % i == 0 and next_node.val % i == 0):
                    gcd.val = i
                    break
            current_node.next = gcd
            node = gcd.next
        return head
        