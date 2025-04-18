class Solution(object):
    def getIntersectionNode(self, headA, headB):
        \\\
        :type headA, headB: ListNode
        :rtype: ListNode
        \\\
        if not headA or not headB:
            return None

        a, b = headA, headB

        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA

        return a
