# Technique used: Two-pointer (Current and Next)
# Time complexity: O(n)
# Space complexity: O(1)
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None # Return None for empty Linked List

        # 'current' acts as our slow pointer
        current = head
        
        # We look ahead at current.next (the fast pointer)
        while current and current.next:
            if current.val == current.next.val:
                # If it's a duplicate, skip the next node
                current.next = current.next.next
            else:
                # If it's unique, just move to the next node
                current = current.next
                
        return head # Return the head of the modified list