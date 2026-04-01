# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        # 1. Create a dummy node pointing to the head
        dummy = ListNode(next=head)
        current = dummy
    
        # 2. Iterate through the list
        while current.next:
            if current.next.val == val:
                # 3. Skip the node with the target value
                current.next = current.next.next
            else:
                # 4. Only move forward if we didn't delete a node
                current = current.next
            
        # 5. Return the 'real' head
        return dummy.next