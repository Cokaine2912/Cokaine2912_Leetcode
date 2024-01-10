# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def rev(head) :
        if head.next == None :
            return head
        current = None 
        aage = head
        ans = current
        while aage :
            current = aage
            aage =aage.next
            current.next = ans
            ans = current
        return current
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        slow = head 
        fast = head 

        while fast.next and fast.next.next :
            fast = fast.next.next
            slow = slow.next
        # print(slow,fast)
        slow = Solution.rev(slow.next)
        temp = head
        ans = 0
        while slow :
            ans = max(slow.val + temp.val , ans)
            temp = temp.next
            slow = slow.next
    

        return ans
        