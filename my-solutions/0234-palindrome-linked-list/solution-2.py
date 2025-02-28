# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        prev = head
        curr = head

        stack = []

        if not head or not head.next:
            return True

        while curr and curr.next:
            prev = prev.next
            curr = curr.next.next
        
        prev = prev

        while prev:
            stack.append(prev.val)
            prev = prev.next
        
        while stack:
            if stack.pop() != head.val:
                return False
            
            head = head.next
        
        return True
        