# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize pointers
        prev = None
        curr = head
        
        while curr:
            # 1. Store the next node temporarily
            next_node = curr.next
            
            # 2. Reverse the current node's pointer
            curr.next = prev
            
            # 3. Shift the pointers one step forward
            prev = curr
            curr = next_node
            
        # At the end, 'prev' will be the new head of the reversed list
        return prev