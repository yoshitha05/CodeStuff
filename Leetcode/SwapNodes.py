# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head
        
        # Initialize pointers
        dummy = ListNode(0)  # Dummy node to simplify edge cases
        dummy.next = head
        prev = dummy
        
        # Iterate through the list, swapping pairs
        while head and head.next:
            # Nodes to be swapped
            first_node = head
            second_node = head.next
            
            # Swapping
            prev.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node
            
            # Reinitialize pointers for the next pair
            prev = first_node
            head = first_node.next
        
        return dummy.next
