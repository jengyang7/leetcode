# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        cur = dummy
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            sum = v1 + v2 + carry
            digit = sum % 10
            carry = sum // 10 # carry to next loop
            cur.next = ListNode(digit)
            cur = cur.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return dummy.next

    # time: O(max(n, m)) - traverse each list onece
    # space: O(1) - output array doesnt count