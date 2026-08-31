# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        critical = []

        prev = head
        curr = head.next
        index = 1

        while curr.next:
            next_node = curr.next

            if (prev.val < curr.val > next_node.val or prev.val > curr.val < next_node.val):
                critical.append(index)
            
            prev = curr
            curr = next_node
            index += 1
        
        if len(critical) < 2:
            return [-1, -1]
        
        min_distance = float("inf")

        for i in range(1, len(critical)):
            min_distance = min(min_distance, critical[i] - critical[i - 1])
        
        max_distance = critical[-1] - critical[0]

        return [min_distance, max_distance]

        # time - O(n)
        # space - O(n)