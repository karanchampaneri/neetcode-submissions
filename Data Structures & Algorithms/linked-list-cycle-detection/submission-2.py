# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        #hash nodes seen.

        seen = set()
        
        curr = head
        i = 0

        while (curr):
            if curr in seen:
                return True
            seen.add(curr)
            curr = curr.next

        return False


