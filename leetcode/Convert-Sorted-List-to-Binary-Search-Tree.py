# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedListToBST(self, head):
        \\\
        :type head: Optional[ListNode]
        :rtype: Optional[TreeNode]
        \\\
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)

        mid = self._findMiddle(head)  # ✅ Fixed: Calling correctly with underscore
        root = TreeNode(mid.val)

        root.left = self.sortedListToBST(head)  # Left half
        root.right = self.sortedListToBST(mid.next)  # Right half

        return root

    def _findMiddle(self, head):
        \\\Finds the middle node of the linked list using slow & fast pointers.\\\
        prev = None
        slow = fast = head

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        if prev:
            prev.next = None  # Disconnect left half

        return slow