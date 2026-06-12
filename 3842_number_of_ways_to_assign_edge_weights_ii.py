from collections import defaultdict
from typing import List

class Solution:
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        n = len(edges) + 1
        MOD = 10**9 + 7
        LOG = n.bit_length()  # how many levels we need

        # build adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # BFS to get depth and parent of each node
        depth = [0] * (n + 1)
        parent = [0] * (n + 1)  # parent[1] = 0 (no parent for root)
        visited = [False] * (n + 1)
        queue = [1]
        visited[1] = True
        while queue:
            next_queue = []
            for node in queue:
                for nb in graph[node]:
                    if not visited[nb]:
                        visited[nb] = True
                        parent[nb] = node
                        depth[nb] = depth[node] + 1
                        next_queue.append(nb)
            queue = next_queue

        # binary lifting table
        # anc[j][v] = 2^j-th ancestor of v
        anc = [[0] * (n + 1) for _ in range(LOG)]
        anc[0] = parent[:]          # direct parent
        for j in range(1, LOG):
            for v in range(1, n + 1):
                anc[j][v] = anc[j-1][anc[j-1][v]]

        # LCA in O(log n)
        def lca(u, v):
            # bring u and v to the same depth
            if depth[u] < depth[v]:
                u, v = v, u
            diff = depth[u] - depth[v]
            for j in range(LOG):
                if (diff >> j) & 1:
                    u = anc[j][u]
            if u == v:
                return u
            # jump both up until they meet
            for j in range(LOG - 1, -1, -1):
                if anc[j][u] != anc[j][v]:
                    u = anc[j][u]
                    v = anc[j][v]
            return anc[0][u]

        # answer queries
        ans = []
        for u, v in queries:
            l = lca(u, v)
            k = depth[u] + depth[v] - 2 * depth[l]
            ans.append(pow(2, k - 1, MOD) if k > 0 else 0)
        return ans

        # time:  O(n log n) preprocessing + O(q log n) queries
        # space: O(n log n) for the binary lifting table