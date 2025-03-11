# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        \\\
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        \\\
        if not head or k == 1:
            return head
        
        # Step 1: Count k nodes 
        count, temp = 0, head
        while temp and count < k:
            temp = temp.next
            count += 1
        
        # If we have k nodes, reverse them
        if count == k:
            prev, curr = None, head
            for _ in range(k):
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            
            # Connect reversed part to the next k-group
            head.next = self.reverseKGroup(curr, k)
            
            return prev  # Return new head after reversal
        
        return head  # Return head if nodes are less than k
