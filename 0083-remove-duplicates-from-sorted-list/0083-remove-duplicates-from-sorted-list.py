# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # start from head -- if next == cur then go to next until you find non duplicate .. make pointer to next non ulicate 
        
        cur = head 
        
        while cur:
            # temp 2 cur 2
            temp = cur
            while cur and cur.next and cur.val == cur.next.val:
                cur = cur.next 
            
            temp.next = cur.next
            cur = cur.next
        return head 
        