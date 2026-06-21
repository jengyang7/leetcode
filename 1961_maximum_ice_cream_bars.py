class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        # greedy sorting
        # sort the costs to get the cheapest ice cream first
        # costs.sort()
        # res = 0

        # for cost in costs:
        #     if cost <= coins:
        #         res += 1
        #         coins -= cost
        #     else:
        #         return res
        
        # return res

        # counting sort
        freq = [0] * 100001

        for cost in costs:
            freq[cost] += 1
        
        count = 0

        for cost in range(1, 100001):
            if freq[cost] == 0:
                continue
            
            can_buy = min(freq[cost], coins // cost)

            count += can_buy
            coins -= can_buy * cost

            if coins < cost:
                break
        
        return count

        # time: O(n + maxCost)
        # space: O(maxCost)