class Solution:
    def addTwoNumbers(self, l1, l2):

        dummy = ListNode()
        head = dummy
        carry = 0

        while l1 or l2 or carry:
            p1 = l1.val if l1 else 0
            p2 = l2.val if l2 else 0

            total = carry+p1+p2
            carry = total//10

            head.next = ListNode(total%10)
            head = head.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy.next