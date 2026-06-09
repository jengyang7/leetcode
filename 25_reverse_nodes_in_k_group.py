# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            kth = group_prev
            for _ in range(k): # iterate k times
                kth = kth.next
                if not kth:
                    return dummy.next
            
            group_next = kth.next

            # reverse k nodes (current group)
            prev = group_next # optimization: automatically stitch the reversed group to the rest of the list
            curr = group_prev.next

            while curr != group_next: # usually is != None
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            temp = group_prev.next # saves a reference to the old head of the group (node 1).
            group_prev.next = kth # Before this line, your list looks broken: dummy is still pointing to 1, but 2 is pointing to 1 as well. This line fixes the bridge so that dummy -> 2 -> 1.
            group_prev = temp # Now that [2 -> 1] is fully reversed and linked, node 1 is the new tail of this section. For the next loop iteration, node 1 will act as the node before the next group of $k$ nodes.