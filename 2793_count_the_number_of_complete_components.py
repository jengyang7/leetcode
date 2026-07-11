class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n
        complete_components = 0

        def dfs(node: int) -> tuple[int, int]:
            """
            Returns:
                node_count: number of nodes in this component
                degree_sum: total degree of all nodes in this component
            """
            visited[node] = True

            node_count = 1
            degree_sum = len(graph[node])

            for neighbor in graph[node]:
                if not visited[neighbor]:
                    child_nodes, child_degree_sum = dfs(neighbor)
                    node_count += child_nodes
                    degree_sum += child_degree_sum

            return node_count, degree_sum

        for node in range(n):
            if not visited[node]:
                node_count, degree_sum = dfs(node)

                # Every undirected edge is counted twice.
                edge_count = degree_sum // 2

                expected_edges = node_count * (node_count - 1) // 2

                if edge_count == expected_edges:
                    complete_components += 1

        return complete_components