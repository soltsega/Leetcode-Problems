# Technique used: 
# Time complexity: O(N)
# Space complexity: O(1)
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Create a placeholder 'dummy' node to start the merged list
        dummy = ListNode()
        # 'tail' will track the last node in our new merged list
        tail = dummy

        # Loop until one of the lists becomes empty
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1    # Connect the smaller node
                list1 = list1.next   # Move the pointer in list1
            else:
                tail.next = list2    # Connect the smaller node
                list2 = list2.next   # Move the pointer in list2
            
            tail = tail.next         # Move our merged list pointer forward
        
        # If one list still has nodes left, attach them all at once
        tail.next = list1 if list1 else list2

        # The actual head of our merged list is the node after dummy
        return dummy.next