# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        curr = head
        prev = dummy = ListNode()
        dummy.next = head
        # if not curr:
        #     return curr
        # if not curr.next and curr.val == val:
        #     return None            
        
        while curr:
            if curr.val == val:
                temp_next = curr.next
                curr.next = None                
                prev.next = temp_next
                curr = temp_next 
                # if temp_next:
                #     curr = temp_next.next
                # else:
                #     curr = None
            else:
                prev = curr 
                curr = curr.next
        return dummy.next
            
            
        