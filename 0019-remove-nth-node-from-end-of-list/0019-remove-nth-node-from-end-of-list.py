# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        slow = dummy
        fast = dummy

        # Move fast n steps ahead
        for i in range(n):
            fast = fast.next

        # Move both until fast reaches the last node
        while fast.next != None:
            slow = slow.next
            fast = fast.next

        # Remove the nth node
        slow.next = slow.next.next

        return dummy.next