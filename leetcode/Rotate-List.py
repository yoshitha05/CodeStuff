# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        \\\
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        \\\
        if not head or not head.next or k == 0:
            return head

        # Step 1: Find the length of the linked list
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        # Step 2: Compute the effective rotation (k could be larger than length)
        k %= length
        if k == 0:
            return head  # No rotation needed

        # Step 3: Find the new tail (length - k - 1) and new head
        new_tail = head
        for _ in range(length - k - 1):
            new_tail = new_tail.next
        
        new_head = new_tail.next

        # Step 4: Break the list and connect the old tail to the old head
        new_tail.next = None
        tail.next = head

        return new_head