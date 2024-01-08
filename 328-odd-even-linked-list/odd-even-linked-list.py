# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head :
            return head
        elif head.next == None :
            return head
        elif head.next.next == None :
            return head

        count = 0
        end = head

        while end.next :
            count += 1
            end = end.next
        temp = head
        if count % 2 == 0 :
            count = count //2 
        else :
            count = count // 2  + 1 
        for i in range(count) :
            end.next = temp.next
            temp.next = temp.next.next
            end.next.next = None 
            temp = temp.next
            end = end.next


        # Approach 1 


    
        return head 
        