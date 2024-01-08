# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        fast = head
        slow = head

        if fast.next == None : 
            return head.next

        while fast.next and fast.next.next :
            fast = fast.next.next
            if fast.next == None :
                slow.next = slow.next.next
                return head
            slow = slow.next

        if fast.next :
            slow.next = slow.next.next
        return head



            
        