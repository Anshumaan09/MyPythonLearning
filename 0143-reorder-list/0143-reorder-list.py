# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        lst = []
        curr = head
        while curr != None:
            lst.append(curr)
            curr = curr.next
        
        left = 0
        right = len(lst) - 1

        while left < right:
            lst[left].next = lst[right]
            left += 1

            if left == right:
                break
            
            lst[right].next = lst[left]
            right -= 1
        
        lst[left].next = None
        