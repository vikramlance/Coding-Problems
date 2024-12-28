# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1, l2 = list1, list2
        
        dummy = curr = ListNode()
        def recur(l1, l2):
            nonlocal curr
            # Base case
            if not l1 and not l2:
                return
            if not l2:
                curr.next = l1 # 4
                return
            if not l1:
                curr.next = l2
                return
                            
            if l1.val < l2.val:
                curr.next = l1  # 1 2
                curr = curr.next # 1 2
                recur(l1.next, l2) # recur (2,3) --> recur (4,3) 
            else:
                curr.next = l2 # 1 3 4
                curr = curr.next # 1 3 4
                recur(l1, l2.next) # recur(1,3) --> recur(4,4) -->  recur(4,None)
            return
        
        recur(l1, l2)
        return dummy.next
            
            
                
        
            
        