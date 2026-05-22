# Technique used: Two pointer technique
# Time complexity: O(N)
# Space compelxity: O(N)


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # O(N) space complexity
        values = []
        current = head

        # O(N) time complexity
        while current:
            values.append(current.val)
            current = current.next
            # O(N) time complexity one for inverting and the other O(N) for comparison
        return values == values[::-1]
        