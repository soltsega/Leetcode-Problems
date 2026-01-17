import heapq

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        min_heap = []
        
        # 1. Put the head of each list into the min-heap
        for i in range(len(lists)):
            if lists[i]:
                # We include the index 'i' as a tie-breaker for 
                # cases where multiple nodes have the same value.
                heapq.heappush(min_heap, (lists[i].val, i, lists[i]))
        
        # 2. Create a dummy head to build the new list
        dummy = ListNode(0)
        current = dummy
        
        # 3. While the heap has nodes, pick the smallest and move forward
        while min_heap:
            val, i, node = heapq.heappop(min_heap)
            current.next = node
            current = current.next
            
            # If there's a next node in the list we just popped from, add it to heap
            if node.next:
                heapq.heappush(min_heap, (node.next.val, i, node.next))
                
        return dummy.next