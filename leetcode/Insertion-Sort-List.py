# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertionSortList(self, head):
        \\\
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        \\\
        dummy = ListNode(0)  # Dummy node to simplify insertion
        curr = head  # Start with the head of the list

        while curr:
            prev = dummy  # Start comparing from the dummy node
            next_node = curr.next  # Store the next node

            # Find the correct position to insert current node
            while prev.next and prev.next.val < curr.val:
                prev = prev.next

            # Insert current node in sorted order
            curr.next = prev.next
            prev.next = curr

        # Move to the next node in the original list
            curr = next_node

        return dummy.next