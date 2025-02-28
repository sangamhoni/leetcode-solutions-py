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

        if not head or not head.next:
            return True

        while curr and curr.next:
            prev = prev.next
            curr = curr.next.next
        
        middleNode = prev
        prev = None
        middlePrev = None

        while middleNode:
            temp = middleNode.next
            middleNode.next = prev
            prev = middleNode
            middleNode = temp
        
        middleNode = prev

        while middleNode:
            if middleNode.val != head.val:
                return False
            
            middleNode = middleNode.next
            head = head.next
        
        return True
