# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # find middle node
        slow = fast = head
        while fast and fast.next:
            slow = slow.next # middle node after this loop
            fast = fast.next.next
        
        # reverse the second half
        prev = None
        curr = slow # middle node
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        # compare twin from first and second reversed half
        max_sum = 0
        first_half = head
        second_half = prev

        while second_half:
            max_sum = max(max_sum, first_half.val + second_half.val)
            first_half = first_half.next
            second_half = second_half.next
        
        return max_sum

        # time = O(n) traverse list linearly
        # space =  O(1) modify in-place