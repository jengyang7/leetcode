# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None

        # to find middle of linked list, we can use slow and fast pointer
        slow = fast = head
        prev = None # node before slow

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        # slow is middle node
        # prev is before middle

        # link prev to slow.next
        prev.next = slow.next

        return head

        # time = O(n)
        # space = O(1)