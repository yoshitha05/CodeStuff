class Solution(object):
    def deleteDuplicates(self, head):
        \\\
        :type head: ListNode
        :rtype: ListNode
        \\\
        current = head  # Pointer to traverse the list
        
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next  # Remove the duplicate node
            else:
                current = current.next  # Move to the next node
        
        return head