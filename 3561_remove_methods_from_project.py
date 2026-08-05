class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        # build directed graph
        graph = [[] for _ in range(n)]

        for caller, called in invocations:
            graph[caller].append(called)
        
        # step 1: find all methods reachable from k using DFS
        suspicious = set()
        stack = [k]

        while stack:
            method = stack.pop()

            if method in suspicious:
                continue
            
            suspicious.add(method)

            for next_method in graph[method]:
                if next_method not in suspicious:
                    stack.append(next_method)
        
        # step 2: check whether a safe method calls a suspicious method
        for caller, called in invocations:
            if caller not in suspicious and called in suspicious:
                # cannot remove the suspicious group
                return list(range(n))
        
        # step 3: remove every suspicious method
        return [method for method in range(n) if method not in suspicious]

        # time: O(n+m) n = number of methods, m = number of invocations
        # space: O(n+m)