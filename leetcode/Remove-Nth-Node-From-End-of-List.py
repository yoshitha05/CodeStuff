# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        \\\
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        \\\
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy
        
        # Move first pointer n+1 steps ahead
        for _ in range(n + 1):
            first = first.next
        
        # Move both first and second pointers
        while first:
            first = first.next
            second = second.next
        
        # Remove the nth node
        second.next = second.next.next
        
        return dummy.next