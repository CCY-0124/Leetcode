# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        res = ListNode(0,None) # the list that we return
        temp = 0 # the vari we store value
        node = head.next  #we start from the second of the list
        dummy = res

        while node: #when node.next is not None
            if node.val == 0: #the second situation: node with 0
                new = ListNode(temp, None) #create a new node call new
                dummy.next = new #we set dummy point to the new node
                dummy = dummy.next #move to the last node on dummy list
                temp = 0 #we reset temp to 0
            else:
                temp += node.val #the first situation: node with values, we add to temp

            node = node.next

        return res.next

