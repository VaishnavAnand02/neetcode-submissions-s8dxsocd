# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        
        while curr:
            next_node = curr.next  # 1. Save the next node
            curr.next = prev       # 2. Reverse the link
            
            # 3. Advance the pointers for the next iteration
            prev = curr
            curr = next_node
            
        # prev is now pointing to the new head of the reversed list
        return prev